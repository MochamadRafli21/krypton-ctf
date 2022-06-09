text = input("Input string to decrypt:  ")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(alpha)):
    result = ""
    for char in text:
        if char in alpha:
            num = alpha.find(char)
            num = num - i
            if num < 0:
                num = num + len(alpha)
            result = result + alpha[num]
        else : result = result + char
    print(f"{i}> {result}")

