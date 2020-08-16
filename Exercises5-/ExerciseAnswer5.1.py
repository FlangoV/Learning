num_numbers = 0
total = 0.0

while True:
    try:
        numbers = input("Enter numbers: ")
        if numbers == 'done':
            break
        numbers = float(numbers)
    except:
        print("bad input")
        continue
    num_numbers = num_numbers + 1
    total = total + numbers

print(num_numbers, total,total/num_numbers)
