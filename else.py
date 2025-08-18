# try:
#    a= int(input("Enter a 1st number = "))
#    b= int(input("enter a 2nd number = "))
#    print("sum",a/b)

# except:      
#    print("Enter a valid data")

# else:
#  print("This is else")


#finally

try:
   a= int(input("Enter a 1st number = "))
   b= int(input("enter a 2nd number = "))
   print("sum",a/b)

except Exception as e:
   print(e)
finally:
 print("This is from finally")