import sys
import os
import subprocess
import builtin_commands
import utils
import cache

builtin_commands = builtin_commands.commands

def get_inputs():
    user_input = input().strip()
    if not user_input:
        return None, []
    
    parts = user_input.split()
    command = parts[0]
    args = parts[1:] if len(parts) > 1 else []
    return command, args

def execute_cmd():
    command, args = get_inputs()
    if not command:
        return
    try:
        if command in builtin_commands:
            builtin_commands[command][0](args)
        else:
            if utils.is_cmd_exe_in_path(command):
                subprocess.run([command] + args, shell=True)
            else:
                print(f"{command}: command not found")
        cache.append_cmd_history(command,args)
    except Exception as e:
        utils.print_error_question(e)

def main():
    while True:
        sys.stdout.write(f"{os.getcwd()} $ ")
        execute_cmd()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ngoodbye.")
        sys.exit(0)
