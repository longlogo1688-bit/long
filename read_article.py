import urllib.request
import urllib.parse
import json

# 使用 Jina Reader 读取微信公众号文章
url = "https://mp.weixin.qq.com/s?src=11&timestamp=1773641072&ver=6601&signature=iMvafLxQYLHpirgW6NQo2yqEqVd0bNKz8ZXTezWk*oBboKnWPEuFCkBdR68sebZYBIWIJBR7QTsuoMnR5t7YQhDFFQMR6o56Z3Gled4416o6N5jEe1Qwhe1cZvDzul1I&new=1"
jina_url = f"https://r.jina.ai/{url}"

try:
    req = urllib.request.Request(jina_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        content = response.read().decode('utf-8')
        print(content[:3000])
except Exception as e:
    print(f"获取失败: {e}")
