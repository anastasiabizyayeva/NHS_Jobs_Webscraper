# NHS_Jobs_Webscraper

A selenium webscraper that pulls out pertinent job posting details from https://www.jobs.nhs.uk/. The current code creates 6000 records, though this can be easily amended.

## Running the Webscraper

This webscraper was created to look at nursing salaries, and as such there are some default parameters in the uploaded code that suit that work. Recommendations for running and amending the code can be found below:

#### Pre-Requisites

* **Python Version:** 3.9
* **Package Requirements:** Clone the repo and create a virtual environment with the packages listed in 'requirements.txt' file

#### Amending the Code 

* **PATH:** Amend to the local path of your ChromeDriver ([download here](https://sites.google.com/a/chromium.org/chromedriver/)) 
* **URL:** Amend to the search results you want to scrape. My URL was found by navigating from the NHS Jobs homepage to 'Browse Jobs' > 'Nursing' 
* **record_count:** Amend to however many records you'd like to scrape 

Once you've made these adjustments, simply run the script - you'll see printouts of progress for every 20 records scraped. 

## Resources Used

* **XPath in Selenium WebDriver:**: https://www.guru99.com/xpath-selenium.html
* **Python Selenium Tutorial:** https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ
* **Real World Example on Web Scraping with Selenium and Beautiful Soup:** https://towardsdatascience.com/real-world-example-on-web-scraping-with-selenium-and-beautiful-soup-3e615dbc1fa1* 

## Data Schema

There are 13 columns pulled by this webscraper:

| Column | Description |
| --- | --- |
| Job Ref | The record's unique NHS Jobs ID |
| Title | Title of the job posting |
| Employer | Organization posting the role |
| Salary | Per annum payment for hte role |
| Posted Date | Date role was posted on NHS Jobs |
| Closing Date | Final day for applications |
| Job Type | Whether the job is permanent, contract, etc. |
| Working Pattern | Whether a roll is full time or part time |
| Pay Scheme | Type of government pay scheme |
| Pay Band | Applies for those in the 'agenda for change' pay scheme. Values are 1 through 9 |
| Department | Which part of the organization an individual would work in |
| Location | Where the role is based |
| Description | Job description for the posting. Can be mined for keywords |

## Limitations

Because it has to click into individual pages for all the information, this isn't a very fast webscraper. It took about two hours to scrape 6000 records. A couple of other amendments can be made - please feel free to use this code as a starting place if you'd like to experiment!

* Data isn't cleaned/ formatted: I prefer to do this in a separate part of the project, but you can edit this scraper to format dates to datetime objects, clean up the salary ranges, feature engineer the location, etc. 
* There isn't an option to filter in the scraper: this project can be improved by allowing individuals to select the particular records they'd like to grab (i.e. filtering by title, location, pay band, or posting date). 
* The scraper doesn't auto-fresh: it's possible to make the scraper pull records on a periodic basis, but that was outside the scope of this project. 
