"""
Data model for comic's which are available on https://xkcd.com
"""

from resources.base import ResourceBase
from utils.fetch_data import hit_url


# REFERENCE CODE
# def comic():
#     comic_id = int(input(f"Which Comic id Data You Want :- "))
#     return comic_id


class RComics(ResourceBase):
    """
    Comics related functionality
    """
    def __init__(self):
        super().__init__()
        self.relative_url = "/{}/info.0.json"

    def get_title(self, comic_id=1):
        comic_id = int(input("Which Comic id title you want:- "))
        complete_url = self.home_url + self.relative_url.format(comic_id)
        response = hit_url(complete_url)
        res_data = response.json()
        title_name = res_data.get("title")
        return title_name

    def get_sample_data(self, comic_id=1):
        comic_id = int(input("Which Comic id data you want:- "))
        complete_url = self.home_url + self.relative_url.format(comic_id)
        response = hit_url(complete_url)
        res_data = response.json()
        return res_data

    def get_image_url(self, comic_id=1):
        comic_id = int(input("Which Comic id image url you want:- "))
        complete_url = self.home_url + self.relative_url.format(comic_id)
        response = hit_url(complete_url)
        res_data = response.json()
        idea = res_data.get("img")
        return idea
