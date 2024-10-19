import requests

def get_page_content(url):
    """指定したURLのコンテンツを取得する関数

    Args:
        url (str): 取得したいページのURL

    Returns:
        str: 取得したページのコンテンツ
    """

    response = requests.get(url)
    response.raise_for_status()  # ステータスコードが異常な場合に例外を発生させる
    return response.text

# 使用例
if __name__ == '__main__':
    url = "https://google.com"
    content = get_page_content(url)
    print(content)