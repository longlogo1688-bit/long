from miku_ai import get_wexin_article
import asyncio
import json

# 搜索 LOGO 设计相关文章
keywords = ['LOGO设计趋势', 'LOGO设计', '品牌设计']
results = []

for keyword in keywords:
    try:
        articles = asyncio.run(get_wexin_article(keyword, 5))
        results.extend(articles)
    except Exception as e:
        print(f'搜索 {keyword} 失败: {e}')

# 去重并按日期排序
seen_urls = set()
unique_results = []
for item in results:
    if item['url'] not in seen_urls:
        seen_urls.add(item['url'])
        unique_results.append(item)

# 保存结果到文件
with open('wechat_logo_search.json', 'w', encoding='utf-8') as f:
    json.dump(unique_results, f, ensure_ascii=False, indent=2)

# 打印结果
for i, item in enumerate(unique_results[:10], 1):
    title = item['title']
    source = item['source']
    date = item['date']
    url = item['url']
    snippet = item['snippet'][:100]
    print(f'{i}. {title}')
    print(f'   来源: {source} | 时间: {date}')
    print(f'   链接: {url}')
    print(f'   摘要: {snippet}...')
    print()
