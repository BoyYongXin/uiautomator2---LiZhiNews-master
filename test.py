import threading

import time
import uiautomator2 as u2
#https://wapapi-litchi.jstv.com/RichArticle/Like/20509242
u1 = u2.connect('fd7b57bb')
sess = u1.session("com.jsbc.lznews")
sess(text="热播视频").click()


# u2 = u2.connect('7c0475fc')
# sess = u2.session("com.jsbc.lznews")
# sess(text="热播视频").click()