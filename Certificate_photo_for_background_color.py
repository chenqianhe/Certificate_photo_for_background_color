import paddlehub as hub
from PIL import Image
import numpy as np
import tkinter.filedialog
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sys


def process(path):

    global rawpath

    tpath = [rawpath]
    input_dict = {"image": tpath}

    results = module.segmentation(data=input_dict)

    # 查看results内容
    # for result in results:
    #     print(result)

    # 图像背景和前景融合

    base_image = Image.open(path).convert('RGB')

    fore_image = Image.open(f'humanseg_output/test.png').resize(base_image.size)

    # 图片加权合成
    scope_map = np.array(fore_image)[:, :, -1] / 255
    scope_map = scope_map[:, :, np.newaxis]
    scope_map = np.repeat(scope_map, repeats=3, axis=2)
    res_image = np.multiply(scope_map, np.array(fore_image)[:, :, :3]) + np.multiply((1 - scope_map),
                                                                                     np.array(base_image))

    # 保存图片
    res_image = Image.fromarray(np.uint8(res_image))
    res_image.save(f'humanseg_output/2.png')

    tkinter.messagebox.showwarning(title='提示', message='已保存到humanseg_output文件夹')

    sys.exit()


def callbackClose():
    tkinter.messagebox.showwarning(title='警告', message='点击了关闭按钮')
    sys.exit(0)


def selectPath():
    global rawpath

    # 选择文件path_接收文件地址
    path_ = tkinter.filedialog.askopenfilename()

    # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
    # 注意：\\转义后为\，所以\\\\转义后为\\
    path_ = path_.replace("/", "\\\\")
    rawpath = path_
    # path设置path_的值
    path.set(path_)


def white_1():  # 当acction被点击时,该函数则生效

    if rawpath is '':
        tkinter.messagebox.showwarning(title='错误', message='未选择文件')
        sys.exit()

    action1.configure(state='disabled')  # 将按钮设置为灰色状态，不可使用状态
    process('photo/white_1.png')


def blue_1():  # 当acction被点击时,该函数则生效

    if rawpath is '':
        tkinter.messagebox.showwarning(title='错误', message='未选择文件')
        sys.exit()

    action2.configure(state='disabled')  # 将按钮设置为灰色状态，不可使用状态
    process('photo/blue_1.png')


def red_1():  # 当acction被点击时,该函数则生效

    if rawpath is '':
        tkinter.messagebox.showwarning(title='错误', message='未选择文件')
        sys.exit()

    action3.configure(state='disabled')  # 将按钮设置为灰色状态，不可使用状态
    process('photo/red_1.png')


def white_2():  # 当acction被点击时,该函数则生效

    if rawpath is '':
        tkinter.messagebox.showwarning(title='错误', message='未选择文件')
        sys.exit()

    action4.configure(state='disabled')  # 将按钮设置为灰色状态，不可使用状态
    process('photo/white_2.png')


def blue_2():  # 当acction被点击时,该函数则生效

    if rawpath is '':
        tkinter.messagebox.showwarning(title='错误', message='未选择文件')
        sys.exit()

    action5.configure(state='disabled')  # 将按钮设置为灰色状态，不可使用状态
    process('photo/blue_2.png')


def red_2():  # 当acction被点击时,该函数则生效

    if rawpath is '':
        tkinter.messagebox.showwarning(title='错误', message='未选择文件')
        sys.exit()

    action6.configure(state='disabled')  # 将按钮设置为灰色状态，不可使用状态
    process('photo/red_2.png')


if __name__ == '__main__':

    rawpath = ""
    module = hub.Module(name="deeplabv3p_xception65_humanseg")  # 调用模型, version='1.0.0'

    main_box = tk.Tk()
    #变量path
    path = tk.StringVar()

    main_box.title("证件照换底换大小")  # 添加标题
    tk.Label(main_box, text="目标路径:").grid(row=0, column=0)

    ttk.Label(main_box, text="请保证路径及名称不含中文").grid(column=1, row=1)
    ttk.Label(main_box, text="原文件最好也是证件照").grid(column=1, row=2)

    tk.Entry(main_box, textvariable=path).grid(row=0, column=1)
    tk.Button(main_box, text="路径选择", command=selectPath).grid(row=0, column=2)

    main_box.protocol("WM_DELETE_WINDOW", callbackClose)

    action1 = ttk.Button(main_box, text="白色一寸", command=white_1)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    action1.grid(column=0, row=3)  # 设置其在界面中出现的位置 column代表列 row 代表行

    action2 = ttk.Button(main_box, text="蓝色一寸", command=blue_1)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    action2.grid(column=0, row=4)  # 设置其在界面中出现的位置 column代表列 row 代表行

    action3 = ttk.Button(main_box, text="红色一寸", command=red_1)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    action3.grid(column=0, row=5)  # 设置其在界面中出现的位置 column代表列 row 代表行

    action4 = ttk.Button(main_box, text="白色二寸", command=white_2)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    action4.grid(column=2, row=3)  # 设置其在界面中出现的位置 column代表列 row 代表行

    action5 = ttk.Button(main_box, text="蓝色二寸", command=blue_2)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    action5.grid(column=2, row=4)  # 设置其在界面中出现的位置 column代表列 row 代表行

    action6 = ttk.Button(main_box, text="红色二寸", command=red_2)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    action6.grid(column=2, row=5)  # 设置其在界面中出现的位置 column代表列 row 代表行

    main_box.mainloop()
