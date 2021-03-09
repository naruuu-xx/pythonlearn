from sys import  argv

script, input_file = argv
def print_all(f):#函数定义
    print(f.read())

def rewind(f):#函数定义
    f.seek(0)

def print_a_line(line_count, f):#函数定义
    print(line_count, f.readline(),end="")

current_file = open(input_file)#打开文件

print("First let's print the whole file :\n")

print_all(current_file)#显示文件

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
