#default_file_path = "output/"
#filename = (default_file_path + input("Output filename: ").removesuffix(".py") + ".py")
#filename = input("Output filename: ").removesuffix(".py") + ".py"
filename = "odd_or_even.py"
max_int = int(input("What should be the end of the \"Odd or Even\" Check? "))

#with open(filename, "w") as f:
#    print("Hello world", file=f)


output = 'input = input("Enter a number: ") \n'

for num in range(max_int + 1):
    if num % 2 == 0:
        value = "Even"
    else:
        value = "Odd"
    output += f'''
if(input == {num}):
    print("The number is {value}")
'''
    
with open(filename, "w") as f:
    print(output, file=f)