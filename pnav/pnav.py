#contains my classes for my pip
from datetime import date
import time
import tkinter
from win10toast import ToastNotifier
from datetime import datetime
from tkinter import *
from bs4 import BeautifulSoup
import requests

class help:
    def help():
        print('Hello! Thank you for choosing the Pnav package. Here are a few of the classes and functions you can choose from:\nrandom: contains random functions and projects.\n\tmessyCheck: this takes a input file and checks it for a-z.\n\tinputOwn: Allows you to input your own array separated by spaces and will search for each item instead of a-z.\n\tcheckDate: takes a date written in year/month/day format and returns how far away it is.\n\tisPalindrome: takes a string as a input and returns a boolean on if the string is a palindrome.\ncandyTimer: uses a gui to get user data and create windows pop-ups or command line notifications so you can ration food to last to a certain time.\n\tsetup: this is what runs the project, it takes no inputs.\nstockScraper: uses beautifulSoup4 to get html data from a webpage and then returns information on a certain stock.\n\tselect: this runs the project and takes no inputs.')

class random:
    default = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def messyCheck(inpfile):
        global default
        if(random.default == ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']):
            inpfile = inpfile.lower()
        for i in random.default:
            if i not in inpfile:
                return "First to fail: "+str(i)
        return 'All items in file.'

    def inputOwn():
        random.default
        default = input('Enter each item you wish to search for, seperated by spaces: ')
        if(default == ''):
            default = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        else:
            default = default.split(' ')

    def checkDate(dateToCheck):
        if(dateToCheck == ''):
            return
        today = date.today()
        today = str(today).split('-')
        bases = dateToCheck.split('/')
        yeardif = int(bases[0]) - int(today[0])
        if yeardif != 0:
            yeardif = yeardif * 365.25
        monthdif = int(bases[1]) - int(today[1])
        if monthdif != 0:
            monthdif = monthdif * 30.416
        daydif = int(bases[2]) - int(today[2])
        var = round((daydif+monthdif+yeardif),0)
        return str(int(var)) 

    def isPalindrome(stringToCheck):
        i = len(stringToCheck)
        i -= 1
        for x in stringToCheck:
            if(x != stringToCheck[i]):
                return False
            i -= 1
        return True


class candyTimer():
    c1Var = False 
    def calculateTime(timeToLast):
        if('h' in timeToLast):
            timeToLast = timeToLast.replace('h', '')
            timeToLast = float(timeToLast)*60^2
        elif('s' in timeToLast):
            timeToLast = timeToLast.replace('s', '')
        else:
            timeToLast = timeToLast.replace('m', '')
            timeToLast = float(timeToLast)*60
        return timeToLast


    def runMain(timeToLast, pieces, nopopup = False):
        interval = float(timeToLast)/int(pieces)
        if(nopopup == True):
            print('-----------------\nYou have selected the no windows pop up option.')
        if(interval < 10):
            dur = interval-1
            interval = 1
        else:
            dur = 10
            interval = interval - 10
        while(int(pieces) > 0):
            print('-----------------')
            while(interval > 30):
                time.sleep(30)
                interval = interval - 30
                print(str(interval)+' seconds remaining until the next piece.\n---------')
            time.sleep(interval)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            pieces = int(pieces) - 1
            if(pieces != 0):
                print('enjoy a piece of candy at '+current_time+', there are '+str(pieces)+' remaining pieces.')
                if(nopopup == False):
                    ToastNotifier().show_toast('Candy Time!', 'Enjoy a piece of candy! There are '+str(pieces)+' remaining pieces.', duration = dur)
            else:
                print('enjoy the final piece of candy at '+current_time+', there are no remaining pieces.')
                if(nopopup == False):
                    ToastNotifier().show_toast('Candy Time!', 'Enjoy the final piece of candy! There are no remaining pieces.', duration = 10)



    #main
    def setup():
        global runMain
        global calculateTime
        global c1var
        master = Tk()
        master.title('Candy Counter')
        def guiGet():
            time = e1.get()
            pieces = e2.get()
            if(candyTimer.c1Var == False):
                master.destroy()
            candyTimer.runMain(str(candyTimer.calculateTime(time)),str(pieces), candyTimer.c1Var)
        def guiGetEnter(e):
            time = e1.get()
            pieces = e2.get()
            if(candyTimer.c1Var == False):
                master.destroy()
            candyTimer.runMain(str(candyTimer.calculateTime(time)),str(pieces), candyTimer.c1Var)
        def toggleVal():
            candyTimer.c1Var = not candyTimer.c1Var
        Label(master, text='Time to last:\n45s = 45 seconds, 20m or 20 = 20 minutes 1.5h = 1:30 minutes:').grid(row=0, columnspan=2)
        Label(master, text='Amount of Candy:').grid(row=1, columnspan=2)
        Label(master, text='Disable Windows Pop-Ups?').grid(row=2, column=0)
        e1 = Entry(master)
        e2 = Entry(master)
        b1 = Button(master, text='Enter', command = guiGet)
        b2 = Button(master, text='Exit', command = master.destroy)
        c1 = Checkbutton(master, command= toggleVal)
        e1.grid(row=0, column=2, columnspan=2)
        e2.grid(row=1, column=2, columnspan=2)
        c1.grid(row=2, column=1)
        b1.grid(row=2, column=2)
        b2.grid(row=2, column=3)
        master.bind('<Return>',guiGetEnter)
        e1.focus()
        master.mainloop()

link = 'HELP'
url = 'https://robinhood.com/stocks/'
class stockScraper():
    def select():
        global link
        link = input('Input the stock ticker symbol or cmd for a list of commands: ').upper()
        print(link)
        if(link == 'HELP'):
            print('Help: use a browser to see a stocks ticker symbol, for instance AAPL for Apple. Do list in input field to see list of stock ticker symbols.')
            return
        elif(link == 'LIST'):
            print('List:\nAAPL:\tApple\nSPY:\tS&P 500 ETF\nTSLA:\tTesla\nAMC:\tAMC Entertainment\nF:\tFord Motor\nSNDL:\tSundial Growers\nMSFT:\tMicrosoft\nAMZN:\tAmazon\nDIS:\tDisney\nNIO:\tNIO')
            return
        elif(link == 'CMD'):
            print('help: gives information on how to input a stock via ticker symbol\nlist: gives a list of a few major stocks and their ticker symbol\ncmd: yields this information')
            return
        stockScraper.getStock()

    def getStock():
        global link
        global url
        page = requests.get(url+link)
        if(page.status_code == 404):
            print('Stock not found or available!')
            return
        soup = BeautifulSoup(page.content, 'html.parser')
        value = soup.find("span", class_='up')
        value = (value['aria-label'])
        priceChanges = soup.find(id="sdp-price-chart-price-change").findAll('span')[0].text
        print('Current stock price of '+link+': '+str(value)+'\nTotal change today: '+priceChanges)