"""
Pydantic model for comics data coming from https://xkcd.com/{<comic_id>}/info.0.json
"""

from pydantic import BaseModel
from pprint import pprint


class Comics(BaseModel):
    """
    Data model for passing the data of comics in xkcd
    """
    month: str
    num: str
    link: str
    year: str
    news: str
    safe_title: str
    transcript: str
    alt: str
    img: str
    title: str
    day: str


if __name__ == "__main__":
    obj = {"month": "5",
           "num": 100,
           "link": "",
           "year": "2006",
           "news": "",
           "safe_title": "Family Circus",
           "transcript": "[[Picture shows a pathway winding through trees to a sink inside a house, out to some swings"
                         " and back to ths sink, out to a ball and back to the sink...]]\nCaption: Jeffy's ongoing "
                         "struggle with obsessive-compulsive disorder\n{{alt text: This was my friend David's idea}}",
           "alt": "This was my friend David's idea",
           "img": "https://imgs.xkcd.com/comics/family_circus.jpg",
           "title": "Family Circus",
           "day": "10"
           }

    data = Comics(**obj)
    pprint(data)
