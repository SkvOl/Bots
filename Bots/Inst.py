from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from faker import Faker
import requests
import easyocr
import secrets
import random
import string
import time
import os

 
current_login = ""
class InstagramBot():
    def __init__(self, username, password, PROXY, Delay):
        try:
            useragent = UserAgent()

            #webdriver.DesiredCapabilities.CHROME['proxy']={"httpProxy":PROXY,"ftpProxy":PROXY, "sslProxy":PROXY,"proxyType":"MANUAL",}
       
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-agent={useragent.random}")
            options.add_argument("--disable-blink-features=AutomationControlled")
            #options.add_argument("--headless")
            if PROXY != "":
                options.add_argument(f"--proxy-server = {PROXY}")
        
            self.Delay = Delay
            self.username = username
            self.password = password

            binary_driver_file = 'YD.exe' # path to YandexDriver
            self.browser = webdriver.Chrome(binary_driver_file, options = options)
            
            if self.Delay == "small":
                time.sleep(1)
            elif self.Delay == "normal":
                time.sleep(random.randint(4,6))
            elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

        except IOError as io:
            print(io) 
        
    def close_browser(self):
        if self.Delay == "small":
             time.sleep(0)
        elif self.Delay == "normal":
             time.sleep(random.randint(1,3))
        elif self.Delay == "huge":
             time.sleep(random.randint(6,8))
       
        self.browser.close()
        self.browser.quit()

    def login(self):
        try:
            browser = self.browser
            browser.get('https://www.instagram.com/')

            if self.Delay == "small":
                time.sleep(1)
            elif self.Delay == "normal":
                time.sleep(random.randint(4,6))
            elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

            username_input = browser.find_element(By.NAME,'username')
            username_input.clear()
            username_input.send_keys(self.username)
      
            if self.Delay == "small":
                time.sleep(0)
            elif self.Delay == "normal":
                time.sleep(random.randint(2,4))
            elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

            password_input = browser.find_element(By.NAME,'password')
            password_input.clear()
            password_input.send_keys(self.password)

            password_input.send_keys(Keys.ENTER)

            if self.Delay == "small":
                time.sleep(0)
            elif self.Delay == "normal":
                time.sleep(random.randint(2,4))
            elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

        except Exception as ex:
            print(ex)
        
    def xpath_exists(self,url):
        browser = self.browser
        try:
            valid = browser.find_element_by_xpath(url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def post_like(self,userpost):
         browser = self.browser
         browser.get(userpost)

         if self.Delay == "small":
            time.sleep(1)
         elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
         elif self.Delay == "huge":
            time.sleep(random.randint(6,8))
        
         if self.xpath_exists(userpost):
             self.close_browser()
         else:
             button_like = browser.find_element(By.CLASS_NAME,"fr66n").click()
             if self.Delay == "small":
                time.sleep(1)
             elif self.Delay == "normal":
                time.sleep(random.randint(2,4))
             elif self.Delay == "huge":
                time.sleep(random.randint(6,8))
             
    def user_follow(self,user_link):
         browser = self.browser
         browser.get(user_link)

         if self.Delay == "small":
            time.sleep(1)
         elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
         elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

         botton__foow = browser.find_element(By.XPATH,"//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']").click()
         
         if self.Delay == "small":
                time.sleep(0)
         elif self.Delay == "normal":
                time.sleep(random.randint(2,4))
         elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

    def download_content(self,userpost):
        browser = self.browser
        browser.get(userpost)

        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        img_path = "//img[@class='FFVAD'][@style='object-fit: cover;']"
        video_path = "//video[@class='tWeCl'][@type='video/mp4']"
        file_name = userpost[-12:-1]

        if os.path.exists(f"content"):
            print("Папка существует")
        else:
            os.mkdir("content")


        if self.xpath_exists(img_path):
             img_src_url =  browser.find_element(By.XPATH,img_path).get_attribute("src")
             get_img = requests.get(img_src_url)
             with open(f"content\\{file_name}.jpg","wb") as img_file:
                  img_file.write(get_img.content)
                        
             if self.Delay == "small":
                time.sleep(2)
             elif self.Delay == "normal":
                time.sleep(random.randint(4,6))
             elif self.Delay == "huge":
                time.sleep(random.randint(6,8))
         
        elif self.xpath_exists(video_path):
            video_src_url =  browser.find_element(By.XPATH,video_path).get_attribute("src")
            get_video = requests.get(video_src_url,stream = True)
            with open(f"content\\{file_name}.mp4","wb") as video_file:
               for chunk in get_video.iter_content(chunk_size = 1024 * 1024):
                   if chunk:
                        video_file.write(chunk)

            if self.Delay == "small":
                time.sleep(2)
            elif self.Delay == "normal":
                time.sleep(random.randint(4,6))
            elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

        else: print("\Ошибка скачивания файла\n")
        
class Create_Bot():
    def __init__(self, PROXY, Delay):
        try:
            useragent = UserAgent()
        
            #webdriver.DesiredCapabilities.CHROME['proxy']={"httpProxy":PROXY,"ftpProxy":PROXY, "sslProxy":PROXY,"proxyType":"MANUAL",}
        
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-agent={useragent.random}")
            options.add_argument("--disable-blink-features=AutomationControlled")
            #options.add_argument("--headless")
            if PROXY != "":
                options.add_argument(f"--proxy-server = {PROXY}")

            self.Delay = Delay
            binary_driver_file = 'YD.exe' # path to YandexDriver
            self.browser = webdriver.Chrome(binary_driver_file, options = options)

            if self.Delay == "small":
                time.sleep(0)
            elif self.Delay == "normal":
                time.sleep(random.randint(2,4))
            elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

        except IOError as io:
            print(io) 

    def download_capcha(self):
        browser = self.browser
        img_path = "//img[@class='captcha__image'][@alt='captcha image']"

        if os.path.exists("captcha"):
            print("Папка существует")
        else:
            os.mkdir("captcha")

        
        img_src_url =  browser.find_element(By.XPATH,img_path).get_attribute("src")
        get_img = requests.get(img_src_url)
        with open(f"captcha\\1.png","wb") as img_file:
             img_file.write(get_img.content)
                        
        if self.Delay == "small":
            time.sleep(2)
        elif self.Delay == "normal":
            time.sleep(random.randint(4,6))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

    def decoding_the_captcha(self):
        try:
             reader = easyocr.Reader(["ru"])
             resoult = reader.readtext("captcha\\1.png",detail=0)

             if self.Delay == "small":
                time.sleep(1)
             elif self.Delay == "normal":
                time.sleep(random.randint(2,4))
             elif self.Delay == "huge":
                time.sleep(random.randint(6,8))

             s = ""
             for i in range(len(resoult)):
                 if i!=len(resoult)-1:
                     s = s  + resoult[i] + " "
                 else:
                     s = s  + resoult[i]
             s = s.upper()
        except Exception as ex:
                print(ex)

        return s

    def Create_mail(self,length, p_type):
        browser = self.browser
        fake = Faker()
        botfname = fake.first_name()
        botlname = fake.last_name()
        botconfirmmus = ['The Beatles','Elvis Presley','Michael Jackson','Elton John','Madonna','Led Zeppelin','Rihanna','Pink Floyd','Eminem','Taylor Swift','Mariah Carey','Queen','Eagles','Whitney Houston','Celine Dion','AC/DC','The Rolling Stones','Drake','Garth Brooks','Kanye West']

        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(length))
    

        botlogin = rand_string
        botpassword = rand_string[::-1]
        

        create_path = 'https://passport.yandex.ru/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1'

        browser.get(create_path)

        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))
        
        bot_firstname_input = browser.find_element_by_xpath("//input[@type='text'][@name='firstname'][@value]").send_keys(botfname)
        
        bot_lastname_input = browser.find_element_by_xpath("//input[@type='text'][@name='lastname'][@value]").send_keys(botlname)
        
        bot_login_input = browser.find_element_by_xpath("//input[@type='text'][@name='login'][@value]").send_keys(botlogin)
       
        bot_password_input = browser.find_element_by_xpath("//input[@type='password'][@name='password'][@value]").send_keys(botpassword)
        
        bot_password_confirm_input = browser.find_element_by_xpath("//input[@type='password'][@name='password_confirm'][@value]").send_keys(botpassword)
        
        bot_confirm_but = browser.find_element_by_xpath("//div[@class='toggle-link link_has-no-phone']").find_element_by_xpath("//span[@data-t='link:default'][@tabindex='0'][@class='Link Link_pseudo Link_view_default']").click()
        
        bot_confirm_mus = browser.find_element_by_xpath("//input[@data-t='field:input-hint_answer'][@name='hint_answer'][@type='text'][@value]").send_keys(botconfirmmus[random.randint(0,19)])
        
        _i = 0
        while browser.current_url == create_path:
              _i = _i + 1
              if _i > 1:
                  cartcha_clear = browser.find_element(By.XPATH,"//input[@data-t='field:input-captcha'][@id='captcha'][@name='captcha'][@type='text'][@value]")
                  cartcha_clear.send_keys(Keys.CONTROL+"a")
                  cartcha_clear.send_keys(Keys.BACKSPACE)
                  print("clear")
                  
                  if self.Delay == "small":
                    time.sleep(0)
                  elif self.Delay == "normal":
                    time.sleep(random.randint(2,4))
                  elif self.Delay == "huge":
                    time.sleep(random.randint(6,8))

              self.download_capcha()

              dtc = self.decoding_the_captcha()
              cartcha_path = browser.find_element_by_xpath("//input[@data-t='field:input-captcha'][@id='captcha'][@name='captcha'][@type='text'][@value]").send_keys(dtc)
              button_register = browser.find_element_by_xpath("//button[@data-t='button:action'][@type='submit'][@class='Button2 Button2_size_l Button2_view_action Button2_width_max Button2_type_submit']").click()
              
              if self.Delay == "small":
                  time.sleep(0)
              elif self.Delay == "normal":
                  time.sleep(random.randint(2,4))
              elif self.Delay == "huge":
                  time.sleep(random.randint(6,8))
         
        if p_type == "Inst":
            self.Create_inst(botlogin,botfname + " " + botlname,botpassword)

    def Create_inst(self,botlogin,botname,botpassword):
        browser = self.browser

        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        browser.get("https://mail.yandex.ru/lite/inbox")

        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        browser.execute_script('''window.open("https://www.instagram.com/accounts/emailsignup/");''')       

        if self.Delay == "small":
            time.sleep(0)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        browser.switch_to.window(browser.window_handles[1])

        if self.Delay == "small":
            time.sleep(0)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        current_login = botlogin + "@yandex.ru"

        inst_reg_mail = browser.find_element_by_xpath("//input [@aria-label='Моб. телефон или эл. адрес'][@name='emailOrPhone'][@value]").send_keys(current_login)

        inst_reg_name = browser.find_element_by_xpath("//input [@aria-label='Имя и фамилия'][@name='fullName'][@value]").send_keys(botname)
        
        inst_reg_user_name = browser.find_element_by_xpath("//input [@aria-label='Имя пользователя'][@name='username'][@value]").send_keys(botlogin)

        inst_reg_pussword = browser.find_element_by_xpath("//input [@aria-label='Пароль'][@name='password'][@value]").send_keys(botpassword)
        
        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        save_reg_button = browser.find_element_by_xpath("//button [@class='sqdOP  L3NKy   y3zKF     '][@type='submit']")
        webdriver.ActionChains(browser).move_to_element(save_reg_button).click(save_reg_button).perform()
        
        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(4,6))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        sel_m = Select(browser.find_element_by_xpath("//select [@title='Месяц:']"))

        sel_m.select_by_value(str(random.randint(1,12)))

        sel_d = Select(browser.find_element_by_xpath("//select [@title='День:']"))

        sel_d.select_by_visible_text(str(random.randint(1,28)))

        sel_e = Select(browser.find_element_by_xpath("//select [@title='Год:']"))

        sel_e.select_by_visible_text(str(random.randint(1985,2008)))

        next_reg_button = browser.find_element_by_xpath("//button [@class='sqdOP  L3NKy _4pI4F  y3zKF     '][@type='button']").click()

        if self.Delay == "small":
            time.sleep(0)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        re_next_reg_button1 = browser.find_element_by_xpath("//button [@class='sqdOP yWX7d    y3zKF     '][@type='button']").click()
        #'sqdOP yWX7d    y3zKF     '
        #'sqdOP yWX7d    y3zKF     '
        #time.sleep(30)
        #re_next_reg_button2 = browser.find_element_by_xpath("//button [@class='sqdOP yWX7d    y3zKF     '][@type='button']").click()
        
        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

        browser.switch_to.window(browser.window_handles[0])

        if self.Delay == "small":
            time.sleep(6)
        elif self.Delay == "normal":
            time.sleep(random.randint(8,16))
        elif self.Delay == "huge":
            time.sleep(random.randint(20,30))

        browser.get("https://mail.yandex.ru/lite/inbox")

        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))
        
        inst_kod =  browser.find_element_by_xpath("//a[@class='b-messages__message__link'][@aria-label]").text

        browser.switch_to.window(browser.window_handles[1])

        kod_to_inst = browser.find_element_by_xpath("//input [@aria-label='Код подтверждения'][@name='email_confirmation_code'][@value]").send_keys(inst_kod[0]+inst_kod[1]+inst_kod[2]+inst_kod[3]+inst_kod[4]+inst_kod[5])

        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))
        
        Finish_button =  browser.find_element_by_xpath("//button [@class='sqdOP  L3NKy _4pI4F  y3zKF     ']").click()

        if self.Delay == "small":
            time.sleep(1)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))

    def close_browser(self):
        if self.Delay == "small":
            time.sleep(0)
        elif self.Delay == "normal":
            time.sleep(random.randint(2,4))
        elif self.Delay == "huge":
            time.sleep(random.randint(6,8))
       
        self.browser.close()
        self.browser.quit()