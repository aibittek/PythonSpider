from selenium import webdriver
import time
import pymongo

# 链接数据库
client = pymongo.MongoClient(host='45.67.223.227', port=8081) #链接数据库
db = client['db'] #设置数据库名
toutiao = db['toutiao'] #设置集合名

#启动webdrive
base_url ='https://www.toutiao.com'
path = 'D:/Soft/VSCode32_Python_Portable/Python378/Scripts/chromedriver.exe'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
brower = webdriver.Chrome(path, options=options)
brower.get(base_url)
brower.implicitly_wait(10)
brower.maximize_window() # 最大化窗口
brower.implicitly_wait(10)
brower.find_element_by_link_text('热点').click()
brower.implicitly_wait(10)

title_list,url_list,sources_list,comments_list=[],[],[],[]
# 获取页面新闻标题，详情页面链接，来源，评论，并添加到列表中
def get_info():
    titles = brower.find_elements_by_xpath('//div[@class="title-box"]/a')
    for title in titles:
        title_list.append(title.text)
    urls = brower.find_elements_by_xpath('//div[@class="title-box"]/a')
    for url in urls:
        url = url.get_attribute('href')
        url_list.append(url)
    sources = brower.find_elements_by_xpath('//a[@class="lbtn source"]')
    for source in sources:
        sources_list.append(source.text)
    comments = brower.find_elements_by_xpath('//a[@class="lbtn comment"]')
    for comment in comments:
        comments_list.append(comment.text)

# 通过下拉进度条一直加载页面
def get_manyinfo():
    brower.execute_script("window.scrollTo(0,1000);")
    time.sleep(1)
    while len(title_list) < 100:
        for i in range(30):
            brower.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(3)
        get_info()
        brower.refresh()
    else:
        brower.close()

# 保存获取的信息保存到mongodb中
def save_info():
    infos = zip(title_list, url_list, sources_list, comments_list)
    for info in infos:
        data={
            '标题': info[0],
            'url': info[1],
            '来源': info[2],
            '评论': info[3]
        }
        result = db['toutiao'].insert_one(data)
        print(data)
    print('数据写入成功')

def main():
    get_manyinfo()
    save_info()

if __name__=="__main__":
    main()