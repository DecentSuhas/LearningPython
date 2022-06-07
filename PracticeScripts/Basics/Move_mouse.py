import pyautogui
import time
import mouse
from datetime import datetime, timedelta


def move_mouse():
    print("\n")
    min_to_run = int(input("How long wanna move cursor? Enter in minutes: "))
    time.sleep(1)
    get_current_time = current_time()
    print("Current Time is :", get_current_time)
    time_to_stop = move_till(min_to_run)
    print("Cursor moves till :", time_to_stop)
    time.sleep(1)
    print("\n")
    print("Starting the movement now!")
    is_it_time = True
    while is_it_time:
        pyautogui.moveTo(100, 100, duration=1)
        time.sleep(2)
        mouse.click('left')
        pyautogui.moveTo(100, 10, duration=1)
        get_current_time = current_time()
        print("Current Time is :", get_current_time, ", Stops at: ", time_to_stop)
        mouse.click('left')
        if get_current_time >= time_to_stop:
            print("Time\'s UP!!, Movement stopped")
            is_it_time = False
            break


def move_till(minutes):
    now = datetime.now()
    # tim = time.localtime()
    # current_time = now.strftime("%H:%M:%S")
    now_plus_10 = now + timedelta(minutes=minutes)
    # new_time = str(now_plus_10).strftime("%H:%M:%S",tim)
    new_time = now_plus_10.strftime("%H:%M:%S")
    # print("Cursor moves till :", new_time)
    return new_time


def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print("Current Time is :", current_time)
    return current_time


move_mouse()
