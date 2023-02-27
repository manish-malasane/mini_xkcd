"""
In this module we are fetching the data from xkcd.com for each comic
In this module we also can fetch data for any 10 comics random resource urls by default
User will also use this as a CLI
"""

import argparse
from pprint import pprint
# Resource class
from datamodel.comic_model import Comics

# Pydantic model
from resources.r_comics import RComics

from utils.randgen import NumGen
from utils.fetch_data import hit_url
from utils.time import timeit
from task_one import get_url


def comic():
    """
    :return: Comic_title, Comic_Data, Comic_Url
                    of passed comic_id
    """
    comic_obj = RComics()
    title = comic_obj.get_title()
    print(f"Comic title :- \n {title}")

    comic_data = comic_obj.get_sample_data()
    comic_data = Comics(**comic_data)
    pprint(f"Comic data :- \n {comic_data}")

    image_url = comic_obj.get_image_url()
    print(f"Image url :- {image_url}")


def random_data():
    """
    Generates the data for any 10 comic id`s by default
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=700)
    parser.add_argument("-l", "--limit", type=int, default=10)
    argument = parser.parse_args()
    print(f"Passed arguments :- \n {argument}")
    obj = NumGen(argument.start, argument.end, argument.limit)
    comics = [element for element in obj]
    print(f"Generating the data for `comic_ids` :- \n {comics}")

    for comic_id in comics:
        print(f"[ INFO ] generating the data of comic_id :- {comic_id}")
        url = get_url(comic_id)
        response = hit_url(url)
        data = response.json()
        pprint(data)


@timeit
def main():
    random_data()
    comic()


if __name__ == "__main__":
    main()
