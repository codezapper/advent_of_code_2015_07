# Advent of code 2015 day 07

Python solution for advent of code, year 2015, day 07

This code will take a text file as input and print the required value to solve the challenge at https://adventofcode.com/2015/day/7

Notes:

- The challenge is easy enough but badly described. At a superficial reading it might look like what is needed is to run a series of operations to connect the logic gates and get a result. What is actually needed is to parse a series of connection that are already there and work all the way back to see what actual value is connected to the requested wire.

- Python works with signed integer, which means that the `NOT` operation needs to be fixed to always work on 16 bits. That is the reason for the `&` with `0xFFFF` in the `NOT`.

- A class is used because the alternative would be a global function that uses a global variable to keep track of the wire outputs. It would be trick to pass the variable every time to the recursive function because dictionaries are mutable, and it might end up storing more values than expected.

## Usage

`python3 gate_solver.py [input_file]`

The `input_file` parameter specifies the input file containing the gates description. If not specified, the default is a file name `input_file.txt`.
