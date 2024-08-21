
from AnilistPython import Anilist
anilist = Anilist()

anime_dict = anilist.get_anime_with_id(126830) #Code Geass
print(anime_dict)