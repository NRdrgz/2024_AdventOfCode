import re
"""
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

"""
--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?

"""

def part_1():
    # Read content as a list
    with open("input.txt", "r") as file:
        input_string = file.read()
    
    # We'll use Regex to identify patterns of mul(d{1,3},d{1,3})
    # Define the regex pattern to match "mul(" followed by 1 to 3 digits
    pattern = 'mul' + '\(' + '\d{1,3}' + ',' + '\d{1,3}' + '\)'

    # Find all matches of the pattern
    matches = re.findall(pattern, input_string)
    
    res_sum = 0
    # For each match we'll extract only the digits and add their product to the result
    for m in matches:
        new_pattern = '\d{1,3}'
        sub_matches = re.findall(new_pattern, m)
        res_sum+=int(sub_matches[0])*int(sub_matches[1])

    print(res_sum)

def part_2():
    # Read content as a list
    with open("input.txt", "r") as file:
        input_string = file.read()
    
    
    pattern = 'mul' + '\(' + '\d{1,3}' + ',' + '\d{1,3}' + '\)'
    # Find all matches of the pattern
    # We use finditer to get the index at the same time
    matches = re.finditer(pattern, input_string)

    # For every match, we'll compute the distance of don't and do before the match, and if there are no don't or if the distance with a do is smaller, we'll keep the match'
    pattern_dont = r"don't\(\)"
    pattern_do = r"do\(\)"
    filtered_matches = []
    for match in matches:
        matched_text = match.group()  # The matched string
        start_index = match.start()  # Start index of the match
        # Try to find a don't occurence, before the match
        dont_matches = re.finditer(pattern_dont,input_string[:start_index])
        do_matches = re.finditer(pattern_do, input_string[:start_index])
        # Convert to array
        dont_matches_arr = [dm for dm in dont_matches]
        do_matches_arr = [d for d in do_matches]
        # If we have a do after a don't, we keep the record, otherwise we don't
        if (len(dont_matches_arr) == 0) or (dont_matches_arr[-1].start() < do_matches_arr[-1].start()):
            filtered_matches.append(matched_text)
    
    res_sum = 0
    # For each match we'll extract only the digits and add their product to the result
    for m in filtered_matches:
        new_pattern = '\d{1,3}'
        sub_matches = re.findall(new_pattern, m)
        res_sum+=int(sub_matches[0])*int(sub_matches[1])

    print(res_sum)
    
    
if __name__ == "__main__":
    part_1()
    part_2()
    
    