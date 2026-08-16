# 📂 Smart File Organizer

A command-line file organizer built with Python.

This is **Project 2** in my project-based Python engineering progression. The project started from a small prototype and is being improved through multiple versions so that each version develops a specific engineering skill.

The goal is not to build a perfect production file manager immediately. The goal is to practice:

**Understand → Design → Code → Test → Review → Refactor → Improve**

---

# 📌 Current Version

## V2 — Classification Refactor & Safer Organization

V2 is the current frozen checkpoint for Project 2.

Compared with the original/base version, V2 introduces:

- `pathlib.Path` for filesystem paths
- User-selected source directories
- Direct-file processing
- Directory skipping
- Case-insensitive extension matching
- Centralized extension configuration
- Centralized destination-folder configuration
- One directory scan
- Automatic category-folder creation
- `Documents`, `Images`, `Videos`, `Audios`, and `Others`
- Duplicate filename handling using sequential suffixes
- File organization summary counts
- Specific handling for `FileExistsError` and `FileNotFoundError`

The application intentionally remains a simple Python CLI using the standard library.

---

# ✨ Features

## 1. Select a source directory

The program asks the user for a directory path.

Example:

```text
C:\Users\Abhi\Downloads
```

The application checks that the supplied path is a directory before processing it.

---

## 2. Process files directly inside the directory

V2 scans the selected directory once and processes only actual files.

Directories are ignored.

Example:

```text
Downloads/
├── report.pdf       → process
├── image.jpg        → process
├── song.mp3         → process
├── Projects/        → ignore
└── Backup/          → ignore
```

---

## 3. File categories

Files are classified into:

```text
Documents
Images
Videos
Audios
Others
```

The destination folders are created inside the selected source directory.

Example:

```text
Downloads/
├── Documents/
├── Images/
├── Videos/
├── Audios/
└── Others/
```

---

## 4. Case-insensitive extension handling

The application normalizes a file's extension to lowercase.

Therefore:

```text
PHOTO.JPG
photo.jpg
Photo.JpG
```

are treated consistently as `.jpg`.

---

## 5. Supported document extensions

The current V2 document set includes:

```text
.doc
.docx
.docm
.dot
.dotx
.dotm
.xls
.xlsx
.xlsm
.xlsb
.xlt
.xltx
.xltm
.pdf
.ppt
.pptx
.pptm
.pps
.ppsx
.ppsm
.pot
.potx
.potm
.accdb
.accde
.accdt
.mdb
.pub
.vsd
.vsdx
.vsdm
```

---

## 6. Supported image extensions

```text
.jpg
.jpeg
.png
.gif
.webp
.svg
.avif
.bmp
.tiff
.tif
.ico
.heic
.heif
```

---

## 7. Supported video extensions

```text
.mp4
.avi
.mov
.mkv
.wmv
.flv
.webm
.m4v
```

---

## 8. Supported audio extensions

```text
.mp3
.wav
.aac
.flac
.ogg
.m4a
.wma
.aiff
.alac
.au
.amr
.ac3
.caf
.opus
.ra
.snd
```

---

## 9. Unsupported files

If a file does not match any known category, it is placed in:

```text
Others/
```

This prevents unsupported files from being silently ignored.

---

## 10. Duplicate filename handling

When a destination already contains a file with the same name, the organizer searches for an available sequential filename.

Example:

```text
report.pdf
report-1.pdf
report-2.pdf
report-3.pdf
```

The organizer checks for collisions before selecting the new name.

The goal is to avoid overwriting an existing file.

---

# 🛠️ Technologies Used

- Python 3
- `pathlib`
- Standard-library filesystem operations
- Git / GitHub

No third-party Python packages are required.

Pillow is intentionally not used because this project classifies files from their extensions rather than analyzing their contents.

---

# 📂 Project Structure

```text
smart_file_organizer_CLI_python/
│
├── main.py
└── README.md
```

The category directories are created dynamically inside the directory selected by the user.

---

# 🚀 Running the Application

## Prerequisites

Install Python 3.

Check the installed version:

```bash
python --version
```

## Run

From the project directory:

```bash
python main.py
```

Then enter the directory that should be organized.

---

# 🏗️ V2 Architecture

The current V2 flow is:

```text
User
  ↓
Enter source directory
  ↓
Validate directory
  ↓
Scan directory once
  ↓
Ignore directories
  ↓
Normalize file extension
  ↓
Find matching category
  ↓
Determine destination folder
  ↓
Create destination folder if required
  ↓
Check filename collision
  ↓
Generate available filename when necessary
  ↓
Move file
  ↓
Update category counter
  ↓
Display summary
```

The important V2 improvement is that the organizer no longer scans the entire source directory separately for each category.

---

# 🔄 Base Version → V1 → V2

## Base Version

The original implementation:

- Used `os.listdir()`
- Used hardcoded destination paths
- Repeated classification blocks
- Supported fewer file types
- Did not provide robust duplicate handling
- Did not have an `Others` category

## V1

V1 introduced:

- `pathlib.Path`
- User-selected destination structure
- Direct-file processing
- Case-insensitive extension matching
- Expanded extension lists
- `Others` category
- Duplicate filename handling
- Summary counts

## V2

V2 focused on refactoring the V1 implementation:

- One directory scan
- Centralized extension configuration
- Centralized folder configuration
- Generic category lookup
- Sequential duplicate naming
- Improved filesystem exception handling
- Cleaner `pathlib` usage

---

# 🧠 Main Engineering Lesson from V2

V1 was mainly about:

> **Making the file organizer work.**

V2 is about:

> **Representing the file-classification rules as data so the program can process all categories through one general flow.**

The important mental shift is:

```text
V1

Document?
    → document logic

Image?
    → image logic

Video?
    → video logic
```

toward:

```text
File
 ↓
Find matching category
 ↓
Category determines destination
 ↓
Move file
```

This reduces duplicated control flow and makes the organizer easier to extend.

---

# 🧪 Testing Scenarios

## Valid directory

Provide a real directory containing mixed files.

Expected:

Files are moved into the correct categories.

## Invalid path

Provide a nonexistent path.

Expected:

The application reports that the path is not a directory.

## File instead of directory

Provide the path of an individual file.

Expected:

The application reports that the selected path is not a directory.

## Existing subdirectories

Existing directories in the source folder should be ignored.

## Mixed-case extensions

Examples:

```text
IMAGE.JPG
REPORT.PDF
VIDEO.Mp4
SONG.MP3
```

Expected:

Correct categorization.

## Duplicate names

If a destination filename already exists, the organizer should create a new sequential name rather than overwrite the existing file.

## Unsupported files

Examples:

```text
script.py
archive.zip
random.xyz
```

Expected:

Move to `Others/`.

## Summary

The final output should report counts for:

```text
Documents
Images
Videos
Audios
Others
```

---

# ⚠️ Known V2 Limitations

V2 is a learning checkpoint, not a production-grade file management application.

The following items are intentionally left for V3 or later.

## 1. Category configuration can still be unified further

V2 stores extension sets and folder names in related but separate structures.

A later version can represent a complete category configuration as a single structure.

## 2. Collision logic can be extracted

The duplicate-name logic currently lives inside the main processing flow.

V3 can separate:

```text
Find available destination name
```

from:

```text
Move the file
```

## 3. Filesystem error handling can be expanded

Possible failures include:

- Permission errors
- Locked or inaccessible files
- Failed directory creation
- Failed file movement
- Files disappearing during processing

A later version can define a more complete failure strategy.

## 4. Category counters are explicit

The current implementation uses separate counters for each category.

A later refactor can make the statistics more data-driven.

## 5. No dry-run mode

The current application performs real file operations immediately.

A later version could support previewing changes before moving files.

## 6. No recursive processing

V2 intentionally processes only files directly inside the selected directory.

Recursive scanning can be considered later.

---

# 🎯 V3 Roadmap

V3 should focus on **cleaner design and stronger filesystem reliability**.

Potential goals:

- [ ] Unify category configuration
- [ ] Extract reusable destination-name logic
- [ ] Further reduce duplicated code
- [ ] Improve filesystem exception handling
- [ ] Improve reporting of failed moves
- [ ] Improve category/count handling
- [ ] Improve function-level separation of responsibilities
- [ ] Add stronger edge-case testing
- [ ] Consider a dry-run mode
- [ ] Review whether recursive organization belongs in a later version

V3 should still remain a standard-library CLI application.

---

# 📈 Current Status

| Item | Status |
|---|---|
| Base version | ✅ Complete |
| V1 upgrade | ✅ Complete |
| V2 one-pass scanning | ✅ Complete |
| File-only processing | ✅ Complete |
| Case-insensitive extensions | ✅ Complete |
| Documents | ✅ Complete |
| Images | ✅ Complete |
| Videos | ✅ Complete |
| Audios | ✅ Complete |
| Others | ✅ Complete |
| Summary counts | ✅ Complete |
| Duplicate protection | ✅ Complete |
| Centralized extension configuration | ✅ Complete |
| Folder configuration | ✅ Complete |
| Generic category lookup | ✅ Complete |
| Unified category structure | 🔄 V3 |
| Reusable collision logic | 🔄 V3 |
| Expanded filesystem error handling | 🔄 V3 |
| Dry-run | 🔄 Future |
| Recursive scanning | 🔄 Future |

---

# 🚀 Project-Based Python Progression

This is Project 2 in the larger progression:

```text
Project 1
Expense Tracker CLI
        ↓
Project 2
Smart File Organizer
        ↓
Project 3
API Information CLI
        ↓
Project 4
URL Shortener API
        ↓
Project 5
AI Text Summarizer API
        ↓
Project 6
Cited PDF RAG Assistant
        ↓
Project 7
AI Interview Evaluator
        ↓
Project 8
Automated AI Evaluation Harness
        ↓
Project 9
Human-in-the-Loop AI Agent
        ↓
Project 10
Full-Stack AI Platform
```

Each project introduces a different engineering problem rather than simply adding features to the previous project.

---

# 👨‍💻 Author

**Abhishek**

Software Engineering & AI Engineering Learner

---

# ⭐ Final Note

Smart File Organizer is intentionally being developed in versions.

The objective is not to create the most feature-rich file organizer.

The objective is to build strong software-engineering habits through repeated cycles of:

**Understand → Design → Code → Test → Debug → Review → Refactor → Improve**

**Build → Learn → Improve → Build Something Harder. 🚀**
