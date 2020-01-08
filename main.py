
"""
From following tutorial: https://www.youtube.com/watch?v=E5cSNSeBhjw


Other possible sources: https://www.youtube.com/watch?v=87Gx3U0BDlo
https://www.edureka.co/blog/web-scraping-with-python/
https://www.youtube.com/watch?v=dXHYE9Zf7YY
https://www.youtube.com/watch?v=mplXYELcnks
https://www.youtube.com/watch?v=tb8gHvYlCFs
git: https://www.youtube.com/watch?v=61WbzS9XMwk
"""
import pandas as pd
import requests #gives acces to websites
from bs4 import BeautifulSoup  #bs gives nice structures to work with when scraping (understands html/css)


url="https://forecast.weather.gov/MapClick.php?lat=38.63579000000004&lon=-92.56629999999996#.XhUJCkdKjIU"
page = requests.get(url)
#print("website retrieval status code: " + str(page.status_code))   # This should print 200
soup = BeautifulSoup(page.content, 'html.parser') #soup object now contains all the html code of the page (same text as if you right click on a page and "view page source")
week_forecast = soup.find(id='seven-day-forecast-body') #finds all desired tags 
#print(week_forecast)    #prints out everything in the body tag
items = week_forecast.find_all(class_= "tombstone-container")   #class is a keyword, so append _
#print(items[0])  #only print first item

#want the names in a name column, description in a desc column, temp in a temp column
#print(items[0].find(class_='period-name').get_text())      #without .get_text() get code with the tags
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())         #not sure why not 'temp temp-low' (as that's what shows in the source code of the website)

period_names = [item.find(class_ ='period-name').get_text() for item in items] # list comprehension == [ expression for item in list if conditional ]
short_descriptions = [item.find(class_ ='short-desc').get_text() for item in items]
temperatures = [item.find(class_ ='temp').get_text() for item in items]

weather_info = pd.DataFrame(
            {
                'period':period_names,
                'description':short_descriptions,
                'temperature':temperatures
                    }
        )
print(weather_info)

weather_info.to_csv('weather.csv')  #create a csv file in the same folder as this file