try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    print("What kind of operation you want to do \n press+ for addition\n press- for substraction \n press / for divisible \n press* for multiplication ")
    
    op=input("Enter your choice:")
    if op=="+":
        print(a+b)
    
    elif op=="-":
        print(a-b)
    
    elif op=="/":
        print(a/b)
    
    elif op=="*":
        print(a*b)
    
except Exception as e :
    print(e)