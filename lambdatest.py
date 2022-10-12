
import unittest
import time
import os
import base64
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.common.by import By

username = "shubhamr"  # Replace the username
access_key = ""  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):



        #self.server = Server(path="/Users/shubhamr/Downloads/python-selenium-sample-master 3/browsermob-proxy-2.1.4/bin/browsermob-proxy")
        
        
        # self.server.start()
        # time.sleep(10)
        # #portn = str(self.server.getPort())

        # self.proxy = self.server.create_proxy()
       
        time.sleep(5)

        #print('self proxy',self.proxy)
        desired_caps = {
            'LT:Options': {
                "build": "Python Demo",  # Change your build name here
                "name": "Python Demo Test",  # Change your test name here
                "platformName": "Windows 11",
                "selenium_version": "4.0.0",
                "console": 'true',  # Enable or disable console logs
                "network": 'true',  # Enable or disable network logs
                #Enable Smart UI Project
                #"smartUI.project": "<Project Name>"
            },
            "browserName": "firefox",
            "browserVersion": "latest",
        }

        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot 
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/

        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=desired_caps)

# tearDown runs after each test case


    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_demo_site(self):

        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print('Loading URL')
        driver.get("https://the-internet.herokuapp.com/upload")

        # Let's select the location
        time.sleep(3)
        driver.find_element(By.ID, "file-upload").send_keys("/Users/shubhamr/Downloads/lt.log")
        submit = driver.find_element(By.ID, "file-submit")
        submit.click()
        print("Location is selected as Bali.")

        #Take Smart UI screenshot
        #driver.execute_script("smartui.takeScreenshot")
        driver.get("https://the-internet.herokuapp.com/download")
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[5]").click()

        file_content = driver.execute_script('lambda-file-content=Member Details _1665505069152.csv')
        #print(file_content)


        data = base64.b64decode(file_content)
        f = open("SampleCSVFile_2kb.csv", "wb")
        f.write(data)
        f.close()




if __name__ == "__main__":
    unittest.main()
