# explore
# make a programm to show daily news
# programm must contain
# 1- print headlines & give an option to read more on that news with detail 

from newsapi import NewsApiClient
import pycountry
import text_speech as tx
# import choose as ch

tx.text_to_speech("welcome to the news fetcher")

newsapi = NewsApiClient(api_key='ec6e90ed7e134c3690fcba3748c3d716')

while True:
    input_country = input("Enter name of the country: ")
    input_counties = [f'{input_country.strip()}']
    countries = {}

    for country in pycountry.countries:
        countries[country.name] = country.alpha_2

    codes = [countries.get(country.title(), 'Unknown code') 
             for country in input_counties]
    option = input("Which category are you intrested in ?\n1- Business\n2- Entertainment \n3- General \n4- Health \n5- Science \n6- Technology \n\n Enter here → ")

    topHeadlines = newsapi.get_top_headlines(category=f'{option.lower()}', language='en' , country=f'{codes[0].lower()}')

    Headlines = topHeadlines['articles']

    if Headlines:
        for i, articles in enumerate(Headlines):
            b = articles['title'][::-1].index("-")
            if "news" in (articles['title'][-b+1:]).lower():
                print(f"{i+1}. {articles['title'][-b+1:]}: {articles['title'][:-b-2]}")
            else:
                print(f"{i+1}. {articles['title'][-b+1:]} News: {articles['title'][:-b-2]}")
        
        while True:
            read_more_choice = input("Do you want to read more about a specific news? (Yes/No): ")
            if read_more_choice.lower() == 'yes':
                news_index = int(input("Enter the number of the news you want to read: "))
                if 1 <= news_index <= len(Headlines):
                    selected_article = Headlines[news_index - 1]
                    print(f"\n{selected_article['title']}\n\n{selected_article['description']}\n\n{selected_article['url']}\n")
                    break
                else:
                    print("Invalid news number. Please enter a number within the range.")
            elif read_more_choice.lower() == 'no':
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

    else:
        print(f"Sorry no articles found for {input_country}, Something Wrong!!!")
    option = input("Do you want to search again[Yes/No]?")
    if option.lower() == 'yes':
        continue
    else:
        exit()