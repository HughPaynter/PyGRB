import os
import urllib.request
import numpy as np

from bs4 import BeautifulSoup
from os.path import join, exists


def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        pass


class GetSWIFTBurst():
    """
    A class to download SWIFT_BAT bursts.

    Parameters
    ----------
    trigger : integer
        The BAT trigger number.

    """

    def __init__(self, trigger, id):



        self._base_string = 'https://swift.gsfc.nasa.gov/results/batgrbcat/'
        self._trigger = trigger
        self._id = id
        self._root = f'data/SWIFT/'
        if len(self._id) == 6:
            self._id = "00" + self._id + "000"
        else:
            self._id = self._id
        self._file_name = f'{self._id}.lc.gz'
        self._url = self._make_url()

        mkdir(self._root)
        self.download_file()

    def _make_url(self):
        """
        Takes the trigger number and find the correct subfolder on the NASA
        server.


        Returns
        -------
        url : string
            Returns the url to the desired trigger folder on the NASA server.

        """

        return f'{self._base_string}/{self._trigger}/data_product/{self._id}/bat/rate/sw{self._id}brtmc.lc.gz'

    def download_file(self):
        """
        Concatenates the trigger folder url with the filename of the required
        datatype and requests the file from the NASA server.
        """
        path = join(self._root, self._file_name)
        if not exists(path):
            remote = f'{self._url}'
            try:
                urllib.request.urlretrieve(remote, path)
            except:
                raise FileNotFoundError(
                    f'The file:  << {self._file_name} >>  '
                    f'does not exist at the specified url:\n'
                    f'{remote}'
                    f'This trigger has either been deleted, or is not a burst.')
        self.path = path


if __name__ == '__main__':
    pass
