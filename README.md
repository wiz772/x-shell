# X-Shell

A simple custom shell built in Python that supports basic commands, history, and error handling.  

---

## Features

- Builtin commands: `help`, `type`, `exit`, `echo`, `pwd`, `clear`, `cd`, `ls`, `history`  
- External command execution (calls system commands if available in PATH)  
- Command history tracking  
- Centralized error handling with optional detailed error display  
- `cd` supports `~`, spaces in paths, and robust error messages  
- `ls` lists files and directories with optional indexing  
- Ready for future extensions like autocomplete and colorized output  

---

## Installation

1. Make sure Python 3 is installed  
2. Clone or download the repository  
3. Run the shell:

```bash
python main.py
