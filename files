__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# clean_cache: takes no arguments and creates an empty folder named cache
# in the current directory. If it already exists,
# it deletes everything in the cache folder.

import os
from zipfile import ZipFile
from pathlib import Path


def clean_cache():
    workdir = os.path.join(os.getcwd(), 'files')
    dir = os.path.join(workdir, 'cache')
    if not os.path.exists(dir):
        os.mkdir(dir)
    else:
        for file in os.listdir(dir):
            path = os.path.join(dir, file)
            os.remove(path)


# cache_zip: takes a zip file path (str) and a cache dir path (str) as
# arguments, in that order. The function then unpacks the indicated zip file
# into a clean cache folder. You can test this with data.zip file.

def cache_zip(zip_path, cache_path):
    clean_cache()
    workdir = os.path.join(os.getcwd(), 'files')
    zip_path = os.path.join(workdir, zip_path)
    cache_path = os.path.join(workdir, cache_path)
    ZipFile(zip_path).extractall(cache_path)


cache_zip('data.zip', 'cache')


# cached_files: takes no arguments and returns a list of all the files
# in the cache. The file paths should be specified in absolute terms.
# Search the web for what this means! No folders should be included in the
# list. You do not have to account for files within folders within the cache
# directory.

def cached_files():
    workdir = os.path.join(os.getcwd(), 'files')
    dir = os.path.join(workdir, 'cache')
    cached_files_list = []
    for file in os.listdir(dir):
        cached_files_list.append(os.path.abspath(os.path.join(dir, file)))
    return cached_files_list


# find_password: takes the list of file paths from cached_files as an argument.
# This function should read the text in each one to see if the password is in
# there. Surely there should be a word in there to indicate the presence of the
# password? Once found, find_password should return this password string.
cached_files_list = cached_files()


def find_password(cached_files_list):
    for file in cached_files_list:
        content = Path(file).read_text()
        # check if string present or not
        if 'password' in content:
            password = content[content.find('password'):]
            password_list = password.split()
            return password_list[1]
