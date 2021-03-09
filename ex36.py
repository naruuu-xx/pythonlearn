def start():
    print("""这是一个测试游戏。请根据提示输入字母，进行操作。
    ok let's start!
    """)
    usrnm()
    print("""there are two doors,left and right.
    Which one do you want to choice?
    这有两扇门，左边和右边，你会选择哪一边？
    """)
    choice = input("> ")
    if choice == "left":
        Cthulhuroom()
    elif choice =="right":
        snakeroom()
    else:
        print("""
        good job the best choice is choose nothing.
        没错，最好的选择就是什么都不选。
        """)
def usrnm():
    print("Hi,I'm N,what's your name?")
    name = input("> ")
    print(f"Ok,your name is {name}?")
def dead(why):
    print(why,"sorry you are lose,you can try it again.")
    exit(0)
def snakeroom():
    dead("""You enter the snakeroom and bited by snake,finally you dead.""")
def Cthulhuroom():
    dead("""Hi,Man you see the Cthulhu,you dead.""")

start()
