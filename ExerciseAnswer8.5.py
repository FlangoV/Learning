read_file = open('mbox-short.txt')
lines_list = list()
count = 0

for line in read_file:
    if line.startswith("From:"):
        continue
    if line.startswith("From "):
        count = count + 1
        lines_list = line.split()[1]
        print(lines_list)

print("There were",count, "lines in the file with From as the first word")
