from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
import re

#chrome选项
options = webdriver.ChromeOptions()
#使用无头chrome
options.set_headless()
#配置并获得WebDriver对象
path = 'D:/Soft/VSCode32_Python_Portable/Python378/Scripts/chromedriver.exe'
driver = webdriver.Chrome(path, chrome_options=options)
#发起get请求
driver.get('http://www.baidu.com/')

input_element = driver.find_element_by_name('wd')
input_element.send_keys('python')
input_element.submit()

try:
    #最多等待10秒直到浏览器标题栏中出现我希望的字样（比如查询关键字出现在浏览器的title中）
    WebDriverWait(driver, 10).until(
        expected_conditions.title_contains('python'))
    print(driver.title)
    bsobj = BeautifulSoup(driver.page_source)
 
    num_text_element = bsobj.find('span', {'class': 'nums_text'})
    print(num_text_element.text)
    nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
    print(''.join(nums))
 
    elements = bsobj.findAll('div', {'class': re.compile('c-container')})
    for element in elements:
        if element.h3 is not None and element.h3.a is not None:
            print('标题：', element.h3.a.text)
            print('链接：', element.h3.a['href'])
            print('===============================================================')

finally:
    #关闭浏览器
    driver.close()