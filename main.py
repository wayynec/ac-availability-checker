# The following starter code is from: https://replit.com/talk/ask/Can-I-use-selenium/11566
from selenium_driver import driver
from slack_client import client
import time


driver.get("https://www.bestbuy.ca/en-ca/product/playstation-5-console/14962185")

def isAvailableText(driver):
  aval = driver.find_element_by_css_selector('.storeAvailabilityContainer_1Ez2A > div > span')
  return aval.text


# set up the infinite loop
while True:
  # check website
  print('refreshing...')
  driver.refresh()
  try:
    text = isAvailableText(driver)
    if text == 'Unavailable for store pickup':
      # update text_to_send
      text_to_send = text 
    else:
      text_to_send = text + ' <@U028BNSQ6A1>'
  except Exception as e:
    text_to_send = e
  
  client.chat_postMessage(channel='#web-scraper', text=text_to_send)

  time.sleep(300)



