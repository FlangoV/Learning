fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    whattoignore=line.find("0")
    number= float(line[whattoignore:])
    count = count + 1
    total = total + number

average = total/count
print("Average spam confidence:",average)
