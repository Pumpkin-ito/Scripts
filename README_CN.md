# 一、MarkDown文本处理器

## 1、功能

该脚本可以将文本处理器中的英文字符自动打上注释，免去了您手工注释代码之劳。

它的功能是这样的，下面的文字是经过文本处理器之前的样子。

这是一段代码print（abd）；

这是经过处理器处理之后的样子。

这是一段代码`print`（`abd`）；

## 2、GUI界面

运行`GuiforChangeMarkdownWord.py`脚本，您可以得到一个`GUI`界面的文本处理器，这将方便您的操作。

## 3、运行逻辑

在脚本`ChangeMarkdownWord.py`中是该处理器的主要代码。

通过正则匹配英文字母的方式来为其两边加上反引号来达到这个效果，并且排除了英文在标题中或者是已经处于代码块中的情况。

## 4、依赖

本项目需要安装以下两个依赖以正常运行。

```
import PySimpleGUI 
import re
```

## 5、一些Bug

因为英文和特殊字符，所以单独的url如：http://www.example.com。会被注释成下面这样。

`http`:`//www.example.com`

但是如果这是一个有标题的url如：[示例网站](http://www.example.com)，这样就不会被注释。

为什么要保留这个bug呢？因为有时候我确实需要注释一些url，并且这样也可以督促大家把需要引用的文章都弄上标题，方便读者们看。

## 6、配合使用更佳

由于在博客园上传Markdown文档时，如果图片本地存放要一张张上传。很麻烦，弄一个图床也有可能因为网络不稳定而看不到图片。

把图片转为Base64是一个不错的方法。

这里借鉴博主 [sureZ_ok](https://home.cnblogs.com/u/sureZ-learning/)的脚本，大家可以复制下来用：[markdown将图片转为Base64格式](https://www.cnblogs.com/sureZ-learning/p/16797820.html)