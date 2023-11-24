import os

def removeEmptyFolders(path, removeRoot=True):
    if not os.path.isdir(path):
        return

    # видалення пустих підпапок папок
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)

    # видалення пустих папок
    files = os.listdir(path)
    if len(files) == 0 and removeRoot:
        print("Removing empty folder:", path)
        os.rmdir(path)