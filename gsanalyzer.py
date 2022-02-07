from typing import final
import gsparser
import gskey

NOT_VERIFIED = 0
VERIFIED = 1
MISSING = 2


class GsAnalyzer:
    prevGsKeys = None
    currentGsKeys = None

    def __init__(self, prevGsFile):
        self.prevGsFile = prevGsFile
        gsPrevParser = gsparser.GsParser()
        gsCurrentParser = gsparser.GsParser()
        
        #парсим предыдущие ключи в объекты
        gsPrevParser.loadKeysFromTextFile(prevGsFile)

        #парсим ключи из текущей системы
        gsCurrentParser.getAllKeysFromShell()

        self.prevGsKeys = gsPrevParser.keys
        self.currentGsKeys = gsCurrentParser.keys 

    def compareAllPaths(self, filename):
        #создание словарей
        print("Сравниваем пути")
        #создаем словари для путей
        prevKeysPaths = {}
        currentKeysPath = {}
        #заполняем словари путями
        for prevKey in self.prevGsKeys:
            prevKeysPaths[prevKey.path] = False
        for currentKey in self.currentGsKeys:
            currentKeysPath[currentKey.path] = NOT_VERIFIED
        #Сравниваем словари
        for path in prevKeysPaths:
            if path in currentKeysPath:
                currentKeysPath[path] = VERIFIED
            else:
                currentKeysPath[path] = MISSING
        #сохраняем отчет в текстовый файл
        file = open(filename, "w")
        for keyPath in currentKeysPath:
            if(currentKeysPath[keyPath] == VERIFIED):
                continue
            else:
                line = "Path: " + currentKeysPath[keyPath] + " "
                if(currentKeysPath[keyPath]) == NOT_VERIFIED:
                    print("Путь: " + keyPath + " НОВЫй")
                    line = line + " NEW!"
                else: #MISSING
                    print("Путь: " + keyPath + " УДАЛЕН")
                    line = line + " DELETED!"
                file.write(line)
        file.close() 

    def compareAllKeys(self, filename):
        print("Сравнивае ключи:")

    def comparePath(prevKey, currentKey):
        if(prevKey.path != currentKey.path):
            return False
        else:
            return True 


