import os

#alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890{}~_^[\\]|@?!<=>:;/.,-+*\"()'&`%$#"
alpha = "txiasvqf erwbphyugokdjnmzclABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}~_^[\\]|@?!<=>:;/.,-+*\"()'&`%$#"

title = "\x1b[38;5;226m  ____\x1b[38;5;190m  ____\x1b[38;5;154m  ____\x1b[38;5;082m  ____\x1b[38;5;083m  _  _\x1b[38;5;084m   ___\x1b[38;5;085m  ____\x1b[38;5;086m    __    \x1b[38;5;087m__   \n\x1b[38;5;226m (  _ \\\x1b[38;5;190m(_  _)\x1b[38;5;154m( ___)\x1b[38;5;082m(    )\x1b[38;5;083m( \( )\x1b[38;5;084m / __)\x1b[38;5;085m(_  _)\x1b[38;5;086m  /__\\\x1b[38;5;087m  (  )  \n\x1b[38;5;226m  ) _ (\x1b[38;5;190m _)(_\x1b[38;5;154m  )__)\x1b[38;5;082m | () |\x1b[38;5;083m )  (\x1b[38;5;084m ( (__\x1b[38;5;085m  _)(_\x1b[38;5;086m  /(__)\\\x1b[38;5;087m  )(__ \n\x1b[38;5;226m (____/\x1b[38;5;190m(____)\x1b[38;5;154m(__)\x1b[38;5;082m  (____)\x1b[38;5;083m(_)\_)\x1b[38;5;084m \___)\x1b[38;5;085m(____)\x1b[38;5;086m(__)(__)\x1b[38;5;087m(____)\n\x1b[38;5;226m                                          by CrazyKoustik\x1b[38;5;015m"

def delscrn():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

##encryption functions
def add(string, l1, l2):
	somme = (string.find(l1) + string.find(l2))%len(alpha)
	return alpha[somme]

def minus(string, l1, l2):
	diff = (string.find(l1) - string.find(l2))%len(alpha)
	return alpha[diff]

def encrypt_f(mess, key):
    if len(key) <= len(mess):
        quot = len(mess)//len(key)
        reste = len(mess)%len(key)
        keyf = ""
        for i in range(quot):
            keyf += key
        keyf += key[:reste]
    else:
        keyf = key[:len(mess)]
    encrypt = ""
    for ind in range(len(mess)):
        encrypt += add(alpha, mess[ind], keyf[ind])
    return encrypt

def decrypt_f(crypted, key):
	if len(key) <= len(crypted):
		quot = len(crypted)//len(key)
		reste = len(crypted)%len(key)
		keyf = ""
		for i in range(quot):
		    keyf += key
		keyf += key[:reste]
	else:
	    keyf = key[:len(crypted)]
	decrypt = ""
	for ind in range(len(crypted)):
	    decrypt += minus(alpha, crypted[ind], keyf[ind])
	return decrypt
##

def hide(text_to_hide, visibletext):
    invisible = ""
    string1 = strg[684:700]
    for car in str(text_to_hide):
        invisible += chr(int(str(ord(string1[2]))[0]+str(ord(string1[7]))[1:]+str(ord(string1[5]))[1]+str(3)+str(ord(string1[0]))[0]) + alpha.find(car))
    return (invisible + visibletext)

def extract(text_to_extract):
    extracted = ""
    string2 = strg[684:700]
    for car in text_to_extract:
        if ord(car) >= int(str(ord(string2[2]))[0]+str(ord(string2[7]))[1:]+str(ord(string2[5]))[1]+str(3)+str(ord(string2[0]))[0]) and ord(car) <= (int(str(ord(string2[2]))[0]+str(ord(string2[7]))[1:]+str(ord(string2[5]))[1]+str(3)+str(ord(string2[0]))[0])+ord(string2[2])-3):
            extracted += alpha[ord(car) - int(str(ord(string2[2]))[0]+str(ord(string2[7]))[1:]+str(ord(string2[5]))[1]+str(3)+str(ord(string2[0]))[0])]
    return extracted

while True:
    print(title)
    while True:
        cle = (str(input("\n\x1b[38;5;202m Choose an encryption key : \x1b[38;5;015m"))).encode("utf-8").decode("ascii", "ignore")
        strg = title[:] + "".join(100*[" "])
        if cle == "":
            print("\x1b[38;5;226m Minimum 1 character (ASCII)\x1b[38;5;015m")
            continue
        break
##
    delscrn()
    print(title)
    while True:
        print("\n\x1b[38;5;046m Choose an option : \n\x1b[38;5;226m  [1] Hide text\n\x1b[38;5;014m  [2] Extract text\n\x1b[38;5;202m  [3] Change encryption key\n\x1b[38;5;001m  [4] Quit\x1b[38;5;015m")
        opt = str(input("\x1b[38;5;046m Option n° : \x1b[38;5;015m"))
##option 1
        if opt == "1":
            while True:
                mess_invisible = (str(input("\n Text to hide : \x1b[38;5;093m"))).encode("utf-8").decode("ascii", "ignore")
                print("\x1b[38;5;015m")
                if mess_invisible == "":
                    continue
                break
            while True:
                mess_couverture = str(input(" Cover text (visible) : "))
                if mess_couverture == "":
                    continue
                break
            print("\n\x1b[38;5;046m Copy ALL the text space between the green stripes :\x1b[38;5;015m\n\n \x1b[48;5;046m \x1b[48;5;000m" + hide(encrypt_f(mess_invisible, cle), mess_couverture) + "\x1b[48;5;046m \x1b[48;5;000m")
##option 2
        elif opt == "2":
            while True:
                mess_to_extract = str(input("\n Text from which to extract : "))
                if mess_to_extract == "":
                    continue
                break
            print("\n\x1b[38;5;046m Hidden text : \x1b[38;5;015m" + decrypt_f(extract(mess_to_extract), cle))
        elif opt == "3":
            quitter = "no"
            delscrn()
            break
        elif opt == "4":
            quitter = "yes"
            break
        else:
            delscrn()
            pass
    if quitter == "yes":
        break
    else:
        pass
