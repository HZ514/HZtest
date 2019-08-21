#!/usr/bin/env python
# encoding: utf-8
import ctypes
import platform
if platform.system() == "Windows":
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
elif platform.system() == "Linux":
    pass


def set_cmd_color(color, handle=None):
    """(color) -> bit
    Example: set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


def print_col_lin(*args,mode=1,colour="o",backgrend="",**kwargs):
    """
    linux终端下的颜色打印
    :param message:需要显示的信息
    :param mode:显示模式，0（默认值，正常显示）、1（高亮，即加粗）、4（下划线）、7（反显）
    :param colour:显示颜色：o(根据终端调整),r(红色),g(绿色),y(黄色),b(蓝色),p(梅色,淡红色),c(天蓝色),d(灰色)
    :param backgrend:背景颜色：o(原始颜色),r(红色),g(绿色),y(黄色),b(蓝色),p(梅色),c(天蓝色),d(灰色)；默认"",表示无背景
    """
    colour_choice = {"o":37,"r":31,"g":32,"y":33,"b":34,"p":35,"c":36,"d":30,
                     "db":34, "dg":32, "dc":36, "dr":31, "dp":35, "dy":33, "dw":37}
    backgrend_choice = {"":0,"o":40,"r":41,"g":42,"y":43,"b":44,"p":45,"c":46,"d":47,
                        "db": 44, "dg": 42, "dc": 46, "dr": 41, "dp": 45, "dy": 43, "dw": 47}
    if backgrend_choice[backgrend] == 0:
        print("\033[{};{}m".format(mode,colour_choice[colour]),*args,"\033[0m",**kwargs)
    else:
        print("\033[{};{};{}m".format(mode, colour_choice[colour],backgrend_choice[backgrend]),*args,"\033[0m", **kwargs)


def print_col_win(*args,mode=1,colour="o",backgrend="",**kwargs ):
    """
    windows终端下的颜色打印
    :param colour:显示颜色：o(白色),r(红色),g(绿色),y(黄色),b(蓝色),p(淡红色),c(天蓝色),d(灰色),
                            db(暗蓝色)，dg(暗绿色)，dsb(暗天蓝色),dr(暗红色),dp(暗粉红色),dy(暗黄色)，
                            dw(暗白色)
    :param backgrend:背景颜色：o(白色),r(红色),g(绿色),y(黄色),b(蓝色),p(淡红色),c(天蓝色),d(灰色),
                                db(暗蓝色)，dg(暗绿色)，dc(暗天蓝色),dr(暗红色),dp(暗粉红色),dy(暗黄色)，
                                dw(暗白色)
                                默认"",表示无背景
    :return:
    """
    colour_choice = {"o": 0x0F, "r": 0x0c, "g": 0x0a, "y": 0x0e, "b": 0x09, "p": 0x0d, "c": 0x0b, "d": 0x08,
                     "db":0x01,"dg":0x02,"dc":0x03,"dr":0x04,"dp":0x05,"dy":0x06,"dw":0x07}
    backgrend_choice = {"": 0x00, "o": 0xf0, "r": 0xc0, "g": 0xa0, "y": 0xe0, "b": 0x90, "p": 0xd0, "c": 0xb0,
                        "d": 0x80,"db":0x10,"dg":0x20,"dc":0x30,"dr":0x40,"dp":0x50,"dy":0x60,"dw":0x70}
    if platform.system() == "Windows":
        set_cmd_color(colour_choice[colour] | backgrend_choice[backgrend],handle=std_out_handle)
    print(*args,**kwargs)
    if platform.system() == "Windows":
        set_cmd_color(0x07, handle=std_out_handle)


def print_colour(*args,mode=1,colour="o",backgrend="",**kwargs ):
    """
    对两个平台进行统一调用接口处理
    :param mode: 该参数linux平台运行有效；显示模式，0（默认值，正常显示）、1（高亮，即加粗）
    :param colour: 显示颜色：o(白色),r(红色),g(绿色),y(黄色),b(蓝色),p(粉红色),c(天蓝色),d(灰色)
                            db(暗蓝色)，dg(暗绿色)，dsb(暗天蓝色),dr(暗红色),dp(暗粉红色),dy(暗黄色)，
                            dw(暗白色)
    :param backgrend: 背景颜色：默认"",表示无背景。o(白色背景),r(红色),g(绿色),y(黄色),b(蓝色),p(粉红色),c(天蓝色),d(灰色)；
                                db(暗蓝色)，dg(暗绿色)，dc(暗天蓝色),dr(暗红色),dp(暗粉红色),dy(暗黄色)，dw(暗白色)
    :return:
    """
    if platform.system() == "Windows":
        print_col_win(*args,mode=mode,colour=colour,backgrend=backgrend,**kwargs)
    elif platform.system() == "Linux":
        print_col_lin(*args,mode=mode,colour=colour,backgrend=backgrend,**kwargs)


if __name__ == "__main__":
    print_colour("白色：you are bad boy")
    print_colour("蓝色：you are bad boy", colour="b")
    print_colour("绿色：you are bad boy", colour="g")
    print_colour("天蓝色：you are bad boy", colour="c")
    print_colour("红色：you are bad boy",colour="r")
    print_colour("粉红色：you are bad boy", colour="p")
    print_colour("黄色：you are bad boy",colour="y")
    print_colour("灰色：you are bad boy",colour="d")
    print_colour("暗蓝色：you are bad boy",colour="db")
    print_colour("暗绿色：you are bad boy",colour="dg")
    print_colour("暗天蓝色：you are bad boy",colour="dc")
    print_colour("暗红色：you are bad boy",colour="dr")
    print_colour("暗粉红色：you are bad boy",colour="dp")
    print_colour("暗黄色：you are bad boy",colour="dy")
    print_colour("暗白色：you are bad boy",colour="dw")

    print_colour("红色背景：you are bad boy",colour="c",backgrend="r")
    print_colour("白色背景：you are bad boy",colour="c",backgrend="o")
    print_colour("黄色背景：you are bad boy",colour="c",backgrend="y")
    print_colour("蓝色背景：you are bad boy",colour="c",backgrend="b")
    print_colour("粉红色背景：you are bad boy",colour="c",backgrend="p")
    print_colour("天蓝色背景：you are bad boy",colour="c",backgrend="c")
    print_colour("灰色背景：you are bad boy",colour="c",backgrend="d")
    print_colour("暗蓝色背景：you are bad boy",colour="c",backgrend="db")
    print_colour("暗绿色背景：you are bad boy",colour="c",backgrend="dg")
    print_colour("暗天蓝背景：you are bad boy",colour="c",backgrend="dc")
    print_colour("暗红色背景：you are bad boy",colour="c",backgrend="dr")
    print_colour("暗粉红色背景：you are bad boy",colour="c",backgrend="dp")
    print_colour("暗黄色背景：you are bad boy",colour="c",backgrend="dy")
    print_colour("暗白色背景：you are bad boy",colour="c",backgrend="dw")
