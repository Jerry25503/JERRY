from urllib import response

import mechanize

import os

import datetime

import getpass

import time

import sys, requests

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)



url = 'https://m.facebook.com/login'



def clear():

    if os.name == 'nt':

        os.system('cls')

    else:

        os.system('xdg-open https://www.facebook.com/Mr.Raja6970')



def sp(stri):

    for letter in stri:

        print(letter, end = "")

        sys.stdout.flush()

        sleep(0.03)


os.system('clear')
logo ="""\033[1;37mWELCOME TO CHAND COMMAND

\033[1;30m
                  ▉▉▉▉
                 ▂▉▉▉▉▂
                \033[1;33m╰▏ ┛┗ ▕╯
                 ╲ 👅 ╱
                 \033[1;32m╱▔╲╱▔╲
               ╱ ╱▏╭╮▕╲ ╲
               ╲ ╲▏╭╮▕╱ ╱       \033[1;31m╔═╗  ╔╦╗  ╔═╗
                \033[1;35m ╲▉▉▉▉╱         \033[1;34m╠═╣   ║   ╠╣
                \033[1;34m  ▏╭╮▕          \033[1;32m╩ ╩   ╩   ╚  
                \033[1;34m  ▏▏▕▕
                  ▏▏▕▕
                \033[1;31m ╭╰ ╮╭╰ ╮
               \033[1;39msᴜʙ \033[1;35mᴋᴀ \033[1;36mʙᴀᴀᴘ
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0;92m
 \033[1;31m.██████╗██╗  ██╗ █████╗ ███╗   ██╗██████╗ 
\033[1;32m.██╔════╝██║  ██║██╔══██╗████╗  ██║██╔══██╗
\033[1;33m.██║     ███████║███████║██╔██╗ ██║██║  ██║
\033[1;34m.██║     ██╔══██║██╔══██║██║╚██╗██║██║  ██║
\033[1;35m.╚██████╗██║  ██║██║  ██║██║ ╚████║██████╔╝
 \033[1;36m.╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 
 
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍    \033[1;39m◈✙◈\033[1;33m MR CHAND 
\033[1;39m━▷ \033[0;91m𝙏𝙀𝘼𝙈     \033[1;39m◈✙◈\033[1;31m TEAM OF ATF
\033[1;39m━▷ \033[0;91m𝙔𝙊𝙐𝙏𝙐𝘽𝙀  \033[1;39m◈✙◈ \033[1;32mCHAND TRICKER
\033[1;39m━▷ \033[0;91m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 \033[1;39m◈✙◈ \033[1;33mfb.com/CH4ND.CH4ND
\033[1;39m━▷ \033[0;91m𝙁𝘽 𝙂𝙍𝙊𝙐𝙋 \033[1;39m◈✙◈ \033[1;34mFACEBOOK ZONE 🙂🙈
\033[1;39m━▷ \033[0;91m𝙎𝘼𝙏𝙐𝙏𝘼𝙎  \033[1;39m◈✙◈ \033[0;92mFREE AND ENJOY
\033[1;39m━▷ \033[0;91m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \033[1;39m◈✙◈ \033[1;37m3.0
\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍    \033[1;39m◈✙◈\033[1;31m OFFLINE ERROR SOLVE
\033[1;39m━▷ \033[1;36m𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝘾𝙃𝘼𝙉𝘿 𝙊𝙒𝙉𝙀𝙍 𝙊𝙁 𝘼𝙏𝙁
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●"""
os.system('clear')
logo2 ="""\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑
\033[1;37mWELCOME TO CHAND COMMAND

\033[1;31m╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  
║║║║╣ ║  ║  ║ ║║║║║╣   
╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝  


\033[1;32m╔╦╗╔═╗
 ║ ║ ║
 ╩ ╚═╝
 
 
\033[1;33m╔═╗╔╦╗╔═╗
╠═╣ ║ ╠╣ 
╩ ╩ ╩ ╚  


\033[1;35m╔╦╗╔═╗╔═╗╦  
 ║ ║ ║║ ║║  
 ╩ ╚═╝╚═╝╩═╝
 
 \033[1;31mOWNER \033[1;32mTOOL \033[1;33mOF \033[1;37mMR \033[1;35mCHAND 

\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑"""
def approval():

  os.system('git pull')

  time.sleep(1)

  uuid = str(os.geteuid())+"DS"+str(os.geteuid())

  id = "CH4ND-TRICKER-"+"".join(uuid)

  os.system('clear')

  print(logo)

  sp("\033[1;39m━▷ You Get Approved for Using Command  Paid Tool 350 Per month \033[1;37m")

  print("\n\033[1;39m━▷ Your Key :\u001b[36m "+id);time.sleep(0.1)

  print ("""\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑""")

  try:

    httpCaht = requests.get("https://github.com/Jerry25503/JERRY/blob/main/atf.py").text

    if id in httpCaht:

      sp("\n\033[1;39m━▷ Congrats You get approved successful And Enjoy")

      msg = str(os.geteuid())

      time.sleep(1)

      pass

    else: 

      sp("\n\033[1;39m━▷ Your Key Not approved please  Say to Admin");

      time.sleep(0.1)

      input('\n\nWHEN YOU BUY TOOL THEN ENTER PRESS')

      tks = ('Hello%20Chand%20Sir%20!%20Please%20Approve%20My%20Key%20This%20My%20Key%20:%20'+id);os.system('am start https://wa.me/+923017787729?text='+tks),approval()

      time.sleep(1)

      exit()

  except Exception as e:

     print(e)

     sp(" >> Unable Data From Server ")

     time.sleep(2)

     exit()


print(logo2)
attemps = 0

while attemps < 12345677901:

    username = input('\n\n\033[1;37mEnter username: ')

    password = input('\033[1;37mEnter password: ')



    if username == 'JERRY' and password == 'JERRY1122':

        print('You have successfully logged in.')

        break

    else:

        print('Incorrect Password ')

        attemps += 1

        continue

os.system('clear')



def login():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = USERNAME

    browser.form['pass'] = PASSWORD

    r = browser.submit()

    f = open("login.html", "wb")

    f.write(r.read())

    f.close()

    browser.select_form(nr = 0)

    print("\033[1m\033[36m", end = "")

    print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
    sp("\033[1;31m[?]\033[0;95m \033[1;37mEnter the Two Factor code \n")
    print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
    apr = str(input('\033[1;31m[?] \033[1;37mEnter Code : '))

    try:

        browser.form['approvals_code'] = apr

    except mechanize._form_controls.ControlNotFoundError:

        print("Wrong password or some shit, check generated file")

        f = open("epage_" + str(USERNAME) + ".html", "wb")

        f.write(r.read())

        f.close()

        exit(1)

    r = browser.submit()

    browser.select_form(nr = 0)

    try:

        browser.form['name_action_selected'] = ['save_device']

    except mechanize._form_controls.ControlNotFoundError:

        print("Some shit gone down, check generated file")

        f = open("epage_" + str(USERNAME) + ".html", "wb")

        f.write(r.read())

        f.close()

        exit(1)

    r = browser.submit()

    f = open("full_login_" + str(USERNAME) + ".html", "wb")

    f.write(r.read())

    f.close()



def findtextchat(curl):

    r = browser.open(curl)

    x = browser.title()

    if x == "Review recent login":

        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")

        exit(1)

    if x == "Login approval needed":

        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")

        exit(1)

    if x == "Epsilon":

        print("\nYour account got locked, recover it kindly and re run the script.")

        exit(1)



def sendtextconvo(comment):

    try:

        browser.select_form(nr = 1)

    except mechanize._mechanize.FormNotFoundError:

        print("Some error occured while finding text area, please check your account")

        exit(1)

    try:

        browser.form['body'] = comment

    except mechanize._form_controls.ControlNotFoundError:

        print("Some error occured while filling text, please check your account")

        exit(1)

    r = browser.submit()

    e = datetime.datetime.now()

    print("\033[1;32m",end = "")

    print (e.strftime("\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\n\033[1;32mMESSEGE SEND SUCCESSFUL ✅ \n \033[1;35mDate - %d/%m/%Y ⏪  \n\033[1;33mTime - %I:%M:%S %p ⏱️\n\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑"))
    print(" \033[1;32mDONE SENDING✅ \033[1;39m", hater, line, "\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● \n")



approval()

os.system('clear')

print("\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●")

print("\033[1;33;40m", end = "")

print(logo)

print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
sp('\n\033[1;37m◑\033[1;36m𝐒𝐔𝐁𝐂𝐑𝐈𝐁𝐄\033[1;37m◑\033[1;31m𝐌𝐘\033[1;37m◑\033[1;32m𝐘𝐎𝐔𝐓𝐔𝐁𝐄\033[1;37m◑\033[1;33m𝐂𝐇𝐀𝐍𝐍𝐀𝐋\033[1;37m◑\033[1;34m𝐅𝐎𝐑\033[1;37m◑\033[1;35m𝐀𝐋𝐋\033[1;37m◑\033[1;39m𝐅𝐑𝐄𝐄\033[1;37m◑\033[1;34m𝐓𝐎𝐎𝐋𝐒\n\n')
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
print('\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
sp("\033[1;39m[+] \033[1;39m𝗟𝗢𝗚𝗜𝗡 𝗙𝗕 𝗜𝗗 𝗧𝗬𝗣𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 & 𝗘𝗠𝗔𝗜𝗟 𝗔𝗡𝗗 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 \n")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
USERNAME = str(input('\033[1;31m[+] \033[1;37m𝗧𝗬𝗣𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 & 𝗘𝗠𝗔𝗜𝗟  : '))
print("\033[1;33;40m", end = "")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
sp("\033[1;39m[+] \033[1;32m𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 \n")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
PASSWORD = str(input('\033[1;31m[?] \033[1;37m𝗧𝗬𝗣𝗘 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : '))
os.system('xdg-open https://youtube.com/@chandtricker436')
login()
print("\033[1;34;40m", end = "")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
sp("\033[1;31m[?] \033[1;37mEnter Chat/inbox Link\n")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
cid = str(input('\033[1;31m[?] \033[1;37mEnter Link : '))
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
sp("\033[1;31m[?] \033[1;37mEnter File Name\n")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
np = str(input('\033[1;31m[?] \033[1;37mEnter File Name : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
sp("\033[1;31m[?] \033[1;37mEnter The Time Delay In Seconds\n")
print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
t = int(input('\033[1;31m[?] \033[1;37mEnter Time : '))

f = open(np, 'r')

lines = f.readlines()

f.close()

print("\033[1;33;40m", end = "")

print('\033[1;31m[+]\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')

hater = input('\033[1;37m[+] \033[1;37mHaters Name : ')

print("\033[1;33;40m", end = "")

print('\033[1;31m[+]\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')

sp("\033[1;32m[?] \033[1;37mEnter The Time In Seconds\n")

print('\033[1;31m[+]\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')

t = int(input('\033[1;32m[?] \033[1;33mEnter Time : '))



os.system('clear')

print(logo)



count = 0

while True:

    try:

        for line in lines:

            if len(line) > 3:

                if count != 0:

                    sleep(t)

                findtextchat(curl)

                sendtextconvo(hater + line)

                count += 1

                if count % 10 == 0:

                    sleep(1)

                    clear()

                    print("\033[1;32m")

    except Exception as e:

        print(e)

        sleep(3)
