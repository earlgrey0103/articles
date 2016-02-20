# Django团队同时发布多个安全更新版本 建议尽快更新

编程派消息，Django团队24日通过官方博客对外发布了多个版本更新——Django 1.7.11, 1.8.7, and 1.9 release candidate 2。据称，这是为了解决一个安全问题。这些更新版本已经可以通过PyPI和[官网下载页面](https://www.djangoproject.com/download/)下载。同时，Django团队还建议所有使用Django的用户尽早升级。

CVE-2015-8213: 修复了模板过滤器（template filter）中可能泄漏设置（settings leak）的安全问题。

> 如果某个Django应用允许用户设置未经验证的日期格式，并将这个日期格式传入日期过滤器（date filter）中，例如`{{ last_updated|date:user_date_format }}`，那么恶意用户就可以通过传入一个设置键（settings key），而非真正的日期格式，获取应用的设置参数，例如： 传入"SECRET_KEY"，而不是"j/m/Y"。

为了解决这个问题，Django团队已经对日期模板过滤器所使用的函数进行了修改，现在只允许访问日期/时间的格式设置。

这个安全问题是Ryan Butterfield发现并报告给Django团队的。

受到影响的版本包括：

- Django master development branch
- Django 1.9 (currently at release candidate status)
- Django 1.8
- Django 1.7

根据Django支持版本协议，Django 1.6和更早的版本不再进行安全更新。而且这也很可能是Django 1.7.x系列版本的最后一次更新，因为预计将于12月1日正式发布Django 1.9。
