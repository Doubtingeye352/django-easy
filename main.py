from gitools.gitmain import gitrun
from pack1.main import code
from dj.djmain import main
import os

prompt = input('The Mode: ')
 
if prompt == 'git':
    gitrun()
    
if prompt == "heroku":
    code()
    
if prompt =='django':
    main()    
