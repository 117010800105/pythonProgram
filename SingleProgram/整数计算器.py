from tkinter import Tk, Button, Entry, StringVar

# 建立窗口程序
win = Tk()
win.title("整数计算器")
win.geometry("240x300")
win.resizable(0, 0)

# 建立文本框
result = StringVar()
entry = Entry(win, background="white", justify="right",
              textvariable=result, font=('', '26', ''))
entry.place(x=25, y=20, width=190, height=50)
result.set("0")


# 定义函数根据按钮内容进行操作
def calc(event):
    global num1, num2, opr
    char = event.widget['text']
    if '0' <= char <= '9':
        result.set(eval(result.get()) * 10 + eval(char))
    if char == 'C':
        result.set('0')
    if char == '+' or char == '-' or char == '*' or char == '/':
        num1 = eval(result.get())
        opr = char
        result.set('0')
    if char == '=':
        num2 = eval(result.get())
        if opr == '+':
            result.set(num1 + num2)
        elif opr == '-':
            result.set(num1 - num2)
        elif opr == '*':
            result.set(num1 * num2)
        elif opr == '/':
            result.set(num1 // num2)
        num1 = eval(result.get())


# 建立按钮数组
strList = ["7", "8", "9", "/", "4", "5", "6",
           "*", "1", "2", "3", "-", "0", "C", "=", "+"]
count = 0
for item in strList:
    btn = Button(win, text=item, font=('', '26', ''))
    btn.place(x=25 + count % 4 * 50, y=80 + count // 4 * 50, width=40, height=40)
    btn.bind('<Button-1>', calc)
    count += 1

# 让程序处于消息监听状态
win.mainloop()
