from os import listdir, mkdir, environ
from os.path import isfile, join
import shutil
import logging

logger = logging.getLogger()
logger.setLevel("INFO")

def getfiles(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f)) and f != 'organizer.py']

def getfolders(dir):
    return [f for f in listdir(dir) if not isfile(join(dir, f))]


desktop_path = join(join(environ['USERPROFILE']), 'Desktop')

files = getfiles(desktop_path)
folders = getfolders(desktop_path)
extensions = []

for a in files:
    a_ext = a.split('.')[-1].lower()
    if a_ext not in extensions:
        extensions.append(a_ext)
        if a_ext not in folders:
            mkdir(f'{desktop_path}\\{a_ext}')
            folders.append(a_ext)
            logger.info(f"Folder \"{desktop_path}\\{a_ext}\" created.")
    try:
        shutil.move(f'{desktop_path}\\{a}', f'{desktop_path}\\{a_ext}')
    except shutil.Error as err:
        logger.error(f"\"{a}\" already exists within folder \"{desktop_path}\\{a_ext}\". File will not be moved.")
    else:
        logger.info(f"Moved file \"{a}\" to \"{desktop_path}\\{a_ext}\"")