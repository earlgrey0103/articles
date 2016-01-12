# 不到一分钟安全部署Django应用

关键词：Django 部署, Django 教程, 安全部署Django应用, 快速部署Django应用

在Python Web开发方面，Django的用户人数应该是最多的。很多开发者在完成应用开发之后，都会面临线上部署Django应用这个头疼的问题。当初我在部署“编程派”网站时，就碰到了很多障碍，折腾了很久才成功。那么，有没有方法能够让我们快速、安全部署Django应用呢？今天给大家分享一个快速部署脚本，可以让你不到一分钟就安全部署Django应用。

## 用法：

在购买的Ubuntu服务器实例上，进入django项目的根目录，然后运行这个部署脚本。

	$ sudo ./deploydjango projectname

脚本成功执行完毕之后，你的Django应用就上线啦！

这时，你可以在浏览器中打开Ubuntu服务器的IP地址，查看上线后的应用。

## 操作指南：

首先，在Django应用的根目录下，安装DeployDjango脚本。

	$ wget https://raw.githubusercontent.com/yask123/DeployDjango/master/deploydjango.sh && chmod +x deploydjango.sh

然后执行部署脚本（`manage.py`文件所在目录）。
	
	$ sudo ./deploydjango.sh project_name

大功告成！

下面是我用Django默认生成的项目进行的测试情况。

![安装Deploy Django脚本](http://ww2.sinaimg.cn/large/006faQNTjw1ezwghe6x6fj30hw0bhacr.jpg)

![运行Gunicorn和Nginx](http://ww2.sinaimg.cn/large/006faQNTjw1ezwghe6x6fj30hw0bhacr.jpg)

## 注意事项：

该脚本只适用于Ubuntu服务器实例上的部署！
还要确保服务器上的80端口已经打开（这样，用户才能访问部署之后的应用）。

## 脚本具体实现步骤

该脚本通过gunicorn服务器在8000端口上运行你的Django应用，然后使用nginx反向代理设置，使用户能够从80端口访问应用。
具体实现步骤如下：
1. 安装nginx、python-pip和gunicorn。
2. 为Django应用正确配置nginx。
3. 在服务器上启动nginx服务。
4. 使用gunicorn启动Django应用。
5. 执行测试，检查是否成功部署（待开发者后续添加）。

这个脚本已经被开发者放在了[Github](https://github.com/yask123/DeployDjango)上，如果在使用过程中碰到了问题，可以直接向开发者提Issue。

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>