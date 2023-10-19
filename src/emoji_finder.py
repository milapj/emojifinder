"""
Usage:
    emoji_finder.py <emoji_description>

Options:
    -h --help       Show this help message and exit

Arguments:
    <emoji_description> A description of the emoji

Example:
    emoji_finder.py "A similing face with sunglasses"

"""

import re
import os
from bs4 import BeautifulSoup
import urllib3
from docopt import docopt

lookup = {}
raw_data = []
with open('resources/basic-emoji-seq.txt') as file:
    line = file.read().replace(' ', '')
    raw_data = line.split('\n')

for item in raw_data:
    unicode = re.match(r'(^[\d+A-Z]+)', item)
    desciption = re.search(r'([a-z]+)#', item)
    if unicode and desciption:
        lookup[desciption.group(1)] = unicode.group(1).replace('FE0F','')

arguments = docopt(__doc__)
user_emoji_description = arguments['<emoji_description>']
print(lookup)
for emoji, unicode in lookup.items():
    if emoji == user_emoji_description:
        unicode = r'\U000' + unicode
        code_point = int(unicode[4:], 16)
        print(f"{chr(code_point)} -> {unicode}")
       