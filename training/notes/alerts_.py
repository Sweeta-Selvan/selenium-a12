'''
Alerts  :   Alerts are not inspectable.
            Suppose if we are able to inspect, then it is not an alert.

            To handle the alerts, we will switch the driver to the alert
            SYNTAX  :   alert_obj = driver.switch_to.alert
                        alert_obj has two attributes to handle the alert
                        *   accept()    :   To accept the alert, we use alert_obj.accept()
                        *   dismiss()   :   To dismiss the alert, we use alert_obj.dismiss()

            There are different types alerts
            *   simple alert    :   If the alert is having only one option, then it is a simple alert.
                                    To handle the simple alert, first switch the driver to the alert
                                    Now we can either use accept or dismiss.
                                    alert_obj.accept()  or      alert_obj.dismiss()

            *   confirmation alert  :   If the alert is having two options, then it is a confirmation alert.
                                    To handle the confirmation alert, first switch the driver to the alert
                                    To click on OK/YES/AGREE,.. we give alert_obj.accept()
                                    To click on CANCEL/NO/DISAGREE,.. we give alert_obj.dismiss()

            *   Prompt alert    :   Here the alert will take the data from the user.
                                    To handle the prompt alert, first switch the driver to the alert
                                    alert_obj.send_keys("data")
                                    alert_obj.accept()




'''
import time


## Confirmation alert

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## getting alert
time.sleep(2)

## switch the driver to the alert
alert_obj = driver.switch_to.alert

alert_obj.accept()
time.sleep(2)

driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## getting alert
time.sleep(2)

alert_obj.dismiss()

############################################################################################################

## simple alert

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
time.sleep(2)

alert_obj = driver.switch_to.alert

alert_obj.accept()
time.sleep(2)

driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
time.sleep(2)
alert_obj.dismiss()

############################################################################################################

## prompt alert

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
time.sleep(2)

alert_obj = driver.switch_to.alert
alert_obj.send_keys('Sherlock Holmes')
alert_obj.accept()

############################################################################################################

# ## authentication popup
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')
#
# ## The above url, to lauch the application only it will give a pop-up which will ask for username and password
# ## We cannot inspect it.
# ## Such pop-ups we call them as athentication pop-ups

##---------------------------------------------------------------------------------------

# ## To handle such pop-ups, we will give the username and password while launching the application .
# ## We will include the username and password in the url only
# ## SYNTAX   :   https://username:password@url
#
# ## for the below application, username and password both is "admin"
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

############################################################################################################

## file-upload pop-up


# ## Uploading single file
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# file_path = r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\ramya_resume.doc'
#
# driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(file_path)

##---------------------------------------------------------------------------------------------------------
# ## multiple files
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# file1 = r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\file1.doc'
# file2 = r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\file2.doc'
# file3 = r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\file3.doc'
#
#
# driver.find_element('xpath', '//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}')

############################################################################################################

## push notifications   :   The notifications like "Allow irctc to send notifications,.." such kind of pop-ups, we call them push notificarions.
##                          Instead of handling them, we disable them. Because the are un-predictable. We might get those alerts or we might not

#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--disable-notifications')
#
# driver = webdriver.Chrome(options=opts)




















































