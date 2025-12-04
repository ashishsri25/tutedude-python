absolute_path = "C:/Users/ashis/tutedude/python/file_folder/appendfile.txt"
relative_path = "appendfile.txt"

input1 = input("Enter text to write to the file: ")
with open(absolute_path, "w") as fh:
    fh.write(input1)

input2 = input("Enter additional test to append: ")
with open(absolute_path, "a") as fh:
    fh.write("\n")
    fh.write(input2)

print(f"Final content of {relative_path}")
with open(absolute_path, "r") as fh:
    print(fh.read())