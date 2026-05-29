from pathlib import Path

junk = Path(r"C:\Users\codet\OneDrive\Desktop\Python\AutomateTheBoringStuff\FileOrganizer\Junk")

dummy_files = [
    "photo.jpg", "screenshot.png", "meme.gif",
    "report.pdf", "notes.txt", "essay.docx",
    "script.py", "index.html", "styles.css",
    "backup.zip", "archive.rar",
    "song.mp3", "weird.xyz", "noextension"
]

for name in dummy_files:
    (junk / name).write_text("dummy content")

print(f"Created {len(dummy_files)} dummy files in {junk}")