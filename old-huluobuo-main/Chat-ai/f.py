print('正在导入界面所需的文件...')
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
#**********************************************************************************************************************#
print('导入AI所需文件...')
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#**********************************************************************************************************************#
print('导入辅助文件...')
import json
from datetime import datetime
import sys
import time


########################################################################################################################


class Chat:

    """一个AI聊天机器人的代码"""
    def __init__(self, master):
        print('初始化...')
        self.master = master
        master.title("AI聊天")
        master.resizable(False, False)
        #--------------------------------------------------------------------------------------------------------------#
        print('准备界面...')
        self.chat_text = ScrolledText(master)
        self.chat_text.pack(fill=tk.BOTH, expand=True)
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.send_button = tk.Button(self.input_frame, text="发送", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        self.chat_history = []
        #--------------------------------------------------------------------------------------------------------------#
        print('绑定按键...')
        self.current_side = "odd"
        self.chat_text.bind("<MouseWheel>", self.scroll_history)
        self.chat_text.bind("<Up>", self.scroll_history_up)
        self.chat_text.bind("<Down>", self.scroll_history_down)
        self.input_entry.bind("<Return>", self.send_message)
        #--------------------------------------------------------------------------------------------------------------#
        print('获取AI所需文件...')
        try:
            with open('./more/V2.json', 'r', encoding='utf-8') as f:
                data = json.loads(f.read())
        except FileNotFoundError:
            print("因AI所需文件未找到，启动失败")
            time.sleep(5)
            sys.exit()
        except json.decoder.JSONDecodeError:
            print("因AI所需文件已损坏，启动失败")
            time.sleep(5)
            sys.exit()
        #--------------------------------------------------------------------------------------------------------------#
        print('创建AI中（可能需要一些时间）')
        self.chatbot = ChatBot('Amy')
        self.trainer = ListTrainer(self.chatbot)
        self.trainer.train(data)
        #--------------------------------------------------------------------------------------------------------------#
        print('准备就绪')
        self.add_message('-----------------------------AI-BOT2.10.10-旗舰版------------------------------')

    #******************************************************************************************************************#

    def get_time(self):
        time = datetime.now()
        return time.strftime("现在时间是： %Y-%m-%d %H:%M:%S")

    #******************************************************************************************************************#

    def send_message(self, event=None):
        message = self.input_entry.get()
        if message:
            self.add_message(str(message))
            message = self.chatbot.get_response(message)
            if "{get_time()}" in str(message):
                message = self.get_time()
            self.add_message(str(message))
            self.input_entry.delete(0, tk.END)

    #******************************************************************************************************************#

    def add_message(self, message):
        side = self.current_side
        color = "white" if side == "odd" else "green"
        anchor = "left" if side == "odd" else "right"
        self.chat_text.tag_configure(side, background=color, justify=anchor)
        self.chat_text.insert(tk.END, message + '\n', side)
        self.chat_history.append((side, message))
        self.current_side = "even" if side == "odd" else "odd"
        self.scroll_to_bottom()

    #******************************************************************************************************************#

    def scroll_to_bottom(self):
        self.chat_text.yview_moveto(1.0)

    #******************************************************************************************************************#

    def scroll_history(self, event):
        if event.delta > 0:
            self.scroll_history_up()
        else:
            self.scroll_history_down()

    #******************************************************************************************************************#

    def scroll_history_up(self):
        self.chat_text.yview_scroll(-1, "units")

    #******************************************************************************************************************#

    def scroll_history_down(self):
        self.chat_text.yview_scroll(1, "units")


########################################################################################################################


########################################################################################################################
#                                                    MORE                                                              #
########################################################################################################################
#        MAKER:    OOOO                                                                                                #
#        EMAIL:    hu_luo_buo@outlook.com                                                                              #
########################################################################################################################
