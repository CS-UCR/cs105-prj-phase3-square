# cs105-prj-phase1-square

## Objective
This is our project on climate change trends. We want to analyze and see if there is a correlation between general weather tends over various areas, and what current meterologists and global warming experts are saying.

## Phase 1 

### Extracted Data 



#### Web-crawler/scraper 
We decided to use Scrapy, a versatile web scraper useful with the framework for Python to help retrieve the data needed. In Scrapy, we built a 'climatebot' spider to crawl information necessary. We used it to get our first dataset (explained in the next paragraph). Scrapy crawled the first page, scraped the link we wanted, then extracted the data in the link from the next page and saved it as a text file to the project folder.


#### Dataset 
The first dataset we want to crawl using Scrapy is the "Climate Change: Earth Surfact Temperature Data" from the years 1750 - 2015. There is more than enough data in this dataset, and includes attributes such as date, average temperature, country, etc. There are multiple .csv files on this page, but we plan to use (at least for now) the Monthly Average Temperature Raw data file.

The second dataset we wwant to use is the ___
and we got this simply by going to the website ourselves and downloading the file and saving it into our project folder.

#### How to run the code?
1) 