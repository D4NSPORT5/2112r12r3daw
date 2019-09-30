import requests, json, random, os
from colorama import Back, Fore, Style
s = '█'
phone = ''
viber = 'false'
whtsapp = 'false'
sms = 'false'
call = 'false'
vk = 'false'
#-------------------------------
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
#-------------------------------
#vk, viber
def zashita():
    global s
    print('''--------------------------------
ПРОГРАММА ДЛЯ ПРОВЕРКИ ПРОСЛУШКИ ТЕЛЕФОНА
Номер: '''+phone+'''
SSID: '''+str(random.randint(0, 9999999999))+'''
id: '''+str(random.randint(0, 99999)))
    if vk == 'false':
        print('Vk: false')
    else:
        print('Vk: '+Fore.GREEN+'TRUE'+Style.RESET_ALL)

    if viber == 'false':
        print('Viber: false')
    else:
        print('Viber: '+Fore.GREEN+'TRUE'+Style.RESET_ALL)

    if whatsapp == 'false':
        print('WhatsApp: false')
    else:
        print('WhatsApp: '+Fore.GREEN+'TRUE'+Style.RESET_ALL)
#Viber: '''+Fore.GREEN+'TRUE'+Style.RESET_ALL+'''
#WhatsApp: '''+Fore.GREEN+'TRUE'+Style.RESET_ALL)
    print('''--------------------------------
Ставить на следующие сервисы защиту?:''')
    if vk == 'false':
        pass
    else:
        print('Vk')
    if viber == 'false':
        pass
    else:
        print('Viber')

    if whatsapp == 'false':
        pass
    else:
        print('WhatsApp')

    otv = input('# ')

    for i in range(1, 20):
        i = '█'
        print(s)
        s+=i

    print('''--------------------------------
ЗАЩИТА ВКЛЮЧЕНА!''')
    if vk == 'false':
        pass
    else:
        print('На номер: '+phone+' поставлена защита для Vk')
    if viber == 'false':
        pass
    else:
        print('На номер: '+phone+' поставлена защита для Viber')

    if whatsapp == 'false':
        pass
    else:
        print('На номер: '+phone+' поставлена защита для WhatsApp')
    print('''--------------------------------''')
#-------------------------------
def proslushka():
    global s
    print('''--------------------------------
ПРОГРАММА ДЛЯ СОЗДАНИЯ ПРОСЛУШКИ ТЕЛЕФОНА
Номер: '''+phone+'''
SSID: '''+str(random.randint(0, 9999999999))+'''
id: '''+str(random.randint(0, 99999)))
    print('''--------------------------------
Поставить прослушку на след. сервисы?:''')
    if vk == 'false':
        pass
    else:
        print('Vk')
    if viber == 'false':
        pass
    else:
        print('Viber')

    if whatsapp == 'false':
        pass
    else:
        print('WhatsApp')
    otv = input('# ')

    for i in range(1, 20):
        i = '█'
        print(s)
        s+=i

    print('''--------------------------------
ПРОСЛУШКА ВКЛЮЧЕНА!''')
    if vk == 'false':
        pass
    else:
        print('На номер: '+phone+' поставлена прослушка для Vk')
    if viber == 'false':
        pass
    else:
        print('На номер: '+phone+' поставлена прослушка для Viber')

    if whatsapp == 'false':
        pass
    else:
        print('На номер: '+phone+' поставлена прослушка для WhatsApp')
    print('''--------------------------------''')
#-------------------------------
def prosluska_tela():
    global s
    print('''--------------------------------
ПРОГРАММА ДЛЯ ПРОВЕРКИ ПРОСЛУШКИ SMS И ЗВОНКОВ
Номер: '''+phone+'''
SSID: '''+str(random.randint(0, 9999999999))+'''
id: '''+str(random.randint(0, 99999)))
    if sms == 'false':
        print('SMS: false')
    else:
        print('SMS: '+Fore.GREEN+'TRUE'+Style.RESET_ALL)

    if call == 'false':
        print('CALL: false')
    else:
        print('CALL: '+Fore.GREEN+'TRUE'+Style.RESET_ALL)
    print('''--------------------------------
Поставить защиту на смс?''')
    otv = input('# ')

    for i in range(1, 20):
        i = '█'
        print(s)
        s+=i

    print('''--------------------------------
ЗАЩИТА ВКЛЮЧЕНА!
Телефон: '''+phone+''' защищен от прослушки смс
--------------------------------''')
#-------------------------------
print('''Какой способ наеба?
1) программа на проверку прослушки вайбера и вотсаппа
2) программа для созданиие прослушки
3) программа для проверки прослушки телефона''')
otv = str(input('#'))
if otv == '1':
    clear()
    print('номер?')
    phone = input('# ')
    print('Vk true or false?')
    vk = input('')
    print('Viber true or false?')
    viber = input('')
    print('WhatsApp true or false?')
    whatsapp = input('')
    clear()
    zashita()
elif otv == '2':
    clear()
    print('номер?')
    phone = input('# ')
    print('Vk true or false?')
    vk = input('')
    print('Viber true or false?')
    viber = input('')
    print('WhatsApp true or false?')
    whatsapp = input('')
    clear()
    proslushka()
elif otv == '3':
    clear()
    print('номер?')
    phone = input('# ')
    print('SMS true or false?')
    sms = input('')
    print('CALL true or false?')
    call = input('')
    clear()
    prosluska_tela()
else:
    clear()
    print('не понял')
