def calculateOverTime(floatHours, floatRate):
        overtimeHours = floatHours - 40
        regularPay = (floatHours-overtimeHours)*floatRate
        overtimeRate = floatRate * 1.5
        overtimePay = overtimeHours*overtimeRate
        overtimePayment = overtimePay+regularPay
        return overtimePayment

def computepay(floatHours, floatRate):
    if floatRate<=40:
        if floatHours>40:
            return calculateOverTime(floatHours, floatRate)
        else:
            regularPay = floatHours*floatRate
            return regularPay
    else:
        print("I can't process this shit")

try:
    floatHours = input("Enter the hours:")
    floatHours = float(floatHours)
    floatRate = input("Enter the rate:")
    floatRate = float(floatRate)

except:
    print("Wrong Inputs")
    input("Try again")

print(computepay(floatHours, floatRate))

input("Close please")
