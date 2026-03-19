import shutil

def is_cmd_exe_in_path(cmd):
    path = shutil.which(cmd)
    if path:
        return True
    return False

def print_error_question(error):
    print("an error occurred")
    while True:
        answer = input("Print the error? (y/n): ").lower()
        if answer == "y":
            print(error)
            break
        elif answer == "n":
            break
        else:
            print("Please enter y or n.")

