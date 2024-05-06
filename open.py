import tkinter as tk
import subprocess
import os

def open_cms():
    python_file = os.path.join(os.path.dirname(__file__), "nexus.py")
    subprocess.Popen(["python", python_file])
    # Close the Tkinter window
    root.destroy()

# Create main window
root = tk.Tk()
root.title("NEXUS")

# Add heading
heading = tk.Label(root, text="NEXUS", font=("Arial", 18))
heading.pack(pady=20)

# Add button
open_cms_button = tk.Button(root, text="Open CMS", command=open_cms)
open_cms_button.pack(pady=10)

# Run the main event loop
root.mainloop()
