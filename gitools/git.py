import os

def makerep():
    return os.system("git init")

def commit():
    print("your commit message: ")
    message = input("")
    os.system("git add -A")
    os.system(f"git commit -m '{message}' ")
    
def branch():
    print("your branch message: ")
    name = input("")
    os.system(f"git branch {name}")
    
def branch2():
    os.system(f"git branch")
    
def checkout():
    print("your branch name: ")
    name = input("")
    os.system(f"git branch {name}")
    
def checkout2():
    os.system(f"git branch")
    
def status():
    os.system(f"git status")
    
def checkout3():
    print('name of branch: ')
    name = input("")
    os.system(f"git checkout -b {name}")
    
def delbranch():
    print('name of branch: ')
    name = input("name of branch: ")
    os.system(f"git branch -d {name}")
    
def delbranch2():
    print('name of branch: ')
    name = input("name of branch: ")
    os.system(f"git branch -D {name}")
    

def addbranch():
    print('name of branch: ')
    name = input("name of branch: ")
    os.system(f"git checkout {name}")
    
    
def merge():
    print('name of branch: ')
    name = input("name of branch: ")
    os.system(f"git merge {name}")
    
def push():
    print('URL')
    name = input("URL: ")
    os.system(f"git remote add origin {name}")
    os.system('git branch -M main')
    os.system(f"git push -u origin main")
