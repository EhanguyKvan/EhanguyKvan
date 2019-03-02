def chushihuacuowu():
    #用于处理初始化库错误
    try:
        import os  #用于新建文件夹
    except ImportError:
        print('请先下载相关库，否则本库则会无法正常运行')
    
    mulu = input() + r'\EhanguyKvan'
    try:
        os.mkdir(mulu)                            #创建文件夹
    except FileNotFoundError:
        print('自定义目录文件夹路径错误，请核对路径输入')
        chushihuacuowu()
    except FileExistsError:
        print('自定义目录文件夹创建错误，请更换路径再次尝试')
        chushihuacuowu()
    except OSError:
        print('自定义目录文件夹路径语法错误，请核对路径语法输入')
        chushihuacuowu()

def Chushihua():
    #用于初始化库
    try:
        import os  #用于新建文件夹
    except ImportError:
        print('请先下载相关库，否则本库则会无法正常运行')
    
    global mulu
    global linshimulu
    mulu = r'C:\Users\Administrator\AppData\Local\EhanguyKvan'
    linshimulu = input()
    if linshimulu != '':
        mulu = linshimulu + r'\EhanguyKvan'
        try:
            os.mkdir(mulu)                            #创建文件夹
        except FileNotFoundError:
            print('自定义目录文件夹路径错误，请核对路径输入')
            chushihuacuowu()
        except FileExistsError:
            print('自定义目录文件夹创建错误，请更换路径再次尝试')
            chushihuacuowu()
        except OSError:
            print('自定义目录文件夹路径语法错误，请核对路径语法输入')
            chushihuacuowu()
    try:
        os.mkdir(mulu)                                        #创建文件夹
    except FileExistsError:
        print('主目录文件夹创建错误，正在尝试路径切换······')
        mulu = r'C:\桌面\EhanguyKvan'
        try:
            os.mkdir(mulu)                                        #创建文件夹
        except FileExistsError:
            print('副目录文件夹创建错误，请检查目录路径或者关闭已打开的本目录')
            chushihuacuowu()

def Ciyun(text,color='white'):
    #coding=utf8                                          # Python3. 以后，可写可不写。
    try:
        import os
        from wordcloud import WordCloud, ImageColorGenerator  # 引入词云WordCloud
        from scipy.misc import imread                         # 引入读取图片的工具
        import jieba                                          # 引入分词的词典
        import matplotlib.pyplot as plt      # 制图包， as作用是重命名长度大的程序，方便引用写码
    except ImportError:
        print('请先下载相关库，否则本库则会无法正常运行')
    
    cut_text = ' '.join(jieba.cut(text))# 让jieba把文本进行分词，从而词云显示“词组”而不是“句子”。并重新命名为cut_text，以示区别。
    wc = WordCloud(                                        # WordCloud()设定词云参数，.generate()将str文本生成词云                  # 设定词云形状是bg_pic。
        font_path='c:\windows\Fonts\simhei.ttf',            # 设定文字的类型为中文黑体。
        background_color=color,                          # 设定图片背景为白色。默认为黑色。
        scale=15,                                          # 设定图片像素密度为15.默认之为1。
    ).generate(cut_text)                                   
    plt.imshow(wc,interpolation='bilinear')        # Bilinear：双线性插值算法，用来缩放显示图片。缩放就是把原图片的像素应用坐标系统，用坐标表示，                                          # 双线性插值算法就是把一个坐标不是整数的点的坐标，用最近的四个整数点坐标指示出来；                                               # 输出时，将云图按照图片的色彩分布进行显示。
    plt.axis('off')                                        # 关闭坐标轴显示
    plt.show() 

def PA(numbers):
    #全称为Multiplication algorithm，翻译为算乘法
    #用途为算乘积
    number = 0
    try:
        List = numbers.split(' ')
    except AttributeError:
        print("输入的不可为字符")
    else:
        try:
            y = (int(List[0]) * int(List[1]))
        except ValueError:
            print("输入的不可为字符")
        else:  
            del List[0]
            del List[1]
            errorm = True
            while (errorm):
                try:
                    if List[0] != '':
                        try:
                            y = y * List[0]
                        except TypeError:
                            print('未知错误')
                            errorm = False
                        except IndexError:
                            errorm = False
                        else:
                            del List[0]
                except IndexError:
                    errom = False
                    break
            print(y)

def Fangcheng(a11, a12, b1, a21, a22, b2):
    #用于算(x * a11 + y * a12 = b1 ;x * a11 + y * a12 = b1 ;类型的二元一次方程)，且必须输入int
    try:
        m = a21 / a11
        ap22 = a22 - m * a12
        bp2 = b2- m + b1
        y = bp2 / ap22
        x = (b1 - a12 * y) / a11
        str(x)
        str(y)
        print('x为' + x + ', y为' + y)
    except TypeError:
        print('请不要输入非整数')
        
def FangchengX(a11, a12, b1, a21, a22, b2):
    #同Fangcheng，不过返回x值(int)
    try:
        m = a21 / a11
        ap22 = a22 - m * a12
        bp2 = b2- m + b1
        y = bp2 / ap22
        x = (b1 - a12 * y) / a11
        return(x)
    except TypeError:
        print('请不要输入非整数')
    
def FangchengY(a11, a12, b1, a21, a22, b2):
    #同Fangcheng，不过返回y值(int)
    try:
        m = a21 / a11
        ap22 = a22 - m * a12
        bp2 = b2- m + b1
        y = bp2 / ap22
        return(y)
    except TypeError:
        print('请不要输入非整数')

def Jisuan(x, y, fuhao):
    #用于简单的四则计算
    try:
        x = float(x)
        y = float(y)
        if fuhao == '+':
            z = x + y
            print(z)
        elif fuhao == '-':
            z = x - y
            print(z)
        elif fuhao == '*':
            z = x * y
            print(z)
        elif fuhao == '/':
            z = x / y
            print(z)
        else:
            print('符号错误，请确定您目前为英文输入法或检查其它问题')
    except ValueError:
        print('你不能输入非实数或其他无效数字')
    except ZeroDivisionError:
        print('你不能除以0！')
        
def FJisuan(x, y, fuhao):
    #同Jisuan函数，不过为返回
    try:
        x = float(x)
        y = float(y)
        if fuhao == '+':
            z = x + y
            return z
        elif fuhao == '-':
            z = x - y
            return z
        elif fuhao == '*':
            z = x * y
            return z
        elif fuhao == '/':
            z = x / y
            return z
        else:
            print('符号错误，请确定您目前为英文输入法或检查其它问题')
    except ValueError:
        print('你不能输入非实数或其他无效数字')
    except ZeroDivisionError:
        print('你不能除以0！')