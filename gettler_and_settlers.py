# class employee:
#     def __init__(self,name, salary):
#         self.name = name
#         self.salary = salary
    
#     def fname(self):
#        return self.name.split(" ")[0]
       


# e= employee("ram hari", 10000)
# print(e.fname())

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def fname(self):
        return self.name.split(" ")[0]
    
    @fname.setter
    def fname(self, newname):
      x=  self.name.split(" ")
      self.name = f"{newname}   "
e= employee("john" ,20000)
e.fname="ram"
print(e.name)