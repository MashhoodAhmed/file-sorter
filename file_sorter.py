import os
import shutil

folder_location = input("Enter the folder location: ")

categories = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".txt", ".docx", ".pptx"],
    "Code": [".py", ".js"]
}

counts = {
    "Images": 0,
    "Documents": 0,
    "Code": 0,
    "Others": 0
}

for item in os.listdir(folder_location):
    src_path = os.path.join(folder_location, item)

    if os.path.isdir(src_path):
        continue  

    _, extension = os.path.splitext(item)
    moved = False

    for folder, extensions in categories.items():
        if extension.lower() in extensions:
            dest_folder = os.path.join(folder_location, folder)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(src_path, dest_folder)
            counts[folder] += 1
            moved = True
            break

    if not moved:
        dest_folder = os.path.join(folder_location, "Others")
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(src_path, dest_folder)
        counts["Others"] += 1

print("\nFile sorting completed:")
for k, v in counts.items():
    print(f"{k}: {v}")
