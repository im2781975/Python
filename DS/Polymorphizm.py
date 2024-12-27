class Duck:   
    def quack(self):      
        print("Quaaaaaack!")   
    def feathers(self):      
        print("The duck has white and gray feathers.")
class Person:    
    def quack(self):       
        print("The person imitates a duck.")    
    def feathers(self):     
        print("The person takes a feather from the ground and shows it.")   
    def name(self):       
        print("John Smith")
def in_the_forest(obj):   
    obj.quack()  
    obj.feathers()
donald = Duck() 
john = Person() 
in_the_forest(donald) 
in_the_forest(john)

class Shape:
    def calculate_area(self):
        raise NotImplemented
class Square(Shape):
    side_length = 2
    def calculate_area(self):
        return self.side_length * 2
class Triangle(Shape):
    base_length = 4    
    height = 3
    def calculate_area(self):
        return 0.5 * self.base_length * self.height
    def get_area(input_obj):
        print(input_obj.calculate_area())
shape_obj = Shape() 
square_obj = Square()
triangle_obj = Triangle()
get_area(shape_obj) 
get_area(square_obj) 
get_area(triangle_obj)

class Square:    
    side_length = 2    
    def calculate_square_area(self):        
        return self.side_length ** 2
class Triangle:   
    base_length = 4   
    height = 3    
    def calculate_triangle_area(self):        
        return (0.5 * self.base_length) * self.height
    def get_area(input_obj):
        if type(input_obj).__name__ == "Square":        area = input_obj.calculate_square_area()    
        elif type(input_obj).__name__ == "Triangle":        
            area = input_obj.calculate_triangle_area()    print(area)
square_obj = Square()
triangle_obj = Triangle()
get_area(square_obj)
get_area(triangle_obj)
