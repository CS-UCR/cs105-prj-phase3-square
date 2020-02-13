# cs105-prj-phase1-square

## Objective
This is our project on climate change trends. We want to analyze and see if there is a correlation between general weather tends over various areas, and what current meterologists and global warming experts are saying.

## Phase 1: Data Collection and Data Cleaning 

#### Web-crawler/scraper 
We decided to use Scrapy, a versatile web scraper useful with the framework for Python to help retrieve the data needed. In Scrapy, we built a 'climatebot' spider to crawl information necessary. We used it to get our first dataset (explained in the next paragraph). Scrapy crawled the first page, scraped the link we wanted, then extracted the data in the link from the next page and saved it as a text file to the project folder.


#### Dataset 
The first dataset we want to crawl using Scrapy is the "Climate Change: Earth Surfact Temperature Data" from the years 1750 - 2015. There is more than enough data in this dataset, and includes attributes such as date, average temperature, country, etc. There are multiple .csv files on this page, but we plan to use (at least for now) the Monthly Average Temperature Raw data file.

The second dataset we wwant to use is the ___
and we got this simply by going to the website ourselves and downloading the file and saving it into our project folder.

#### How to run the code?
1) Assuming one already has Scrapy installed (if not refer here [Scrapy Installation](http://doc.scrapy.org/en/latest/intro/install.html#intro-install) ), create your project with the command " scrapy startproject insertCleverName "

2) In the newly created directory, write your function code for your spider to crawl your dataset (refer to climatebot.py code) and save it under the spiders folder.

3) Now that your spider has been created, you are ready to crawl and retrieve information! Do this with "scrapy crawl insertNameOfSpider"

4) There you have it! You have crawled, scraped, and extracted data (depending on your spider code). 

5) To go even further into understanding what is happening, one can use the command "scrapy shell insertUrlLinkHere" and test out functions needed for scrapy to use.  If done correctly, it would look something like
![Scrapy shell](/Users/kaddy/Desktop/W2020/CS 105/Project/cs105-prj-phase1-square/images/ScrapyShell.png)