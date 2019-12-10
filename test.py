# import subprocess
# import psutil
#
# def judgeprocess(processname):
#     pl = psutil.pids()
#     for pid in pl:
#         if psutil.Process(pid).name() == processname:
#             print()
#             return True
#     else:
#         return False
#
# process = subprocess.Popen("frpc.exe")
#
# print(process)
#
# if judgeprocess('frpc.exe') == True:
#     print("正在运行")
#     process.terminate()
# else:
#     print("没有运行")


# import time
# from splinter import Browser
#
#
# def login(url):
#     browser = Browser('chrome', executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#     browser.visit(url)
#     # wait web element loading
#     # fill in account and password
#     browser.find_by_id('userName').fill('admin')
#     browser.find_by_id('password').fill('888888')
#     browser.find_by_id('verifyCode').fill('8888')
#     # click the button of login
#     browser.find_by_id('login').click()
#     time.sleep(5)
#     # close the window of brower
#     browser.quit()
#
#
# if __name__ == '__main__':
#     addr = 'http://192.168.1.74/loginSystem'
#     login(addr)


# 手动滚动
# import time
# from selenium import webdriver
# from bs4 import BeautifulSoup
# # driver = webdriver.Chrome()
# driver = webdriver.Edge()
#
# driver.get('http://www.baidu.com/')
#
#
#
# input_element = driver.find_element_by_id("kw").send_keys("青岛 关键字")
# driver.find_element_by_id("su").click()
# # 这里要延时一下，不然找不到返回页面
# time.sleep(3)
#
#
# bsobj = BeautifulSoup(driver.page_source, features="html.parser")
# num_text_element = bsobj.find('span', {'class': 'nums_text'})
# print(num_text_element)
# nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
# str = (''.join(nums)).replace(',','')
# print(int(str))
#
#
# driver.set_window_size(1200, 900)
# driver.execute_script("""
#     (function () {
#         var y = 0;
#         var step = 100;
#         window.scroll(0, 0);
#         function f() {
#             if (y < document.body.scrollHeight) {
#                 y += step;
#                 window.scroll(0, y);
#                 setTimeout(f, 100);
#             } else {
#                 window.scroll(0, 0);
#                 document.title += "scroll-done";
#             }
#         }
#         setTimeout(f, 1000);
#     })();
# """)
# time.sleep(1)
# driver.save_screenshot('screenshot.png')


## 按照元素截图
# from selenium import webdriver
# from PIL import Image
# import time
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com/')
#
# driver.find_element_by_id("kw").send_keys("青岛 关键字")
# driver.find_element_by_id("su").click()
# time.sleep(1)
#
# width = driver.execute_script('return document.body.scrollWidth')
# height = driver.execute_script('return document.body.scrollHeight')
# driver.set_window_size(width, height)
#
# driver.save_screenshot("test.png")
# driver.close()


#
# driver.save_screenshot('button.png')
# element = driver.find_element_by_id("content_left")
#
# print(element.location)                # 打印元素坐标
# print(element.size)                    # 打印元素大小
#
# left = element.location['x']
# top = element.location['y']
# right = element.location['x'] + element.size['width']
# bottom = element.location['y'] + element.size['height']
#
# im = Image.open('button.png')
# im = im.crop((left, top, right, bottom))
# im.save('button.png')




# # 通过WebDriver操作进行查找
# # 无头浏览器，支持无浏览器操作
#
# from selenium import webdriver
# import time
#
#
# def main():
#     # 创建浏览器实例
#     driver = webdriver.Chrome()
#     url = 'http://www.baidu.com'
#     driver.get(url)
#
#     # 打印出wrapper中的文字内容
#     text = driver.find_element_by_id('wrapper').text
#     print(text)
#
#     # 打印出HTML页面的标题
#     print(driver.title)
#
#     # 得到页面的快照，得到百度首页的的截图
#     driver.save_screenshot('77_2.png')
#
#     # id='kw'是百度的输入框
#     driver.find_element_by_id('kw').send_keys(u'大熊猫')
#
#     # id='su'是百度搜索的按钮，百度一下，click模拟点击
#     driver.find_element_by_id('su').click()
#
#     # 搜索需要时间，等待一下再截图
#     time.sleep(5)
#     driver.save_screenshot('大熊猫搜索结果.png')
#
#     # 关闭浏览器
#     driver.close()
#
#
# if __name__ == '__main__':
#     main()


from selenium import webdriver
from PIL import Image
import time

driver = webdriver.Edge()
time.sleep(1)
# driver.maximize_window()
driver.get('http://www.baidu.com/')
driver.find_element_by_id("kw").send_keys("青岛 关键字")
driver.find_element_by_id("su").click()

# input = driver.find_element_by_link_text("下一页")
# print(input)

#
#
#
# script = '''
#     var viewHeight = document.documentElement.clientHeight;
#     var bodyHeight = document.body.scrollHeight;
#     return {'viewHeight': viewHeight, 'bodyHeight': bodyHeight};
# '''
# height_values = driver.execute_script(script)
# default_name = 'capture_0.png'
# driver.save_screenshot(default_name)
# image_list = [(default_name, 0)]
# image_width = 0
#
# if height_values['viewHeight'] < height_values['bodyHeight']:  # 有滚动条
#     is_over = False
#     scrollY = 0
#
#     while not is_over:
#         script = '''
#             scrollTo(arguments[0], arguments[1]);
#         '''
#         x = 0
#         y = min(height_values['bodyHeight'] - scrollY, height_values['viewHeight'])
#         scrollY += y
#         fn = 'capture_%s.png' % scrollY
#         driver.execute_script(script, x, scrollY)
#         time.sleep(2)
#         driver.save_screenshot(fn)
#
#         if scrollY == height_values['bodyHeight']:
#             is_over = True
#             cropY = height_values['viewHeight'] - y
#
#             im = Image.open(fn)
#             image_width = im.width
#             im = im.crop((0, cropY, image_width, height_values['viewHeight']))
#             im.save(fn)
#
#         image_list.append((fn, scrollY))
#
# if image_list:
#     merge_img = Image.new('RGB', (image_width, height_values['bodyHeight']), 0xffffff)
#
#     j = 0
#     for f, scrollY in image_list:
#         print(f)
#         img = Image.open(f)
#         merge_img.paste(img, (0, j))
#         j += height_values['viewHeight']
#     merge_img.save('merge.png')
#
# driver.quit()



### 上一个版本
# from PIL import Image
# import numpy as np
# driver.get_screenshot_as_file("screenshot.png")

# ## 滚动截图
# window_height = driver.get_window_size()['height']
# print(window_height)
# # page_height = driver.execute_script('return document.documentElement.scrollHeight')
# # print(page_height)
# # todo test
# element = driver.find_element_by_id("content_left")
# page_height = element.size['height']
# print(page_height)
# # todo test
#
# # todo 处理第一张图
# element1 = driver.find_element_by_class_name("s_tab")
# element2 = driver.find_element_by_class_name("nums")
# element3 = driver.find_element_by_class_name("s_form")
# im = Image.open('temp.png')
# # 搜索框
# height1 = element1.size['height']
# # 数目框
# height2 = element2.size['height']
# # 下拉搜索框
# height3 = element2.size['height']
# im = im.crop((element.location['x'],
#               element.location['y'],
#              element.location['x'] + element.size['width'],
#              element.location['y'] + window_height - element1.size['height'] - element2.size['height']))
# im.save('temp.png')
# # todo test
#
#
# if page_height > window_height:
#     n = page_height // window_height        # 需要滚动的次数
#     base_mat = np.atleast_2d(Image.open('temp.png'))  # 打开截图并转为二维矩阵
#
#     for i in range(n):
#         driver.execute_script(f'document.documentElement.scrollTop={window_height*(i+1)-height1-height2};')
#         # driver.execute_script(f'document.documentElement.scrollTop={window_height*(i+1)};')
#         time.sleep(1)
#         driver.save_screenshot(f'temp_{i}.png')  # 保存截图
#         #todo
#         element = driver.find_element_by_id("content_left")
#         im = Image.open(f'temp_{i}.png')
#         im = im.crop((element.location['x'],
#                       height3,
#                       element.location['x'] + element.size['width'],
#                       window_height * (i + 1)-height3))
#         im.save(f'temp_{i}.png')
#         #todo
#         mat = np.atleast_2d(Image.open(f'temp_{i}.png'))  # 打开截图并转为二维矩阵
#         base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
#     Image.fromarray(base_mat).save('screenshot.png')



