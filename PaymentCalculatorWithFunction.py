hrs = input("Enter Hours:")
floatHours = float(hrs)
rate = input("Enter the Rate:")
floatRate = float(rate)

def computepay():
    if floatRate<=40:
        if floatHours>40:
            overtimeHours = floatHours -40
            regularPay = (floatHours-overtimeHours)*floatRate
            overtimeRate = floatRate *1.5
            overtimePay = overtimeHours*overtimeRate
            return regularPay+overtimePay
        else:
            return floatHours*floatRate
    else:
        print("I can't process this shit")

print(computepay())

input("Close please")
