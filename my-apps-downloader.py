'''Current version: 0.1.1'''

import os
import sys
import pathlib

# Prevents potential conflict between auto-py-to-exe and concurrent.futures
# See explanation: https://nitratine.net/blog/post/issues-when-using-auto-py-to-exe/?utm_source=auto_py_to_exe&utm_medium=readme_link&utm_campaign=auto_py_to_exe_help#using-concurrentfutures
from multiprocessing import freeze_support

# Combines multithreading and progress bars
from tqdm.contrib.concurrent import thread_map

import apps

def get_answer():
    while True:
        answer = input("Would you like to proceed? (y/n) ").strip().lower()
        if answer in ('yes', 'y', 'no', 'n'):
            return answer

def download_app(app):
    '''Scrapes an app's website, finds the link to download the setup files,
    and downloads it.
    
    ----PARAMETER----
    app: an instance of the App class'''
    
    # Check that direct download url isn't already provided
    if app.download_url == None:
        app.request_page()
        app.get_content_type()
        if app.content_type == 'HTML':
            app.get_html_links()            
        elif app.content_type == 'JSON':
            app.get_json_links()
        app.get_download_url()
    app.get_file_name()
    app.download_installer()

if __name__ == '__main__':
    # Ask user for confirmation
    print("The following software will be downloaded:")
    [print("- " + key) for key in apps.programs.keys()]
    answer = get_answer()
    if answer in ('no', 'n'):
        sys.exit()
    
    # Where to download the files
    directory = os.path.join('Desktop', 'installers')
    download_path = os.path.join(pathlib.Path.home(), directory)

    # Check if download directory already exists
    if not os.path.isdir(download_path):
        os.mkdir(download_path)
    os.chdir(download_path)

    freeze_support() # keeps concurrent.futures from causing issues

    apps_list = list(apps.programs.values())
    # For testing purposes
    # names = list(apps.programs.keys())[:10]
    # print(names)
    # sample = apps_list[:10]
    # Download everything from apps.py
    # 6 threads is the sweet spot for performance with 30-40 apps
    thread_map(download_app, apps_list, max_workers=6, colour='green')

    # Alternative for multithreading (but no progress bar)
    # import concurrent.futures
    # with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    #     executor.map(download_app, apps.programs.values())

    print("All files successfully downloaded.")

    while True:
        open_folder = input("The program will now exit. Would you like to open the destination folder? (y/n) ").strip().lower()
        if open_folder in ('yes', 'y'):
            # Open target folder
            path = os.path.realpath(download_path)
            os.startfile(path)
            sys.exit()
        elif open_folder in ('no', 'n'):
            sys.exit()