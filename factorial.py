def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Factor of {number} is {factorial(number)}")
