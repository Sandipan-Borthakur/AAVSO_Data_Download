from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import shutil

def aavso_data_download(objName,datapath,startdate='All',stopdate='All',whoami = 'Student',whythedata='Data Analysis'):
    path = 'temporary_aavso_data_storage'
    op = webdriver.ChromeOptions()
    p = {'download.default_directory': path}
    op.add_argument('--headless')
    op.add_argument('--disable-gpu')
    op.add_experimental_option('prefs', p)
    s=Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=s,options=op)
    driver.get('https://www.aavso.org/data-download')
    name = driver.find_element(By.NAME, 'auid')
    name.clear()
    name.send_keys(objName)
    start = driver.find_element(By.NAME, 'start')
    start.clear()
    start.send_keys(startdate)
    stop = driver.find_element(By.NAME, 'stop')
    stop.clear()
    stop.send_keys(stopdate)
    names = driver.find_element(By.NAME, 'whoami')
    names = Select(names)
    names.select_by_visible_text(whoami)
    purpose = driver.find_element(By.NAME, 'purpose')
    purpose = Select(purpose)
    purpose.select_by_visible_text(whythedata)
    element = driver.find_element(By.NAME,'op' )
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.XPATH,'/html/body/div/div/div/section/div/div/table/tbody/tr[1]/td[2]/h3/a').click()

    while len(os.listdir(path))==0:
        time.sleep(5)
    print("Download begins...")
    while os.listdir(path)[0].split('.')[-1] == 'crdownload':
        time.sleep(2)
    print("Download completed...")
    filepath = os.path.join(path,'aavso_'+objName+'.txt')
    os.rename(os.path.join(path,os.listdir(path)[0]),filepath)
    shutil.copyfile(filepath,datapath)
    shutil.rmtree(path)
