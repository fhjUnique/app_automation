from global_ import global_cls
from appium import webdriver
from utils.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, time

my_logger = Logger(logger='WebTools').getlog()


class WebTools(object):
    def __init__(self):
        pass

    # 启动手机APP
    def start_app(self):
        my_logger.info('开始启动APP...')
        desired_cups = {}
        desired_cups['deviceName'] = global_cls.deviceName  # 设备名称
        desired_cups['platformName'] = global_cls.platformName  # 设备平台
        desired_cups['platformVersion'] = global_cls.platformVersion  # 设备系统版本
        desired_cups['autoAcceptAlerts'] = global_cls.autoAcceptAlerts  # 默认选择接受弹窗的条款
        desired_cups['noReset'] = global_cls.noReset  # 是否不重复安装APP
        desired_cups['appPackage'] = global_cls.appPackage
        desired_cups['appActivity'] = global_cls.appActivity
        i = 0
        while i < 3:
            i = i + 1
            try:
                self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cups)  # 启动app
                my_logger.info('启动成功,开始执行测试用例！')
                return self.driver
            except Exception as e:
                my_logger.error('fail --- 第' + str(i) + '次启动APP未成功')
                my_logger.error(e)

    # 退出手机APP
    def stop_app(self):
        self.driver.quit()


    # 隐式等待时间
    def wait_implicit(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 显性等待时间
    def web_driver_wait(self, ele_type, element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((ele_type, element)))

    # 获取元素+显示等待
    def find_element(self, ls):
        try:
            if ls[2] == 'id':
                self.web_driver_wait(By.ID, ls[1])
                return self.driver.find_element_by_id(ls[1])
            elif ls[2] == 'name':
                self.web_driver_wait(By.NAME, ls[1])
                return self.driver.find_element_by_name(ls[1])
            elif ls[2] == 'xpath':
                self.web_driver_wait(By.XPATH, ls[1])
                return self.driver.find_element_by_xpath(ls[1])
            elif ls[2] == 'link_text':
                self.web_driver_wait(By.LINK_TEXT, ls[1])
                return self.driver.find_element_by_link_text(ls[1])
            elif ls[2] == 'class_name':
                self.web_driver_wait(By.CLASS_NAME, ls[1])
                return self.driver.find_element_by_class_name(ls[1])
            elif ls[2] == 'partial_link_text':
                self.web_driver_wait(By.PARTIAL_LINK_TEXT, ls[1])
                return self.driver.find_element_by_partial_link_text(ls[1])
            elif ls[2] == 'css_selector':
                self.web_driver_wait(By.CSS_SELECTOR, ls[1])
                return self.driver.find_element_by_css_selector(ls[1])
            elif ls[2] == 'tag_name':
                self.web_driver_wait(By.TAG_NAME, ls[1])
                return self.driver.find_element_by_tag_name(ls[1])
        except Exception as e:
            my_logger.error('fail --- ' + '未找到元素')
            my_logger.error(e)

    # 获取元素
    def find_have_element(self, ls):
        if ls[2] == 'id':
            return self.driver.find_element_by_id(ls[1])
        elif ls[2] == 'name':
            return self.driver.find_element_by_name(ls[1])
        elif ls[2] == 'xpath':
            return self.driver.find_element_by_xpath(ls[1])
        elif ls[2] == 'link_text':
            return self.driver.find_element_by_link_text(ls[1])
        elif ls[2] == 'class_name':
            return self.driver.find_element_by_class_name(ls[1])
        elif ls[2] == 'partial_link_text':
            return self.driver.find_element_by_partial_link_text(ls[1])
        elif ls[2] == 'css_selector':
            return self.driver.find_element_by_css_selector(ls[1])
        elif ls[2] == 'tag_name':
            return self.driver.find_element_by_tag_name(ls[1])

    # 清除输入框事件
    def clear(self, ls, log='null'):
        if log != 'null':
            my_logger.info(log)
        if self.find_element(ls):
            self.find_element(ls).clear()

    # 鼠标点击事件
    def click(self, ls, log='null'):
        if log != 'null':
            my_logger.info(log)
        if self.find_element(ls):
            self.find_element(ls).click()

    # 输入内容方法
    def input(self, ls, input_value, log='null'):
        if log != 'null':
            my_logger.info(log)
        if self.find_element(ls):
            self.find_element(ls).send_keys(input_value)

    # 获取元素的text
    def get_text(self, ls, log='null'):
        if log != 'null':
            my_logger.info(log)
        if self.find_element(ls):
            text = self.find_element(ls).text
            return text

    # 向上滑动屏幕
    def swipeUp(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动屏幕
    def swipeDown(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动屏幕
    def swipLeft(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # 向右滑动屏幕
    def swipRight(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # 校验按钮是否为选中状态
    def is_selected(self, ls, log='null'):
        if log != 'null':
            my_logger.info(log)
        if self.find_element(ls):
            flag = self.find_element(ls).is_selected()
            return flag

    # 错误截屏
    def screen_shot(self, message):
        file_path = global_cls.screen_path
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + message + '.png'
        self.driver.get_screenshot_as_file(screen_name)
