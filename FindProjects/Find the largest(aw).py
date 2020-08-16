maximum = None
minimum = None

while True:
    numbers = input("Enter numbers: ")
    if numbers == 'done':
        break
    try:
        numbers = float(numbers)
    except:
        print("Oh no, something went wrong")
        continue
    if maximum == None:
        maximum = numbers
    elif minimum == None:
        minimum = numbers
    elif maximum < numbers:
        maximum = numbers
    elif minimum > numbers:
        minimum = numbers

print("Maximum:",maximum,"Minimum:",minimum)
