import shutil


def copy_file(name, path=None):
    try:
        if path is not None and path != '':
            shutil.copyfile(f"{path}\\{name}", 'Additional_files/temporary_data.ams')
        else:
            shutil.copyfile(f"{name}", 'Additional_files/temporary_data.ams')
        return True
    except:
        return False
