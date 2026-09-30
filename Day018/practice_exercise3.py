# Exercise 3: String Indexing and Even slicing.

# Display only those characters which are present at an 
# even index number in the given string.

# Given input string "pynative"

# Answer
# Method 1

given_input = "pynative"
even_index = given_input[0::2]

def even_index():
    for each_char in even_index:
        print(each_char)
        
    
print(f"Original String is {given_input}.")
print("Printing only even index chars...")

even_index()

# Method 2

given_input = "pynative"

print(f"Original String is {given_input}")
print(f"Printing only even numbers")

for even_index in range(0, len(given_input), 2):
    print(given_input[even_index])

