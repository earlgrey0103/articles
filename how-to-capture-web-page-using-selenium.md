# Selenium快速截屏 完胜浏览器截图插件

Selenium 是一个可以让浏览器自动化地执行任务的工具，常用于自动化测试。与bs4等结合使用，也适合爬取动态网页数据。不过没想到，它居然可以用于网页截屏，而且由于可编程性，用法更具想象空间。

目前，Selenium 支持 Java、C#、Ruby 以及 Python 四种客户端语言。如果你使用 Python，则只需要在命令行里输入```pip install selenium```并回车，即可安装 selenium 的 Python 版本的客户端支持。

## 如何截取整个网页窗口

如果想截取整个窗口的话，可以使用 ```driver.save_screenshot()``` 。下面以编程派的网站为例，编写一个脚本截取首页的截图：

```python
from selenium import webdriver

browser = webdriver.Firefox()
url = "http://codingpy.com"
browser.set_window_size(1200, 900)
browser.get(url)

browser.save_screenshot("codingpy.png")
browser.close()

```

我们运行这段代码之后，会当前目录创建名为codingpy.png的图片文件。我们看一下实际效果（我已对图片进行裁剪，只保留了前面一部分）。

![编程派网站首页截图]()

我们发现，第二篇文章的配图没有加载出来，是空白的。这是因为我在设计时要求窗口滚动到元素位置时才加载图片。

## 通过 Selenium 执行JS脚本

不过还好 Selenium 支持注入JS脚本。我们现在首页上上执行了一段 JavaScript 脚本，将页面的滚动条拖到最下方，然后再拖回顶部，最后才截图。这样可以解决像上面那种按需加载图片的情况。

下面是改进后的代码，封装进了一个名为 ```capture`` 的函数中：

```python
from selenium import webdriver
import time


def capture(url, save_fn="capture.png"):
    browser = webdriver.Firefox() # Get local session of firefox
    browser.set_window_size(1200, 900)
    browser.get(url) # Load page
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);

            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }

            setTimeout(f, 1000);
        })();
    """)

    for i in xrange(30):
        if "scroll-done" in browser.title:
            break
        time.sleep(10)

    browser.save_screenshot(save_fn)
    browser.close()


if __name__ == "__main__":

    capture("http://codingpy.com")
```



http://oldj.net/article/capture-with-selenium/

## 如何截取某个网页元素


screenshot(filename)
Gets the screenshot of the current element. Returns False if there is
any IOError, else returns True. Use full paths in your filename.
Args:
filename: The full path you wish to save your screenshot to.
Usage:
element.screenshot(‘/Screenshots/foo.png’)

## 结语

与 PageSaver 等浏览器插件相比，Selenium 功能更为强大，例如，它可以在页面上注入并执行一段 JS，还可以模拟鼠标点击等行为，而且可以同时运行多个实例（多个线程同时截图）。这样看来，使用 Selenium 来给页面截图似乎是一个不错的选择。

http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
