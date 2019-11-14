# *_*coding:utf-8 *_*
import time
import uiautomator2 as u2
import threading

class PhoneThread(threading.Thread):

    def __init__(self, serial, option_nav):
        threading.Thread.__init__(self)
        self.serial = serial
        self.device = u2.connect(serial)
        self.sess = self.device.session("com.jsbc.lznews")
        self.option_nav = option_nav

    def run(self):
        self.crawl(self.option_nav)

    def crawl(self, option_nav):
        self.sess(text=option_nav).click()
        while True:
            self.swipeUp(self.device,t=0.5)
            #time.sleep(2)

    def swipeUp(self, d, t=0.5):


        # width = self.sess.info['displayWidth']
        # height = self.sess.info['displayHeight']
        #
        # x1 = width * 0.5
        # y1 = height * 0.85
        # y2 = height * 0.25
        # d.swipe(x1, y1, x1, y2, t)
        x1 = 0
        y1 = 1648
        y2 = 291
        x2 = 30
        d.swipe(x1, y1, x2, y2, t)

if __name__ == '__main__':
    phone_list = []
    #传入手机设备号和手机对应滑动的模块
    phone_device_list = [
        #('fd7b57bb',"热播视频"),
        ('7c0475fc',"热播视频")
    ]

    for device_id, nav in phone_device_list:
        phone = PhoneThread(device_id, nav)
        phone_list.append(phone)

    for i in phone_list:
        i.start()