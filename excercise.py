s = "abcdefghijklmnopqrstuvwxy"

partSize = len(s) // 5

for i in range(0, partSize):
    print(s[i*5:i*5+5])
