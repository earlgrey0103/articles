# 新时代编辑必备的脚本

文章结构：

```
- article
  - article.md
  - images
    - tmp.png
    - file.jpg
```

辅助脚本列表：

1. html2md.py：将指定 url 转换为 md 格式的文件，可以传入 selector 参数，选择想要保存的内容。
2. code2png.py：将指定 url 中的代码示例保存为截图。
3. download_image.py：下载指定 url 中的图片，提供图片的 selector。
4. upload2cos.py：将指定文件夹中的图片上传到腾讯云 COS。
5. upload2zhihu.py：将指定文件夹中的图片上传到知乎（上传API待研究）。

参考：https://www.zhihu.com/question/29925879

6. gen2article.py：保存图片链接已替换为 COS 或知乎图片地址的 md 文件。

## 处理顺序

1. 传入文章对应的 URL，文章正文的 CSS Selector，解析为 Markdown
2.1 将正文中的代码部分截图，逐一上传至 COS 并按顺序保存 ACCESS URL
2.2 将代码截图逐一上传至知乎，并按顺序保存 URL
3. 使用 ACCESS URL 逐一替换 Markdown 文件中 [code] [/code] 部分 （using re），alt
4. 计算 Markdown 文件的字数及阅读时间，添加至 Markdown 文件首行