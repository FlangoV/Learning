file_handle = open("romeo.txt")
word_list = list()

# Função que organiza uma linha
def OrganizeWordsInLists(line, word_list):
    for word in range(len(line.split())):
        eachword = line.split()[0 + word]
        if not eachword in word_list:
            word_list.append(eachword)
            
# Loop para cada linha
for line in file_handle:
    OrganizeWordsInLists(line, word_list)

word_list.sort()
print(word_list)
