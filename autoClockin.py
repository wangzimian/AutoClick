import moveclick
from auto_open_wechat import main

if __name__ == "__main__":
    # detect_mouse_ordinate()
    try:
        main()
    except TypeError:
        print("Error1: 程序中止，测试鼠标已经开始！！！")
        moveclick.detect_mouse_ordinate()