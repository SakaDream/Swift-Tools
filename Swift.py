#!/usr/bin/python
import os, sys, os.path

def help():
	print("To create or open a Swift package, please command: ./swift.py <your_project_name>\n")
	print("To see your projects as a list, please command: ./swift.py ls")

def check_workspace():
	if os.path.isdir(os.path.expanduser("~") + '/swift/workspace') == True:
		print("Checking workspace... Done!")
	else:
		print("Workspace doeexists. Making workspace...")
		os.system("mkdir ~/swift/workspace")

def create_project(n):
	print("Making " + n + " project folder...")
	os.system("mkdir ~/swift/workspace/" + n)
	print("Making Package.swift...")
	os.system("touch ~/swift/workspace/" + n + "/Package.swift")
	print("Making Sources folder...")
	os.system("mkdir ~/swift/workspace/" + n + "/Sources")
	print("Making main.swift...")
	os.system("touch ~/swift/workspace/" + n + "/Sources/main.swift")
	print("Openning main.swift...")
	os.system("gedit ~/swift/workspace/" + n + "/Sources/main.swift")

def open_project(n):
	print("Openning project...")
	os.system("gedit ~/swift/workspace/" + n + "/Sources/main.swift")

def list_projects():
	print("List of projects:\n")
	os.system("cd ~/swift/workspace && ls")

def remove_project(n):
	print("Removing project...")
	os.system("rm -r ~/swift/workspace/" + n)
	print("Remove complete!")

if len(sys.argv) == 1:
	help()

if len(sys.argv) == 2:
	if sys.argv[1] == "ls":
		list_projects()
	else:
		check_workspace()
		os.chdir(os.path.expanduser("~") + '/swift/workspace')
		if os.path.isdir(sys.argv[1]) == True:
			open_project(sys.argv[1])
		else:
			create_project(sys.argv[1])

if(len(sys.argv)) == 3:
	os.chdir(os.path.expanduser("~") + '/swift/workspace')
	if os.path.isdir(sys.argv[2]) == True:
		remove_project(sys.argv[2])
	else:
		print("Project doesn't exists!")	

