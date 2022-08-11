import tkinter as tk

def calc():
    def go():
        print(eval(entry1.get()))
    win = tk.Tk()  # 初始化
    # 创建单行可输入文本框
    entry1 = tk.Entry(win, width=50)
    # entry1=tkinter.Entry(win,show="*",width=50,bg="red",fg="black")
    # 创建Button按键
    frequency = tk.Button(win, text='确认', command=go)  # 输入次数信息的Entry控件
    frequency.pack()
    entry1.pack()
    win.mainloop()

def echo(stringlist):
    string = stringlist.split("+")
    for i in string:
        print(i,end="")
    print()
