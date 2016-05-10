# 利用 Python + Selenium 自动化快速截图

关键词：selenium截图, selenium 自动化测试, selenium 爬取动态网页, 网页截图, selenium python 教程, 截取整个页面窗口, Python 教程

URL：take-screenshot-of-web-page-using-selenium

Selenium 是一个可以让浏览器自动化地执行任务的工具，常用于自动化测试。与bs4等结合使用，也适合爬取动态网页数据。不过没想到，它居然可以用于网页截图，而且由于可编程性，用法更具想象空间。

目前，Selenium 支持 Java、C#、Ruby 以及 Python 四种客户端语言。如果你使用 Python，则只需要在命令行里输入```pip install selenium```并回车，即可安装 selenium 的 Python 版本客户端支持。

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


我们发现，第二篇文章的配图没有加载出来，是空白的。这是因为我在设计时要求窗口滚动到元素位置时才加载图片。

## 先执行JS脚本再截图

不过还好 Selenium 支持注入JS脚本。我们先在首页上执行一段 JavaScript 脚本，将页面的滚动条拖到最下方，然后再拖回顶部，最后才截图。这样可以解决像上面那种按需加载图片的情况。

下面是改进后的代码，封装进了一个名为 ```take_screenshot`` 的函数中：

```python
from selenium import webdriver
import time

def take_screenshot(url, save_fn="capture.png"):
    browser = webdriver.Firefox() 
    browser.set_window_size(900, 500)
    browser.get(url)
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
    take_screenshot("http://codingpy.com")
```

## 如何截取某个网页元素

有时候我们只想截取某个网页元素的图片呢？比如说会动态变化的验证码。本来 Selenium 也提供了对元素截图的支持，只要在选中的元素上调用其 ```screenshot()``` 方法即可。

但是在实际使用时却遇到了 ```Unrecognized command``` 这个异常，经过一段时间检索也没有找到解决办法。所以，只能曲线救国，利用 Selenium 执行JS代码，将页面上不需要的元素一一删除，只保留我们希望留下的元素，然后再利用上面的窗口截屏功能。

例如，如果我们只截取编程派网站右侧的二维码，可以执行这样一段JQuery代码：

```javascript
$('#main').siblings().remove();
$('#related__wrapper').siblings().remove();
$('.ui.sticky').siblings().remove();
$('.follow-me').siblings().remove();
$('img.ui.image').siblings().remove();
```
代码执行完毕之后，就只剩下二维码的图片了。然后我们再截屏。不过这样有一点不好，就是截屏图片的下方会有大量空白内容。

## 结语

虽然对元素截图出现了问题，但是 Selenium 的这个截图功能还是非常强大的。如上所示，它可以在页面上注入并执行一段 JavaScript 代码，还可以模拟鼠标点击等行为；而且可以同时运行多个实例，多个线程同时截图。

总的来说，使用 Selenium 进行网页截图是个不错的选择。

### 参考资料

- [Capture with Selenium](http://oldj.net/article/capture-with-selenium/)
- [Selenium Python Docs](http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement)
