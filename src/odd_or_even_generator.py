#default_file_path = "output/"
#filename = (default_file_path + input("Output filename: ").removesuffix(".py") + ".py")
filename = input("Output filename: ").removesuffix(".py") + ".py"

with open(filename, "w") as f:
    print("Hello world", file=f)