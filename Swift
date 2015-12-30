from os import system
import sys
from os.path import exists
from os.path import isdir

def help():
	print("To create a Swift package, please command: python swift.py <your_project_name>")

def check_workspace():
	if isdir('/home/mint/swift/workspace') == True:
		print("Checking workspace... Done!")
	else:
		print("Workspace is not exists. Making workspace...")
		system("mkdir swift/workspace")

def run_command(n):
	print("Making " + n + " project folder...")
	system("mkdir swift/workspace/" + n)
	print("Making Package.swift...")
	system("touch swift/workspace/" + n + "/Package.swift")
	print("Making Sources folder...")
	system("mkdir swift/workspace/" + n + "/Sources")
	print("Making main.swift...")
	system("touch swift/workspace/" + n + "/Sources/main.swift")
	print("Openning main.swift...")
	system("gedit swift/workspace/" + n + "/Sources/main.swift")

if len(sys.argv) == 1:
	help()

if len(sys.argv) == 2:
	check_workspace()
	if isdir('/home/mint/workspace/' + sys.argv[1]) == True:
		print("This project is already exists. Please enter other project name.\n")
		exit(0)
	else:	
		run_command(sys.argv[1])
