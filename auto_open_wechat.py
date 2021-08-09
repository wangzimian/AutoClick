from openwechatwork import *
import time

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
        # 1. 打开服务大厅界面
        start_service_position(200, 387)
        # 1.1 打开健康信息系统
        health_system(320, 361)
        # 2. 打开学生健康申报并下滑到底
        start_student_lowdown(840, 610)
        # v3.0 版本测试 2021-08-02 v4.0 南京疫情开始 2021-0809
        # 3. 开始上报并下滑到底
        # v2.0 测试新版的开始上报
        start_report_position(696, 710)
        # 5. 确认是否为绿码
        # health_code_green(502, 398)
        health_infor_filling(visit=(501,303), health_code=(497, 402), place=(500, 499))
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
        start_permist_pane(375, 619)
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
