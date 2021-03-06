# Case-study 8.2
# Raspopova Alexandra (50%)
# Adristi Fauzi (40%)
# Belozertseva Maria (30%)

import os
import pathlib


def main():
    '''
    The main function that outputs the path to the current directory and the menu. Calls the command execution function.
    :return: None
    '''
    print(os.getcwd())
    function = acceptCommand()
    runCommand(function)


def acceptCommand():
    function = int(input('1. Просмотр каталога \n2. На уровень вверх \n3. На уровень вниз '
                         '\n4. Количество файлов и каталогов \n5. Размер текущего каталога (в байтах) '
                         '\n6. Поиск файла \n7. Выход из программы \nВыберите пункт меню: '))
    if function < 1 or function > 7:
        print("Номер пункта введен неверно, попробуйте еще раз.")
        return acceptCommand()
    return function


def runCommand(command):
    if command == 1:
        return paths()
    elif command == 2:
        return moveUp()
    elif command == 3:
        currentDir = os.getcwd()
        moveDown(currentDir)
    elif command == 4:
        path = input("Введите путь к нужному каталогу: ")
        return countFiles(path)
    elif command == 5:
        path = input("Введите путь к нужному каталогу: ")
        print(countBytes(path))
    elif command == 6:
        target=input("Введите имя файла, который нужно найти: ")
        path=input("Введите путь к нужному каталогу: ")
        findFiles(target, path)
    elif command == 7:
        print("Выход из программы.")
        exit()

        
def paths():  # просмотр каталога
    currentDirectory = pathlib.Path('.')
    for currentFile in currentDirectory.iterdir():
        if os.path.isfile(currentFile):
            print('Файл:', currentFile)
        if os.path.isdir(currentFile):
            print('Каталог:', currentFile)
    runCommand(acceptCommand())


def moveUp():  # перейти на уровень вверх
    currentDirectory = os.getcwd()
    m = currentDirectory
    l = (m.rfind('\\'))
    if len(m) != 3:
        str = m[:l]
    else:
        str = m[:l + 1]
    os.chdir(str)
    print((str))
    runCommand(acceptCommand())


def moveDown(currentDir): #перейти на уровень вниз
    sub=input('Введите имя подкаталога: ')
    if os.path.exists(sub):
        os.chdir(currentDir+'\\'+sub)
        print(os.getcwd())
    print("Неверно введено имя подкаталога")
    runCommand(acceptCommand())

def countFiles(path): #подсчитывает количество файлов в указанном каталоге
    totalFiles = 0
    totalDir = 0
    for base, dirs, files in os.walk(path):
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    print('Total number of files', totalFiles)
    print('Total Number of directories', totalDir)
    print('Total:', (totalDir + totalFiles))
    runCommand(acceptCommand())


def countBytes(path): #подсчитывает суммарный объем (в байтах) всех файлов в указанном каталоге
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += countBytes(entry.path)
    except FileNotFoundError:
        print("Каталога не существует.")
    except NotADirectoryError:
        return os.path.getsize(path)
    except PermissionError:
        print("Нет доступа к данному каталогу.")
        return 0
    return total


def findFiles(target, path):
    path_list=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(target):
                path_file = os.path.join(root, file)
                path_list.append(path_file)
    if len(path_list)!=0:
        print(*path_list)
    print("Файла нет ни в одном из каталогов.")
    runCommand(acceptCommand())


main()
