user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data successfully writen to output.txt \n")

#Append additional data to the file
additional_input = input("Enter additional text to append to the file: ")
print("Data successfully appended")

# Open the file in append mode and add more content
with open("output.txt", "a") as file:
    file.write(additional_input + "\n") 

#display the content of the file
print("\nFinal content of the file 'output.txt':")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
