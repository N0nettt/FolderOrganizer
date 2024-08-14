import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define your file types
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv")
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf", '.avi')
image = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif")
text = (".txt", ".doc", ".docx", ".odt", ".rtf", ".tex", ".wks", ".wps", ".wpd", ".epub", ".mobi", ".azw", ".html", ".htm", ".xhtml", ".md", ".csv", ".tsv", ".log", ".xlsx")
zips = ('.gz', '.zip', '.rar')

def is_audio(file):
    return os.path.splitext(file)[1].lower() in audio

def is_video(file):
    return os.path.splitext(file)[1].lower() in video

def is_image(file):
    return os.path.splitext(file)[1].lower() in image

def is_text(file):
    return os.path.splitext(file)[1].lower() in text

def is_zips(file):
    return os.path.splitext(file)[1].lower() in zips    

def organize_folder():
    if not folder_to_clear.get():
        messagebox.showwarning("Warning", "Please select a folder first.")
        return

    ext_to_file = {
        'audio': os.path.join(folder_to_clear.get(), 'Audio'),
        'video': os.path.join(folder_to_clear.get(), 'Videos'),
        'image': os.path.join(folder_to_clear.get(), 'Images'),
        'zip': os.path.join(folder_to_clear.get(), 'CompressedFiles'),
        'pdf': os.path.join(folder_to_clear.get(), 'PDFs'),
        'text': os.path.join(folder_to_clear.get(), 'Text Files'),
        'exe': os.path.join(folder_to_clear.get(), 'Install Media'),
        'other': os.path.join(folder_to_clear.get(), 'Other files')
    }

    # Create all the folders if they don't exist
    for path in ext_to_file.values():
        os.makedirs(path, exist_ok=True)

    numberOfFiles = 0

    for file in os.listdir(folder_to_clear.get()):
        full_file_path = os.path.join(folder_to_clear.get(), file)
        if not os.path.isdir(full_file_path):
            numberOfFiles += 1
            if is_audio(file):
                shutil.move(full_file_path, os.path.join(ext_to_file['audio'], os.path.splitext(file)[0]))
            elif is_video(file):
                shutil.move(full_file_path, os.path.join(ext_to_file['video'], os.path.splitext(file)[0]))
            elif is_image(file):
                shutil.move(full_file_path, os.path.join(ext_to_file['image'], os.path.splitext(file)[0]))
            elif is_text(file):
                shutil.move(full_file_path, os.path.join(ext_to_file['text'], os.path.splitext(file)[0]))
            elif is_zips(file):
                shutil.move(full_file_path, os.path.join(ext_to_file['zip'], os.path.splitext(file)[0]))
            elif os.path.splitext(file)[1] == '.pdf':
                shutil.move(full_file_path, os.path.join(ext_to_file['pdf'], os.path.splitext(file)[0]))
            elif os.path.splitext(file)[1] == '.exe':
                shutil.move(full_file_path, os.path.join(ext_to_file['exe'], os.path.splitext(file)[0]))
            else:
                shutil.move(full_file_path, os.path.join(ext_to_file['other'], os.path.splitext(file)[0]))

    messagebox.showinfo("Success", f"Successfully moved {numberOfFiles} files!")
    os.startfile(folder_to_clear.get())

def select_folder():
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        folder_to_clear.set(selected_folder)
        #check number of files in the folder
        num_files = len([f for f in os.listdir(selected_folder) if os.path.isfile(os.path.join(selected_folder, f))])
        folder_path_label.config(text=f"Folder Path: {selected_folder}")
        file_count_label.config(text=f"Number of Files: {num_files}")

# Create the GUI
root = tk.Tk()
root.title("File Organizer")

# Calculate screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size
window_width = 400
window_height = 200

# Calculate position
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Define Tkinter variables
folder_to_clear = tk.StringVar()

# Add a button to select the folder
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=10)

# Add a button to start the organization
organize_button = tk.Button(root, text="Organize Files", command=organize_folder)
organize_button.pack(pady=10)

# Add labels to display folder path and file count
folder_path_label = tk.Label(root, text="Folder Path: Not Selected")
folder_path_label.pack(pady=5)

file_count_label = tk.Label(root, text="Number of Files: 0")
file_count_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
