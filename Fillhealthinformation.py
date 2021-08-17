from moveclick import move_and_click

import pyautogui

def fill(coordincate, message):
    move_and_click(coordincate)
    pyautogui.typewrite(message, '0.25')
    pyautogui.press("enter")   
    return True

def fill_origin(province_coordinate, city_coordinate):
    fill(province_coordinate, message='hunan')
    fill(city_coordinate, message='yiyang')
    return True

def fill_vaccine_date(coordincate):
    date = ['2','0','2','1','-','0','5','-','1','6']
    fill(coordincate, date)
    return True
