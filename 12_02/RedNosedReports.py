"""
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""

"""
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

"""

def part_1():

    # Maximum number of diff between levels (included)
    max_diff = 3

    # Minimum number of diff between levels (included)
    min_diff = 1

    # Initialize safe reports
    safe_reports = 0

    # Read content as a list
    with open("input.txt", "r") as file:
        reports = file.readlines()

    for report in reports:
        # Transform string in array
        report = report.split(" ")
        # Cast to int 
        report = [int(r) for r in report]
        # If safe, increment
        safe_reports += int(is_safe_part_1(report, min_diff, max_diff))
    
    print(f"The number of safe reports is {safe_reports}")

def is_safe_part_1(report, min_diff, max_diff):
    """
        Smarter way could be to compute differences:
        differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
        and verify that all differences are positive or negative (increasing or decreasing) and within range
        # Check if differences are all positive or all negative
        is_increasing = all(d > 0 for d in differences)
        is_decreasing = all(d < 0 for d in differences)
        
        # Check if the differences are within the range [1, 3]
        within_range = all(1 <= abs(d) <= 3 for d in differences)
    """
    # Initialize is_increasing
    is_increasing = True 
    if report[1] <= report[0]:
        is_increasing = False

    for i in range(len(report)-1):
        # Test on diff and test on increase/decrease
        if (abs(report[i+1]-report[i]) < min_diff) or (abs(report[i+1]-report[i]) > max_diff) or (is_increasing and (report[i+1]<report[i])) or (not is_increasing and (report[i+1]>report[i])):
            return False
    return True



def part_2():
    # Problem dampening
    problem_damp = 1

    # Maximum number of diff between levels (included)
    max_diff = 3

    # Minimum number of diff between levels (included)
    min_diff = 1

    # Initialize safe reports
    safe_reports = 0

    # Read content as a list
    with open("input.txt", "r") as file:
        reports = file.readlines()

    for report in reports:
        # Transform string in array
        report = report.split(" ")
        # Cast to int 
        report = [int(r) for r in report]
        # If safe, increment
        safe_reports += int(is_safe_part_2(report, min_diff, max_diff, problem_damp))
    
    print(f"The number of safe reports is {safe_reports}")

def is_safe_part_2(report, min_diff, max_diff, problem_damp):
    # Initialize is_increasing
    is_increasing = True 
    if report[1] <= report[0]:
        is_increasing = False

    for i in range(len(report)-1):
        # Test on diff and test on increase/decrease
        if (abs(report[i+1]-report[i]) < min_diff) or (abs(report[i+1]-report[i]) > max_diff) or (is_increasing and (report[i+1]<report[i])) or (not is_increasing and (report[i+1]>report[i])):

            # We use problem dampening and we test again the report without the level i or the level i+1 or the level i-1:
            if problem_damp > 0:
                new_report_1 = report[:i] + report[i + 1:]
                new_report_2 = report[:i+1] + report[i+1 + 1:]
                new_report_3 = report[:i-1] + report[i-1 + 1:]
                return is_safe_part_2(new_report_1, min_diff, max_diff, problem_damp-1) or is_safe_part_2(new_report_2, min_diff, max_diff, problem_damp-1) or is_safe_part_2(new_report_3, min_diff, max_diff, problem_damp-1)
                break

            else:
                return False


    return True


if __name__ == "__main__":
    part_1()
    part_2()
    