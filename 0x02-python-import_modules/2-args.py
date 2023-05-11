#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = len(sys.argv)
    if args - 1 == 0:
        print("{} arguments.".format(args - 1))
    elif args - 1 == 1:
        print("{} argument:".format(args - 1), end='\n')
        print("{}: {}".format(args - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(args - 1))
        for i in range(1, args):
            print("{}: {}".format(i, sys.argv[i]))
