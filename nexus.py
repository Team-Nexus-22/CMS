import subprocess
import time
import webbrowser

def run_command_in_cmd(command):
    try:
        # Open Command Prompt and execute the command
        subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', command], shell=True)
    except Exception as e:
        print("An error occurred:", e)

    # Wait for a moment for the server to start
    time.sleep(5)  # Adjust the time as needed
    
    # Open the server in the browser
    url = "http://192.168.4.134:8000"
    webbrowser.open(url)

# Example usage
command_to_execute = "python manage.py runserver 192.168.4.134:8000"
run_command_in_cmd(command_to_execute)
