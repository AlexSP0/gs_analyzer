import gskey
import gsparser

parser = gsparser.GsParser()
print("Parsing!")
parser.getAllKeysFromShell()
print("Saving!")
parser.saveKeysInTextFile("2222.txt")
print("Saving csv!")
parser.saveKeysInCsvFile("2222.csv")
