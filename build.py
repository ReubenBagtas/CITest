from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '71.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768'
}

driver = webdriver.Remote(
    command_executor='http://reubenbagtas1:huFvajTEqQv6YpxNsBpx@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print driver.title
print "hello worldssss"
driver.quit()