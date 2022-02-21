import numpy as np
import datetime
import time
from calendar import monthrange
from mousemovement import MouseMovement
import pyautogui as pg


class LPProgram:

    def __init__(self, data):
        self.database = data.to_numpy()
        self.table = []
        self.worker_table = []
        self.month = None
        self.year = None
        self.nr_of_days = None
        self.extra_free = []
        self.change = 1000
        self.c = 4
        self.d = 2
        self.e = 6
        self.f = 0
        self.absence = ['U', 'UZ', 'UB', 'UO', 'UT', 'UM', 'KU', 'WO', 'BD', 'CH', 'N', 'SZ', 'SZ.K.', 'NUN', 'UW',
                        'OP', 'O', 'OS', 'W', 'P', 'K', 'cov', 'R', 'Z', 'SZ.']
        self.workHours = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'L', 'H', 'J', 'M']
        self.eightWork = ['A', 'B', 'G']
        self.mouse = MouseMovement(self)
        self.firstSaturday = None
        self.saturdayList = []

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def prepare_data(self):  #
        csv_array = []
        for i in range(len(self.database)):
            array_row = "".join(self.database[i])
            array_row = array_row.split(";")
            csv_array.append(array_row)  # zamiana stringow na tablice

        for i in range(len(csv_array)):
            try:
                if csv_array[i][1] == '' and csv_array[i][0] == '':
                    csv_array.pop(i)
            except:
                continue
        self.table = np.array(csv_array)  # z każdego wiersza usuwane zbędne komórki

    def define_name(self):
        for i in range(0, len(self.table), 2):
            name = self.table[i][1]
            surname = self.table[i + 1][1]
            name_surname = f'{name} {surname}'  # pozyskanie imienia i nazwiska z dwóch różnych wierszy
            for j in range(2):
                name = np.delete(name, 0)  # usuwanie 2 pierwszych komórek w wierszu zawierających niepotrzebne dane
            name_array = np.array([name_surname])  # zmienienie na tablice, aby później użyć funkcji concentrate
            for j in range(self.nr_of_days + 1, len(name), 1):
                name = np.delete(name, self.nr_of_days + 1)  # usuwane komórki z danymi wychodzącymi poza zakres
                # miesiąca
            name = np.concatenate((name_array, name), axis=0)
            if name[1] != "" and name[2] != "" and name[3] != "" and name[4] != "":  # zabezpiecznie przed złymi danymi
                self.worker_table.append(
                    name.tolist())  # tworzenie nowej tablicy zawierającej przygotowane dane ka zdego pracownika

    def weekend_days_to_array(self):  # tworzenie tablicy zawierającej daty, które przypadają na sobote
        for i in range(7):
            if datetime.date(self.year, int(self.month), i + 1).strftime('%A') == "Saturday":
                self.firstSaturday = i + 1
        for day in range(self.firstSaturday, self.nr_of_days, 7):
            self.saturdayList.append(day)

    def replace_z(self, worker):
        # wyszukiwanie 'z' w liście dni, wpisanie w miejsce z odpowiedniej ilosci godzin przypadajacej na sobote,
        # a w miejsce 'z' ustawiany dzień nieprzepracowany
        if "Z" in self.worker_table[worker]:
            for day in range(len(self.worker_table[worker])):
                if self.worker_table[worker][day] == "Z":
                    for i in self.saturdayList:
                        if self.worker_table[worker][i] in self.workHours:
                            self.worker_table[worker][day] = self.worker_table[worker][i]
                            self.worker_table[worker][i] = "X"
                            break

    def define_date(self):
        print("Czy miesiac posiada dni wolne od pracy y/n")
        freeday = input()
        if freeday == "y":
            print("Wpisz daty wolnego oddzielone przecinkami (np. 10,11,31)")
            freeday = input()
            self.extra_free = freeday.split(",")
            self.extra_free = np.array(self.extra_free)  # ustalanie dni ustawowo wolnych od pracy
        print("Wpisz rok")
        self.year = int(input())
        print("Wpisz numer miesiąca")
        self.month = int(input())
        if self.month < 10:
            self.month = "".join("0" + str(self.month))
        else:
            self.month = str(self.month)
        self.nr_of_days = monthrange(self.year, int(self.month))
        self.nr_of_days = self.nr_of_days[1] - 1  # przypisanie odpowiedniej ilości dni w miesiacu

    def recognise_absence(self, absence_type):
        # funckja okreslajaca na podstawie tablicy oraz wybranego dnia rodzaj nieobecności

        if absence_type == self.absence[0]:
            self.mouse.urlop()

        if absence_type == self.absence[1]:
            self.mouse.urlop()

        if absence_type == self.absence[2]:
            self.mouse.bezplatny()

        if absence_type == self.absence[3]:
            self.mouse.okolicznosciowe_platne()

        if absence_type == self.absence[4]:
            self.mouse.macierzynskie()

        if absence_type == self.absence[5]:
            self.mouse.macierzynskie()

        if absence_type == self.absence[6]:
            self.mouse.zwolnienie_platne()

        if absence_type == self.absence[8]:
            self.mouse.zwolnienie_platne()

        if absence_type == self.absence[9]:
            self.mouse.chorobowe()

        if absence_type == self.absence[10]:
            self.mouse.nieobecnosc()

        if absence_type == self.absence[11]:
            self.mouse.zwolnienie_platne()

        if absence_type == self.absence[12]:
            self.mouse.zwolnienie_platne()

        if absence_type == self.absence[13]:
            self.mouse.nieobecnosc_nieplatna()

        if absence_type == self.absence[15]:
            self.mouse.opieka_nad_dzieckiem()

        if absence_type == self.absence[16]:
            self.mouse.opieka()

        if absence_type == self.absence[19]:
            self.mouse.zwolnienie_platne()

        if absence_type == self.absence[20]:
            self.mouse.zwolnienie_platne()

        if absence_type == self.absence[21]:
            self.mouse.chorobowe()

        if absence_type == self.absence[22]:
            self.mouse.zwolnienie_platne()

        if absence_type == self.absence[24]:
            self.mouse.zwolnienie_platne()

    def recognise_hours(self, hours_type):  # wykrywanie ilości godzin przepracowanych

        if hours_type == self.workHours[0]:
            return str(8)

        if hours_type == self.workHours[1]:
            return str(8)

        if hours_type == self.workHours[2]:
            return str(self.c)

        if hours_type == self.workHours[3]:
            return str(2)

        if hours_type == self.workHours[4]:
            return str(6)

        if hours_type == self.workHours[5]:
            return str(0)

        if hours_type == self.workHours[6]:
            return str(8)

    def run(self):
        pg.FAILSAFE = True
        self.define_date()
        self.prepare_data()
        self.define_name()
        self.mouse.init_screen_resolution()
        self.weekend_days_to_array()

        print("Czy występuje zmiana? y/n")  # zmiana przepracowanych dni w zależności od id pracownika
        if input() == "y":
            print("Na którym numerze pracownika występuje zmiana?")
            self.change = int(input())
        for worker in range(len(self.worker_table)):
            self.replace_z(worker)
            if int(worker) == self.change:
                self.c = 3
            credentials = self.worker_table[worker][0]
            self.worker_table[worker] = np.delete(self.worker_table[worker], 0)
            # po przypisaniu imienia i nazwiska, jest usuwane, żeby przetrwarzać tylko odpowiednia ilosc dni
            time.sleep(2)
            self.mouse.changeworker(credentials)
            time.sleep(2)
            for day in range(0, len(self.worker_table[worker]), 1):
                if self.worker_table[worker][day] in self.absence and self.worker_table[worker][day] != "W" and \
                        self.worker_table[worker][day] != "WO":
                    pg.typewrite("\n")
                    time.sleep(2)
                    self.mouse.abs_val()
                    self.mouse.adddata(str(day + 1))
                    self.recognise_absence(self.worker_table[worker][day])

                if self.worker_table[worker][day] in self.workHours:
                    if datetime.date(self.year, int(self.month), day + 1).strftime('%A') == "Sunday" or datetime.date(
                            self.year, int(self.month), day + 1).strftime('%A') == "Saturday" or np.any(
                        self.extra_free == str(
                            day + 1)):  # wykrywanie czy dany dzien jest weekendem lub dniem wolnym od pracy
                        self.mouse.work_button()
                        time.sleep(2)
                        self.mouse.work_val()
                        self.mouse.adddata(str(day + 1))
                        self.mouse.weekend_hour_add(self.recognise_hours(self.worker_table[worker][day]))
                    else:
                        print(self.worker_table[worker][day])
                        if self.worker_table[worker][day] in self.eightWork:
                            time.sleep(0.5)  # pomijanie dni nie wymagających wpisywania
                        else:
                            self.mouse.work_button()
                            time.sleep(2)
                            self.mouse.work_val()
                            self.mouse.adddata(str(day + 1))
                            self.mouse.hour_add(self.recognise_hours(self.worker_table[worker][day]))
