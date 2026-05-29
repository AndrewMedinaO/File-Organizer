from pathlib import Path
import shutil

folder = Path(__file__).parent / "Junk"

for file in folder.iterdir():
    if file.is_dir():
        shutil.rmtree(file)
