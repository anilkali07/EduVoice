import os

files_to_delete = [
    "../../DigitalPermissionApprovalHub/JULES_REPORT.md",
    "../../DigitalPermissionApprovalHub/db.sqlite3",
    "../../DigitalPermissionApprovalHub/render.yaml"
]

for file_path in files_to_delete:
    # Resolve relative to current script
    abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))
    if os.path.exists(abs_path):
        try:
            os.remove(abs_path)
            print(f"Successfully deleted {abs_path}")
        except Exception as e:
            print(f"Failed to delete {abs_path}: {e}")
    else:
        print(f"File not found: {abs_path}")
