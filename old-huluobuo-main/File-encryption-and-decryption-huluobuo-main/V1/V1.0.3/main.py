import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import logging

# 配置日志
logging.basicConfig(filename='file_encryptor.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_key():
    """生成并保存密钥"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("信息", "密钥已生成并保存为 secret.key")
    logging.info("密钥已生成并保存为 secret.key")

def load_key(key_path):
    """加载保存的密钥"""
    try:
        return open(key_path, "rb").read()
    except FileNotFoundError:
        messagebox.showerror("错误", "密钥文件未找到")
        logging.error("密钥文件未找到: %s", key_path)
        return None

def encrypt_file(file_name, key_path):
    """加密文件"""
    key = load_key(key_path)
    if key is None:
        return

    fernet = Fernet(key)
    try:
        with open(file_name, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(file_name, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
        messagebox.showinfo("信息", f"文件 {file_name} 已加密")
        logging.info("文件 %s 已加密", file_name)
    except Exception as e:
        messagebox.showerror("错误", f"加密失败: {e}")
        logging.error("加密失败: %s", e)

def decrypt_file(file_name, key_path):
    """解密文件"""
    key = load_key(key_path)
    if key is None:
        return

    fernet = Fernet(key)
    try:
        with open(file_name, "rb") as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(file_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
        messagebox.showinfo("信息", f"文件 {file_name} 已解密")
        logging.info("文件 %s 已解密", file_name)
    except Exception as e:
        messagebox.showerror("错误", f"解密失败: {e}")
        logging.error("解密失败: %s", e)

def select_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def select_key(entry):
    key_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, key_path)

def main():
    root = tk.Tk()
    root.title("文件加解密工具")

    tk.Label(root, text="文件路径:").grid(row=0, column=0, padx=10, pady=10)
    file_entry = tk.Entry(root, width=50)
    file_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="选择文件", command=lambda: select_file(file_entry)).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="密钥路径:").grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(root, width=50)
    key_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="选择密钥", command=lambda: select_key(key_entry)).grid(row=1, column=2, padx=10, pady=10)

    tk.Button(root, text="生成密钥", command=generate_key).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(root, text="加密文件", command=lambda: encrypt_file(file_entry.get(), key_entry.get())).grid(row=2, column=1, padx=10, pady=10)
    tk.Button(root, text="解密文件", command=lambda: decrypt_file(file_entry.get(), key_entry.get())).grid(row=2, column=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()                                    #O!!! 100!!!