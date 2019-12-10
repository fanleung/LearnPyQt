
from PyQt5.QtWidgets import (QApplication, QCheckBox,  QDialogButtonBox, QComboBox,
                             QGridLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget, QSpinBox)
from PyQt5.QtCore import Qt
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import imgkit
import threading


threads = []

# 查看chrome 的版本，下载对应的 chromeDriver 版本

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.url = ""
        self.customPageNum = 100
        self.realPageNum = 100
        self.currentTime = ""

        # 配置imgkit config
        self.imgkitConfig = imgkit.config(wkhtmltoimage=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe")
        self.imgKitOptions = {
            # http://user:password@myproxyserver:8080
            # '--proxy': 'http://113.119.82.69:9000',
            '--proxy': 'socks5://127.0.0.1:1080',
            # 'custom-header':  headers
        }

    def initUI(self):

        self.label1 = QLabel("关键字1")
        self.lineEdit1 = QLineEdit()
        self.label1.setBuddy(self.lineEdit1)

        self.EnableBox1 = QCheckBox("使能")
        self.EnableBox1.setChecked(True)
        # self.EnableBox1.stateChanged.connect(self.enable1)

        findButton = QPushButton("搜索")
        findButton.setDefault(True)
        findButton.clicked.connect(self.searchWeb)


        moreButton = QPushButton("拓展")
        moreButton.setCheckable(True)
        moreButton.setAutoDefault(False)

        # 创建浏览器类型选择下拉菜单
        self.labelBrowser = QLabel("浏览器选择")
        self.browserCombo = QComboBox(self)
        self.browserCombo.addItem("chrome 浏览器")
        self.browserCombo.addItem("Edge 浏览器")

        # 创建搜索引擎类型选择下拉菜单
        self.labelSearch = QLabel("搜索引擎选择")
        self.searchCombo = QComboBox(self)
        self.searchCombo.addItem("baidu.com")
        self.searchCombo.addItem("Google.com")


        # 创建一个数字选择框
        self.labelNum = QLabel("截图页数")
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(1, 100)  # 1
        self.spinbox.setSingleStep(1)  # 2
        self.spinbox.setValue(100)  # 3

        # 构建一个 拓展的 QWidget
        extension = QWidget()

        # 关键字2
        self.label2 = QLabel("关键字2")
        self.lineEdit2 = QLineEdit()
        self.label2.setBuddy(self.lineEdit2)
        self.EnableBox2 = QCheckBox("使能")
        self.EnableBox2.setChecked(False)

        self.label3 = QLabel("关键字3")
        self.lineEdit3 = QLineEdit()
        self.label3.setBuddy(self.lineEdit3)
        self.EnableBox3 = QCheckBox("使能")
        self.EnableBox3.setChecked(False)

        self.label4 = QLabel("关键字4")
        self.lineEdit4 = QLineEdit()
        self.label4.setBuddy(self.lineEdit4)
        self.EnableBox4 = QCheckBox("使能")
        self.EnableBox4.setChecked(False)

        self.label5 = QLabel("关键字5")
        self.lineEdit5 = QLineEdit()
        self.label5.setBuddy(self.lineEdit5)
        self.EnableBox5 = QCheckBox("使能")
        self.EnableBox5.setChecked(False)

        buttonBox = QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(findButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(moreButton, QDialogButtonBox.ActionRole)

        moreButton.toggled.connect(extension.setVisible)

        extensionLayout = QGridLayout()
        extensionLayout.setContentsMargins(0, 0, 0, 0)
        extensionLayout.addWidget(self.EnableBox2, 1, 0)
        extensionLayout.addWidget(self.label2, 1, 1)
        extensionLayout.addWidget(self.lineEdit2, 1, 2)
        extensionLayout.addWidget(self.EnableBox3, 2, 0)
        extensionLayout.addWidget(self.label3, 2, 1)
        extensionLayout.addWidget(self.lineEdit3, 2, 2)
        extensionLayout.addWidget(self.EnableBox4, 3, 0)
        extensionLayout.addWidget(self.label4, 3, 1)
        extensionLayout.addWidget(self.lineEdit4, 3, 2)
        extensionLayout.addWidget(self.EnableBox5, 4, 0)
        extensionLayout.addWidget(self.label5, 4, 1)
        extensionLayout.addWidget(self.lineEdit5, 4, 2)

        extension.setLayout(extensionLayout)


        first = QWidget()
        firstLayout = QGridLayout()
        firstLayout.setContentsMargins(0, 0, 0, 0)
        firstLayout.addWidget(self.EnableBox1, 0, 0)
        firstLayout.addWidget(self.label1, 0, 1)
        firstLayout.addWidget(self.lineEdit1, 0, 2)

        first.setLayout(firstLayout)

        topLayout = QHBoxLayout()
        topLayout.addWidget(buttonBox)
        topLayout.addWidget(self.labelBrowser)
        topLayout.addWidget(self.browserCombo)
        topLayout.addWidget(self.labelSearch)
        topLayout.addWidget(self.searchCombo)
        topLayout.addWidget(self.labelNum)
        topLayout.addWidget(self.spinbox)


        # mainLayout = QGridLayout()
        mainLayout = QVBoxLayout()
        # 关键性的参数设置
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(first)
        mainLayout.addWidget(extension)
        # mainLayout.setRowStretch(2, 1)


        self.setLayout(mainLayout)
        self.setWindowTitle('搜索截图')
        self.show()
        # 隐藏拓展UI
        extension.hide()

    def getCurrentTimeString(self):
        time_stamp = time.time()  # 当前时间的时间戳
        local_time = time.localtime(time_stamp)
        # 因为文件名有符号限制，所以都用 '-' 隔开
        str_time = time.strftime('%Y-%m-%d %H-%M-%S', local_time)
        self.currentTime = str(str_time)


    def handleKey1(self):
        # 处理第一个
        if self.EnableBox1.isChecked() == True:
            # 新建文件夹，并删除文件夹内的所有文件
            if not os.path.exists("搜索1"):
                os.makedirs("搜索1")
            for i in os.listdir("搜索1"):
                path = os.path.join("搜索1", i)
                os.remove(path)

            # 打开浏览器
            if self.browserCombo.currentText() == "chrome 浏览器":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Edge()
                time.sleep(1)
            driver.get(self.url)

            if self.url == 'http://www.google.com/':
                # todo 处理 google
                input = driver.find_element_by_xpath('//input[@name="q"]')
                input.send_keys(self.lineEdit1.text())
                input.send_keys(Keys.RETURN)

                # # 获取 google 搜索共有多少页
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # bsobj = BeautifulSoup(driver.page_source, 'lxml')
                # # 获取当前url
                # # print(driver.current_url)
                # time.sleep(2)
                # num_text_element = bsobj.find('div', {'id': 'resultStats'})
                # nums = filter(lambda s: s.isdigit(), num_text_element.text.partition(',')[0])
                # self.realPageNum = (int(''.join(nums)) + 9) // 10
                # print('搜索结果: ', self.realPageNum)
                # # print('self.realPageNum: ', self.realPageNum)

                # # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.realPageNum < self.customPageNum:
                    self.customPageNum = self.realPageNum

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                                 '搜索1/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit1.text(), (i+1)),
                                 config=self.imgkitConfig, options=self.imgKitOptions)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    # 到了最后一页不再点击了,并且关闭浏览器
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)


            else:
                # # todo 处理 百度
                driver.find_element_by_id("kw").send_keys(self.lineEdit1.text())
                driver.find_element_by_id("su").click()
                # 这里要延时一下，确保已经到搜索结果页面，可适当延长
                time.sleep(2)

                # 获取百度搜索共有多少页
                # 暂时不需要这种方法
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # 获取当前url
                # # print(driver.current_url)
                # num_text_element = bsobj.find('span', {'class': 'nums_text'})
                # nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
                # self.realPageNum = (int((''.join(nums)).replace(',', '')) + 9) // 10

                # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.customPageNum > 76:
                    self.customPageNum = 76

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                         '搜索1/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit1.text(), (i+1)),
                                 config=self.imgkitConfig)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页>")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)


    def handleKey2(self):
        # 处理第一个
        if self.EnableBox2.isChecked() == True:
            # 新建文件夹，并删除文件夹内的所有文件
            if not os.path.exists("搜索2"):
                os.makedirs("搜索2")
            for i in os.listdir("搜索2"):
                path = os.path.join("搜索2", i)
                os.remove(path)

            # 打开浏览器
            if self.browserCombo.currentText() == "chrome 浏览器":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Edge()
                time.sleep(1)
            driver.get(self.url)

            if self.url == 'http://www.google.com/':
                # todo 处理 google
                input = driver.find_element_by_xpath('//input[@name="q"]')
                input.send_keys(self.lineEdit2.text())
                input.send_keys(Keys.RETURN)

                # # 获取 google 搜索共有多少页
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # bsobj = BeautifulSoup(driver.page_source, 'lxml')
                # # 获取当前url
                # # print(driver.current_url)
                # time.sleep(2)
                # num_text_element = bsobj.find('div', {'id': 'resultStats'})
                # nums = filter(lambda s: s.isdigit(), num_text_element.text.partition(',')[0])
                # self.realPageNum = (int(''.join(nums)) + 9) // 10
                # print('搜索结果: ', self.realPageNum)
                # # print('self.realPageNum: ', self.realPageNum)

                # # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.realPageNum < self.customPageNum:
                    self.customPageNum = self.realPageNum

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                                 '搜索2/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit2.text(), (i+1)),
                                 config=self.imgkitConfig, options=self.imgKitOptions)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    # 到了最后一页不再点击了,并且关闭浏览器
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)


            else:
                # # todo 处理 百度
                driver.find_element_by_id("kw").send_keys(self.lineEdit2.text())
                driver.find_element_by_id("su").click()
                # 这里要延时一下，确保已经到搜索结果页面，可适当延长
                time.sleep(2)

                # 获取百度搜索共有多少页
                # 暂时不需要这种方法
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # 获取当前url
                # # print(driver.current_url)
                # num_text_element = bsobj.find('span', {'class': 'nums_text'})
                # nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
                # self.realPageNum = (int((''.join(nums)).replace(',', '')) + 9) // 10

                # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.customPageNum > 76:
                    self.customPageNum = 76

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                         '搜索2/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit2.text(), (i+1)),
                                 config=self.imgkitConfig)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页>")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)

    def handleKey3(self):
        # 处理第一个
        if self.EnableBox3.isChecked() == True:
            # 新建文件夹，并删除文件夹内的所有文件
            if not os.path.exists("搜索3"):
                os.makedirs("搜索3")
            for i in os.listdir("搜索3"):
                path = os.path.join("搜索3", i)
                os.remove(path)

            # 打开浏览器
            if self.browserCombo.currentText() == "chrome 浏览器":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Edge()
                time.sleep(1)
            driver.get(self.url)

            if self.url == 'http://www.google.com/':
                # todo 处理 google
                input = driver.find_element_by_xpath('//input[@name="q"]')
                input.send_keys(self.lineEdit3.text())
                input.send_keys(Keys.RETURN)

                # # 获取 google 搜索共有多少页
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # bsobj = BeautifulSoup(driver.page_source, 'lxml')
                # # 获取当前url
                # # print(driver.current_url)
                # time.sleep(2)
                # num_text_element = bsobj.find('div', {'id': 'resultStats'})
                # nums = filter(lambda s: s.isdigit(), num_text_element.text.partition(',')[0])
                # self.realPageNum = (int(''.join(nums)) + 9) // 10
                # print('搜索结果: ', self.realPageNum)
                # # print('self.realPageNum: ', self.realPageNum)

                # # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.realPageNum < self.customPageNum:
                    self.customPageNum = self.realPageNum

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                                 '搜索3/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit3.text(), (i+1)),
                                 config=self.imgkitConfig, options=self.imgKitOptions)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    # 到了最后一页不再点击了,并且关闭浏览器
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)


            else:
                # # todo 处理 百度
                driver.find_element_by_id("kw").send_keys(self.lineEdit3.text())
                driver.find_element_by_id("su").click()
                # 这里要延时一下，确保已经到搜索结果页面，可适当延长
                time.sleep(2)

                # 获取百度搜索共有多少页
                # 暂时不需要这种方法
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # 获取当前url
                # # print(driver.current_url)
                # num_text_element = bsobj.find('span', {'class': 'nums_text'})
                # nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
                # self.realPageNum = (int((''.join(nums)).replace(',', '')) + 9) // 10

                # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.customPageNum > 76:
                    self.customPageNum = 76

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                         '搜索3/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit3.text(), (i+1)),
                                 config=self.imgkitConfig)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页>")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)

    def handleKey4(self):
        # 处理第一个
        if self.EnableBox4.isChecked() == True:
            # 新建文件夹，并删除文件夹内的所有文件
            if not os.path.exists("搜索4"):
                os.makedirs("搜索4")
            for i in os.listdir("搜索4"):
                path = os.path.join("搜索4", i)
                os.remove(path)

            # 打开浏览器
            if self.browserCombo.currentText() == "chrome 浏览器":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Edge()
                time.sleep(1)
            driver.get(self.url)

            if self.url == 'http://www.google.com/':
                # todo 处理 google
                input = driver.find_element_by_xpath('//input[@name="q"]')
                input.send_keys(self.lineEdit4.text())
                input.send_keys(Keys.RETURN)

                # # 获取 google 搜索共有多少页
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # bsobj = BeautifulSoup(driver.page_source, 'lxml')
                # # 获取当前url
                # # print(driver.current_url)
                # time.sleep(2)
                # num_text_element = bsobj.find('div', {'id': 'resultStats'})
                # nums = filter(lambda s: s.isdigit(), num_text_element.text.partition(',')[0])
                # self.realPageNum = (int(''.join(nums)) + 9) // 10
                # print('搜索结果: ', self.realPageNum)
                # # print('self.realPageNum: ', self.realPageNum)

                # # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.realPageNum < self.customPageNum:
                    self.customPageNum = self.realPageNum

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                                 '搜索4/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit4.text(), (i+1)),
                                 config=self.imgkitConfig, options=self.imgKitOptions)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    # 到了最后一页不再点击了,并且关闭浏览器
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)


            else:
                # # todo 处理 百度
                driver.find_element_by_id("kw").send_keys(self.lineEdit4.text())
                driver.find_element_by_id("su").click()
                # 这里要延时一下，确保已经到搜索结果页面，可适当延长
                time.sleep(2)

                # 获取百度搜索共有多少页
                # 暂时不需要这种方法
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # 获取当前url
                # # print(driver.current_url)
                # num_text_element = bsobj.find('span', {'class': 'nums_text'})
                # nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
                # self.realPageNum = (int((''.join(nums)).replace(',', '')) + 9) // 10

                # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.customPageNum > 76:
                    self.customPageNum = 76

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                         '搜索4/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit4.text(), (i+1)),
                                 config=self.imgkitConfig)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页>")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)

    def handleKey5(self):
        # 处理第一个
        if self.EnableBox5.isChecked() == True:
            # 新建文件夹，并删除文件夹内的所有文件
            if not os.path.exists("搜索5"):
                os.makedirs("搜索5")
            for i in os.listdir("搜索5"):
                path = os.path.join("搜索5", i)
                os.remove(path)

            # 打开浏览器
            if self.browserCombo.currentText() == "chrome 浏览器":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Edge()
                time.sleep(1)
            driver.get(self.url)

            if self.url == 'http://www.google.com/':
                # todo 处理 google
                input = driver.find_element_by_xpath('//input[@name="q"]')
                input.send_keys(self.lineEdit5.text())
                input.send_keys(Keys.RETURN)

                # # 获取 google 搜索共有多少页
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # bsobj = BeautifulSoup(driver.page_source, 'lxml')
                # # 获取当前url
                # # print(driver.current_url)
                # time.sleep(2)
                # num_text_element = bsobj.find('div', {'id': 'resultStats'})
                # nums = filter(lambda s: s.isdigit(), num_text_element.text.partition(',')[0])
                # self.realPageNum = (int(''.join(nums)) + 9) // 10
                # print('搜索结果: ', self.realPageNum)
                # # print('self.realPageNum: ', self.realPageNum)

                # # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.realPageNum < self.customPageNum:
                    self.customPageNum = self.realPageNum

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                                 '搜索5/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit5.text(), (i+1)),
                                 config=self.imgkitConfig, options=self.imgKitOptions)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    # 到了最后一页不再点击了,并且关闭浏览器
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)


            else:
                # # todo 处理 百度
                driver.find_element_by_id("kw").send_keys(self.lineEdit5.text())
                driver.find_element_by_id("su").click()
                # 这里要延时一下，确保已经到搜索结果页面，可适当延长
                time.sleep(2)

                # 获取百度搜索共有多少页
                # 暂时不需要这种方法
                # bsobj = BeautifulSoup(driver.page_source, features="html.parser")
                # # 获取当前url
                # # print(driver.current_url)
                # num_text_element = bsobj.find('span', {'class': 'nums_text'})
                # nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
                # self.realPageNum = (int((''.join(nums)).replace(',', '')) + 9) // 10

                # 如果搜索页数少于设置的截图页数，以搜索页数为准
                if self.customPageNum > 76:
                    self.customPageNum = 76

                for i in range(self.customPageNum):
                    print(driver.current_url)
                    try:
                        result = imgkit.from_url(str(driver.current_url),
                         '搜索5/{0}_{1}_{2}.jpeg'.format(self.currentTime, self.lineEdit5.text(), (i+1)),
                                 config=self.imgkitConfig)
                    except:
                        # 此处一个Exit with code 1 due to network error: ContentNotFoundError异常
                        # 此异常为是因为css文件引用了外部的资源，如：字体，图片，iframe加载等。
                        # 选择忽略此异常
                        pass
                    # print(result)
                    # time.sleep(1)
                    if i == self.customPageNum - 1:
                        driver.close()
                        return
                    """
                    判断是否还能再翻页
                    """
                    try:
                        nextPage = driver.find_element_by_link_text("下一页>")
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                    # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        driver.close()
                        return
                    else:
                        # 没有发生异常，则继续点击下一页
                        # nextPage.click()
                        driver.execute_script("arguments[0].click();", nextPage)


    def searchWeb(self):

        threads.clear()

        # 获取当前时间
        self.getCurrentTimeString()

        # 获取 搜索引擎 地址
        if self.searchCombo.currentText() == "baidu.com":
            self.url = 'http://www.baidu.com/'
        else:
            self.url = 'http://www.google.com/'

        # 获取选择下载的页数
        self.customPageNum = self.spinbox.value()

        # 创建多线程
        t1 = threading.Thread(target=self.handleKey1)
        threads.append(t1)
        t2 = threading.Thread(target=self.handleKey2)
        threads.append(t2)
        t3 = threading.Thread(target=self.handleKey3)
        threads.append(t3)
        t4 = threading.Thread(target=self.handleKey4)
        threads.append(t4)
        t5 = threading.Thread(target=self.handleKey5)
        threads.append(t5)

        # 启动进程
        for t in threads:
            t.start()
        # 守护进程
        for t in threads:
            t.join()


    def enable1(self, state):
        if state == Qt.Checked:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
