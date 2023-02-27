"""
This module specially dedicated for resources which we have to implement in some modules
"""


class ResourceBase:
    """
    Base class representing required methods to be implemented in resource class
    """
    def __init__(self):
        self.home_url = "https://xkcd.com"

    def get_title(self):
        raise NotImplementedError

    def get_sample_data(self):
        raise NotImplementedError

    def get_image_url(self):
        raise NotImplementedError
