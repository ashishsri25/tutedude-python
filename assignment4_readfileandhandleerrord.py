try:
    file_name = "C:/Users/ashis/tutedude/python/file_folder/sample.txt"
    file_name = "C:/Users/ashis/tutedude/python/file_folder/sample1.txt"  # for file not found
    i=1
    with open(file_name,"rt") as fh:
     lines = sum(1 for line in fh)
    print("Reading file content.")
    with open(file_name, "rt") as fh:
        while i<=lines:
            print(f"Line{i}:{fh.readline().rstrip("\n")}")
            i=i+1
except FileNotFoundError as e:
    print(f"The file {file_name} not found")
# finally:
#     fh.close()





