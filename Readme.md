# File Sorter (Python)

A simple Python script to automatically organize files in a folder based on their file types.

The script scans a specified directory and moves files into categorized folders such as Images, Documents, Code, and Others, making file organization quick and effortless.

## Features
- Automatically sorts files into predefined categories
- Creates folders if they do not already exist
- Skips directories and processes only files
- Displays a summary of sorted files
- Simple command-line interface

## Categories
- **Images**: `.jpg`, `.png`
- **Documents**: `.pdf`, `.txt`, `.docx`, `.pptx`
- **Code**: `.py`, `.js`
- **Others**: All remaining file types

## Requirements
- Python 3.x

## Installation
Clone the repository:
```bash
git clone https://github.com/your-username/file-sorter.git
cd file-sorter
Usage

Run the script using Python:

python file_sorter.py


When prompted, enter the full path of the folder to be sorted:

Enter the folder location: C:\Users\YourName\Downloads

Example

Before:

photo.jpg
script.py
report.pdf
notes.txt
archive.zip


After:

Images/
  photo.jpg
Code/
  script.py
Documents/
  report.pdf
  notes.txt
Others/
  archive.zip