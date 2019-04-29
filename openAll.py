###################################################
#     @author Richard Martínez 2019/04/26         #
#     Open masive Programs, Folders and files     #
#     All Settings is in openAll.ini              #
###################################################
import subprocess, json, os

try:
	from configparser import ConfigParser
except ImportError:
	from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()
config.read('openAll.ini')

def decodeIni(str):
	return json.loads(str.replace("\\", "/"))

#TODO:controlar cuando la carpeta o el archivo o el programa no existen
#TODO:if list is empty not process

openingList = decodeIni(config.get("APPS", "APPS_LIST"))
print("Opening Apps:")
for x in openingList:
	#TODO:Verificar si el programa ya está abierto
	#TODO:check if proccess complete open next process
	subprocess.Popen(x)
	print(x)

openingList = decodeIni(config.get("FOLDERS", "FOLDERS_LIST"))
print("Opening Folders:")
for x in openingList:
	#TODO:Verificar si la carpeta ya está abierta
	os.startfile("\"%s\"" % (x))
	print(x)

openingList = decodeIni(config.get("FILES", "FILES_LIST"))
print("Opening Files:")
for x in openingList:
	#TODO:open with default app
	#TODO:Verificar si el archivo ya está abierto
	os.startfile("\"%s\"" % (x))
	print(x)
