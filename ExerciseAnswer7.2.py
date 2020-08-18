filename = input("Enter the filename: ")
readfile = open(filename)
count = 0
total = 0

for line in readfile:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ignorethis = line.find('0')
    needthis = float(line[ignorethis:])
    count = count + 1
    total = total + needthis

average = total/count

print("The average confidence is:", average)
