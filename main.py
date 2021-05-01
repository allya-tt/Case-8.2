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
        return path()
    elif command == 2:
        return moveUp()
    #elif command == 3:
        #return moveDown(currentDir)
    #elif command == 4:
        #return countFiles(path)
    #elif command == 5:
        #return countBytes(path)
    #elif command == 6:
        #return findFiles(target, path)
    elif command == 7:
        print("Выход из программы.")
        exit()


# определение пути

def path():
    currentDirectory = pathlib.Path('.')
    for currentFile in currentDirectory.iterdir():
        if os.path.isfile(currentFile):
            print('Файл:', currentFile)
        if os.path.isdir(currentFile):
            print('Каталог:', currentFile)
    runCommand(acceptCommand())


def moveUp():
    os.path.join(os.path.dirname(__file__), os.pardir)


main()
