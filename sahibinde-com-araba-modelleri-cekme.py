import pymysql 
import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
import re
import math

def sahibindenAracData():
    notyet = True
    while notyet:
        try:
            connection = pymysql.connect(host = 'myhostaddress', user = 'username', charset='utf8', passwd = 'password', db = 'dbname',cursorclass=pymysql.cursors.DictCursor, autocommit=True)
            cursor = connection.cursor()
            notyet = False
            return connection, cursor
        except:
            time.sleep(3)
            pass


firefoxProfile = FirefoxProfile()
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
firefoxProfile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefoxProfile)
driver.get("https://www.sahibinden.com/kategori/otomobil")
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

say = 0
while(say < 73):
    markalar = driver.find_element_by_class_name("jspPane").find_elements_by_tag_name("a")[say].text
    print("Marka : " + markalar)
    driver.find_element_by_class_name("jspPane").find_elements_by_tag_name("a")[say].click()
    time.sleep(4)

    say2 = 0
    seri_sayisi = driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")
    time.sleep(3)
    while(say2 < len(seri_sayisi)):

        try:
            seri = driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")[say2].text
            print("Seri : " + markalar + "-" + seri)
            driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")[say2].click()
            time.sleep(3)
        except:
            time.sleep(3)
            seri = driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")[say2].text
            print("Seri : " + markalar + "-" + seri)
            driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")[say2].click()
            time.sleep(3)
        say3 = 0
        try: 
            model1_sayisi = driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")
            time.sleep(3)
            if len(model1_sayisi) > 0:

                while(say3 < len(model1_sayisi)):
                    model1 = driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")[say3].text
                    print("Model 1 :" + markalar + "-" + seri + "-" + model1)
                    driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")[say3].click()
                    time.sleep(3)

                    try:
                        say4 = 0
                        model2_sayisi = driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")
                        if len(model2_sayisi) > 0:
                            while(say4 < len(model2_sayisi)):
                                model2 = driver.find_elements_by_class_name("jspPane")[1].find_elements_by_tag_name("a")[say4].text
                                print("Model 2 :" + markalar + "-" + seri + "-" + model1 + "-" + model2)
                                say4 = say4 + 1
                                time.sleep(3)
                               
                                connection, cursor = sahibindenAracData()
                                cursor.execute("INSERT INTO araba_modelleri (marka,seri,model,model2,eklenme_tarihi) VALUES ('"+markalar+"','"+seri+"','"+model1 +"','"+model2+"', NOW())")
                                print("data kaydedildi...")
                               
                        else:
                            connection, cursor = sahibindenAracData()
                            cursor.execute("INSERT INTO araba_modelleri (marka,seri,model,eklenme_tarihi) VALUES ('"+markalar+"','"+seri+"','"+model1 +"', NOW())")
                            print("data kaydedildi...")

                    except:
                        pass

                    driver.execute_script("window.history.go(-1)")
                    say3 = say3 + 1
                    time.sleep(4)
                    
                driver.execute_script("window.history.go(-1)")
                say2 = say2 + 1
                time.sleep(4)
            else:
                connection, cursor = sahibindenAracData()
                cursor.execute("INSERT INTO araba_modelleri (marka,seri,eklenme_tarihi) VALUES ('"+markalar+"','"+seri+"', NOW())")
                print("data kaydedildi...")
        except:
            pass

    driver.execute_script("window.history.go(-1)") #bulunduğu sayfadan geri döner
    time.sleep(4)
    say = say+1
  
