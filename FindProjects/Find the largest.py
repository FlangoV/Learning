largest_so_far = 0.0

while True:
    try:
        numbers = input("Enter numbers: ")
        if numbers == 'done':
            break
        numbers = float(numbers)
        print(numbers)
    except:
        print("Bad input")
        continue
    if largest_so_far > numbers:
        continue
    elif numbers > largest_so_far:
        largest_so_far = numbers

print(largest_so_far)
