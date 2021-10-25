import requests
import json
import time
from models import Article
from typing import List, Optional
import json
from datetime import datetime

# creating set for storage id of already displayed articles
already_checked = set()
# loop while is needed for 5 minutes' feature
while True:
    # gathering data from first endpoint
    list_of_articles_response = requests.get('https://mapping-test.fra1.digitaloceanspaces.com/data/list.json')
    # changing response into text
    list_of_articles = list_of_articles_response.text
    # extracting dictionaries from text
    parse_json = json.loads(list_of_articles)
    # creating empty list for merging dictionaries into one later
    list_of_details = []
    # looping through dictionaries from first endpoint
    for element in range(len(parse_json)):
        # from dictionaries extracting id of articles
        article_id = parse_json[element]['id']
        # checking if id hasn't been displayed already
        if article_id not in already_checked:
            # adding new id to the set
            already_checked.add(article_id)
            # gathering data from the second endpoint by creating link with article_id extracted before
            article_details_response = requests.get(f'https://mapping-test.fra1.digitaloceanspaces.com/data/articles/'
                                                    f'{article_id}.json')
            # changing response into text
            article_details_text_raw = article_details_response.text
            # adjusting keys from endpoint to keys from BaseModel
            article_details_text = article_details_text_raw.replace('"pub_date":', '"publication_date":')
            article_details_text = article_details_text.replace('"category":', '"categories":')
            # extracting dictionaries from text
            article_details_dict = json.loads(article_details_text)
            # changing data type from 'categories' to set
            article_details_dict['categories'] = {article_details_dict['categories']}
            # replace ; to : in time displaying
            article_details_dict['publication_date'] = article_details_dict.get("publication_date").replace(';', ':')
            # changing displaying time to datetime
            article_details_dict['publication_date'] = datetime.strptime(article_details_dict["publication_date"],
                                                                         '%Y-%m-%d-%H:%M:%S')
            # creating list with "banned" html tags
            banned_html_tags = ['<b>', '</b>', "\'", '<p>', '</p>', '<hr>', '<i>', '<a>', '<bold>']
            # looping through article sections
            for section in article_details_dict['sections']:
                # searching for "text" sections
                if 'text' in section:
                    # looping through tags in list with "banned" tags
                    for tag in banned_html_tags:
                        # replacing every tag with empty space
                        section['text'] = section.get('text').replace(tag, '')
            # endpoints don't contain links to articles so I've created ones
            article_details_dict['url'] = f'https://some.website/article/{article_id}.html'
            # adding dictionary from endpoint to the list in the end of getting through the loop
            list_of_details.append(article_details_dict)
    # writing data from list with dictionaries to the Article class
    articles: List[Article] = [Article(**item) for item in list_of_details]
    # displaying data from Article class about every article, which is stored
    for element in range(len(articles)):
        print(f"{articles[element]}\n")
    #waiting 5 minutes before going through while loop one again
    time.sleep(300)
