"""
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?
"""

"""
--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

# Read the input and transform as matrix
def read_file():
    with open("input.txt", "r") as file:
        input_string = file.readlines()
    return input_string

def part_1():
    input_string = read_file()
    #input_string = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]

    m = len(input_string) # Number of rows
    n = len(input_string[0]) # Number of columns    
    
    # Let's iterate over the matrix and for every X that we find, we'll try finding MAS in all directions 
    # We also need to handle exceptions in case we go out of bounds
    # XMAS can only be contiguous 
    counter = 0
    for i in range(m):
        for j in range(n):
            print(f"Checking {i},{j}")
            if input_string[i][j] == "X":
                # Check for XMAS in all directions
                # Need to add a check for the negative index to not go all around
                try:
                    if input_string[i][j+1] == "M" and input_string[i][j+2] == "A" and input_string[i][j+3] == "S":
                        print(f"XMAS found on right of {i},{j}")
                        counter+=1
                except:
                    pass
                try:
                    if input_string[i][j-1] == "M" and input_string[i][j-2] == "A" and input_string[i][j-3] == "S" and j-1 >= 0 and j-2 >= 0 and j-3 >= 0:
                        print(f"XMAS found on left of {i},{j}")
                        counter+=1
                except:
                    pass
                try:
                    if input_string[i-1][j] == "M" and input_string[i-2][j] == "A" and input_string[i-3][j] == "S" and i-1 >= 0 and i-2 >= 0 and i-3 >= 0:
                        print(f"XMAS found on top of {i},{j}")
                        counter+=1
                except:
                    pass
                try:
                    if input_string[i+1][j] == "M" and input_string[i+2][j] == "A" and input_string[i+3][j] == "S":
                        print(f"XMAS found on bottom of {i},{j}")
                        counter+=1
                except:
                    pass
                try:
                    if input_string[i+1][j+1] == "M" and input_string[i+2][j+2] == "A" and input_string[i+3][j+3] == "S":
                        print(f"XMAS found on bottom right of {i},{j}")
                        counter+=1
                except:
                    pass
                try:
                    if input_string[i+1][j-1] == "M" and input_string[i+2][j-2] == "A" and input_string[i+3][j-3] == "S" and j-1 >= 0 and j-2 >= 0 and j-3 >= 0:
                        print(f"XMAS found on bottom left of {i},{j}")
                        counter+=1
                except:
                    pass
                try:
                    if input_string[i-1][j+1] == "M" and input_string[i-2][j+2] == "A" and input_string[i-3][j+3] == "S" and i-1 >= 0 and i-2 >= 0 and i-3 >= 0:
                        print(f"XMAS found on top right of {i},{j}")
                        counter+=1
                except:
                    pass
                try:
                    if input_string[i-1][j-1] == "M" and input_string[i-2][j-2] == "A" and input_string[i-3][j-3] == "S" and j-1 >= 0 and j-2 >= 0 and j-3 >= 0 and i-1 >= 0 and i-2 >= 0 and i-3 >= 0:
                        print(f"XMAS found on top left of {i},{j}")
                        counter+=1
                except:
                    pass
    print(f"The number of XMAX occurences is {counter}")

def part_2():
    # For this one we'll base our search on the "A" letter which is at the center
    input_string = read_file()
    m = len(input_string) # Number of rows
    n = len(input_string[0]) # Number of columns    
    
    counter = 0
    for i in range(m):
        for j in range(n):
            print(f"Checking {i},{j}")
            if input_string[i][j] == "A" and i-1 >= 0 and i+1 < m and j-1 >= 0 and j+1 < n:
                if ((input_string[i-1][j-1] == "M" and input_string[i+1][j+1] == "S") \
                or (input_string[i-1][j-1] == "S" and input_string[i+1][j+1] == "M")) \
                and \
                ((input_string[i-1][j+1] == "M" and input_string[i+1][j-1] == "S") \
                or (input_string[i-1][j+1] == "S" and input_string[i+1][j-1] == "M")) \
                :
                    print(f"XMAS on {i},{j}")
                    counter+=1
    print(f"The number of XMAX occurences is {counter}")

if __name__ == "__main__":
    part_1()
    part_2()
    
    