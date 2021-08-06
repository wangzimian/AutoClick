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

# 测试鼠标坐标
def detect_mouse_ordinate():
    while True:
        coordinate = pyautogui.position()
        print("The current coordinate is: ", coordinate)
        time.sleep(1)
    return True

def move_and_click(position):
    pyautogui.moveTo(position)
    # time.sleep(1)
    pyautogui.click(clicks = 1)
    time.sleep(1)
    return True

def pen_wechat_work(x, y):
    open_wechat_work = (x, y)
    move_and_click(open_wechat_work)
    time.sleep(0.5)
    print("0. 软件已经打开")
    return True

def start_service_position(x, y):
    start_service_position = (x,y)
    move_and_click(start_service_position)
    time.sleep(0.5)
    print("1. 打开服务大厅")
    return True

def health_system(x, y):
    health_system = (x, y)
    move_and_click(health_system)
    print("2. 打开健康信息系统")
    return True

def start_student_lowdown(x, y):
    start_student = (x, y)
    move_and_click(start_student)
    time.sleep(6)
    student_health_situation_report((436, 288), 717, 287)
    pyautogui.click(clicks = 1)
    pyautogui.vscroll(-200)
    time.sleep(0.5)
    print("3. 已经下滑到底")
    time.sleep(0.5)
    return True

def start_report_position(x, y):
    start_report_position = (x, y)
    move_and_click(start_report_position)
    time.sleep(8)
    student_health_situation_report((563, 534), 830, 523)
    pyautogui.click(clicks = 1)
    pyautogui.vscroll(-200)
    time.sleep(1)
    print("4. 已经打开开始上报界面并下滑到底！")
    return True

def health_code_green(x, y):
    health_code_green = (x, y)
    move_and_click(health_code_green)
    print("5. 已经确认为绿色健康码")
    time.sleep(1)
    return True

def check_nucleic_acid_and_vincce(x, y):
    check_nucleic_acid = (x, y)
    move_and_click(check_nucleic_acid)
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
    move_and_click(click_box_ordinate)
    print("==========输入测核酸日期=======")
    pyautogui.typewrite(lst, '0.25')
    pyautogui.position()
    print("7. 已经输入测核算日期")
    time.sleep(1)
    return True

def start_permist_pane(x, y):
    start_permist_pane = (x, y)
    move_and_click(start_permist_pane)
    print("8. 已经承若")
    time.sleep(1)
    return True

def start_submit_position(x, y):
    start_submit_position = (x, y)
    move_and_click(start_submit_position)
    time.sleep(3)
    print("9. 已经成功提交")
    return True

def detect_result(start, end_x, end_y):
    '''
    start = (544, 472)
    end_x, end_y = x=638, y=496
    '''
    move_and_click(start)
    # 按下鼠标左键用1.0秒拖拽到(x,y) 选择文字
    pyautogui.dragTo(x=end_x, y=end_y, duration=1.0, button='left')
    pyautogui.hotkey('command', 'c', interval=0.5)
    box_context = pyperclip.paste()
    try:
        if box_context == "Sorry, please make sure all required fields are filled out correctly!":
            print("上报失败!，测试鼠标已经开始！！！")
            detect_mouse_ordinate()
        elif box_context == "打卡成功":
            print("10. 上报成功!")
        else:
            print("Error3: 程序中止，测试鼠标已经开始！！！")
            detect_mouse_ordinate()
    except TypeError:
        print("Error4: 程序中止，测试鼠标已经开始！！！")
        close_windows(244, 196, 183, 110)
        detect_mouse_ordinate()
    time.sleep(1)
    return True

def close_small_win(x, y):
    move_and_click((x, y))
    print("关闭小窗口")
    time.sleep(0.5)
    return True

def close_big_win(x, y):
    move_and_click((x, y))
    print("关闭大窗口")
    return True

# 获取当前时间
def get_curr_date():
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    print("今天是%s年%s月%s日，开始进行健康报告打卡！！！"%(year, month, day))
    return int(time.strftime("%Y%m%d"))

# 检测是否进入“学生健康状况申报”页面
def student_health_situation_report(start, end_x, end_y):
    move_and_click(start)
    # 按下鼠标左键用1.0秒拖拽到(x,y) 选择文字
    pyautogui.dragTo(x=end_x, y=end_y, duration=1.0, button='left')
    pyautogui.hotkey('command', 'c', interval=0.5)
    box_context = pyperclip.paste()
    try:
        if box_context == "学生健康状况申报":
            print("===成功打开申报页面===")
            return True
        else:
            print("网速太慢，请检查网络继续上报")
            close_windows(244, 196, 183, 110)
            exit(0)
    except TypeError:
        print("运行中止: 关闭窗口")
        close_windows(244, 196, 183, 110)
        exit(0)
    time.sleep(1)

def close_windows(x_big, y_big, x_small, y_small):
    # 8. 关闭小窗口
    close_small_win(x_big, y_big)
    # 9. 关闭大窗口
    close_big_win(x_small, y_small)
    return 0

def main():
    # start_time = time.process_time()
    start_time = time.time()
    i = 0
    date_list = ['2','0','2','1','-','0','6','-','2','4']
    # 获取当前年月日
    current_date = get_curr_date()
    date = sum_list(date_list)
    while i <= int(sys.argv[1]):
        print("=======今天打开第%d次！======"%(i+1))
        # 0. 打开企业微信
        # open_wechat_work = (1276, 10)
        pen_wechat_work(1282, 10)
        # 1. 打开服务大厅界面
        # pyautogui.position()
        start_service_position(200, 387)
        # 1.1 打开健康信息系统
        # health_system = (260, 294)
        health_system(320, 361)
        # 2. 打开学生健康申报并下滑到底
        start_student_lowdown(840, 610)
        # v3.0 版本测试 2021-08-02
        # 3. 开始上报并下滑到底
        # v2.0 测试新版的开始上报
        start_report_position(696, 710)
        # 5. 确认是否为绿码
        health_code_green(502, 398)
        # 6 是否一周内测核酸和接种过疫苗
        # check_nucleic_acid_and_vincce(500, 587)
        # if current_date <= 20210702:
        #     # 一周内测过了
        #     check_nucleic_acid(509, 583)
        #     # 7 输入测试日期
        #     check_NA_time(457, 620, date_list)
        #     # 8. 承若方框
        #     start_permist_pane(377, 657)
        # else:
            # 没有测过
            # check_nucleic_acid(565, 582)
        # 8. 承诺方框
        start_permist_pane(378, 618)
        # 9. 提交
        start_submit_position(328, 243)
        # 10. 查看是否提交成功
        detect_result((495, 474), 638, 496)
        time.sleep(2)
        # 关闭窗口
        close_windows(244, 196, 183, 110)
        i += 1
    end_time =time.time()
    print("运行时间：%d s"%(end_time - start_time))

if __name__ == "__main__":
    # detect_mouse_ordinate()
    try:
        main()
    except TypeError:
        print("Error1: 程序中止，测试鼠标已经开始！！！")
        detect_mouse_ordinate()
