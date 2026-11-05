import os
from tqdm import tqdm
import time
def menu():
    print("Add task (1)")
    print("Remove task (2)")
    print("Task info (3)")
    print("Show tasks (4)")
    print("Add tasks from CSV (5)")
    print("Export tasks (6)")
    print("EXIT (0)")
    def inp():
        try:
            i = int(input("Enter from menu numbers: "))
        except: 
            print("Enter a number!")
        return i
    r = inp()
    while (r > 6) or (r<0):
        print("Enter an available number!")
        r = inp()
    return r


def terminal_clearer():
    os.system("cls" if os.name == "nt" else "clear")

def pbar( s  , job):
    for _ in tqdm(range(5) , bar_format="{percentage:0.0f}%|{bar}{desc}" , ncols= 30 , desc=f"{job}"):
        time.sleep(s/5)
