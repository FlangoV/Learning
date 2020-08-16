try:
    file = input("Enter a file name:")
except:
    print("Non existant file")
    input("Press Enter to exit")
    exit()

readings = open(file)
for lines in readings:
    lines = lines.rstrip()
    lines = print(lines.upper())
