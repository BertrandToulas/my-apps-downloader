'''TO TEST A NEWLY-ADDED PROGRAM'''

import os
import pathlib

import apps

def download_app(app):
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
    directory = os.path.join('Desktop', 'installers')
    download_path = os.path.join(pathlib.Path.home(), directory)
    if not os.path.isdir(download_path):
        os.mkdir(download_path)
    os.chdir(download_path)
    path = os.path.realpath(download_path)
    os.startfile(path)

    # Insert app to test here
    to_test = apps.programs['insert_app_name']
    download_app(to_test)

    print(f"{to_test} successfully downloaded.")