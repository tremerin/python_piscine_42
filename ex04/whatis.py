import sys

if len(sys.argv) == 2:
    #try
    num = int(sys.argv[1])
    if type(num) != int:
        print("AssertionError: argument is not an integer")
    else:
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")