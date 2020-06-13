#!/usr/bin/python
"""Move files from Download folder to specific folders

Downloads/*.mobi goes to ~/Documents/books/mobi/
Downloads/*.epub goes to ~/Documents/books/epub/
Downloads/*.pdf goes to ~/Documents/books/pdf/

"""

import re
import os
from datetime import datetime
import logging

HOME = os.getenv("HOME")
DOWNLOADS_FOLDER = HOME +  "/" + "Downloads" + "/"
BOOKS_FOLDER = HOME + "/" + "Documents/books" + "/"
LOG_FILE = HOME + "/coding/crontabs/move_files.log"


def logger_config():
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        filename=LOG_FILE,
                        datefmt='%H:%M',
                        level='INFO')




def get_file_extension(file_name):
    """

    """
    regex = re.compile(r'\.(mobi|epub|pdf)')
    return regex.search(file_name).group()[1::]


def move_files():
    """

    """
    logger = logging.getLogger(LOG_FILE)
    regex = re.compile(r'^.*\.(mobi|epub|pdf)$')
    files_to_move = list(filter(lambda file_name:
                                regex.match(file_name),
                                os.listdir(DOWNLOADS_FOLDER)))

    def mv(file_name):
        # import ipdb; ipdb.set_trace()
        file_extension = get_file_extension(file_name)
        old_folder = DOWNLOADS_FOLDER + file_name
        new_folder = BOOKS_FOLDER + file_extension + '/' + file_name
        os.rename(old_folder, new_folder)


    [mv(file_name) for file_name in files_to_move]


    logger.info("Total files moved: {0}".format(len(files_to_move)))


def main():
    logger_config()
    move_files()


if __name__ == "__main__":
    main()

    logging.shutdown()
