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
    locations = []
    
    links = driver.find_elements_by_xpath("//div[contains(@class, 'vacancy')]//following-sibling::a[1]")
    for link in links:
        link_text = link.get_attribute("href")
        print(link_text)
    # this_window = driver.current_window_handle # get current/main window

    # for link in links:
    #     link.click()
    #     driver.switch_to_window([win for win in driver.window_handles if win !=this_window][0]) # switch to new window
    #     date = driver.find_elements_by_class_name("mstat-date")
    #     for d in date:
    #         print(d.text)
    #     driver.close() # close new window
    #     driver.switch_to_window(this_window) # switch back to main window

#Get the 'vacancy' container and loop through it 

    results = main.find_elements_by_class_name('vacancy')
    
#Loop over each vacancy 

    for result in results:
        
        link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2 > a[href]")))  
        
        link.click()
        
        j_type = driver.find_elements_by_xpath("//dt[.='Job Type:']/following-sibling::dd[1]")
        for x in j_type:
            print(x.text)
        
        w_pattern = driver.find_elements_by_xpath("//dt[.='Working pattern:']/following-sibling::dd[1]")
        for x in w_pattern:
            print(x.text)
        
        p_scheme = driver.find_elements_by_xpath("//dt[.='Pay Scheme:']/following-sibling::dd[1]")
        for x in p_scheme:
            print(x.text)
        
        p_band = driver.find_elements_by_xpath("//dt[.='Pay Band:']/following-sibling::dd[1]")
        for x in p_band:
            print(x.text)
            
        s_function = driver.find_elements_by_xpath("//dt[.='Specialty/Function:']/following-sibling::dd[1]")
        for x in s_function:
            print(x.text)
        
        location = driver.find_elements_by_xpath("//dt[.='Location:']/following-sibling::dd[1]")
        for x in location:
            print(x.text)
        
        description = driver.find_elements_by_xpath("/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[2]/div[3]")
        for x in description:
            print(x.text)
        
        # link = driver.find_element_by_xpath("//h2[1]//a[1]")
        
        # time.sleep(4)
        
        # link.click()
        
        
        # time.sleep(4)
        # driver.back()
        
        # time.sleep(4)
        # link = driver.find_element_by_xpath("//h2[1]//a[1]")
                
        #Get title
        
        title = result.find_element_by_css_selector("h2 > a[href]").get_attribute("title")
        titles.append(title)        
        
        #Get salary info 
        
        salary = result.find_element_by_class_name('salary')
        salaries.append(salary.text)
        
        #Get location info
               
        employer = result.find_element_by_class_name('agency')
        employers.append(employer.text)
    
        
        
        #Click into title 
        
        #Get into from side panel
        
        #Main page info 
        
        #Return back to previous page
        
    j_ref = driver.find_elements_by_xpath("//dt[.='Job Ref:']/following-sibling::dd")
    for x in j_ref:
        job_ref.append(x.text)
        
    posted_date = driver.find_elements_by_xpath("//dt[.='Posted:']/following-sibling::dd")
    for x in posted_date:
        posted_dates.append(x.text)
    
    closing_date = driver.find_elements_by_xpath("//dt[.='Closing Date:']/following-sibling::dd")
    for x in closing_date:
        closing_dates.append(x.text)
    
    data = {'Job Ref': job_ref, 'Title':titles,'Employer': employers, 'Salary': salaries, 'Posted Date': posted_dates, 'Closing Date': closing_dates}
    
    df = pd.DataFrame(data)
    print(df['Job Ref'].head())

#Click on next page when there's no more page left
#print a test of the row (df.iloc[1])

finally:
    driver.quit()