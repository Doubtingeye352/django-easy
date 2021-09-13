import os 



def code():
    prompt = input('> ')
    
    if prompt == 'install':
        os.system('brew tap heroku/brew && brew install heroku')
        
    elif prompt == 'host':
        os.system('heroku login')
        os.system('git init')
        os.system('git add -A')
        comess = input("commit message: ")
        os.system(f'git commit -m {comess}')
        name = input("app name: ")
        os.system(f'heroku create {name}')
        os.system(f'heroku git:remote -a {name}')
        os.system('pip install gunicorn')
        location = input('wsgi file location: ')
        os.system("touch Procfile")
        f = open('Procfile', 'w')
        f.write(f"web: gunicorn {location}")
        f.close()
        os.system("pip freeze > requiremnts.txt")
        os.system('git add -A')
        comess2 = input("commit message: ")
        os.system(f'git commit -m {comess2}')
        os.system("git push heroku master")
        print("process completed now just go tto heroku.com and add database and  allowed host and then you are done!")
        
        
    elif prompt == 'exit':
        exit()
        
    for i in range(30):
        code()
            
    else:
        print("unkown command")
        
        
def post(request):
    #get items from front end and add them to the database
    
    if request.method == 'POST':
        if request.POST.get('Title'):
            c= code()
            
            c.Title = request.POST.get('Title')
            c.Lang = request.POST.get('lang')
            c.Snippet = request.POST.get('snippet')
            c.Description = request.POST.get('des')
            
            c.save()
            print('test')
   
    
    return render(request, 'post.html')
