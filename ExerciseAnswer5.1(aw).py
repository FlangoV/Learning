num_numbers = 0
total = 0.0
done = False

while done == False:
    try:
        numbers = input("Enter your numbers: ")
        if numbers == 'done':
            done = True
        numbers = float(numbers)
    except:
        print("bad input")
        continue
    num_numbers = num_numbers + 1
    total = total + numbers
    
print(num_numbers, total,total/num_numbers)
