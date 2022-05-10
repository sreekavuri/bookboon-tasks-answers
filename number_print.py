def print_num(x, y):
    for n in range(x, y):
        z = n % 10
        if z == 0:
            if n in words:
                print(words[n])
        else:
            print(n)


words = {0: "Zero", 10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
         80: "Eighty", 90: "Ninety", 100: "Hundred"}

print_num(0, 101)
