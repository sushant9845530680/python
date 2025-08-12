class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def fname(self):
        print(self.name)
    
    @staticmethod
    def sum(a,b):
      return a+b
      
e= employee("john" ,20000)
print(e.sum(10,12))
