#ref link: https://www.youtube.com/watch?v=XYUXFR5FSxI&ab_channel=codebasics
import argparse


arg_parser = argparse.ArgumentParser(description="THIS IS ARGUMENT PARSER")

#----------positional arguments(these are mandatory arguments)----------#
arg_parser.add_argument("num1",help="NUMBER 1",type=int)
arg_parser.add_argument("num2",help="NUMBER 2",type=int)
arg_parser.add_argument("operation",help="OPERATION TO BE PERFORMED add sub mul",choices=["add","sub","mul"])

args = arg_parser.parse_args()
#command for executing is: $python one_argparse.py 3 4 add
print(f"Entered Positional number 1: {args.num1} type:{type(args.num1)}")
print(f"Entered Positional number 2: {args.num2} type:{type(args.num2)}")
print(f"Entered Positional Operation: {args.operation} type:{type(args.operation)}")

if args.operation == "add":
    print("PERFORMING ADDITION")
    res = args.num1 + args.num2
elif args.operation == "sub":
    print("PERFORMING SUBTRACTION")
    res = args.num1 + args.num2
elif args.operation == "mul":
    print("PERFORMING MULTIPLICATION")
    res = args.num1 * args.num2

print(f"RESULT IS: {res}")