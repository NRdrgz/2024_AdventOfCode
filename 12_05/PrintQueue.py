"""
--- Day 5: Print Queue ---
Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a very familiar printer beckons you over.

The Elf must recognize you, because they waste no time explaining that the new sleigh launch safety manual updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.

For example:

47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47

The first section specifies the page ordering rules, one per line. The first rule, 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)

The second section specifies the page numbers of each update. Because most safety manuals are different, the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifying which updates are already in the right order.

In the above example, the first update (75,47,61,53,29) is in the right order:

75 is correctly first because there are rules that put each other page after it: 75|47, 75|61, 75|53, and 75|29.
47 is correctly second because 75 must be before it (75|47) and every other page must be after it according to 47|61, 47|53, and 47|29.
61 is correctly in the middle because 75 and 47 are before it (75|61 and 47|61) and 53 and 29 are after it (61|53 and 61|29).
53 is correctly fourth because it is before page number 29 (53|29).
29 is the only page left and so is correctly last.
Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.

The second and third updates are also in the correct order according to the rules. Like the first update, they also do not include every page number, and so only some of the ordering rules apply - within each update, the ordering rules that involve missing page numbers are not used.

The fourth update, 75,97,47,61,53, is not in the correct order: it would print 75 before 97, which violates the rule 97|75.

The fifth update, 61,13,29, is also not in the correct order, since it breaks the rule 29|13.

The last update, 97,13,75,29,47, is not in the correct order due to breaking several rules.

For some reason, the Elves also need to know the middle page number of each update being printed. Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:

75,47,61,53,29
97,61,53,29,13
75,29,13
These have middle page numbers of 61, 53, and 29 respectively. Adding these page numbers together gives 143.

Of course, you'll need to be careful: the actual list of page ordering rules is bigger and more complicated than the above example.

Determine which updates are already in the correct order. What do you get if you add up the middle page number from those correctly-ordered updates?
"""
"""
--- Part Two ---
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
"""

# Read the input and transform as array
def read_file(input_str):
    with open(input_str, "r") as file:
        input_string = file.readlines()
    return input_string


# The idea that I have is us a dictionnary for each page with 2 arrays: before_page and after_page respectively containing the infos of the pages that should be before and after the page

def create_rule_dictionnary(input_string):
    page_dict = {}
    # Read the input
    input_string = read_file("input_1.txt")
    for rule in input_string:
        first_page = int(rule.split("|")[0])
        second_page = int(rule.split("|")[1].replace("\n",""))
        # If the page is not in the dictionnary, we add it
        if first_page not in page_dict:
            page_dict[first_page] = {"before_page":[], "after_page":[]}
        if second_page not in page_dict:
            page_dict[second_page] = {"before_page":[], "after_page":[]}
        
        # We add the infos to the dictionnary
        page_dict[second_page]["before_page"].append(first_page)
        page_dict[first_page]["after_page"].append(second_page)
    return page_dict

def part_1():
    page_dict = create_rule_dictionnary("input_1.txt")
    # Now we use the dictionnary to check if the pages are in the right order
    # We'll iterate over the updates and for each update, we'll check if the pages are in the right order
    # We'll also keep track of the middle page
    middle_pages = []
    # Read the input
    input_string = read_file("input_2.txt")

    for update in input_string:
        # Initialize safe update boolean
        safe_update = True
        # Convert to array
        update = update.split(",")
        update = [int(u) for u in update]

        # For each page, we'll check if the page is in the right order 
        for i in range(len(update)): 
            current_page = update[i]
            # Ignore the page if it's not in the dictionnary
            if current_page not in page_dict:
                continue
                
            # Check if any page before the update, is in the after_page of the current page
            for b in update[:i]:
                if b in page_dict[current_page]["after_page"]:
                    safe_update = False
                    break
            # Check if any page after the update, is in the before_page of the current page
            for a in update[i+1:]:
                if a in page_dict[current_page]["before_page"]:
                    safe_update = False
                    break
        
        # If the update is safe, we'll compute the middle page
        if safe_update:
            middle_pages.append(update[len(update)//2])

    # Print the sum of middle pages
    print(f"The sum of the middle pages is {sum(middle_pages)}")

def part_2():
    res = 0
    # Now if the update is bad, we'll want to fix it 

    page_dict = create_rule_dictionnary("input_1.txt")    
    # Read the input
    input_string = read_file("input_2.txt")

    for update in input_string:
    
        # Convert to array
        update = update.split(",")
        update = [int(u) for u in update]
        broken_update = False

        # For each page, we'll check if the page is in the right order 
        i = 0
        while i < len(update):
            current_page = update[i]
            # Ignore the page if it's not in the dictionnary
            if current_page not in page_dict:
                i+=1
                continue
                
            # Check if any page in the update before the current_page, is in the after_page of the current page
            # If so, we'll flip the pages
            for j in range(i):
                tested_page = update[j]
                if tested_page in page_dict[current_page]["after_page"]:
                    # We'll swap the pages
                    update[j], update[i] = current_page, tested_page
                    broken_update = True
                    # We restart the loop
                    i = 0
                    break
                      
            # Check if any page in the update after the current_page, is in the before_page of the current page
            # If so, we'll flip the pages
            for j in range(i+1, len(update)):
                tested_page = update[j]
                if tested_page in page_dict[current_page]["before_page"]:
                    # We'll swap the pages
                    update[j], update[i] = current_page, tested_page
                    broken_update = True
                    # We restart the loop
                    i = 0
                    break
                     
            i+=1 
        
        # If the update was broken and we fixed it, we take the middle page
        if broken_update:
            res += update[len(update)//2]
    
    print(f"The sum of the middle pages is {res}")
    
        
        
if __name__ == "__main__":
    part_1()
    part_2()