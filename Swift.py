#!/usr/bin/python
import os, sys, os.path

def help():
	print("To create a Swift package, please command: python swift.py <your_project_name>")

def check_workspace():
	if os.path.isdir(os.path.expanduser("~") + '/swift/workspace') == True:
		print("Checking workspace... Done!")
	else:
		print("Workspace is not exists. Making workspace...")
		os.system("mkdir ~/swift/workspace")

def run_command(n):
	os.chdir(os.path.expanduser("~") + '/swift/workspace')
	print("Making " + n + " project folder...")
	os.system("mkdir " + n)
	print("Making Package.swift...")
	os.system("touch Package.swift")
	print("Making Sources folder...")
	os.system("mkdir " + n + "/Sources")
	print("Making main.swift...")
	os.system("touch ~/swift/workspace/" + n + "/Sources/main.swift")
	print("Openning main.swift...")
	os.system("gedit ~/swift/workspace/" + n + "/Sources/main.swift")

if len(sys.argv) == 1:
	help()

if len(sys.argv) == 2:
	check_workspace()
	os.chdir(os.path.expanduser("~") + '/swift/workspace')
	if os.path.isdir(sys.argv[1]) == True:
		print("This project is already exists. Please enter other name.")
		exit()
	else:	
		run_command(sys.argv[1])
