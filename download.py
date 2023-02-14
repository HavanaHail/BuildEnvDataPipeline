from office365_api import SharePoint
import re
import sys
from pathlib import PurePath

folder_name = sys.argv[1]

folder_dest = sys.argv[2]
#vvv this should be 'None' if all files are to be downloaded
file_name = sys.argv[3]
#vvv this should be 'None' if no pattern match is needed
file_name_pattern = sys.argv[4]

def save_file(file_name, file_obj):
    file_dir_path = PurePath(folder_dest, file_name)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)

def get_file(file_name, folder):
    file_obj = SharePoint()._download_file(file_name, folder)
    save_file(file_name, file_obj)

def get_files(folder):
    files_list = SharePoint()._get_file_list(folder)
    for file in files_list:
        get_file(file.name, folder)

def get_files_by_pattern(keyword, folder):
    files_list = SharePoint()._get_file_list(folder)
    for file in files_list:
        if re.search(keyword, file.name):
            get_file(file.name, folder)

if __name__ == '__main__':
    if file_name != 'None':
        get_file(file_name, folder_name)
    elif file_name_pattern != 'None':
        get_files_by_pattern(file_name_pattern, folder_name)
    else:
        get_files(folder_name)