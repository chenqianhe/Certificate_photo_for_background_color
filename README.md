# 基于Paddle的自制证件照小工具

**这个工具是在AI抠图的基础上，再加上换底和换大小功能做成的小软件，拥有简易的GUI界面。接着往下看完，你就能拥有一款自己专属证件照小工具了！**

## 一、简介

- 先来看看效果吧
- 图片源自网络
- 首先是原图

![img](https://ai-studio-static-online.cdn.bcebos.com/6c717429b23c4339b029c4f4461a28ace7e471123e58424ba8c79a4748dc7c93)

- 然后是中间的扣图结果

![img](https://ai-studio-static-online.cdn.bcebos.com/2b03c818033844ddbff511f5200582da4f37f545a2f5421687aa23231915acdd)

- 可以看到基本扣的十分干净
- 然后再看看最终的红色二寸照片

![img](https://ai-studio-static-online.cdn.bcebos.com/37833b8bd0184752a1c9c6d4f2cdfce3b9b908edabd84b11a6d19babc301e196)

- 可以看到效果是非常不错的

接下来看看我们的GUI界面，让这样一款小工具更加简便好用

- 首先是进入界面，非常简洁，选取照片后点击你想要格式的按钮即可

![img](https://ai-studio-static-online.cdn.bcebos.com/5f1cc0de0c45439296ac5b67c77e87b90678f5c3d917477c9c475dc11aff85b1)

- 如果你没有选去就点击的话会有报错提示

![img](https://ai-studio-static-online.cdn.bcebos.com/37a3627b8d554c6b841690a341cf631a81273c4848d64431a532b373b43314af)

- 如果正常选择文件，完成转换的进程之后，会提示成功和保存的位置

![img](https://ai-studio-static-online.cdn.bcebos.com/53fb67cb3e464177b90ee4a83b9d20ce53bf80d88dda43ffb992cbc224196e45)

- 进入文件夹就可以看到成果了

![img](https://ai-studio-static-online.cdn.bcebos.com/b6089933b96c4d108032517b9f9ef5a7bcf273ec2c59417c99c92ff1695303e4)

##  二、实现方式

### 1.扣图模型

扣图模型我们选择的是Paddle的deeplabv3p_xception65_humanseg模型。 这是一个已经训练好的模型，我们可以直接使用，简便易用。

### 2.接下来来看代码实现

首先导入要用到的库

```python

import paddlehub as hub
from PIL import Image
import numpy as np
import tkinter.filedialog
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sys
```

先看我们的图片处理函数，这一部分直接利用现成的模型，提取图片，并进行合成

```python
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
```



接下来是GUI部分

callbackClose函数是关闭程序时的提示框

selectPath函数是选取文件的函数

```python
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

```



下面六个函数对应六种不同的处理方式

- 白色、蓝色、红色，一寸，两寸

```python
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
```

然后是主函数，加载模型，和GUI的主界面的建立。

```python
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
```



最后，当所有代码调试完成之后，您就可以对程序进行打包了，生成一个EXE文件，这样，您就真正拥有了一款属于您自己的证件照小工具了！！！