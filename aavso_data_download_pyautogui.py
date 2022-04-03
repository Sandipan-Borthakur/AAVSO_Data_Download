import webbrowser
import pyautogui
import time

def aavso_automated_data_download(source_name,savefilepath,start_date = 'all',end_date = 'all'):
    url = 'https://www.aavso.org/data-download'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    time.sleep(5)
    for i in range(15):
        pyautogui.press('tab')
    pyautogui.write(source_name)
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.write(start_date)
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.write(end_date)
    time.sleep(0.5)
    for i in range(6):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('e')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('s')
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('d')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    for i in range(6):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    for i in range(16):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(savefilepath)
    time.sleep(0.5)
    pyautogui.press('enter')

aavso_automated_data_download(source_name='V1948 Cyg',savefilepath = 'E:\V1948Cyg')

