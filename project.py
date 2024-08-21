from tkinter import Image

from AnilistPython import Anilist
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
    font=Figlet(font='contessa')
    print(font.renderText('Welcome to Anime Search'))
    anilist=Anilist()
    anime=input('Type the show of the anime that you want\n')
    anilist.print_anime_info(anime)



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
                anime_link=f'https://anilist.co/anime/{aniList}'

                print(f'The anime from this image is ',end="")
                anime_name=getAnimeInner(aniList)
                print('This is the anime link '+anime_link)
                break
            else:
                continue
    elif choice=='jpeg' or choice=='jpg':
        file_name=input('Please input the file name')
        file_name=file_name.lstrip().rstrip().lower()
        file_type=['.jpeg','.jpg']
        while True:
            if file_name in file_type:
                im=Image.open(file_name)
                response = requests.get("https://api.trace.moe/search?url={}"
                                        .format(urllib.parse.quote_plus(f"{im}"))
                                        ).json()
                aniList = response['result'][0]['anilist']
                anime_link = f'https://anilist.co/anime/{aniList}'

                print(f'The anime from this image is ', end="")
                anime_name = getAnimeInner(aniList)
                print('This is the anime link ' + anime_link)
                break
            else:
                continue



    else:
        print('Incorrect Type has been used')



def getAnimeInner(ani_id):

    anilist = Anilist()
    anime_dict = anilist.get_anime_with_id(ani_id)
    anime_name = anime_dict['name_english']
    print(anime_name)
if __name__ == "__main__":
    main()
