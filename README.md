**笔记_自动化工具uiautomator2安装和使用教程**

**1、参考链接**

 GitHub： https://github.com/openatx/uiautomator2 

**2、工作原理：**

三、uiautomator2工作原理：

![img](https://img2018.cnblogs.com/blog/1231206/201903/1231206-20190317123618691-734760575.png)

如图所示，python-uiautomator2主要分为两个部分，python客户端，移动设备

- python端: 运行脚本，并向移动设备发送HTTP请求
- 移动设备：移动设备上运行了封装了uiautomator2的HTTP服务，解析收到的请求，并转化成uiautomator2的代码。

整个过程

1. 在移动设备上安装`atx-agent`(守护进程), 随后`atx-agent`启动uiautomator2服务(默认7912端口)进行监听
2. 在PC上编写测试脚本并执行（相当于发送HTTP请求到移动设备的server端）
3. 移动设备通过WIFI或USB接收到PC上发来的HTTP请求，执行制定的操作

**三、安装测试**

**第一步：**

先准备一台（不要两台）开启了`开发者选项`的安卓手机，连接上电脑，确保执行`adb devices`可以看到连接上的设备。

- 运行`pip3 install -U uiautomator2`安装uiautomator2
- 运行`python3 -m uiautomator2 init`安装包含httprpc服务的apk到手机+`atx-agent, minicap, minitouch`

**第二步：**

命令行运行`python`打开python交互窗口。然后将下面的命令输入到窗口中。

```
import uiautomator2 as u2

d = u2.connect() # connect to device
print(d.info)
```

这时看到类似下面的输出，就可以正式开始用我们这个库了。因为这个库功能太多，后面还有很多的内容，需要慢慢去看 ....

```
{'currentPackageName': 'net.oneplus.launcher', 'displayHeight': 1920, 'displayRotation': 0, 'displaySizeDpX': 411, 'displaySizeDpY': 731, 'displayWidth': 1080, 'productName': 'OnePlus5', '
screenOn': True, 'sdkInt': 27, 'naturalOrientation': True}
```

**四、应用及操作**

**调用uiautomator2的过程**

1. 配置手机设备参数，设置具体操作的是哪一台手机
2. 抓取手机上应用的控件，制定对应的控件来进行操作
3. 对抓取到的控件进行操作，比如点击、填写参数等。

**配置手机设备参数**

python-uiautomator2连接手机的方式有两种，一种是通过WIFI，另外一种是通过USB。两种方法各有优缺点。
WIFI最便利的地方要数可以不用连接数据线，USB则可以用在PC和手机网络不在一个网段用不了的情况。

1. 使用WIFI连接

   手机获取到手机的IP，并确保电脑可以PING通手机。手机的IP可以在设置-WIFI设置里面获取到。
   比如手机的IP是`192.168.0.100`，连接设备的代码为

   ```
   import uiautomator2 as u2d = u2.connect('192.168.0.100')
   ```

2. 使用USB连接

   手机的序列号可以通过`adb devices`获取到，假设序列号是`123456f`，连接代码为

   ```
   import uiautomator2 as u2d = u2.connect_usb('123456f')
   ```

#### 抓取手机上应用的控件

安装方法: `pip install --pre weditor`

使用方法: 
首先运行`python -m weditor`，之后浏览器会自动打开一个网页 `http://atx.open.netease.com` （注：这个网址仅提供一个前端，而`python -mweditor`这个命令则本地开放了HTTP的接口，前端去跟本地的服务去通信）

定位方式

1. ResourceId定位: `d(resourceId="com.smartisanos.clock:id/text_stopwatch").click()`
2. Text定位 `d(text="秒表").click()`
3. Description定位 `d(description="..").click()`
4. ClassName定位 `d(className="android.widget.TextView").click()`


看完安装教程和简单使用，我们回归正传：

本项目是目的抓取荔枝新闻手机app，新闻，和江苏模块的下视频信息，项目比较基础

抓取流程：
    uiautomator2 连接两个手机（分别进入到新闻和江苏模块下），模拟手机滑动，

    mitmproxy 获取数据信息的json的链接，写入mongo数据库

    爬虫程序，负责扫MongoDB数据库，请求链接抓取信息

如有问题联系文本作者：
·····1426866609@qq.com    qq同号···············