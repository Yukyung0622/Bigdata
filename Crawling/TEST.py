from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import  datetime
import time


#가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

#데이터 수집 URL
browser.get('http://www.weather.go.kr/w/obs-climate/land/city-obs.do')

#파일 디렉터리 생성
dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

#파일 생성 및 데이터 파싱
fname = "{:Weather_%Y-%m-%d-%H-%M.csv}".format(datetime.now())
file = open(dir+'/'+fname, 'w', encoding='utf-8')


weather = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for wt in weather:
    # time.sleep(1)
    t1 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a').text
    t2 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
    t3 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
    t4 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
    t5 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
    t6 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
    t7 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text
    t8 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
    t9 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(9)').text
    t10 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(10)').text
    t11 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(11)').text
    t12 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(12)').text
    t13 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(13)').text
    t14 = wt.find_element(By.CSS_SELECTOR, 'td:nth-child(14)').text

    file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14))

file.close()
print('데이터 수집 완료..!')

