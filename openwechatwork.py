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

def pen_wechat_work(x, y):
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
    return True

def start_student_lowdown(student_health_report, begin_submit):
    s = "学生健康"
    moveclick.move_and_click(student_health_report)
    student_health_situation_report((457, 279), 574, 288, s) # 检测页面是否正确打开
    # pyautogui.click(clicks = 1)
    pyautogui.vscroll(-200)
    moveclick.move_and_click(begin_submit)
    time.sleep(0.5)
    return True

def start_report_position(visit, health_code, place, vaccine_date):
    s = "状况申报"
    student_health_situation_report((718, 543), 841, 543, s) # 检测页面是否正确打开
    fill_origin(province_coordinate=(435, 789), city_coordinate=(590, 785))
    print("4. 已经打开学生健康状况申报下滑到底，准备填写申报信息...")
    pyautogui.vscroll(-200)
    health_infor_filling(visit, health_code, place)
    fill_vaccine_date(vaccine_date)
    time.sleep(1)
    return True

def health_infor_filling(visit, health_code, place):
    '''
    visit, health_code, place 都是所在栏坐标位置
    '''
    # 是否接触过半个月内有疫情重点地区旅居史的人员
    check_visit = moveclick.move_and_click(visit)
    time.sleep(0.5)
    # 健康码是否为绿码
    check_health_code = moveclick.move_and_click(health_code)
    time.sleep(0.5)
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
    time.sleep(1)
    return True

def start_submit_position(x, y):
    start_submit_position = (x, y)
    moveclick.move_and_click(start_submit_position)
    time.sleep(3)
    print("6. 点击提交按钮")
    return True

def detect_result(start, end_x, end_y):
    '''
    start = (544, 472)
    end_x, end_y = x=638, y=496
    '''
    count = 0
    try:
        while count < 3:
            box_context = click_and_paste(start, end_x, end_y)
            if box_context == "Sorry, please make sure all required fields are filled out correctly!":
                print("打开失败!，测试鼠标已经开始！！！")
                moveclick.detect_mouse_ordinate()
            elif box_context == "打卡成功":
                print("7. 打卡成功!")
                break
            else:
                time.sleep(1)
                count += 1
            if count == 2:
                print("Error3: 打卡失败，程序中止，测试鼠标已经开始！！！")
                moveclick.detect_mouse_ordinate()
    except TypeError:
        print("Error4: 程序中止，测试鼠标已经开始！！！")
        close_windows(244, 196, 183, 110)
        moveclick.detect_mouse_ordinate()
    time.sleep(1)
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


def click_and_paste(start, end_x, end_y):
    """
    start: the corrdinate of begining copy
    end_x, end_y: the corrdinate of ending copy
    """
    moveclick.move_and_click(start)
    # 按下鼠标左键用1.0秒拖拽到(x,y) 选择文字
    pyautogui.dragTo(x=end_x, y=end_y, duration=1.0, button='left')
    pyautogui.hotkey('command', 'c', interval=0.5)
    box_context = pyperclip.paste()
    return box_context

# 检测是否进入“学生健康状况申报”页面
def student_health_situation_report(start, end_x, end_y, s):
    '''
    start: 开始复制的坐标位置 (end_x, end_y) 结束复制的位置
    s 复制的内容
    '''
    try:
        for i in range(3):
            box_context = click_and_paste(start, end_x, end_y)
            if box_context == s:
                print("===成功打开申报页面===")
                break
            else:
                print("网速太慢，请耐心等待第%d次"%(i+1))
                time.sleep(3)
        else:
            print("网络未连接，请连接网络后再打卡！")
            close_windows(244, 196, 183, 110)
            exit(0)
    except TypeError:
            print("运行中止: 关闭窗口")
            close_windows(244, 196, 183, 110)
            exit(0)
            time.sleep(1)
    return 0

def close_windows(x_big, y_big, x_small, y_small):
    # 8. 关闭小窗口
    close_small_win(x_big, y_big)
    # 9. 关闭大窗口
    close_big_win(x_small, y_small)
    return 0