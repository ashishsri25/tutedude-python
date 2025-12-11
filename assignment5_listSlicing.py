n=int(input("Enter the length of the list: "))
my_list = list(range(1,n+1))
# for i in range(1,n+1):
#     my_list.append(i)
print(f"Original list: {my_list}")
new_list = my_list[:5]
print(f"Extracted first 5 elements: {new_list}")
print(f"Reverse extracted elements: {new_list[::-1]}")