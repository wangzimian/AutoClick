import pyautogui
import time


# 测试鼠标坐标
def detect_mouse_ordinate():
    while True:
        coordinate = pyautogui.position()
        print("The current coordinate is: ", coordinate)
        time.sleep(1)
    return True

# 移动鼠标并点击
def move_and_click(position):
    pyautogui.moveTo(position)
    # time.sleep(1)
    pyautogui.click(clicks = 1)
    time.sleep(1)
    return True
# 
# detect_mouse_ordinate()