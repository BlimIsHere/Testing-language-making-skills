import re

def interpret_log_command(command):
    # Use regex to match the command in the format log "message"
    match = re.match(r'log\s+"([^"]+)"', command)
    if match:
        # Extract the message and print it
        message = match.group(1)
        print(message)
    else:
        print("Invalid command format. Use: log \"message\"")

# Example usage
interpret_log_command('log "Hello, World!"')
interpret_log_command('log "This is a test message."')
