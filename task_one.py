"""
In this module we are fetching the data from xkcd and storing only title names in a list of str
User will also use this as a CLI
"""
import argparse
from utils.randgen import NumGen
from utils.time import timeit
from utils.fetch_data import hit_url


def get_url(comic_id):
    """
    Fetches the url

    :param comic_id: int
    :return: str
    """
    home_url = "https://xkcd.com"
    relative_url = "/{}/info.0.json"
    absolute_url = home_url + relative_url.format(comic_id)
    return absolute_url


@timeit
def main():
    """
    Returns only title names of comics
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=100)
    parser.add_argument("-l", "--limit", type=int, default=5)
    argument = parser.parse_args()
    print(f"Passed arguments :- \n {argument}")
    obj = NumGen(argument.start, argument.end, argument.limit)
    comics = [element for element in obj]
    print(f"Generating the data for `comic_ids` :- \n {comics}")

    title = []
    for comic_id in comics:
        print(f"[ INFO ] generating the data of comic_id :- {comic_id}")
        url = get_url(comic_id)
        response = hit_url(url)
        data = response.json()
        title.append(data.get("title"))
    return title


if __name__ == "__main__":
    print(main())
