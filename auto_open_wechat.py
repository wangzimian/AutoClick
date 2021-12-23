import moveclick
from openwechatwork import *

import time

def contain_position():
    ''' 
    visit: 是否接触过半个月内有疫情重点地区旅居史的人员
    health_code: 健康码是否为绿码
    place: 半个月内是否到过国内疫情重点地区
    '''
    return start_report_position(visit=(529, 400), health_code=(526, 500), place=(526, 597))
    # return True

def detect_box():
    # 获取检测方框的内容
    box_context = click_and_paste(startOrdinate=(524, 563), endOrdinate=(666, 623))
    # 检测次数
    i = 0
    # 检测方框可能出现的情况
    ls = ["Sorry, please make sure all required fields are filled out correctly!", "是否接触过半个月内有疫情重点地区旅居史的人员:Please select an option", "是否为绿码:Please select an option", "Please select an option"]
    # 开始检测，若是"打卡成功"，则跳出循环，若不是则循环进入第二次，若三次循环皆错，则显示错误
    while i <= 2:
        if box_context in ls:
            print("点击失败，请尝试第%d次！请再次提交"%(i+1))
            # 点击确认ok
            moveclick.move_and_click((829, 635))
            # 点击三连
            health_infor_filling(visit=(629, 400), health_code=(526, 500), place=(526, 597))
            # 点击提交
            start_submit_position(328, 232)
            # 跳出本次循环 并在此进行判断
            i += 1
        elif box_context == "打卡成功":
            print("7. 打卡成功!")
            # 跳出整个循环
            break
        else:
            print("Error2: 判断打卡中止，测试鼠标已经开始！")
            return moveclick.detect_mouse_ordinate()
    else:
        print("Error3: 已经三次点击未成功，请切换手动点击！")
        exit(0)
    return True

def clockin(times):
    ''' 打开企业微信，打开服务界面，打开信息系统，打开疫情风险提醒 '''
    print("=======今天打开第%d次！======"%(times + 1))
    # 0. 打开企业微信
    open_wechat_work(1286, 10)
    print("0. 软件已经打开")
    # 1. 打开服务大厅界面
    start_service_position(200, 387)
    print("1. 打开服务大厅")
    # 1.1 打开健康信息系统
    health_system(871, 608)
    print("2. 打开健康信息系统并准备阅览全文...")
    # 2. 打开学生健康申报网页，下滑到底，点击开始上报
    start_student_lowdown(begin_submit=(718, 878))
    print("3. 学生健康状况申报：已经阅览全国疫情中高风险地区名单")
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
        # v3.0 版本测试 2021-08-02 v4.0 南京疫情开始 2021-0809
        # v5.0 版本 2021-12-23 西安疫情
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
        clockin(times=i)
        # 3. 开始上报并下滑到底
        # v2.0 测试新版的开始上报
        contain_position()
        # 8. 承诺方框
        start_permist_pane(400, 785)
        # 9. 提交
        start_submit_position(328, 232)
        print("6. 点击提交按钮")
        # 10. 查看是否提交成功
        detect_box()
        time.sleep(1)
        # 关闭窗口
        close_windows(244, 196, 184, 111)
        i += 1
    end_time =time.time()
    print("运行时间：%d s"%(end_time - start_time))
