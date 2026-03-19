import os
import sys
import subprocess
import shutil
import cache

def cmd_type(args):
    if not args:
        print("type: missing argument")
        return

    cmd = args[0]
    if cmd in commands:
        print(f"{cmd} is a shell builtin")
        return

    path = shutil.which(cmd)
    if path:
        print(f"{cmd} is {path}")
        return

    print(f"{cmd}: not found")

def cmd_echo(args):
    print(" ".join(args))

def cmd_exit(args):
    sys.exit(0)

def cmd_pwd(args):
    print(os.getcwd())

def cmd_clear(args):
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.run(cmd, shell=True)

def cmd_cd(args):
    if not args or args[0] == "~":
        path = os.path.expanduser("~")
    else:
        path = " ".join(args).strip('"')
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"cd: {path}: no such file or directory")
    except NotADirectoryError:
        print(f"cd: {path}: is not a directory")
    except PermissionError:
        print(f"cd: {path}: not authorized")

def cmd_ls(args):
    cwd = os.getcwd()
    index = 1
    for index, file in enumerate(sorted(os.listdir(cwd)), start=1):
        path_to_file = os.path.join(cwd, file)
        if os.path.isdir(path_to_file):
            print(f"{index}: {file}/")
        else:
            print(f"{index}:", file)
        index+=1

def cmd_history(args):
    for command in cache.get_cmd_history():
        cmd_name = command["cmd_name"]
        cmd_args = " ".join(command["cmd_args"])
        cmd_timestamp = command["cmd_timestamp"]
        print(f"- {cmd_timestamp} : {cmd_name} {cmd_args} ")

def cmd_help(args):
    for name, (_, desc) in commands.items():
        print(f" - {name}: {desc}")

commands = {
    "help": (cmd_help, "Display the help menu."),
    "type": (cmd_type, "Show the type of a command."),
    "exit": (cmd_exit, "Exit the shell."),
    "echo": (cmd_echo, "Print a message."),
    "pwd": (cmd_pwd, "Print the current working directory."),
    "clear": (cmd_clear, "Clear the terminal."),
    "cd": (cmd_cd, "Change the current directory."),
    "ls": (cmd_ls, "List directory contents."),
    "history": (cmd_history, "Show command history.")
}