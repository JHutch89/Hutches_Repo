import requests
from bs4 import BeautifulSoup

def scrape_kdnuggets():
    url = "https://www.kdnuggets.com/news/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = soup.find_all('div', class_='post-content')  # Updated selector
    
    news_list = []
    for article in articles:
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        summary = article.find('p').text.strip() if article.find('p') else ''
        news_list.append({
            'title': title,
            'link': link,
            'summary': summary
        })
    
    print("KDnuggets news list:", news_list)  # Debugging line
    return news_list

def scrape_datasciencecentral():
    url = "https://www.datasciencecentral.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = soup.find_all('div', class_='content-title')  # Updated selector
    
    news_list = []
    for article in articles:
        title = article.find('a').text.strip()
        link = article.find('a')['href']
        summary = ''  # Assuming no summary is available
        news_list.append({
            'title': title,
            'link': link,
            'summary': summary
        })
    
    print("Data Science Central news list:", news_list)  # Debugging line
    return news_list

def display_news():
    news_list = scrape_kdnuggets() + scrape_datasciencecentral()
    
    if not news_list:
        print("No news articles found.")
        return
    
    combined_text = "\n\n".join([f"Title: {news['title']}\nSummary: {news['summary']}\nLink: {news['link']}" for news in news_list])
    
    print("Here's what's new in the world of data:\n\n" + combined_text + "\n\nStay curious, keep exploring, and let's parse the future together! – JSON Hutches")

display_news()  # Run the function to see the output
