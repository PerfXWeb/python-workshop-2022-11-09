import selenium_framework
import time

username = "XXXXXXXXXX"
password = "XXXXXXXXXXXX"
course = "XXXXXXXXXX"
lv_number = "XXXXXXXXX"

sf = selenium_framework.SeleniumBrowser("macos")

sf.start_driver()
driver = sf.driver

driver.get("https://lpis.wu.ac.at/lpis")
time.sleep(3)
sf.find_xpath('//input[@type="text"]').send_keys(username)
time.sleep(1)
sf.find_xpath('//input[@type="password"]').send_keys(password)
time.sleep(1)
sf.find_xpath('//input[@type="submit"]').click()
time.sleep(5)
sf.find_xpath(f"//span[text()='{course}']/ancestor::td//a[contains(text(),'anmelden')]").click()
time.sleep(5)
sf.find_xpath(f"//a[text()='{1052}']/ancestor::tr//input[@type='submit']").click()
