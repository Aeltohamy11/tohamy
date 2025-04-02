import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def facebook_login(email, password):
    driver = webdriver.Chrome()
    driver.get("https://facebook.com")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    return driver

if __name__ == "__main__":
    while True:
        try:
            # هنا تكتب منطق النشر الخاص بك
            print("جاري التشغيل...")
            time.sleep(60*30)  # انتظار 30 دقيقة
        except Exception as e:
            print(f"خطأ: {e}")
            time.sleep(60*5)  # انتظار 5 دقائق بعد الخطأ
