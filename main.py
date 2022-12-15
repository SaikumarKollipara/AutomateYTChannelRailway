from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep
from datetime import timedelta


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    # driver = createDriver()
    # driver.get('https://youtube.com')
    # source_code = driver.page_source
    # print(source_code[:100])
    print('Started')
    run()
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


def run():
    print('Entered run func')
    driver = createDriver()
    driver.get('https://kaggle.com')
    sleep(2)
    print('browser opened')

    #signIn button
    driver.find_element_by_css_selector('#site-container > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) a').click()
    sleep(2)
    # email signin
    driver.find_element_by_css_selector('form > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) a').click()
    #email & pass
    sleep(2)
    email = driver.find_element_by_css_selector('[name="email"]')
    email.send_keys('kkrksaikumar@gmail.com')
    email.send_keys(Keys.ENTER)
    password = driver.find_element_by_css_selector('[name="password"]')
    password.send_keys('Skumar@123')
    password.send_keys(Keys.ENTER)
    sleep(2)

    # Go to notebook
    driver.get('https://www.kaggle.com/code/krksaikumar/automateytchannel/edit')
    print('notebook opened')
    sleep(35)

    # run all 
    driver.find_element_by_css_selector('[title="Run all"]').click()
    print('running')

    totalTime = (3 * 60 * 60) + (0 * 60) + (0)
    logTime = (0 * 60 * 60) + (10 * 60) + (0)
    for i in range(1, totalTime//logTime+1):
        print(f'{(logTime * i)} {timedelta(seconds=logTime * i)} completed')
        sleep(logTime)
    
    driver.close()