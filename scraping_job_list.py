'''
Fetches the list of quality jobs in Mountain View, California,USA 
in software engineering and prints the jobs for Staff position
in Intuit.inc.
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

# Creating object of Firefox driver
driver = webdriver.Firefox()

#Fetch the url   
driver.get("http://careers.intuit.com/professional")
driver.find_element_by_link_text("Explore your career options!").click()

#Search for the element with xpath for Category dropdown
category = driver.find_element_by_xpath(".//*[@id='ddlASCategory']") 
categorySelect = Select(category)
#Select the string from category drop down 
categorySelect.select_by_value("Software Engineering")

#Search for the element with xpath for country dropdown
country = driver.find_element_by_xpath(".//*[@id='ddlASCountry']") 
countrySelect = Select(country)
#Select USA from country drop down
countrySelect.select_by_value("USA") 

#Search for the element with xpath for state dropdown
state = driver.find_element_by_xpath(".//*[@id='ddlASState']")
stateSelect = Select(state)
#Select California from state drop down
stateSelect.select_by_value("California") 

#Search for the element with xpath for city dropdown
city = driver.find_element_by_id("ddlASCity") 
citySelect = Select(city)
#Select the Mountain View from city drop down
citySelect.select_by_value("Mountain View") 

#Clicks on the button
driver.find_element_by_xpath(".//*[@id='btnASGo']").click()

#Input 'quality' in the job title textbox
keyword = driver.find_element_by_xpath(".//*[@id='jobTitleKeyword']")
keyword.send_keys("quality")

#Clicks on the go button
driver.find_element_by_xpath(".//*[@id='btGo']").click()
time.sleep(3)

#Prints the jobs available for 'quality'
results_table = driver.find_element_by_xpath(".//*[@id='conteinerForSearchResults']/table")
rows = results_table.find_elements_by_tag_name("tr")

iteration_length = len(rows) - 1
num_of_result = 0
#Iterates over all the entries that came up
for i in range(1, iteration_length):
    result = driver.find_element_by_xpath(".//*[@id='search_result_link_%d']" % i).text
    #Looks for the entry that has 'Staff' in the title and prints them
    if 'Staff' in result: 
        num_of_result += 1
        print(result)

if num_of_result == 0:
    print ("No results found for Staff position!")

