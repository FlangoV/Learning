hrs = input("Enter Hours:")
floatHours = float(hrs)
rate = input("Enter the Rate:")
floatRate = float(rate)

if floatRate<=40:
    if floatHours>40:
        overtimeHours = floatHours -40
        regularPay = (floatHours-overtimeHours)*floatRate
        overtimeRate = floatRate *1.5
        overtimePay = overtimeHours*overtimeRate
        print("Pay:",regularPay+overtimePay)
    else:
        print("Pay:",floatHours*floatRate)
else:
    print("I can't process this shit")
input("Close please")
