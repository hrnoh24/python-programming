symbol2num = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

s = "MCMXCIV"

total_sum = 0
idx = 0
while idx < len(s):
    if idx == len(s) - 1:
        total_sum += symbol2num[s[idx]]
        break

    if (s[idx] == "I" and (s[idx+1] == "V" or s[idx+1] == "X")) or \
        (s[idx] == "X" and (s[idx+1] == "L" or s[idx+1] == "C")) or \
        (s[idx] == "C" and (s[idx+1] == "D" or s[idx+1] == "M")):
        total_sum += symbol2num[s[idx+1]] - symbol2num[s[idx]]
        idx += 2
        continue

    total_sum += symbol2num[s[idx]]
    idx += 1

print(total_sum)