text = "X-DSPAM-Confidence:    0.8475";
pos1 = text.find('0.8475')
pos2 = text.find('5')
result = text[pos1 : pos2]
result = float(result)
print(result)
