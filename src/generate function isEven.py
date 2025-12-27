max_int = 9999

output = "def isEven(num):\n"

for num in range (max_int + 1):
    #output += f"if (num == {num}):\n     return \"{num % 2 == 0}\""
    output += f"    if (num == {num}):\n        return {num % 2 == 0}\n"

with open("function isEven.py", "w") as file:
    print(output, file=file)