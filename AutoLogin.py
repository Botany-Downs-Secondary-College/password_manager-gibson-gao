from selenium import webdriver

driver = webdriver.Chrome()

def WebPortal_Login():
    driver.get("https://webportal.bdsc.school.nz/index.php/home")
    driver.find_element_by_id("login-username").send_keys("gibson.gao")
    driver.find_element_by_id("login-password").send_keys("")
    driver.find_element_by_class_name("btn btn-info").click()

WebPortal_Login()
