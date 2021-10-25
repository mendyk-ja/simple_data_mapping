import requests
import json
import time
from models import Article
from typing import List, Optional
import json
from datetime import datetime

# w zasadzie to wszystko działa jk było wymagane w opisie, najlepiej nie ruszać i zrobić backup.
# pozostało dodać  projekt na gita, zrobić readme i opisać jak uruchomić projekt
# jak już będzie wersja ostateczna to trzeba tez zmienić na 5 minut zamiast 10 sekund

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
            print(already_checked)

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
        print(articles[element])

    time.sleep(10)







        #article_data = parse_json[1]
        #print(article_data)

    # article_details_response = requests.get(f'https://mapping-test.fra1.digitaloceanspaces.com/data/articles/'
    #                                         f'{article_id}.json')
    # article_details_text = article_details_response.text
    # article_details_dict = json.loads(article_details_text)
    #print(article_details_dict)
    # print(type(article_details_dict))
    # article_media_response = requests.get(f'https://mapping-test.fra1.digitaloceanspaces.com/data/media/'
    #                                       f'7793136.json')
    # article_media_text = article_media_response.text
    # article_media_dict = json.loads(article_media_text)

    #article_media_dict jest listą słowników
    #print(article_media_dict)
    # parse_json2 = json.loads(article_media)
    # print(parse_json1)

    # def merge(parse_json, parse_json1, parse_json2):
    #     return [a + b + c for (a, b, c) in zip(parse_json, parse_json1, parse_json2)]
    # print(merge(parse_json, parse_json1, parse_json2))

    # for article1, article2, article3 in parse_json[], parse_json1[], parse_json2[]:
    #     parse_json3 = [{key: value for (key, value) in (article1.items() + article2.items() + article3.items())}]
    #     print(parse_json3)
    # złączenie słowników w jeden aby wpisac je jako jeden do klasy
    # merged = {**article_data, **article_details_dict}
    # print(merged)



            # {key: value for (key, value) in (parse_json[x].items() + parse_json2[x].items() + parse_json2[x].items())}


    #     for article1, article2, article3 in parse_json, parse_json1, parse_json2:
    #         parse_json3 = {key: value for (key, value) in (article1.items() + article2.items() + article3.items())}
    #          print(parse_json3)
    #

    # # print(articles[0])
    # # print(article_id)
    # print(article_details)
    # print(article_media)

    # Makes loop to wait 10 seconds

    # active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
    # print(active_case)

# Sprawdzić czy jeden słownik zawierający pola możemy w ogóle wgrać do klasy Article
# Przygotować dane z jsona tak, aby było możliwe przekazanie ich do bazy
# Media są w liście słowników czyli trzeba te wszystkie słowniki zmerdzować
# wszystkie informacje do bazy znajdują się w drugim api czyli article_details

# ok, czyli teraz muszę tylko podmienić nazwy dwóch zmiennych - "url" i "publication_date"