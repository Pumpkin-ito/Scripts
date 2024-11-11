# Bing Web Scraper

这是一个用于从 Bing 搜索引擎抓取 `title`、`url` 和 `domain` 的 Python 脚本，并将结果保存到 CSV 文件中。

## 环境
- 此脚本基于Python3.12.6开发。

## 功能
- 抓取 Bing 搜索结果的 `title`、`url` 和 `domain`。
- 将结果保存为 CSV 文件。

## 安装
1. 下载Bing-Scraper.py脚本以及requirements.txt文件。

2. 安装所需依赖：
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法
运行脚本：
    ```bash
    python Bing-Scraper.py "您在Bing搜索框中输入的内容" -s(可选，该选项用于静默输出)
    ```

结果文件：
- 自动在当前目录下保存为scraped_bing_data.csv文件。
- 可以使用powershell对其进行处理，提取去重后的域名信息等。

## 一些Bug
- 有时候使用该脚本会无法获取结果，尝试等待一会再执行。

Todo List：
- 增加其他搜索引擎的结果提取功能。

