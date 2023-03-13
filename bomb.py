from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import requests

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)
            
while 1:
    system("cls||clear")
    print("""{}
      _       _   _    
     (_)     | | | |   
      _ _ __ | |_| | __
     | | '_ \| __| |/ /
     | | | | | |_|   < 
     |_|_| |_|\__|_|\_|  
    Sms : {}57 | by {}ParzivalTM\n                                                                                                               
    """.format(Fore.LIGHTRED_EX, Style.RESET_ALL, Fore.RED))
    try:
        print(Fore.LIGHTMAGENTA_EX + " \n [1] - SMS Gönder\n [2] - Proxy Scraper\n [3] - Çıkış\n\n")
        menu = (input(Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon Numarası : "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Gerek Yok): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"SMS Sayısı {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "SMS gönderme aralığı : "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nSMSler gönderildi! Enter'a basarak menüye dönebilirsin.")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "[1] - All")
        print(Fore.LIGHTRED_EX + "[2] - Http")
        print(Fore.LIGHTRED_EX + "[3] - Socks4")
        print(Fore.LIGHTRED_EX + "[4] - Socks5")
        proxymenu = input(Fore.LIGHTYELLOW_EX + "Seçim : ")
        f = open('Proxys.txt', 'wb')
        if proxymenu == "":
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
                sleep(3)
                continue
        elif proxymenu == 1:
            r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxymenu}&timeout=10000&country=all")
            f.write(r1.content)
            f.close()
            print(Fore.LIGHTRED_EX + "İşlem Bitti 3 saniye sonra menüye dönüceksiniz.")
            sleep(3)
        elif proxymenu == 2:
            r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all")
            f.write(r1.content)
            f.close()
            print(Fore.LIGHTRED_EX + "İşlem Bitti 3 saniye sonra menüye dönüceksiniz.")
            sleep(3)
        elif proxymenu == 3:
            r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
            f.write(r1.content)
            f.close()
            print(Fore.LIGHTRED_EX + "İşlem Bitti 3 saniye sonra menüye dönüceksiniz.")
            sleep(3)
        elif proxymenu == 4:
            r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
            f.write(r1.content)
            f.close()
        print(Fore.LIGHTRED_EX + "İşlem Bitti 3 saniye sonra menüye dönüceksiniz.")
        sleep(3)

    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
