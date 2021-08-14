from dj.admin import startproject,runserver,migrate,makemigrations,makeapp,testserver,test

def main():
    
    prompt = input('> ')
    
    if prompt == 'startproject':
        startproject()
        
    elif prompt == 'runserver':
        runserver()
        
    elif prompt == 'makemigrations':
        makemigrations()
        
    elif prompt == 'startapp':
        makeapp()
        
    elif prompt == 'testserver':
        testserver()
        
    elif prompt == 'test':
        test()
        
    elif prompt == 'migrate':
        migrate()
        
    elif prompt == 'exit':
        exit()
        
    
    else:
        print("unknown command")
        
        
        
    for i in range(1000):
        main()
        
    
    