import pandas as pd
import pyautogui as pg
from program import LPProgram


if __name__ == '__main__':
    df = pd.read_csv("", header=None)
    program = LPProgram(df)
    pg.FAILSAFE = True
    program.run()
