from playwright.sync_api import sync_playwright
import requests
import time





token = '5637147882:AAH0nSsU9jM2655KoagUWO4MUTKmPKMQVOE'
chat_id = '-1001680706416'
mensagem = 'ta chegando a hora corno'
url = f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text={mensagem}'


with sync_playwright() as p:
    browser = p.firefox.launch()
    page = browser.new_page()
    page.goto("https://historicosblaze.com") 
    time.sleep(3) 
    page.locator('xpath=//*[@id="page-header"]/div/div[2]/div/ul/li[12]/a/span').click()
    time.sleep(3) 
    page.fill('xpath=//*[@id="user_email"]', 'grupomodafoka2@gmail.com')
    time.sleep(3)
    page.fill('//*[@id="user_password"]', '@IMPACTOdjah2')
    time.sleep(3)
    page.locator('xpath=//*[@id="new_user"]/div[4]/button').click()
    time.sleep(3)
    page.locator('xpath=//*[@id="page-header"]/div/div[2]/div/ul/li[2]/a/i').click()
    time.sleep(3)
    page.locator('xpath=//*[@id="page-header"]/div/div[2]/div/ul/li[2]/ul/li[2]/a/span').click()
    time.sleep(3)
    
    while True:
        a = page.locator('xpath=//*[@id="doubles-stats"]/div[3]/div[2]/div/strong').text_content()
        av = int(a)
        print(av)
        if av > 1:
            requests.get(url)
        time.sleep(60) 


