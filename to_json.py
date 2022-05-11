import json
class Brand:
    def __init__(self,b_name,b_year):
        self.b_name=b_name
        self.b_year=b_year
        
class Product(Brand):
    def __init__(self, name, b_name, b_year, price):
        super().__init__(b_name, b_year)    
        self.name=name
        self.price=price
    def toJson(self):
        jsonCon = json.dumps(self.__dict__)
        return jsonCon

computer=Product("Laptop",'Lenova',2020,'750')
print(computer.toJson()) 