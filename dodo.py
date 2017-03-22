"""
def task_py_params_list():
    def print_a_list(list):
        for item in list:
            print(item)
    return {'actions':[(print_a_list,)],
            'params':[{'name':'list',
                       'short':'l',
                       'long': 'list',
                       'type': list,
                       'default': [],
                       'help': 'Collect a list with multiple -l flags'}],
            'verbosity':2,
            }
"""

import requests
import shutil
import sys
import os
from bs4 import BeautifulSoup
from splinter.browser import Browser

def get_url(url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open('/tmp/download.gif', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return True
    else:
        return False
            
def task_download():
    def _download(url):
        status = get_url(url)
        return status

    return {
        'actions': [(_download, ),],
        'params':[{'name':'url',
                   'default':'',
                   'short':'u',
                   'long':'url',
                   'help':'Url to gifinate'}],
        'verbosity':2
    }

def task_gifinate():
    return {
        'actions': ['gifinator --path /tmp/download.gif --smallgif /tmp/download_resize.gif'],
        'verbosity':2
    }
    
