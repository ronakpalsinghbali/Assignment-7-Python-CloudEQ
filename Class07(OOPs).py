# Class method is bound to the class and not the object of the class. It can access only class variables.

# Super() method is used to access the methods and properties of a parent class in the derived class.





# Class example:

class Car:
    def __init__(self,person,company,model,color,type):          # Constructor 
        self.person = person
        self.company = company
        self.model = model
        self.color = color
        self.type = type
      
        

    def my_car_info(self):                                       # Function

        print(f"{self.person}'s car's company is {self.company} and it is of {self.color} color, the model of the car is {self.model}, and it runs on {self.type}. \n")

   
         
        

Ronak_car = Car("RONAK","TATA","NEXON","GREEN","DIESEL")
Mayank_car = Car("MAYANK","KIA","SELTOS","BLACK","PETROL")
Shiwam_car = Car("SHIWAM","HYUNDAI","VERNA","RED","DIESEL")




Ronak_car.my_car_info()
Mayank_car.my_car_info()
Shiwam_car.my_car_info()