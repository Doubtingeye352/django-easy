import os

def startproject():
    name = input("name of project: ")
    os.system(f'django-admin startproject {name}')
    os.system(f'mv {name} {name}-project')
    
def runserver():
    os.system(f'python3 manage.py runserver')
    
def migrate():
    os.system(f'python3 manage.py migrate')
    
def makemigrations():
    os.system(f'python3 manage.py makemigrations')
    
def makeapp():
    os.system(f'python3 manage.py startapp')
    
def testserver():
    os.system(f'django-admin testserver')
    
def test():
    os.system(f'django-admin test')
    
    