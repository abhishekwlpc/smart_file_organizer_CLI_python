# Smart File Organizer

A command-line file organization application built with Python.

This is **Project 2** in my project-based Python engineering progression. The project is being developed in multiple versions so I can practice designing, building, testing, debugging, and refactoring Python applications independently.

## Current Version

**V1 — File Classification & Organization Upgrade**

V1 improves the original prototype by introducing:

- `pathlib.Path` for filesystem paths
- User-selected source directories
- Direct-file processing only
- `Documents`, `Images`, `Videos`, `Audios`, and `Others` categories
- Case-insensitive extension matching
- Automatic destination-folder creation
- Duplicate filename protection using UUID-based names
- Unsupported-file handling through `Others`

The project intentionally uses the Python standard library only.

## Features

### Directory selection

The program asks the user for a directory path and verifies that the supplied path is a directory.

### Direct-file processing

Only files directly inside the selected directory are processed. Existing subdirectories are ignored.

Example:

```text
Downloads/
├── report.pdf      -> process
├── photo.jpg       -> process
├── song.mp3        -> process
├── Projects/       -> ignore
└── Backup/         -> ignore
```

### Categories

The organizer creates these directories inside the selected directory when needed:

```text
Documents/
Images/
Videos/
Audios/
Others/
```

### Case-insensitive extensions

Extensions are normalized to lowercase so examples such as:

```text
PHOTO.JPG
photo.jpg
Photo.JpG
```

are treated consistently.

### Supported document extensions

The current V1 list includes:

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

### Supported image extensions

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

### Supported video extensions

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

### Supported audio extensions

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

### Unsupported files

Any extension not recognized by the supported mappings is moved to:

```text
Others/
```

### Duplicate filenames

When a destination already contains a file with the same name, V1 generates a UUID-based alternative name before moving the file. This avoids overwriting the existing destination file.

## Technologies

- Python 3
- `pathlib`
- `shutil`
- `uuid`
- Standard-library filesystem operations
- Git / GitHub

Pillow is intentionally not used in V1 because the organizer only needs filename-extension classification, not image-content analysis.

## Project Structure

```text
smart_file_organizer_CLI_python/
│
├── Audios/
├── Documents/
├── Images/
├── Videos/
├── Others/
├── main.py
└── README.md
```

The category directories are created inside the selected source directory.

## Running

Check Python:

```bash
python --version
```

Run:

```bash
python main.py
```

Then enter the directory to organize.

## Architecture

The current V1 flow is:

```text
User
  ↓
Enter directory
  ↓
Validate directory
  ↓
Inspect direct children
  ↓
Normalize extension
  ↓
Classify file
  ↓
Choose destination category
  ↓
Check duplicate filename
  ↓
Generate alternative name if required
  ↓
Move file
```

## Base Version → V1 Improvements

| Area | Base Version | V1 |
|---|---|---|
| Path handling | `os` + string paths | `pathlib.Path` |
| User-selected directory | Yes | Yes |
| Direct-file processing | Partial | Yes |
| Destination paths | Hardcoded | Derived from selected directory |
| Documents | Limited set | Expanded |
| Images | Limited set | Expanded |
| Videos | Limited set | Expanded |
| Audio | Limited set | Expanded |
| Case-insensitive extensions | No | Yes |
| Duplicate protection | No | Yes |
| Unsupported files | Ignored | `Others/` |
| Automatic category folders | Partial | Yes |

## Known V1 Limitations

V1 is a learning implementation, not a production file-management utility.

### Repeated classification logic

Documents, images, videos, audio, and other files are currently processed in separate blocks. V2 should reduce this duplication.

### Hardcoded extension mappings

The extension sets are currently defined directly in the source file. V2 can centralize the category configuration.

### Duplicate naming

UUID-based names avoid collisions, but they are not especially user-friendly. V2 can explore names such as:

```text
report.pdf
report-1.pdf
report-2.pdf
```

while still checking for collisions.

### No operation summary

V1 does not yet report counts such as:

```text
Documents: 5
Images: 8
Videos: 2
Audios: 3
Others: 4
```

This is a strong V2 candidate.

### Limited filesystem error handling

Permission errors, inaccessible files, and move failures are not yet handled comprehensively.

### No dry-run

The current program performs real filesystem changes immediately.

### No recursive processing

V1 intentionally processes only direct files. Recursive scanning can be considered later.

## V2 Roadmap

V2 should focus on **refactoring and reliability**, not simply adding more extensions.

Planned candidates:

- [ ] Centralize extension-to-category mappings
- [ ] Reduce duplicated classification loops
- [ ] Create reusable helper functions
- [ ] Improve duplicate filename generation
- [ ] Add operation summary/counts
- [ ] Handle file move errors explicitly
- [ ] Handle permission errors
- [ ] Improve invalid-path handling
- [ ] Improve CLI messages
- [ ] Consider dry-run mode
- [ ] Expand edge-case testing
- [ ] Decide whether recursive processing belongs in a later version

## Testing

Important tests include:

### Valid directory

Give the program a real directory containing mixed file types.

Expected: files are moved into the correct categories.

### Invalid path

Give a nonexistent path.

Expected: the application reports that the path is not a directory.

### File instead of directory

Give the path of a single file.

Expected: the application reports that the selected path is not a directory.

### Mixed-case extensions

Examples:

```text
IMAGE.JPG
report.PDF
video.Mp4
song.MP3
```

Expected: correct categorization.

### Duplicate filename

A file with a destination name that already exists should not overwrite the existing file.

### Unsupported extension

Examples:

```text
script.py
archive.zip
random.xyz
```

Expected: move to `Others/`.

### Existing category directories

Existing category directories should not be treated as files to organize.

## Engineering Lessons

Project 1 focused on:

```text
Data
 ↓
Functions
 ↓
JSON persistence
```

Project 2 introduces:

```text
Filesystem
 ↓
Paths
 ↓
Files vs directories
 ↓
Classification
 ↓
Safe movement
```

The purpose is to learn how filesystem operations can introduce real side effects and why those operations need deliberate design.

## Project Progression

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

## Current Status

| Item | Status |
|---|---|
| Base version | Complete |
| User-selected directory | Complete |
| Directory validation | Complete |
| `pathlib` usage | Complete |
| Direct-file processing | Complete |
| Documents category | Complete |
| Images category | Complete |
| Videos category | Complete |
| Audios category | Complete |
| Others category | Complete |
| Case-insensitive extensions | Complete |
| Duplicate protection | Complete |
| Centralized classification | V2 |
| Move-error handling | V2 |
| Operation summary | V2 |
| Dry-run mode | Future |
| Recursive processing | Future |

## Author

**Abhishek**

Software Engineering & AI Engineering Learner

## Final Note

Smart File Organizer is intentionally being developed in versions.

The objective is not to create the most feature-rich file organizer. The objective is to practice:

**Understand → Design → Code → Test → Debug → Review → Refactor → Improve**

Build → Learn → Improve → Build Something Harder.
