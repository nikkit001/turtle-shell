import wget
import pip


# SETTINGS:
# program directory(sapp):
# NOTE: if letting sappdir blank it will ask you every time where u want to install the sapp package!!!
sappdir = ''


# NOTE: THIS IS A GITHUB INSTALLER BASED ON WGET!!!
def sapp():
    global idir
    global pkg
    sapp = input('sapp pkg: ')
    if sappdir == '':
        idir = input('where do u want to install ' + sapp + '?')
    else:
        idir = sappdir
    if sapp == 'test':
        pkg = 'url'
    wget.download(pkg)

        
def urlget():
    url = input('url: ')
    wget.download(url)