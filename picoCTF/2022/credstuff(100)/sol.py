#!../../../venv/bin/python
import sys
import codecs

if __name__ == '__main__':
    with open('./leak/usernames.txt', 'r') as unames:
        with open('./leak/passwords.txt', 'r') as pwds:
            for uname, pwd in zip(unames, pwds):
                uname = uname.rstrip()
                pwd = pwd.rstrip()
                if uname == 'cultiris':
                    print(uname)
                    print(codecs.encode(pwd, 'rot_13'))
                    break
