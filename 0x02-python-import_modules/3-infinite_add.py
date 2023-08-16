#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Exclude the script name itself
    total = sum(map(int, arguments))
    print(total)
