import argparse
import logging
import os
import platform
import subprocess
import sys
from configparser import ConfigParser

handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

path_conf = os.path.join(os.getcwd(), "config.ini")
encoding = 'UTF-8'
section = 'general'
folder = 'Scripts' if platform.system() == 'Windows' else 'bin'
python = 'python' if platform.system() == 'Windows' else 'python3'


def __set_config_option(name_option: str):
    """Добавить опцию в конфиг
    :param name_option: название опции
    """

    config = ConfigParser()
    if os.path.isfile(path_conf):
        config.read(path_conf, encoding=encoding)
    if not config.has_section(section):
        config.add_section(section)
    if name_option == 'path_tests':
        path_tests = input('Укажите путь до репозиториев с тестами: ')
        config.set(section, name_option, path_tests)
    elif name_option == 'path_env':
        path_env = input('Укажите путь до виртуального окружения: ')
        config.set(section, name_option, path_env)
    elif name_option == 'main_product':
        product = input('Укажите основной продукт для работы: ')
        config.set(section, name_option, product)

    with open(path_conf, 'w', encoding=encoding) as config_file:
        config.write(config_file)


def __get_config_option(name_option: str, required_option: bool = True):
    """Получить опцию из конфига
    :param name_option: название опции
    :param required_option: обязательная ли опция конфига для работы
    """

    config = ConfigParser()
    option = ''
    while True:
        config.read(path_conf, encoding=encoding)
        if config.has_option(section, name_option):
            option = config.get(section, name_option).replace('\\', '/').replace('~', os.path.expanduser('~'))
            if option:
                return option
        if not required_option:
            return option
        __set_config_option(name_option)


def __get_products():
    """Получить информацию о продуктах"""

    path_tests = __get_config_option('path_tests')
    products = {
        'uatf':
            {
                'Repo': 'https://github.com/UATCO/uatf.git',
                'Path': f'{path_tests}/uatf',
            },
        'big_geek_tests':
            {
                'Repo': 'https://github.com/UATCO/big_geek_tests.git',
                'Path': f'{path_tests}/big_geek_tests',
            }
    }
    return products


def clone():
    """Выкачать репозитории"""

    product_name = __get_config_option('main_product')
    products = __get_products()
    path = __get_config_option('path_tests')
    repo = products[product_name]['Repo']
    if not os.path.exists(products[product_name]['Path']):
        subprocess.run(f'git clone {repo}', cwd=path, shell=True)

    #накатываем uatf
    repo = products['uatf']['Repo']
    subprocess.run(f'git clone {repo}', cwd=path, shell=True)


def create_venv():
    """Создать виртуальное окружение"""

    path_env = os.path.join(__get_config_option('path_tests'), __get_config_option('main_product'), 'venv')
    subprocess.run(f'{python} -m venv --system-site-packages {path_env}', shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clone/update/checkout repositories')
    parser.add_argument('-clone', action='store_true', help='Clone repositories')
    parser.add_argument('-create_venv', action='store_true', help='Create venv')
    # parser.add_argument('-reqs', action='store_true', help='Install requirements')
    # parser.add_argument('-checkout', type=str, help='Checkout branches')
    # parser.add_argument('-pull', action='store_true', help='Pull branches')
    args = parser.parse_args()
    if args.clone:
        clone()
    if args.create_venv:
        create_venv()
    # if args.reqs:
    #     install_requirements()
    # if args.checkout:
    #     checkout(args.checkout)
    # if args.pull:
    #     pull()
