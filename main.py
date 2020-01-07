
"""
From following tutorial: https://www.youtube.com/watch?v=E5cSNSeBhjw


Other possible sources: https://www.youtube.com/watch?v=87Gx3U0BDlo
https://www.edureka.co/blog/web-scraping-with-python/
https://www.youtube.com/watch?v=dXHYE9Zf7YY
https://www.youtube.com/watch?v=mplXYELcnks
https://www.youtube.com/watch?v=tb8gHvYlCFs
git: https://www.youtube.com/watch?v=61WbzS9XMwk
"""

import requests
from bs4 import beautifulsoup4  #bs gives nice structures to work with when scraping (understands html/css)

page = requests.get(' ')
soup = BeautifulSoup(page.content, 'html.parser') #soup object now contains all the html code of the page (same text as if you right click on a page and "view page source")
print(soup.find_all('a')) #finds all a tags (links)



