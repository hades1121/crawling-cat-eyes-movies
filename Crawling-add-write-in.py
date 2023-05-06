import requests
import json
import urllib3


# 抓取首页
def get_one_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.text
    return None


# 写入文件
def write_to_file(html):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(html)


def main():
    url = 'https://www.gutenberg.org/ebooks/search/?query=book&submit_search=%E6%90%9C%E7%B4%A2&start_index=26'
    # url可以更改
    html = get_one_page(url)
    write_to_file(html)


main()
