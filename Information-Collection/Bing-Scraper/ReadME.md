# Bing Web Scraper

这是一个用于从 `Bing` 搜索引擎抓取 `title`、`url` 和 `domain` 的 `Python` 脚本，并将结果保存到 `CSV` 文件中。

## 环境
-  此脚本基于 `Python` `3.12.6` 开发。

## 功能
-  抓取 `Bing` 搜索结果的 `title`、`url` 和 `domain`。
-  将结果保存为 `CSV` 文件。

## 安装
`1.` 下载 `Bing-Scraper.py` 脚本以及 `requirements.txt` 文件。

`2.` 安装所需依赖：
```bash
pip install -r requirements.txt
```

## 使用方法
运行脚本：
```bash
# 基础用法
python Bing-Scraper.py "您在Bing搜索框中输入的内容" -s  # -s 参数为可选，用于静默输出

# 示例，搜索域名为Zoomeye.hk的网页，不包含www或web开头的
python Bing-Scraper.py "site:zoomeye.hk -www -web"
```

运行截图：

![img/运行截图.png](https://github.com/Pumpkin-ito/Scripts/blob/main/Information-Collection/Bing-Scraper/img/%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE.png)
