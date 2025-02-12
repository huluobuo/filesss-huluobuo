import tkinter as tk


class Gui():

    def __init__(self, root):
        self.root = root


    def button_1_func(self):
        print('button_1_func')


    def window(self):
        self.root.title('')  # 设置窗口标题
        # self.root.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')   # 设置窗口图标
        # 设置窗口大小变量
        width = 300
        height = 300
        # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)


        self.root.geometry(size_geo)
    
    def subassembly(self): 

        # 主窗口设置
        self.Label_1 = tk.Label(self.root, text='Hello World!', font=('Arial', 12), width=10, height=2)
        self.button_1 = tk.Button(self.root, text='Click Me!', command=self.button_1_func)


    def show_things(self):
        self.Label_1.pack()
        self.button_1.pack()
    
    def run(self):
        self.window()
        self.subassembly()
        self.show_things()
        self.root.mainloop()



if __name__ == '__main__':
    root = tk.Tk()
    gui = Gui(root)
    gui.run()
