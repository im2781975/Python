def input_number(msg, err_msg=None):    
while True:       
    try:
        return float(raw_input(msg))        
    except ValueError:            
        if err_msg is not None:                
            print(err_msg) 
def input_number(msg, err_msg=None):
    while True:        
        try:            
            return float(input(msg))       
        except ValueError:      
            if err_msg is not None:                
            print(err_msg)
print("Hello, ", end="\n") 
print("World!")
print("Hello, ", end="") 
print("World!")
print("Hello, ", end="<br>")
print("World!")
print("Hello, ", end="BREAK")
print("World!")
