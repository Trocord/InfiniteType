import requests
from art import *
from colorama import *

print(Fore.MAGENTA + '')
tprint('InfiniteType')
print('-------------------------> By iTrojang <-------------------------')
print()
channel = input('[InfinteType]Enter Channel ID >> ')

token = 'OTYzMDY2NjY1MjA0MDg0NzM2.Gc3n3K.743zAqvacPb2TLJTzUIwitEuospDnPnVE1E-4k'
#https://discord.com/api/v9/channels/965651238790250529/typing

while True:
    headers = {
        'authorization': token
    }
    requests.post(f'https://discord.com/api/v9/channels/{channel}/typing',headers=headers)