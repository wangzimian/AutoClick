
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


sta = time.time()

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://yqtb.sysu.edu.cn/infoplus/form/XNYQSB/start') # log in link web
def check_id(idName):
    time.sleep(0.5)
    return driver.find_element(By.ID, idName).click()
# login account
driver.find_element(By.ID, "un").send_keys("888888") 
driver.find_element(By.ID, "pd").send_keys('888888')
driver.find_element(By.ID, "index_login_btn").click()

# 点击开始上报
check_id("preview_start_button")
print("Login finished.....")

# driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[12]/td[1]/div/div/span/span[1]/span/span[2]').click()

# time.sleep(0.3)

# driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys('广东省')

# time.sleep(0.5)

driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li').click()

# time.sleep(0.5)

#  ======== 输入广州市 ========

# driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[12]/td[2]/div/div/span/span[1]/span/span[2]').click()

# time.sleep(0.3)

# driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys('广州市')

# time.sleep(0.5)

# driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li').click()

# time.sleep(0.5)

# =========== 番禺区 ==========

# driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[12]/td[3]/div/div/span/span[1]/span/span[2]').click()

# time.sleep(0.3)

# driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys('番禺区')

# time.sleep(0.5)

# driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li/span/u').click()

# # time.sleep(0.5)

# driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[13]/td/div/input').send_keys('外环东路132号')

# print("=====已填写住处======")

# 当日是否外出
check_id("V1_CTRL238")
print("无外出")

# 是否接触过经医疗机构诊断的疑似或确诊病例
check_id("V1_CTRL46")
print("无疑似")

# 是否接触过半个月内有疫情重点地区旅居史的人员
check_id("V1_CTRL262")
print("无接触")

# 健康码是否为绿码
check_id("V1_CTRL37")
print("绿吗？绿码")

# 承若
check_id("V1_CTRL82")
print("承若了")

# 提交 每一次提交按钮的id都不一样 因此需要先找到id然后点击
driver.find_element(By.CLASS_NAME,"command_button_content").click()

time.sleep(1)

text = driver.find_element(By.CLASS_NAME, "form_do_action_error").text
count = 0
while text is None:
    time.sleep(0.5)
    count += 1
    print(count)


end = time.time()
print("The check-in result is %s and customs %d s!"%(text, end - sta))
driver.quit()