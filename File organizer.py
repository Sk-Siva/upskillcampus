#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil

def create_folders(directory, folders):
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(directory):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        # Add more categories and file extensions as needed
    }

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()

            for category, extensions in file_types.items():
                if file_extension in extensions:
                    category_path = os.path.join(directory, category)
                    shutil.move(file_path, os.path.join(category_path, file))
                    print(f'Moved {file} to {category} folder')
                    break

def main():
    print("Welcome to File Organizer!")
    directory = input("Enter the directory path to organize: ")

    if not os.path.exists(directory):
        print("Directory not found. Please enter a valid directory path.")
        return

    folders = ['Images', 'Documents', 'Videos']
    create_folders(directory, folders)
    organize_files(directory)

    print("File organization completed successfully.")

if __name__ == "__main__":
    main()


# In[ ]:




