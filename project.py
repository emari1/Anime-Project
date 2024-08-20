
from pprint import pprint
import requests
import os
from pyfiglet import Figlet
import urllib.parse
figlet=Figlet(font='slant')
print(figlet.renderText('Anime'))
print('Welcome to Anime Application')


def main():

    while True:
        print('Which function would you like to use?')
        print('''
        1. Anime Search
        2. Anime Reverse Image Search
        ''')
        selection=int(input())
        match selection:
            case 1:
                getAnime()
                break
            case 2:
                function_2()
                break
            case _:
                continue



def getAnime():
    print('hello')



def function_2():
    font2=Figlet(font='doom')
    print(font2.renderText('Welcome to Anime Images'))
    print("You can use this function to reverse Image search a scene of an anime through the use of JPEG or the use of URL")
    print('Choose URL or JPEG to start')
    choice=input().lstrip().rstrip().lower()
    if choice=='url':
        while True:
            url=input('Please input the url')
            url.lstrip().rstrip().lower()
            if url.startswith('https'):
                response=requests.get("https://api.trace.moe/search?url={}"
                     .format(urllib.parse.quote_plus(f"{url}"))
                     ).json()
                aniList=response['result'][0]['anilist']
                print(aniList)
                anime_link=f'https://anilist.co/anime/{aniList}'
                getAnimeInner(aniList)
                print('This is the anime link '+anime_link)
                break
            else:
                continue
    elif choice=='jpeg' or choice=='jpg':
        print('work in progress')
    else:
        print('Incorrect Type has been used')



def getAnimeInner(ani_id):
    query = '''
    query ($id: Int) { # Define which variables will be used in the query (id)
      Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
          romaji
          english
          native
        }
      }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'id': ani_id
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    name=response['data'][0]['title']['romaji']
    print(name)


if __name__ == "__main__":
    main()
