import moveclick
from Fillhealthinformation import fill_origin, fill_vaccine_date

import os
import subprocess

from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps

import pyautogui
import time
import sys

import pyperclip
# path = r'/Applications/Wechat_Work.app'
# os.system("open" + shlex.quote(path))

# 0. 自动打开微信企业软件
# subprocess.call(
#     ["/usr/bin/open", "-W", "-n", "-a", path]
# )
# print("The wechat work is open")
# 获取窗口焦点
# 本机屏幕分辨率为（2880，1800）
# coordinate = pyautogui.locateCenterOnScreen(image_path)
# print(coordinate)
# screen = pyautogui.size()
# print(screen) # 获取的屏幕分辨率为（1680， 1050）
# x = int(coordinate.x * screen.width / 2880)
# y = int(coordinate.y * screen.heith / 2880)
# print(x, y)
# coordinate = pyautogui.position()

def open_wechat_work(x, y):
    open_wechat_work = (x, y)
    moveclick.move_and_click(open_wechat_work)
    time.sleep(0.5)
    return True

def start_service_position(x, y):
    start_service_position = (x,y)
    moveclick.move_and_click(start_service_position)
    time.sleep(0.5)
    return True

def health_system(x, y):
    health_system = (x, y)
    moveclick.move_and_click(health_system)
    time.sleep(0.8)
    return True

def start_student_lowdown(begin_submit):
    time.sleep(0.1)
    student_health_situation_report(startOrdinate=(460, 281), endOrdinate=(568, 283), situationReprot="学生健康") # 检测页面是否正确打开
    # pyautogui.click(clicks = 1)
    pyautogui.vscroll(-200)
    moveclick.move_and_click(begin_submit)
    time.sleep(0.5)
    return True

def start_report_position(visit, health_code, place):
    # situationReprot用来检查页面
    time.sleep(0.5)
    student_health_situation_report(startOrdinate=(718, 543), endOrdinate=(841, 543), situationReprot = "状况申报") # 检测页面是否正确打开
    # fill_origin(province_coordinate=(435, 789), city_coordinate=(590, 785))
    print("4. 已经打开学生健康状况申报下滑到底，准备填写申报信息...")
    # 添加当日是否外出(x=522, y=935)
    # 2022-2-28 已经不需要每天都点否 固隐藏
    # moveclick.move_and_click((522, 935)) 
    # 2022-3-26 又一次增加是否外出
    pyautogui.vscroll(-10)
    time.sleep(0.5)
    moveclick.move_and_click(position=(546, 598))
    time.sleep(0.1)
    pyautogui.vscroll(-80)
    health_infor_filling(visit, health_code, place)
    # fill_vaccine_date(vaccine_date)
    # time.sleep(1)
    return True

def timeWait():
    # 避免重复改参数
    return time.sleep(0.1)

def health_infor_filling(visit, health_code, place):
    '''
    visit, health_code, place 都是所在栏坐标位置
    visit: 是否接触过半个月内有疫情重点地区旅居史的人员
    health_code: 健康码是否为绿码
    place: 半个月内是否到过国内疫情重点地区
    '''
    # 是否接触过半个月内有疫情重点地区旅居史的人员
    # timeWait()
    check_visit = moveclick.move_and_click(visit)
    # timeWait()
    # 健康码是否为绿码
    check_health_code = moveclick.move_and_click(health_code)
    # timeWait()
    #半个月内是否到过国内疫情重点地区
    check_place = moveclick.move_and_click(place)
    return True

def health_code_green(x, y):
    health_code_green = (x, y)
    moveclick.move_and_click(health_code_green)
    print("5. 已经确认为绿色健康码")
    time.sleep(1)
    return True

def check_nucleic_acid_and_vincce(x, y):
    check_nucleic_acid = (x, y)
    moveclick.move_and_click(check_nucleic_acid)
    time.sleep(1)
    # print("6. 核酸已经测过！")
    print("6. 已经接种过疫苗！")
    return True

def sum_list(lst):
    # 列表生成式子 判断列表中元素是否为数字
    list1 = [i for i in lst if i.isdigit() is True]
    # 转换列表中数字的类型：字符串型 到 数字型
    list2 = list(map(int, list1))
    # 对列表中元素求和，从低位到高位
    return sum([list2[i]*10**(len(list2)-i-1) for i in range(len(list2))])

def check_NA_time(x, y, lst):
    click_box_ordinate = (x, y)
    moveclick.move_and_click(click_box_ordinate)
    print("==========输入测核酸日期=======")
    pyautogui.typewrite(lst, '0.25')
    pyautogui.position()
    print("7. 已经输入测核算日期")
    time.sleep(1)
    return True

def start_permist_pane(x, y):
    start_permist_pane = (x, y)
    moveclick.move_and_click(start_permist_pane)
    print("5. 已经承若")
    time.sleep(0.3)
    return True

def start_submit_position(x, y):
    start_submit_position = (x, y)
    moveclick.move_and_click(start_submit_position)
    time.sleep(0.1)
    return True

def close_small_win(x, y):
    moveclick.move_and_click((x, y))
    print("关闭小窗口")
    time.sleep(0.5)
    return True

def close_big_win(x, y):
    moveclick.move_and_click((x, y))
    print("关闭大窗口")
    return True

# 获取当前时间
def get_curr_date():
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    print("今天是%s年%s月%s日，开始进行健康报告打卡！！！"%(year, month, day))
    return int(time.strftime("%Y%m%d"))


def click_and_paste(startOrdinate, endOrdinate):
    """
    start: the corrdinate of begining copy
    end_x, end_y: the corrdinate of ending copy
    """
    moveclick.move_and_click(startOrdinate)
    # endOrdinate = (end_x, end_y)
    # 按下鼠标左键用1.0秒拖拽到(x,y) 选择文字
    pyautogui.dragTo(x=endOrdinate[0], y=endOrdinate[1], duration=0.1, button='left')
    pyautogui.hotkey('command', 'c', interval=0.05)
    box_context = pyperclip.paste()
    return box_context

# 检测是否进入“学生健康状况申报”页面
def student_health_situation_report(startOrdinate, endOrdinate, situationReprot):
    '''
    start: 开始复制的坐标位置 (end_x, end_y) 结束复制的位置
    situationReprot 复制的内容
    '''
    try:
        for i in range(3):
            box_context = click_and_paste(startOrdinate, endOrdinate)
            if box_context == situationReprot:
                print("===成功打开申报页面===")
                break
            else:
                print("网速太慢，请耐心等待第%d次"%(i+1))
                time.sleep(5)
        else:
            print("网络未连接，请连接网络后再打卡！")
            close_windows()
            exit(0)
    except TypeError:
            print("运行中止: 关闭窗口")
            close_windows()
            exit(0)
    return 0

def close_windows():
    # 8. 关闭小窗口
    close_small_win(244, 196)
    # 9. 关闭大窗口
    close_big_win(183, 110)
    return 0