from gitools.git import makerep, commit,branch,branch2,checkout,checkout2,status,delbranch,delbranch2,addbranch,merge,push

def gitrun():
    prompt = input(">")
    
    
    if prompt == 'init':
        makerep()
    
    elif prompt == 'commit':
        commit()
    
    elif prompt == 'branch':
        branch()
    
    elif prompt == 'Branch':
        branch2()
    
    elif prompt == 'checkout':
        checkout()
    
    elif prompt == 'Checkout':
        checkout2()
    
    elif prompt == 's':
        status()
    
    elif prompt == 'delbranch':
        delbranch()
    
    elif prompt == 'DELbranch':
     delbranch2()
    
    elif prompt == 'checkout-b':
        addbranch()
    
    elif prompt == 'merge':
        merge()
    
    elif prompt == 'push':
        push()
        
    elif prompt == 'exit':
        exit()
        
    else:
        return print("unknown command")
        
    for i  in range(1000):
        gitrun()