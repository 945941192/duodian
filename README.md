川哥项目：
一. 安装环境
    1. 安装java sdk
        https://blog.csdn.net/YuanLiYin079/article/details/81433964
        留下一点疑惑，就是环境变量的配置

    2. 安装安卓 sdk
        https://www.jianshu.com/p/c1c604992206 (不好用)
        这个第一种方式安装 adb 成功

    3. 安装安卓模拟器
        mac上安装Genymotion
        https://www.jianshu.com/p/f7b087e49531
        如何使用：
            https://www.cnblogs.com/rainboy2010/p/6387770.html
            遇到问题，不能安装安卓app，已截图，解决方案在上述博客中：
                Genymotion-ARM-Translation.zip 拖到手机中

            问题：不能启动应用；
            https://blog.csdn.net/GHY2016/article/details/83422620
            Genymotion-ARM-Translation.zip各安卓版本合集

二. 自动化相关环境

    相关教程： 
        https://www.cnblogs.com/Mushishi_xu/p/7685888.html

    安装 appium：
        https://www.jianshu.com/p/d36ff3707862

    mac 安装pip
        https://www.jianshu.com/p/66d85c06238c
 
         pip install selenium
            Successfully installed selenium-3.141.0 urllib3-1.25.7

         pip install Appium-Python-Client
            Successfully installed Appium-Python-Client-0.48



三， 代码部分
    1. 直接获取当前的app包名：
        adb shell "dumpsys window windows | grep mFocusedApp"
        
    2. 定位元素
        1） 问题：uiautomatorviewer 报错，
            解决：要降低javaSDK的版本
                相关连接：https://www.jianshu.com/p/3075a55e33ba
            卸载：
                https://blog.csdn.net/qq_30889373/article/details/78863313

            解决：
                OK  安装java SDK 8版本


    知道了 id com.wm.dmall:id/a5l
    跳过导航页：
        https://www.cnblogs.com/liushengchieh/p/9084827.html 
    保留登录状态：
        https://testerhome.com/topics/9031
        添加：
            desired_caps['noReset'] = True  可以不用管导航栏了

    将页面向上滑动：

    遇到问题：
        ui那个命令不能定位出 webview 的元素
        解决方法：
            1） ❌ 使用Chrome浏览器对应出来
                配这个东西太复杂了
            2） ✅ 使用appium 的 inspector工具可以定位到
                最近发现使用Appium Inspector即可实现H5页面元素的定位, 不需要额外安装任何软件。

            appium  使用 Inspector 查看元素
                连接：
                    https://www.jianshu.com/p/0a19409c0d37

    3. 并发

