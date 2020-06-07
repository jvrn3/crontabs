"""Move files from Download folder to specific folders

Downloads/*.mobi goes to ~/Documents/books/mobi/
Downloads/*.epub goes to ~/Documents/books/epub/
Downloads/*.pdf goes to ~/Documents/books/pdf/

"""

import re
import os

HOME = os.getenv("HOME")
DOWNLOADS_FOLDER = HOME +  "/" + "Downloads" + "/"
BOOKS_FOLDER = HOME + "/" + "Documents/books" + "/"

def get_file_extension(file_name):
    """

    """
    regex = re.compile(r'\.(mobi|epub|pdf)')
    return regex.search(file_name).group()[1::]

def move_files():
    """

    """
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


def main():
    move_files()

if __name__ == "__main__":
    main()
