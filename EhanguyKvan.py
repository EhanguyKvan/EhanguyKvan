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
