import requests


# 抓取首页
def get_one_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = 'http://maoyan.com/board'
    html = get_one_page(url)
    print(html)


main()
