import gsparser

parser = gsparser.GsParser()
print("Parsing!")
parser.getAllKeysFromShell()
print("Saving!")
parser.saveKeysInTextFile("report.txt")
print("Saving csv!")
parser.saveKeysInCsvFile("2222.csv")
