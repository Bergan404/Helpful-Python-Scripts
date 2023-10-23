import os

# listdir returs a list of all the names within the file, doesnt print it but it shows them
entries = os.listdir('/Users/berganoudshoorn/Downloads/')

# Using a for loop to itterate through all the listiings and print them as strings
for entry in entries:
 print(entry)
