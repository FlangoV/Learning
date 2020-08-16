def computepay(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6 and score >-0.1:
        return "F"

try:
    score = input("Insert your score: ")
    score = float(score)
except:
    score = -1
    print("Wrong input")
    input("Try again")

print(computepay(score))
