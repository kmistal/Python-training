from io import BytesIO
from PIL import Image
import requests
import subprocess
import platform
from os import path, getcwd, mkdir


def run_lolcat_factory():
    cats_path = getcwd() + '/cats'

    print_header()
    create_cats_directory(cats_path)
    download_cats(cats_path)
    open_cats_directory(cats_path)


def print_header():
    print('------------------------')
    print('     LOLCAT FACTORY     ')
    print('------------------------')


def create_cats_directory(cats_path):
    if not path.isdir(cats_path):
        mkdir(cats_path)


def download_cats(cats_path):
    print('Contacting cat service for cat pictures...')
    cats_to_download = 2
    for i in range(cats_to_download):
        cat_image = fetch_cat(i + 1)
        save_image(i + 1, cat_image, cats_path)


def open_cats_directory(cats_path):
    if platform.system() == 'Darwin':
        subprocess.call(['open', cats_path])
    elif platform.system() == 'Windows':
        subprocess.call(['start', cats_path])
    else:
        subprocess.call(['xdg-open', cats_path])


def save_image(id, image, cats_path):
    file_name = cats_path + '/cat_{}'.format(id) + '.jpg'
    image.save(file_name, "JPEG", quality=80, optimize=True, progressive=True)


def fetch_cat(id):
    print('Downloading cat {}...'.format(str(id)), end=' ', flush=True)
    cats_url = 'https://consuming-python-services-api.azurewebsites.net/cats/random'
    try:
        req = requests.get(cats_url)
        cat_image = Image.open(BytesIO(req.content))
        print('Done')
        return cat_image
    except Exception as error:
        print('Error')
        print(error)


if __name__ == "__main__":
    run_lolcat_factory()
