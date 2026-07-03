# FileReader 1.1

FileReader is a simple Python project that can read the contents of a text file aloud or directly speak text entered by the user. It uses the built-in Windows Speech API through PowerShell and works offline.

## About

This project was built as one of my first Python projects to practice:

- File Handling
- Loops
- Conditional Statements
- User Input
- Text-to-Speech
- Working with the `os` module

## Features

- Read any text file from your computer.
- Speak the contents of a text file.
- Speak text entered directly by the user.
- Automatically checks whether a file exists.
- Displays the file content before speaking it.
- Supports continuous input using a loop.
- Works completely offline on Windows.

## Technologies Used

- Python 3
- Python os module
- Windows PowerShell Speech API

## Project Structure

```
FileReader/
│
├── main.py
├── default.txt
└── README.md
```

## How to Run

### Clone the repository

```bash
git clone https://github.com/vaibhav-vyas-01/FileReader.git
```

### Open the project

```bash
cd FileReader
```

### Run the program

```bash
python main.py
```

## Example

### Speaking Text

```
Enter full file path OR text:

Hello, my name is Vaibhav.
```

Output

```
The computer speaks:

Hello, my name is Vaibhav.
```

### Reading a File

```
Enter full file path OR text:

C:\Users\Vaibhav\Desktop\notes.txt
```

Output

```
The file is displayed on the screen.

The computer reads the contents aloud.
```

## Current Limitations

- Designed for Windows.
- Uses PowerShell for speech output.
- Very large text files may not perform as well because the speech command is sent through PowerShell.

## Future Improvements

- Graphical User Interface (Tkinter)
- File Picker
- Voice Selection
- Speech Rate Control
- PDF Reader Support
- Better handling of large text files
- Cross-platform support

## Learning Outcome

While building this project, I learned:

- Reading files using Python
- Checking file existence
- Using loops for continuous execution
- Working with user input
- Integrating Python with Windows PowerShell
- Building a simple command-line application


## Author

**Vaibhav Vyas**

GitHub: https://github.com/vaibhav-vyas-01
