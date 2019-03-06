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
        
def TJisuan(a, b):
    #用于计算x+y=a;x-y=b类型的算式
    x = (a + b)/2
    y = (a - b)/2
    print('x为' + x + 'y为' + y)
    
def FTJisuanX(a, b):
    #同TJisuan，不过为返回x
    x = (a + b)/2
    y = (a - b)/2
    return x
    
def FTJisuanY(a, b):
    #同TJisuan，不过为返回y
    x = (a + b)/2
    y = (a - b)/2
    return y
    
def Qiuhe(a=0, b):
    #求和用，默认到0
    x = b(a+b)/2
    return x
