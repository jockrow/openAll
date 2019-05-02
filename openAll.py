###################################################
#     @author Richard Martínez 2019/04/26         #
#     Open masive Programs, Folders and files     #
#     All Settings is in openAll.ini              #
###################################################
import subprocess, json, os, psutil, re

try:
	from configparser import ConfigParser
except ImportError:
	from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()
config.read('openAll.ini')

def runningProcess(processName):
	return re.sub(r".*/", "", processName) in (p.name() for p in psutil.process_iter())

def openList(typeKey):
	list = json.loads(config.get(typeKey, typeKey + "_LIST").replace("\\", "/"))
	if len(list) > 0:
		print("OPENING " + typeKey + ":")
		for x in list:
			print("DEBUG:" + x)
			message = ""
			if typeKey == "APPS":
				#TODO:check if proccess complete open next process
				#DONE:Verificar si el programa ya está abierto
				if runningProcess(x):
					message = "CURRENT APP IS RUNNING:"
				else:
					subprocess.Popen(x)
			else:
				if not os.path.exists(x):
					message = typeKey.replace("S", "") + " IS NOT EXISTS:"
					#TODO:Verificar si el archivo ya está abierto
					#message = "CURRENT " + typeKey + " IS OPENING:"
				else:
					os.startfile("\"%s\"" % (x))
			message += x
			print(message)

openList("APPS")
openList("FOLDERS")
openList("FILES")