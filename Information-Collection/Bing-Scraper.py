#Author Pumpkins & ChatGPT

# 相关依赖 / Relevant dependencies
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import argparse
from colorama import init, Fore, Style
import urllib.parse

# 初始化 colorama
init()

# 欢迎界面
title = """

          ___                    __                               
        ||/  | /                /                                 
        ||___|(  ___  ___  ___ (___  ___  ___  ___  ___  ___  ___ 
        ||   )| |   )|   )         )|    |   )|   )|   )|___)|   )
        ||__/ | |  / |__/       __/ |__  |    |__/||__/ |__  |    
                     __/                           |                 

        Bing-Scrape 
        Powered by Pumpkin & ChatGPT 
"""

# 打印带有颜色的欢迎界面
# Print welcome message with English and Chinese
print(Fore.CYAN + title + Style.RESET_ALL)
print(Fore.CYAN + "Welcome to the Bing-Scrape tool - Extract information efficiently!" + Style.RESET_ALL)
print(Fore.CYAN + "欢迎使用Bing-Scrape工具 - 高效提取信息！" + Style.RESET_ALL)

print(Fore.GREEN + "Author: Pumpkin & ChatGPT (mostly done by ChatGPT)" + Style.RESET_ALL)
print(Fore.GREEN + "作者：Pumpkin & ChatGPT（主要由ChatGPT完成）" + Style.RESET_ALL)

print(Fore.BLUE + "Use this tool responsibly and adhere to all web scraping best practices." + Style.RESET_ALL)
print(Fore.BLUE + "请负责任地使用此工具，并遵循所有网页抓取的最佳实践。" + Style.RESET_ALL)

print(Fore.YELLOW + "Here is a brief introduction to how to use this tool." + Style.RESET_ALL)
print(Fore.YELLOW + "接下来是简单用法介绍。" + Style.RESET_ALL)

print(Fore.YELLOW + "Simply add the content you would enter in the Bing search box as the Query parameter for the script. If you find the output too verbose, use -s for silent mode.")
print(Fore.YELLOW + "只需将您在Bing搜索框输入的内容作为Query参数加入脚本即可，如果您觉得输出太冗长，输入-s会静默输出。" + Style.RESET_ALL)


# 定义命令行参数解析器
parser = argparse.ArgumentParser(description='Search Bing and scrape results.')
parser.add_argument('query', type=str, help='The search query to be used in Bing.')
parser.add_argument('--silent', '-s', action='store_true', help='Silent mode, no console output')


# 解析命令行参数
args = parser.parse_args()

# 自动识别query中的参数是否url转码，如果没有转码帮忙转码
def ensure_url_encoding(query):
    # 检查是否需要 URL 编码
    if urllib.parse.unquote(query) == query:
        # 如果未转码，进行转码
        return urllib.parse.quote(query)
    else:
        # 已转码，不做处理
        return query

# 获取结果中的Url，Domain,Title
def search_bing_all_pages(base_query, start_index=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    results = []
    first = start_index

    while True:
        url = f"https://www.bing.com/search?q={base_query}&first={first}&FORM=PERE"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            print("Request failed, status code:", response.status_code)
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        # 检查是否有“没有与此相关的结果”的提示 / Check if there is "没有与此相关的结果"
        no_results = soup.find(string="没有与此相关的结果")
        if no_results:
            print("已到达最后一页，没有更多结果。")
            print("Reached the last page, no more results.")
            break

        # 提取搜索结果 / Extract search results
        page_results = []
        for item in soup.find_all('li', {'class': 'b_algo'}):
            title = item.find('h2').text
            link = item.find('a')['href']
            domain = urlparse(link).netloc

            if title and link:
                page_results.append({
                    'title': title,
                    'url': link,
                    'domain': domain
                })

        if not page_results:
            print("未找到更多搜索结果，停止抓取。")
            print("No more results found, stopping the extraction.")
            break

        results.extend(page_results)
        # 静默输出
        if not args.silent:
            # 打印当前页抓取的数量和更新起始位置 / Print number of results from the current page and update the starting position
            print(f"{Fore.BLUE}抓取到第 {first} 条，该页显示了 {len(page_results)} 条结果。{Style.RESET_ALL}")
            print(f"Fetched page starting at {first}, with {len(page_results)} results.")

        # 假设每页显示10个结果进行自增 / Assume increment by 10 for each page
        first += len(page_results)

    return results


# 测试搜索功能 / Test the search function
query = ensure_url_encoding(args.query)
all_search_results = search_bing_all_pages(query)

# 打印搜索结果 / Print the search results
if not args.silent:
    print(f"{Fore.BLUE}======= 结果集输出 / Result Set Output ======={Style.RESET_ALL}")
    for i, result in enumerate(all_search_results, start=1):
        print(f"{i}. Title:{Fore.CYAN}{result['title']}{Style.RESET_ALL}")
        print(f"     URL: {Fore.GREEN}{result['url']}{Style.RESET_ALL}")
        print(f"     Domain: {Fore.GREEN}{result['domain']}{Style.RESET_ALL}")

# 转换为 DataFrame
df = pd.DataFrame(all_search_results)
# 判断结果是否为空
if not df.empty:
    # 统计结果数量
    num_rows = df.shape[0]
    # 打印带有颜色的输出
    print(Fore.GREEN + f"结果总计 {num_rows} 条" + Style.RESET_ALL)
    # 保存为 CSV 文件
    csv_path = 'scraped_bing_data.csv'
    df.to_csv(csv_path, index=False, columns=["title", "url", "domain"])
else:
    print(Fore.RED + f"为抓取到数据，请检查是否被反爬虫机制拦截！" + Style.RESET_ALL)
