import re

# Sample input string
input_string = "Hello, this is an example sentence! It has some punctuation."

# Define the regex pattern
pattern = r'[^a-zA-Z.,!?]*'

# Use re.findall() to find all matches of the pattern in the input string
matches = re.findall(pattern, input_string)

# Print the matched sequences
for match in matches:
    print("Match:", match)
