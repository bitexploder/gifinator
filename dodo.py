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
    
def task_make_yaml():
    def _make_yaml(emoji):
        s = ''
        s += 'title: one emoji\n'
        s += 'emojis:\n'
        s += '  - name: {}\n'.format(emoji)
        s += '    src: /tmp/download_resize.gif'
        s += '\n'

        print(emoji)
        
        with open('/tmp/upload.yaml', 'w') as f:
            f.write(s)

        return True
    
        
    return {
        'actions': [(_make_yaml, )],
        'params':[{'name':'emoji',
                   'default':'',
                   'short':'e',
                   'long':'emoji',
                   'help':'Emoji name'}],
        'verbosity':2        
    }

# class EmojiImporter(object):

#     def __init__(self, slack_team=None, slack_email=None, slack_pass=None):
#         self.slack_team = slack_team or os.environ.get('SLACK_TEAM')
#         self.slack_email = slack_email or os.environ.get('SLACK_EMAIL')
#         self.slack_pass = slack_pass or os.environ.get('SLACK_PASS')

#         if not all((self.slack_team, self.slack_email, self.slack_pass)):
#             raise ValueError(
#                 'Make sure to set SLACK_TEAM, SLACK_EMAIL and SLACK_PASS '
#                 'environment variables')

#         self.emojis = []

#     def get_all_the_things(self):
#         req = requests.get('https://www.hipchat.com/emoticons')
#         soup = BeautifulSoup(req.content)
#         divs = soup.findAll('div', {'class': 'emoticon-block'})

#         for div in divs:
#             name = div.text.strip()[1:-1]
#             img = div.find('img')
#             img_url = img.attrs['src']
#             filepath = download_file(img_url, filedir='/tmp/emojis')
#             emoji = Emoji(name, filepath)
#             self.emojis.append(emoji)
#             print('Downloaded: {}...'.format(emoji))

#     def login(self):
#         print('logging in...')
#         self.browser = Browser('chrome')
#         browser = self.browser
#         print('got browser...')

#         url = 'https://{}.slack.com/?redir=/customize/emoji'
#         url = url.format(self.slack_team)
#         browser.visit(url)

#         print('ok')

#         browser.fill('email', self.slack_email)
#         browser.fill('password', self.slack_pass)

#         print ('ok2')
        
#         keep_me = browser.find_by_name('remember')[0]
#         keep_me.uncheck()

#         print('ok3')
        
#         sign_in = browser.find_by_id('signin_btn')[0]
#         sign_in.click()

#         print('ok4')

#     def deal_with_it(self, emoji):
#         browser = self.browser

#         def fill_and_submit(emoji):
#             browser.fill('name', emoji.name)
#             browser.fill('img', emoji.imagepath)
#             submit = browser.find_by_value('Save New Emoji')[0]
#             submit.click()
#             time.sleep(1 + random.randrange(1, 20) / 10)

#         fill_and_submit(emoji)
#         errors = browser.find_by_css('.alert.alert_error')
#         for error in errors:
#             if 'There is already an emoji named' in error.text:
#                 # for now appending 2 to emoji name and trying again
#                 emoji.name += '2'
#                 fill_and_submit(emoji)
#                 errors = browser.find_by_css('.alert.alert_error')
#                 if errors:
#                     return False

#         success = browser.find_by_css('.alert.alert_success')
#         for s in success:
#             if 'Your new emoji has been saved' in s.text:
#                 return True

#     def yougotitdude(self):
#         if getattr(self, 'browser', False):
#             self.browser.quit()
            
# class Emoji(object):

#     def __init__(self, name, imagepath):
#         self.name = name
#         self.imagepath = imagepath

#     def __str__(self):
#         return '{} - {}'.format(self.name, self.imagepath)

#     def __repr__(self):
#         return str(self)

# def task_emoji_upload():
#     def _emoji_upload():
#         emoji = Emoji('goat98', '/tmp/download_resize.gif')
        
#         ei = EmojiImporter("carvesystems",
#                            "jeremy.allen@carvesystems.com",
#                            "pantie-mattinss-schemata-jersey")
#         ei.login()
#         ei.deal_with_it(emoji)
        
        
#     return {
#         'actions':[_emoji_upload],
#         'verbosity':2
#     }
