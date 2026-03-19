from datetime import datetime

cmd_history = []
MAX_HISTORY = 100

def get_cmd_history():
    return cmd_history

def append_cmd_history(cmd, args):
    if cmd.strip():
        if len(cmd_history) >= MAX_HISTORY:
            cmd_history.pop(0)
        cmd_history.append({
            "cmd_name": cmd,
            "cmd_args": args,
            "cmd_timestamp": datetime.now().replace(microsecond=0).isoformat()
        })