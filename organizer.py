from os import listdir, mkdir, environ
from os.path import isfile, join
from shutil import move

def getfiles(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f)) and not 'organizer.py']

def getfolders(dir):
    return [f for f in listdir(dir) if not isfile(join(dir, f))]

desktop_path = join(join(environ['USERPROFILE']), 'Desktop')

files = getfiles(desktop_path)
folders = getfolders(desktop_path)
extensions = []

for a in files:
    print(a)
    a_ext = a.split('.')[-1].lower()
    if a_ext not in extensions:
        extensions.append(a_ext)
        if a_ext not in folders:
            mkdir(f'{desktop_path}\\{a_ext}')
            folders.append(a_ext)
    move(f'{desktop_path}\\{a}', f'{desktop_path}\\{a_ext}')

        

           