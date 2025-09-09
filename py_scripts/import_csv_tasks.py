import csv
from pathlib import Path

BACKLOG_PATH = Path("../tasks/backlog.md")
CSV_PATH = Path("../notes/all_tasks_consolidated.csv")


# Map CSV columns to backlog fields
def format_task(row):
    return f"""
### Task: {row['title']}
- **ID:** {row['task_id']}
- **Stage:** {row['stage']} ({row['stage_name']})
- **File:** {row['file']}
- **Type:** {row['type']} ({row['category']})
- **Priority:** {row['priority']}
- **Status:** {row['status']}
- **Description:** {row['description']}
- **Spec Reference:** (add manually if needed)
"""


def import_tasks(csv_path, backlog_path):
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = [format_task(row) for row in reader]
    with open(backlog_path, "a", encoding="utf-8") as backlog:
        for task in tasks:
            backlog.write(task + "\n")


if __name__ == "__main__":
    import_tasks(CSV_PATH, BACKLOG_PATH)
    print(f"Imported tasks from {CSV_PATH} to {BACKLOG_PATH}")
