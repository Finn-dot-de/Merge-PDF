# PDF Merge Tool

## Description
The **PDF Merge Tool** is a simple Python script that automatically detects, sorts, and merges all PDF files in the current directory into a single file. The order of the PDFs is determined by their filenames – either numerically (e.g., 1, 2, 3) or alphabetically (A, B, C). The merged file is saved as `merged.pdf`.

## Features
- Automatic detection of all PDFs in the current folder
- Sorting of files by numerical or alphabetical order
- Merging of all PDFs into a single file using PyPDF2
- Output of the merged file as `merged.pdf`
- Error message if no PDFs are found in the directory

## Installation
### Requirements
- Python 3.x
- PyPDF2 library

Install PyPDF2 with:
```sh
pip install PyPDF2
```

### Creating an Executable File (Windows)
If you want to compile the script into an `.exe`, you can use `pyinstaller`:
```sh
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=icon.ico --name "MergePDFs" main.py
```
The `.exe` file will be located in the `dist` folder.

## Usage
1. Place all the PDF files you want to merge into a folder.
2. Run the script:
   ```sh
   python main.py
   ```
3. If using the `.exe`, simply run `MergePDFs.exe`.
4. The file `merged.pdf` will be created in the same directory.

## License
This project is released under the MIT License. Feel free to use it for personal and commercial purposes.

