# Developed by: Suhas KS

import subprocess
import pyautogui
import time
import cv2
import os

connectbtn = os.path.abspath("connectbtn.png")
nextbtn = os.path.abspath("Nextbtn.png")
signinbtn = os.path.abspath("Signinbtn.png")
calloption = os.path.abspath("Calloption.png")
close = os.path.abspath("close.png")
signinText = os.path.abspath("signinText.png")
passwordText = os.path.abspath("passwordText.png")

email_id = "suhas.ks@philips.com"
password = "Krishna@23"

def move_mouse_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(2)


def enter_text(text_value):
    close_any_connect(close)
    text_email = text_value
    pyautogui.typewrite(text_email)
    time.sleep(1)


def launch_app():
    time.sleep(5)
    kill_app()
    subprocess.Popen('C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpnui.exe')
    time.sleep(2)


def connect_to_vpn():
    click_on_btn(connectbtn)
    check_for_textfield(signinText, email_id)
    click_on_btn(nextbtn)
    time.sleep(4)
    check_for_textfield(passwordText, password)
    click_on_btn(signinbtn)
    time.sleep(2)
    click_on_btn(calloption)


def kill_app():
    subprocess.call("TASKKILL /F /IM vpnui.exe", shell=True)
    time.sleep(5)


def click_on_btn(btn_name):
    count = 0
    while count < 20:
        try:
            iconX, iconY = pyautogui.locateCenterOnScreen(btn_name, confidence=0.7)
            pyautogui.click(iconX, iconY)
            count = 20
        except Exception as e:
            count += 1
            time.sleep(2)
            print("Waiting for the screen to load...")
            close_any_connect(close)


def check_for_textfield(element, text):
    text_value = text
    count = 0
    while count < 20:
        try:
            iconX, iconY = pyautogui.locateCenterOnScreen(element, confidence=0.9)
            pyautogui.typewrite(text_value)
            time.sleep(2)
            count = 20
        except Exception as e:
            count += 1
            time.sleep(2)
            print("Waiting for the field to enter credentials...")


def close_any_connect(btn_name):
    try:
        iconX, iconY = pyautogui.locateCenterOnScreen(btn_name, confidence=0.8)
        pyautogui.click(iconX, iconY)
        print("Closed Any connect dialog..!")
    except TypeError:
        print("Any connect screen is not displayed!")


launch_app()
connect_to_vpn()

