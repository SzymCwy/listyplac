import datetime
import time
from calendar import monthrange

import numpy as np
import pandas as pd
import pyautogui as pg
import pydirectinput
import pyperclip

df = pd.read_csv("", header=None)


class LPProgram:

    def __init__(self, data):
        self.database = data.to_numpy()
        self.table = []
        self.workertable = []
        self.month = 0
        self.year = 2021
        self.nrofdays = 0
        self.extrafree = []
        self.change = 1000
        self.c = 4
        self.d = 2
        self.e = 6
        self.f = 0
        self.absence = ['U', 'UZ', 'UB', 'UO', 'UT', 'UM', 'KU', 'WO', 'BD', 'CH', 'N', 'SZ', 'SZ.K.', 'NUN', 'UW',
                        'OP', 'O', 'OS', 'W', 'P', 'K', 'cov', 'R', 'Z', 'SZ.']
        self.workHours = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'L', 'H', 'J', 'M']
        self.eightWork = ['A', 'B', 'G']
        self.mouse = MouseMovement()
        self.firstSaturday = 0
        self.saturdayList = []

    def prerp(self):  #
        csvarray = []
        for i in range(len(self.database)):
            arrrow = "".join(self.database[i])
            arrrow = arrrow.split(";")
            csvarray.append(arrrow)  # zamiana stringow na tablice

        for i in range(len(csvarray)):
            try:
                if csvarray[i][1] == '' and csvarray[i][0] == '':
                    csvarray.pop(i)
            except:
                continue
        self.table = np.array(csvarray)  # z każdego wiersza usuwane zbędne komórki

    def namesurname(self):
        for i in range(0, len(self.table), 2):
            name = self.table[i]
            name1 = name[1]
            surname = self.table[i + 1]
            surname1 = surname[1]
            namesurname = f'{name1} {surname1}'  # pozyskanie imienia i nazwiska z dwóch różnych wierszy
            for j in range(2):
                name = np.delete(name, 0)  # usuwanie 2 pierwszych komórek w wierszu zawierających niepotrzebne dane
            namesurar = np.array([namesurname])
            for j in range(self.nrofdays + 1, len(name), 1):
                name = np.delete(name, self.nrofdays + 1)  # usuwane komórki z danymi wychodzącymi poza zakres miesiąca
            name = np.concatenate((namesurar, name), axis=0)
            if name[1] != "" and name[2] != "" and name[3] != "" and name[4] != "":
                self.workertable.append(
                    name.tolist())  # tworzenie nowej tablicy zawierającej przygotowane dane ka zdego pracownika

    def weekenddaytoarray(self):  # tworzenie tablicy zawierającej daty, które przypadają na sobote
        for i in range(7):
            if datetime.date(self.year, int(self.month), i + 1).strftime('%A') == "Saturday":
                self.firstSaturday = i + 1
        for day in range(self.firstSaturday, self.nrofdays, 7):
            self.saturdayList.append(day)

    def replacez(self, worker):
        # wyszukiwanie 'z' w liście dni, wpisanie w miejsce z odpowiedniej ilosci godzin przypadajacej na sobote,
        # a w miejsce 'z' ustawiany dzień nieprzepracowany
        if "Z" in self.workertable[worker]:
            for day in range(len(self.workertable[worker])):
                if self.workertable[worker][day] == "Z":
                    for i in self.saturdayList:
                        if self.workertable[worker][i] in self.workHours:
                            self.workertable[worker][day] = self.workertable[worker][i]
                            self.workertable[worker][i] = "X"
                            break

    def definedate(self):
        print("Czy miesiac posiada dni wolne od pracy y/n")
        freeday = input()
        if freeday == "y":
            print("Wpisz daty wolnego oddzielone przecinkami (np. 10,11,31)")
            freeday = input()
            self.extrafree = freeday.split(",")
            self.extrafree = np.array(self.extrafree)  # ustalanie dni ustawowo wolnych od pracy
        print("Wpisz rok")
        self.year = int(input())
        print("Wpisz numer miesiąca")
        self.month = int(input())
        if self.month < 10:
            self.month = "".join("0" + str(self.month))
        else:
            self.month = str(self.month)
        self.nrofdays = monthrange(self.year, int(self.month))
        self.nrofdays = self.nrofdays[1] - 1  # przypisanie odpowiedniej ilości dni w miesiacu

    def recoagniseabsence(self, absencetype):
        # funckja okreslajaca na podstawie tablicy oraz wybranego dnia rodzaj nieobecności

        if absencetype == self.absence[0]:
            self.mouse.urlop()

        if absencetype == self.absence[1]:
            self.mouse.urlop()

        if absencetype == self.absence[2]:
            self.mouse.bezplatny()

        if absencetype == self.absence[3]:
            self.mouse.okolicznoscioweplatne()

        if absencetype == self.absence[4]:
            self.mouse.macierzynskie()

        if absencetype == self.absence[5]:
            self.mouse.macierzynskie()

        if absencetype == self.absence[6]:
            self.mouse.zwolnienieplatne()

        if absencetype == self.absence[8]:
            self.mouse.zwolnienieplatne()

        if absencetype == self.absence[9]:
            self.mouse.chorobowe()

        if absencetype == self.absence[10]:
            self.mouse.nieobecnosc()

        if absencetype == self.absence[11]:
            self.mouse.zwolnienieplatne()

        if absencetype == self.absence[12]:
            self.mouse.zwolnienieplatne()

        if absencetype == self.absence[13]:
            self.mouse.nieobecnoscnieplatna()

        if absencetype == self.absence[15]:
            self.mouse.opiekanaddzieckiem()

        if absencetype == self.absence[16]:
            self.mouse.opieka()

        if absencetype == self.absence[19]:
            self.mouse.zwolnienieplatne()

        if absencetype == self.absence[20]:
            self.mouse.zwolnienieplatne()

        if absencetype == self.absence[21]:
            self.mouse.chorobowe()

        if absencetype == self.absence[22]:
            self.mouse.zwolnienieplatne()

        if absencetype == self.absence[24]:
            self.mouse.zwolnienieplatne()

    def recoagnisehours(self, hourstype):  # wykrywanie ilości godzin przepracowanych

        if hourstype == self.workHours[0]:
            return str(8)

        if hourstype == self.workHours[1]:
            return str(8)

        if hourstype == self.workHours[2]:
            return str(self.c)

        if hourstype == self.workHours[3]:
            return str(2)

        if hourstype == self.workHours[4]:
            return str(6)

        if hourstype == self.workHours[5]:
            return str(0)

        if hourstype == self.workHours[6]:
            return str(8)

    def run(self):
        pg.FAILSAFE = True
        self.definedate()
        self.prerp()
        self.namesurname()
        self.mouse.initscreenres()
        self.weekenddaytoarray()

        print("Czy występuje zmiana? y/n")  # zmiana przepracowanych dni w zależności od id pracownika
        if input() == "y":
            print("Na którym numerze pracownika występuje zmiana?")
            self.change = int(input())
        for worker in range(len(self.workertable)):
            self.replacez(worker)
            if int(worker) == self.change:
                self.c = 3
                print("zmiana")
            credentials = self.workertable[worker][0]
            self.workertable[worker] = np.delete(self.workertable[worker], 0)
            # po przypisaniu imienia i nazwiska, jest usuwane, żeby przetrwarzać tylko odpowiednia ilosc dni
            time.sleep(2)
            self.mouse.changeworker(credentials)
            time.sleep(2)
            for day in range(0, len(self.workertable[worker]), 1):
                if self.workertable[worker][day] in self.absence and self.workertable[worker][day] != "W" and \
                        self.workertable[worker][day] != "WO":
                    pg.typewrite("\n")
                    time.sleep(2)
                    mouseclick.absval()
                    self.mouse.adddata(str(day + 1))
                    self.recoagniseabsence(self.workertable[worker][day])

                if self.workertable[worker][day] in self.workHours:
                    if datetime.date(self.year, int(self.month), day + 1).strftime('%A') == "Sunday" or datetime.date(
                            self.year, int(self.month), day + 1).strftime('%A') == "Saturday" or np.any(
                        self.extrafree == str(
                            day + 1)):  # wykrywanie czy dany dzien jest weekendem lub dniem wolnym od pracy
                        mouseclick.workbutton()
                        time.sleep(2)
                        mouseclick.workval()
                        self.mouse.adddata(str(day + 1))
                        mouseclick.weekendhouradd(self.recoagnisehours(self.workertable[worker][day]))
                    else:
                        print(self.workertable[worker][day])
                        if self.workertable[worker][day] in self.eightWork:
                            time.sleep(0.5)  # pomijanie dni nie wymagających wpisywania
                        else:
                            mouseclick.workbutton()
                            time.sleep(2)
                            mouseclick.workval()
                            self.mouse.adddata(str(day + 1))
                            mouseclick.houradd(self.recoagnisehours(self.workertable[worker][day]))


class MouseMovement:
    def __init__(self):  # inicjalizacja tablic zawierajacych x,y pól
        self.screenres = []
        self.searchbar = [675, 108]
        self.hourWindow = [924, 447]
        self.hourWindowWeekend = [921, 522]
        self.sumHours = [927, 392]
        self.workvalidationpixel = [1165, 238]
        self.absvalidationpixel = [1392, 247]

    def initscreenres(self):
        self.screenres = pg.size()

    def changeworker(self, name):  # funkcja zmieniająca pracownika
        pg.moveTo(self.searchbar)
        pg.click()
        pyperclip.copy(name)
        pg.keyDown('ctrlleft')
        pg.press('v')
        pg.keyUp('ctrlleft')
        time.sleep(1)
        pg.typewrite("\n")
        time.sleep(1)

    @staticmethod
    def adddata(day):  # ustawienie daty
        if int(day) < 10:
            day = "".join("0" + day)
        pg.typewrite(day)
        pg.typewrite(program.month)
        pg.typewrite(str(program.year))
        time.sleep(0.5)

    def workval(self):  # Sprawdzanie czy okienko poprawnie się wyświetliło
        pg.moveTo(self.workvalidationpixel)
        if pg.pixel(pg.position()[0], pg.position()[1]) != (232, 17, 35):
            raise ValueError('nie otworzyło się okno godzin')

    def absval(self):  # Sprawdzanie czy okienko poprawnie się wyświetliło
        pg.moveTo(self.absvalidationpixel)
        if pg.pixel(pg.position()[0], pg.position()[1]) != (232, 17, 35):
            raise ValueError('Nie otworzyło się okno absencji')

    @staticmethod
    def urlop():
        pg.typewrite('\t')
        pg.typewrite('\t')
        pydirectinput.press('down')
        pg.typewrite('\n')
        time.sleep(1)
        if pg.pixel(900, 590) == (240, 240, 240):
            time.sleep(0.3)
            pydirectinput.press('left')
            pg.typewrite('\n')

    @staticmethod
    def chorobowe():
        pg.typewrite('\n')
        time.sleep(5)
        if pg.pixel(900, 590) == (240, 240, 240):
            time.sleep(0.3)
            pg.typewrite('\n')

    @staticmethod
    def macierzynskie():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(2):
            pydirectinput.press('down')
        pg.typewrite('\n')
        time.sleep(1)
        if pg.pixel(900, 590) == (240, 240, 240):
            time.sleep(0.3)
            pydirectinput.press('left')
            pg.typewrite('\n')

    @staticmethod
    def wychowawczy():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(3):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def bezplatny():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(4):
            pydirectinput.press('down')
        pg.typewrite('\n')

    @staticmethod
    def okolicznoscioweplatne():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(5):
            pydirectinput.press('down')
        pg.typewrite('\n')

    @staticmethod
    def zwolnienieplatne():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(6):
            pydirectinput.press('down')
        pg.typewrite('\n')

    @staticmethod
    def opiekanaddzieckiem():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(7):
            pydirectinput.press('down')
        pg.typewrite('\n')
        time.sleep(1)
        if pg.pixel(900, 590) == (240, 240, 240):
            time.sleep(0.3)
            pydirectinput.press('left')
            pg.typewrite('\n')

    @staticmethod
    def opieka():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(8):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def nieobecnosc():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(9):
            pydirectinput.press('down')
        pg.typewrite('\n')

    @staticmethod
    def poszukiwaniepracy():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(10):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def nieobecnoscplatna():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(11):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def nieobecnoscnieplatna():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(12):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def sluzba():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(13):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def zwolnieniezeswiadczenia():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(14):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def przestoj():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(15):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def workbutton():
        pg.keyDown('ctrlleft')
        pg.press('\n')
        pg.keyUp('ctrlleft')

    def houradd(self, ammount):
        pg.click(self.hourWindow)
        pg.typewrite(str(ammount))
        pg.typewrite('\n')

    def weekendhouradd(self, ammount):
        pg.click(self.sumHours)
        pg.typewrite(str(8))
        pg.click(self.hourWindow)
        pg.click(self.hourWindowWeekend)
        pg.typewrite(str(ammount))
        pg.typewrite('\n')


program = LPProgram(df)
pg.FAILSAFE = True
mouseclick = MouseMovement()
program.run()
