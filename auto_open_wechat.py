import moveclick
from openwechatwork import *

import time

def contain_position():
    start_report_position(visit=(523,309), health_code=(520, 409), place=(522, 508))
    return True

def detect_box():
    for i in range(2):
        box_context = ""
        box_context = click_and_paste((519, 514), 682, 559)
        if box_context == "Sorry, please make sure all required fields are filled out correctly!" or box_context == "Please select an option":
            print("点击失败，再来一次！")
            moveclick.move_and_click((829, 570))
            health_infor_filling(visit=(523,309), health_code=(520, 409), place=(522, 508))
            start_submit_position(328, 232)
            # 跳出本次循环 并在此进行判断
            i += 1
            continue
        elif box_context == "是否接触过半个月内有疫情重点地区旅居史的人员:Please select an option":
            print("点击失败，再来一次！")
            moveclick.move_and_click((829, 570))
            health_infor_filling(visit=(525,319), health_code=(521, 421), place=(522, 517))
            start_submit_position(328, 232)
            i += 1
            # 跳出本次循环 并在此进行判断
            continue
        elif box_context == "打卡成功":
            print("7. 打卡成功!")
            # 跳出整个循环
            break
        else:
            print("Error2: 判断打卡中止，测试鼠标已经开始！！！")
            moveclick.detect_mouse_ordinate()
    else:
        print("Error3: 未知错误，测试鼠标已经开始！！！")
        moveclick.detect_mouse_ordinate()
    return True

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
        pen_wechat_work(1282, 10)
        print("0. 软件已经打开")
        # 1. 打开服务大厅界面
        start_service_position(200, 387)
        print("1. 打开服务大厅")
        # 1.1 打开健康信息系统
        health_system(871, 608)
        print("2. 打开健康信息系统并准备阅览全文...")
        # 2. 打开学生健康申报网页，下滑到底，点击开始上报
        start_student_lowdown(student_health_report=(850, 610), begin_submit=(712, 705))
        print("3. 学生健康状况申报：已经阅览全国疫情中高风险地区名单")
        # v3.0 版本测试 2021-08-02 v4.0 南京疫情开始 2021-0809
        # 3. 开始上报并下滑到底
        # v2.0 测试新版的开始上报
        contain_position()
        # 5. 确认是否为绿码
        # health_code_green(502, 398)
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
        start_permist_pane(396, 682)
        # 9. 提交
        start_submit_position(328, 232)
        # 10. 查看是否提交成功
        detect_box()
        time.sleep(1)
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
        moveclick.detect_mouse_ordinate()
    # main()