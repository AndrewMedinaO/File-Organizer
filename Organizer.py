from pathlib import Path
import shutil

folder = Path(__file__).parent / "Junk"


categories = {
    ".jpg": "Images", ".png": "Images", ".gif": "Images",
    ".pdf": "Documents", ".txt": "Documents", ".docx": "Documents",
    ".py": "Code", ".html": "Code", ".css": "Code",
    ".zip": "Archives", ".rar": "Archives",
    ".mp3": "Audio"
}


for file in folder.iterdir():
    if file.is_dir():
        continue

        
    category = categories.get(file.suffix,"Other")
    destination = folder / category
    destination.mkdir(exist_ok=True)

    Dest_New = destination / file.name
    counter = 1
    while Dest_New.exists():
        newName = f"{file.stem}{counter}{file.suffix}"
        Dest_New = destination / newName
        counter += 1


    shutil.move(file, Dest_New)
    print(f"{file.name} moved to {category}")