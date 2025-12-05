import os
import shutil

# Define the main directory where the folders will be organized
main_directory = "organized_files"

# Define the categories and their extensions
file_types = {
    'audio': ['.wav', '.aiff'],
    'images': ['.jpeg', '.jpg', '.png'],
    'documents': ['.pdf', '.docx', '.txt']
}

# Create the main directory if it doesn't exist
if not os.path.exists(main_directory):
    os.makedirs(main_directory)

# Create subfolders for each category

