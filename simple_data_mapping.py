import requests
import json
import time
from models import Article
from typing import List, Optional
import json
from datetime import datetime


already_checked = set()
while True:
    list_of_articles_response = requests.get('https://mapping-test.fra1.digitaloceanspaces.com/data/list.json')
    list_of_articles = list_of_articles_response.text
    parse_json = json.loads(list_of_articles)
    list_of_details = []
    for element in range(len(parse_json)):
        article_id = parse_json[element]['id']
        if article_id not in already_checked:
            already_checked.add(article_id)
            #print(already_checked)

            article_details_response = requests.get(f'https://mapping-test.fra1.digitaloceanspaces.com/data/articles/'
                                                    f'{article_id}.json')
            article_details_text_raw = article_details_response.text
            article_details_text = article_details_text_raw.replace('"pub_date":', '"publication_date":')
            article_details_text = article_details_text.replace('"category":', '"categories":')
            article_details_dict = json.loads(article_details_text)
            article_details_dict['categories'] = {article_details_dict['categories']}
            article_details_dict['publication_date'] = article_details_dict.get("publication_date").replace(';', ':')
            article_details_dict['publication_date'] = datetime.strptime(article_details_dict["publication_date"],
                                                                         '%Y-%m-%d-%H:%M:%S')
            banned_html_tags = ['<b>', '</b>', "\'", '<p>', '</p>', '<hr>', '<i>', '<a>', '<bold>']
            for section in article_details_dict['sections']:
                if 'text' in section:
                    for tag in banned_html_tags:
                        section['text'] = section.get('text').replace(tag, '')

            article_details_dict['url'] = f'https://some.website/article/{article_id}.html'
            list_of_details.append(article_details_dict)

    articles: List[Article] = [Article(**item) for item in list_of_details]
    for element in range(len(articles)):
        print(f"{articles[element]}\n")

    time.sleep(300)
