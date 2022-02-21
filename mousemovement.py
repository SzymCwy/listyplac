import pyautogui as pg
import pydirectinput
import pyperclip
import time


class MouseMovement:
    def __init__(self, program):  # inicjalizacja tablic zawierajacych x,y pól
        self.screen_resolution = []
        self.searchbar = [675, 108]
        self.hour_window = [924, 447]
        self.hour_window_weekend = [921, 522]
        self.sum_hours = [927, 392]
        self.work_validation_pixel = [1165, 238]
        self.absence_validation_pixel = [1392, 247]
        self.program = program

    def init_screen_resolution(self):
        self.screen_resolution = pg.size()

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

    def adddata(self, day):  # ustawienie daty
        if int(day) < 10:
            day = "".join("0" + day)
        pg.typewrite(day)
        pg.typewrite(self.program.get_month())
        pg.typewrite(str(self.program.get_year()))
        time.sleep(0.5)

    def work_val(self):  # Sprawdzanie czy okienko poprawnie się wyświetliło
        pg.moveTo(self.work_validation_pixel)
        if pg.pixel(pg.position()[0], pg.position()[1]) != (232, 17, 35):
            raise ValueError('nie otworzyło się okno godzin')

    def abs_val(self):  # Sprawdzanie czy okienko poprawnie się wyświetliło
        pg.moveTo(self.absence_validation_pixel)
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
    def okolicznosciowe_platne():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(5):
            pydirectinput.press('down')
        pg.typewrite('\n')

    @staticmethod
    def zwolnienie_platne():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(6):
            pydirectinput.press('down')
        pg.typewrite('\n')

    @staticmethod
    def opieka_nad_dzieckiem():
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
    def poszukiwanie_pracy():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(10):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def nieobecnosc_platna():
        pg.typewrite('\t')
        pg.typewrite('\t')
        for i in range(11):
            pydirectinput.press('down')
        pg.typewrite('\n')
        pg.typewrite('\n')
        pg.typewrite('esc')
        pydirectinput.press('esc')

    @staticmethod
    def nieobecnosc_nieplatna():
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
    def zwolnienie_ze_swiadczenia():
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
    def work_button():
        pg.keyDown('ctrlleft')
        pg.press('\n')
        pg.keyUp('ctrlleft')

    def hour_add(self, amount):
        pg.click(self.hour_window)
        pg.typewrite(str(amount))
        pg.typewrite('\n')

    def weekend_hour_add(self, amount):
        pg.click(self.sum_hours)
        pg.typewrite(str(8))
        pg.click(self.hour_window)
        pg.click(self.hour_window_weekend)
        pg.typewrite(str(amount))
        pg.typewrite('\n')
