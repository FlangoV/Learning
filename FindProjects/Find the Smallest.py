smallest_so_far = None

while True:
    try:
        numbers = input("Enter numbers: ")
        if numbers == 'done':
            break
        numbers = float(numbers)
        smallest_so_far = numbers
    except:
        print("Bad input")
        continue
    if smallest_so_far > numbers:
        continue
    elif numbers < smallest_so_far:
        smallest_so_far = numbers


print(smallest_so_far)
