import argparse
import logging
import shutil
import os

from colorama import Fore, Back, Style
from glob import glob
from time import sleep

LOGGER = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description='Organizes files in your computer based on the file type you want to filter out.',
    prog='File organizer',
    epilog='2022 - Indigo Copyright'
    )
parser.add_argument(
    '-t',
    '--type',
    help='The file type you want the program to search for.',
    nargs='+',
    type=str
)
parser.add_argument(
    '-dir',
    '--directory',
    help='The directory where you want to organize',
    type=str,
    default=os.getcwd()
)
args = parser.parse_args()
# it should be a python script that can be invoked with arguments
default_filetypes= ['csv','pdf']
# pick file either csv or xls or xlsx

def program_entry():
    file_types = args.type
    directory_path =  args.directory
    if not file_types:
        print(Fore.RED + 'No args provided')
        sleep(1)
        print(Fore.GREEN + 'Do you want us to sort csv or pdf? Y | N')
        user_input = input()
        if user_input.lower() != 'y':
            return print(Fore.RED + 'System Exit')

    file_processor(file_types, directory_path)
        
def file_processor(file_type, directory_path):
    
    if not file_type:
        file_type = default_filetypes
    file_type.extend(default_filetypes)
    for file_ext in set(file_type):
        files = glob(os.path.join(directory_path, '*.{}'.format(
            file_ext
        )))
        print(Fore.CYAN + 'Found {} {} files'.format(
            len(files), file_ext
        ))
        new_folder = os.path.join(directory_path, '{}s Files'.format(
            file_ext
        ))
        try:
            os.makedirs('{}'.format(
                new_folder
            ))
            print(Fore.CYAN + 'New folder {} created'.format(
                new_folder
            ))
        except FileExistsError as e:
            pass
        for file in files:
            shutil.move(file, new_folder, copy_function=shutil.copy2)
            


if __name__ == '__main__':
    program_entry()