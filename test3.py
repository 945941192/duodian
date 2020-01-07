#coding=utf-8
from appium import webdriver
import time

class HelloWorld(object):
    def test_enterFilter(self):
        desired_caps = dict()
        # 平台的名字，大小写无所谓，不能乱写
        desired_caps['platformName'] = 'andRoId'
        # 平台的版本，（5.4.3 可以写 5.4.3，5.4，5）
        desired_caps['platformVersion'] = '5'
        # 设备的名字，随便写，不能乱写
        desired_caps['deviceName'] = 'model:Samsung_Galaxy_S6'
        # 要打开的应用程序
        desired_caps['appPackage'] = 'com.wm.dmall'
        # 要打开的界面
        desired_caps['appActivity'] = '.MainActivity'
        desired_caps['noReset'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

        # set1: 点击送到家
        self.driver.find_element_by_xpath("//*[@bounds='[1,2373][288,2560]']").click()

        # set2: 点击定位哪个店  --> 输入店名
        # self.driver.find_element_by_xpath("//*[@bounds='[508,400][948,502]']").click()
        # self.driver.find_element_by_xpath("//*[@bounds='[120,340][1260,484]']").send_keys("西三旗")

        # set3: 点击茅台预售
        self.driver.implicitly_wait(50)
        self.driver.find_element_by_xpath("//*[@bounds='[40,1093][1400,1510]']").click()
        # return "hello"
     
        while 1:
            self.driver.implicitly_wait(1)
            time.sleep(1)
            local_time = time.strftime('%H:%M:%S',time.localtime(time.time()))
            print "local_time is ", local_time
            if local_time == "09:06:00":
                # set4: 点击立即抢购
                self.driver.implicitly_wait(1)
                self.driver.find_element_by_xpath("//*[@bounds='[1076,1244][1364,1340]']").click()
                # set5: 点击排队购买
                self.driver.find_element_by_xpath("//*[@bounds='[144,2328][1296,2524]']").click()
                # 先用资格查询做测试
                # self.driver.find_element_by_xpath("//*[@bounds='[336,816][684,916]']").click()
                # 排队等待20s 然后点击下单
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath("//*[@content-desc='确认下']").click()
                break

        while 1:
            time.sleep(5)
            self.driver.implicitly_wait(1)
            print "查看页面信息是否抢到了！！"


if __name__ == '__main__':
    # 8点55启动  9点监控点击抢购
    obj = HelloWorld()
    obj.test_enterFilter()
