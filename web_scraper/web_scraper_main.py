# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:19:00 2020

@author: Anastasia
"""

#Import packages

from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions  
import time

import pandas as pd 
import numpy as np

#Establish path to Chromedriver

PATH = "C:/Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Establish connection to URL

driver.get("https://www.jobs.nhs.uk/xi/search_vacancy/?action=search&staff_group=SG40&keyword=Nurse%20Sister%20Matron&logic=OR")

#Set column names for Dataframe

df_columns = ['Job Reference', 'Title', 'Posted Date', 'Closing Date', 'Job Type', 'Working Pattern', 'Pay Scheme', 'Pay Band', 'Specialty Function', 'Employer', 'Department', 'Description']

#Ensure main search results populate before further action is taken

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'resultsContainer')))

#Create empty lists to hold results 
    
    job_ref = []
    titles = []
    employers = []
    salaries = []
    posted_dates = []
    closing_dates = []
    job_types = []
    working_patterns = []
    pay_schemes = []
    pay_bands = []
    departments = []
    locations = []
    descriptions = []

    #Get the 'vacancy' container and loop through it 

    results = main.find_elements_by_class_name('vacancy')
    
#Loop over each vacancy 

    for result in results:
                
        #Get title
        
        title = result.find_element_by_css_selector("h2 > a[href]").get_attribute("title")
        titles.append(title)  
        
        department = result.find_element_by_tag_name("h3").text
        departments.append(department)
        
        #Get salary info 
        
        salary = result.find_element_by_class_name('salary')
        salaries.append(salary.text)
        
        #Get location info
               
        employer = result.find_element_by_class_name('agency')
        employers.append(employer.text)
    
    link_list = []
    
    links = driver.find_elements_by_xpath("//span[contains(@class, 'icons icon-covid-19')]/following-sibling::a[1]")
    for link in links:
        link_text = link.get_attribute("href")
        link_list.append(link_text)
    
    # this_window = driver.current_window_handle # get current/main window

    for link in link_list:
        driver.get(link)
        
        j_type = driver.find_elements_by_xpath("//dt[.='Job Type:']/following-sibling::dd[1]")
        if not j_type: x = "None"
        else: x = j_type[0].text
        job_types.append(x)
        
        w_pattern = driver.find_elements_by_xpath("//dt[.='Working pattern:']/following-sibling::dd[1]")
        if not w_pattern: x = "None"
        else: x = w_pattern[0].text
        working_patterns.append(x)
        
        p_scheme = driver.find_elements_by_xpath("//dt[.='Pay Scheme:']/following-sibling::dd[1]")
        if not p_scheme: x = "None"
        else: x = p_scheme[0].text
        pay_schemes.append(x)
        
        
        p_band = driver.find_elements_by_xpath("//dt[.='Pay Band:']/following-sibling::dd[1]")
        if not p_band: x = "None"
        else: x = p_band[0].text
        pay_bands.append(x)
         
        location = driver.find_elements_by_xpath("//dt[.='Location:']/following-sibling::dd[1]")
        if not location: x = "None"
        else: x = location[0].text
        locations.append(x)
        
        description = driver.find_elements_by_xpath("/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[2]/div[3]")
        if not description: x = "None"
        else: x = description[0].text
        descriptions.append(x)
        
        driver.back()
        
    j_ref = driver.find_elements_by_xpath("//dt[.='Job Ref:']/following-sibling::dd")
    for x in j_ref:
        job_ref.append(x.text)
        
    posted_date = driver.find_elements_by_xpath("//dt[.='Posted:']/following-sibling::dd")
    for x in posted_date:
        posted_dates.append(x.text)
    
    closing_date = driver.find_elements_by_xpath("//dt[.='Closing Date:']/following-sibling::dd")
    for x in closing_date:
        closing_dates.append(x.text)
    
    data = {'Job Ref': job_ref, 'Title':titles,'Employer': employers, 'Salary': salaries, 'Posted Date': posted_dates, 'Closing Date': closing_dates, 'Job Type': job_types, 'Working Pattern': working_patterns, 'Pay Scheme': pay_schemes, 'Pay Band': pay_bands, 'Department': departments, 'Location': locations, 'Description': descriptions}
    
    for k,v in data.items():
        print(k + str(len(v)))
    # df = pd.DataFrame(data)
    # print(df.head())
    print(data['Pay Band'])

#Click on next page when there's no more page left
#print a test of the row (df.iloc[1])

finally:
    driver.quit()