import gskey
import csv
import subprocess

class GsParser:
    keys = None

    def getAllKeysFromShell(self):
        #получаем все ключи из оболочки
        print("Parsing keys!")
        keys_list = subprocess.run(["gsettings", "list-recursively"], stdout=subprocess.PIPE, text=True)
        
        #разбиваем их по строкам
        lines = keys_list.stdout.splitlines(True)

        #Парсим путь и имя ключа
        self.keys = []
        for line in lines:
            new_key = gskey.GsKey()
            new_key.parsePathAndName(line)
            self.keys.append(new_key)
        
        #Парсим тип ключа и перечислители, если они есть
        print("Parsing types!")
        for key in self.keys:
            print("Parsing type for: " + key.path + " " + key.name)
            key_type = subprocess.run(["gsettings", "range", key.path, key.name], stdout=subprocess.PIPE, text=True)
            key.parseType(key_type.stdout)

        #Парсим описание ключа
        print("Parsing descriptions!")
        for key in self.keys:
            print("parsing descriptions key: " + key.name)
            key_description = subprocess.run(["gsettings", "describe", key.path, key.name], stdout=subprocess.PIPE, text=True )
            key.parseDescription(key_description.stdout)

    #загружаем ключи из текстового файла
    def loadKeysFromTextFile(self, filename):
        print("Загружаем ключи из файла: " + filename)
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        self.keys = []
        for line in lines:
            new_key = gskey.GsKey()
            new_key.setKeyFromLine(line)
            self.keys.append(new_key)

    #сохраняем ключи в тектовый файл
    def saveKeysInTextFile(self, filename):
        file = open(filename, "w")
        for key in self.keys:
            file.write(key.getTotalLine())
        file.close()
        
        #сохраняем ключи в виде csv-файла
    def saveKeysInCsvFile(self, filename):
        csv_file = open(filename, "w", encoding='utf-8')
        file_writer = csv.writer(csv_file, delimiter = "|", lineterminator="\n")
        for key in self.keys:
            file_writer.writerow([key.path, key.name, key.type, key.description, key.enum_parameters_or_range])
        csv_file.close()
