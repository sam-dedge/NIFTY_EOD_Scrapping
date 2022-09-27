from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time
from datetime import date

proj_path = os.getcwd()
driver_path = proj_path + "\chromedriver.exe"
#print("PATH to webdriver: \"" + driver_path + "\"")

browser_options = webdriver.ChromeOptions()

today = date.today()
today = today.strftime("%d%b%Y")
download_path = os.path.join(proj_path+"\sample",today)
#print('PATH:', download_path)
if not os.path.exists(download_path):
    os.mkdir(download_path)

prefs = {"download.default_directory": download_path}
browser_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=browser_options)

driver.get("https://www.nseindia.com/option-chain")
print('Website Title: ', driver.title)

#eq_select = driver.find_element_by_id("equity_optionchain_select")
sel_tickr = Select(driver.find_element_by_id("equity_optionchain_select"))
sel_tickr.select_by_visible_text("NIFTY")
time.sleep(1)

sel_maturity = driver.find_element_by_id("expirySelect")
dropdown_maturity = Select(sel_maturity)
time.sleep(1)
#print(sel_maturity)
#print(dropdown_maturity)
#dropdown_maturity.select_by_value("Select")

maturities = []
for opt in dropdown_maturity.options:
    maturities.append(opt.text)

maturities = maturities[1:4]
#print(maturities)

#dropdown_maturity.select_by_visible_text(maturities[1])
for matu in maturities:
    dropdown_maturity.select_by_visible_text(matu)
    time.sleep(1)
    sel_dwld = driver.find_element_by_id("downloadOCTable")
    sel_dwld.click()


#search = driver.find_element_by_id("equity_optionchain_select")
#search.send_keys("NIFTY")
#search.send_keys(Keys.RETURN)

#print(driver.page_source)

time.sleep(3)
driver.quit()