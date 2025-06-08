"""
Write code that asks the user for their name, then opens a file called name.txt
and writes that name to it. Use open and close for this question.
"""
user_name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(user_name)
out_file.close()


"""
In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question.
"""
in_file = open("name.txt", "r")
name_from_file = in_file.read() # Using read() to get the whole content
in_file.close()
print(f"Hi {name_from_file}!")

"""
Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59. 
Use with instead of open and close for this question.
"""
with open("numbers.txt", "w") as file:
    file.write("17\n")
    file.write("42\n")
    file.write("400\n")

total_first_two = 0
with open("numbers.txt", "r") as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()
    total_first_two = int(line1) + int(line2)

print(f"The sum of the first two numbers is: {total_first_two}") # Expected: 59

"""
Now write a fourth block of code that prints the total for all lines in numbers.txt. 
This should work for a file with any number of numbers. Use with instead of open and close for this question.
"""

total_all_numbers = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total_all_numbers += int(line)
print(f"The total of all numbers is: {total_all_numbers}") # Expected: 459