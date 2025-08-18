import argparse
parser = argparse.ArgumentParser()
parser.add_argument("num1",type=int)
parser.add_argument("num2",type=int)
parser.add_argument("operation", choices=["add","sub","div","mul"])
args = parser.parse_args()

if(args.operation =="add"):
  print(args.num1+args.num2)

elif(args.operation =="sub"):
  print(args.num1-args.num2)

elif(args.operation =="mul"):
  print(args.num1*args.num2)

elif(args.operation =="div"):
  print(args.num1/args.num2)

else:
  print("Invalid operator")