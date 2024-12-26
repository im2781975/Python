def factorial(n):    
    if n == 0:        
        return 1    
    else:       
        return n * factorial(n - 1)
        
def factorial(n):    
    if n == 0:        
        return 1    
    elif n == 1:        
        return 1    
    else:        
        return n * factorial(n - 1)

def fib(n):    
    if n == 0 or n == 1:        
        return n    
    else:       
        return fib(n - 2) + fib(n - 1)
        

def factorial(n):   
    product = 1 
    while n > 1:       
        product *= n        
        n -= 1 
    return product 
def fib(n):    
    a, b = 0, 1
    while n > 0:        
        a, b = b, a + b  
        n -= 1 
    return a
    
def fib(n): 
    if n <= 1:
        return (n,0)    
    else:       
        (a, b) = fib(n - 1)        
        return (a + b, a)
        
root
- A  
    - AA 
    - AB
- B 
    - BA
    - BB    
        - BBA
root = get_root(tree)
for node in get_children(root):    
    print(get_name(node))    
    for child in get_children(node):       
        print(get_name(child))        
        for grand_child in get_children(child):            
            print(get_name(grand_child))
def list_tree_names(node):    
    for child in get_children(node):       
        print(get_name(child))        
        list_tree_names(node=child) 
list_tree_names(node=get_root(tree))

def list_tree_names(node, lst=[]):    
    for child in get_children(node):        
        lst.append(get_name(child))        
        list_tree_names(node=child, lst=lst)    
    return lst
list_tree_names(node=get_root(tree))

n = 0 
for i in range (1, n+1): 
    n += i
def recursion(n):   
    if n == 1:        
        return 1   
    return n + recursion(n - 1)

def cursing(depth): 
    try:    
        cursing(depth + 1) # actually, re-cursing  
    except RuntimeError as RE:   
        print('I recursed {} times!'.format(depth)) 
cursing(0)

def countdown(n):    
    if n == 0:        
        print "Blastoff!"  
    else:        
        print n        
        countdown(n-1)

def find_max(seq, max_so_far):    
    if not seq:        
        return max_so_far    
    if max_so_far < seq[0]:        
        return find_max(seq[1:], seq[0])   
    else:        
        return find_max(seq[1:], max_so_far)

@tail_call_optimized
def factorial(n, acc=1):  
    "calculate a factorial" 
    if n == 0:   
        return acc  
    return factorial(n-1, n*acc)
print factorial(10000)
@tail_call_optimized 
def fib(i, current = 0, next = 1):  
    if i == 0:    
        return current 
    else:    
        return fib(i - 1, next, current + next)
print fib(10000)

