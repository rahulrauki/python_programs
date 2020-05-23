from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name= input('Enter the name of the user ot group: ')
msg=input("enter your message")
count= int(input('enter the count'))

input('Enter anything after scanning the code')
user= driver.find_element_by_xpath('//span[@title = "{}"]', format(name))
user.click()

msg_box= driver.find_element_by_class_name('_1P1pp')

for i in range(count):
    msg_box.send_keys(msg)
    button= driver.find_element_by_class_name('weEq5')
    button.click()
