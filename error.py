# try:
#    a= int(input("Enter a 1st number = "))
#    b= int(input("enter a 2nd number = "))
#    print("sum",a+b)

# except:      
         #exception as e
#    print("Enter a valid data")
   
try:
   a= int(input("Enter a 1st number = "))
   b= int(input("enter a 2nd number = "))
   print("sum",a+b)

except ValueError:
   print("Enter a valid number")

except ZeroDivisionError:
   print("Enter a value greater than 0")

except Exception as a:
   print(a)