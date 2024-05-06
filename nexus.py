import sys
import os
import subprocess
import webbrowser
import win32gui
import win32con

def run_command_in_cmd(command):
    try:
        # Open Command Prompt and execute the command
        subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', command], shell=True)
    except Exception as e:
        print("An error occurred:", e)

def minimize_cmd_window():
    # Find the Command Prompt window by its title containing the specified substring
    cmd_window = None
    substr = "Command Prompt: C:\\Windows\\system32\\cmd.exe - python manage.py runserver 192.168.4.134:8000"
    def callback(hwnd, extra):
        if substr in win32gui.GetWindowText(hwnd):
            extra.append(hwnd)

    windows = []
    win32gui.EnumWindows(callback, windows)
    if windows:
        cmd_window = windows[0]

    print("Window handle:", cmd_window)
    if cmd_window:
        # Minimize the Command Prompt window
        win32gui.ShowWindow(cmd_window, win32con.SW_MINIMIZE)
        print("Command Prompt window minimized.")
    else:
        print("Command Prompt window not found.")

def main():
    # Determine the path to the directory containing the script
    script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    # Change directory to the script directory
    os.chdir(script_dir)

    # Example usage
    command_to_execute = "python manage.py runserver 192.168.4.134:8000"
    run_command_in_cmd(command_to_execute)

    # Minimize the Command Prompt window
    minimize_cmd_window()

    # Open the server in the browser
    url = "http://192.168.4.134:8000"
    webbrowser.open(url)

if __name__ == "__main__":
    main()
