"""
The subprocess.run() function is used to run the shell command. Set shell=True to run the command in a shell environment.
capture_output=True captures the output of the command, and text=True decodes the output as text (UTF-8 by default).
The output of the shell command is stored in result.stdout and printed to the console.
"""

import subprocess

# Define the shell command you want to run
command = "ls -l"  # Example command (list files in long format)

# Run the shell command
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Print the output of the shell command
print("Shell command output:")
print(result.stdout)