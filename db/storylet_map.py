"""
Storylet Map Visualizer
Creates a visual graph of storylet connections and navigation flow.
"""

import sqlite3
import json
from collections import defaultdict, Counter
import webbrowser
import tempfile
import os


def get_storylets_from_db():
    """Get all storylets from the database."""
    conn = sqlite3.connect("worldweaver.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, text_template, requires, choices, weight, position 
        FROM storylets
    """
    )

    storylets = []
    for row in cursor.fetchall():
        storylet = {
            "id": row[0],
            "title": row[1],
            "text": row[2][:50] + "..." if len(row[2]) > 50 else row[2],
            "requires": json.loads(row[3]) if row[3] else {},
            "choices": json.loads(row[4]) if row[4] else [],
            "weight": row[5],
            "position": json.loads(row[6]) if row[6] else {"x": 0, "y": 0},
        }
        storylets.append(storylet)

    conn.close()
    return storylets


def analyze_connections(storylets):
    """Analyze location connections and variable flow."""
    positions = set()
    position_storylets = defaultdict(list)
    variables_required = set()
    variables_set = Counter()
    dead_end_variables = set()

    # Extract positions and analyze variable flow
    for storylet in storylets:
        pos = (storylet["position"].get("x", 0), storylet["position"].get("y", 0))
        positions.add(pos)
        position_storylets[pos].append(storylet)

        # Track required variables
        for var in storylet["requires"].keys():
            variables_required.add(var)

        # Analyze choices for variable setting (location changes are now position changes)
        for choice in storylet["choices"]:
            choice_sets = choice.get("set", {})
            for var, value in choice_sets.items():
                variables_set[var] += 1

    # Find dead-end variables (set but never required)
    all_set_vars = set(variables_set.keys())
    dead_end_variables = all_set_vars - variables_required

    return {
        "positions": positions,
        "position_storylets": position_storylets,
        "variables_required": variables_required,
        "variables_set": dict(variables_set),
        "dead_end_variables": dead_end_variables,
    }


def generate_html_map(storylets, analysis):
    """Generate an HTML visualization of the storylet map."""

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>WorldWeaver Storylet Map</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{ 
            font-family: 'Segoe UI', sans-serif; 
            margin: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }}
        .container {{ 
            max-width: 1200px; 
            margin: 0 auto; 
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }}
        .header {{ 
            text-align: center; 
            margin-bottom: 30px; 
        }}
        .stats {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 20px; 
            margin-bottom: 30px; 
        }}
        .stat-box {{ 
            background: rgba(255,255,255,0.1); 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid rgba(255,255,255,0.2);
        }}
        .stat-title {{ 
            font-weight: bold; 
            margin-bottom: 10px; 
            color: #feca57;
        }}
        .location-graph {{ 
            background: rgba(255,255,255,0.05); 
            border-radius: 10px; 
            padding: 20px; 
            margin: 20px 0;
        }}
        .location-node {{ 
            background: rgba(46, 204, 113, 0.2);
            border: 2px solid #2ecc71;
            border-radius: 8px;
            padding: 10px;
            margin: 10px;
            display: inline-block;
            min-width: 150px;
            text-align: center;
        }}
        .isolated-location {{ 
            background: rgba(231, 76, 60, 0.2);
            border-color: #e74c3c;
        }}
        .connection-arrow {{ 
            color: #feca57;
            font-weight: bold;
        }}
        .dead-vars {{ 
            background: rgba(231, 76, 60, 0.2);
            border: 1px solid #e74c3c;
            border-radius: 5px;
            padding: 10px;
            margin-top: 10px;
        }}
        .storylet-list {{
            max-height: 200px;
            overflow-y: auto;
            font-size: 0.9em;
        }}
        .storylet-item {{
            margin: 5px 0;
            padding: 5px;
            background: rgba(255,255,255,0.1);
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🗺️ WorldWeaver Storylet Map</h1>
            <p>Visual analysis of storylet connections and navigation flow</p>
        </div>
        
        <div class="stats">
            <div class="stat-box">
                <div class="stat-title">📊 Overview</div>
                <div>Total Storylets: {len(storylets)}</div>
                <div>Total Unique Positions: {len(analysis['positions'])}</div>
            </div>
            
            <div class="stat-box">
                <div class="stat-title">🔗 Variable Flow</div>
                <div>Variables Required: {len(analysis['variables_required'])}</div>
                <div>Variables Set: {len(analysis['variables_set'])}</div>
                <div>Dead-End Variables: {len(analysis['dead_end_variables'])}</div>
            </div>
        </div>
"""

    # Position Grid Visualization
    html_content += """
        <div class="location-graph">
            <h3>🗺️ Storylet Position Grid</h3>
            <p>Each storylet is plotted at its (x, y) position.</p>
            <div id="grid" style="position:relative; width:800px; height:600px; background:rgba(255,255,255,0.05); border-radius:10px; border:1px solid #fff;">
    """

    # Find grid bounds
    xs = [pos[0] for pos in analysis["positions"]]
    ys = [pos[1] for pos in analysis["positions"]]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    range_x = max_x - min_x if max_x > min_x else 1
    range_y = max_y - min_y if max_y > min_y else 1

    # Plot each storylet at its position
    for pos, storylets_at_pos in analysis["position_storylets"].items():
        grid_x = int(700 * (pos[0] - min_x) / range_x) + 50
        grid_y = int(500 * (pos[1] - min_y) / range_y) + 50
        for storylet in storylets_at_pos:
            html_content += f'<div style="position:absolute; left:{grid_x}px; top:{grid_y}px; min-width:120px; background:rgba(46,204,113,0.2); border:2px solid #2ecc71; border-radius:8px; padding:10px; text-align:center; color:#fff;">'
            html_content += (
                f'<strong>{storylet["title"]}</strong><br>(x={pos[0]}, y={pos[1]})'
            )
            html_content += "</div>"

    html_content += """
            </div>
        </div>
    """

    # Dead-end variables warning
    if analysis["dead_end_variables"]:
        html_content += f"""
            <div class="dead-vars">
                <strong>⚠️ Dead-End Variables</strong><br>
                These variables are set by choices but never required by any storylet:<br>
                <em>{', '.join(analysis['dead_end_variables'])}</em>
            </div>
"""

    html_content += """
        </div>
        
        <div class="stat-box">
            <div class="stat-title">💡 Recommendations</div>
            <ul>
                <li>Add location-changing choices to isolated locations</li>
                <li>Create storylets that require the dead-end variables</li>
                <li>Ensure each location has multiple entry/exit points</li>
                <li>Add "travel" storylets that connect distant locations</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

    return html_content


def main():
    """Generate and display the storylet map."""
    print("🗺️ Generating WorldWeaver Storylet Map...")

    # Get data
    storylets = get_storylets_from_db()
    if not storylets:
        print("❌ No storylets found in database!")
        return

    # Analyze connections
    analysis = analyze_connections(storylets)

    # Generate HTML
    html_content = generate_html_map(storylets, analysis)

    # Save to temp file and open
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, encoding="utf-8"
    ) as f:
        f.write(html_content)
        temp_file = f.name

    print(f"✅ Map generated: {temp_file}")
    # Browser auto-open removed per user request

    # Print summary
    print(
        f"""
🗺️ STORYLET MAP SUMMARY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 {len(storylets)} storylets across {len(analysis['positions'])} unique positions
⚠️  {len(analysis['dead_end_variables'])} dead-end variables: {', '.join(analysis['dead_end_variables'])}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    )


if __name__ == "__main__":
    main()
