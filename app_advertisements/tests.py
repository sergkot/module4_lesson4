from django.test import TestCase


# Create your tests here.

def get_files_from_media():
    import os
    os.chdir('..')
    os.chdir('media')
    path = os.getcwd()
    print(path)
    # чтение записей
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            # печать всех записей, являющихся файлами
            if entry.is_file():
                print(entry.name)

if __name__ == '__main__':
    get_files_from_media()
