from loguru import logger
from lizhi_news_spider import paerser
from uiautomator2_run import uiautomator2_run


def start_uiautomator2():
    '''
    #需要自启
    :return:
     # 开启自动化模拟手机滑动程序
    #uiautomator2_run.py
    '''
    pass
def start_mitm():
    '''
    #需要自启
    :return:
    # 开启mitmproxy抓包工具
    # 'cmd命令执行 mitmdump -s mtdu.py | python extract.py'
    '''
    pass
def begin_callback():
    logger.info('\n********** spider_main begin **********')

def end_callback():
    logger.info('\n********** spider_main end **********')


def main():

    # 开启爬虫
    paerser.parser_info()


if __name__ == '__main__':
    main()
