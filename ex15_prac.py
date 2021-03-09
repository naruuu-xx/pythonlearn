from sys import argv

script  = argv#解包
filename = input("the filename is:")

txt = open(filename)#把文件打开

print(f"Here's your file {filename}:")#键入文件名字
print(txt.read())#查看键入的文件

#print("Type the filename again:")#再次键入文件名字
#file_again = input(">")

#txt_again = open(file_again)#再次打开文件

#print(txt_again.read())#再次阅读文件
