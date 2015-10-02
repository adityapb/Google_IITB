# Google_IITB
**Django implementation of [SearchEngine](https://github.com/adityapb/searchEngine) project.**
##About
**A search engine to search through all webpages IITB domain**<br>
There are 4 parts to the project<br>
###Crawler
It was used to get upto 2000 links and their titles by crawling the web starting from [here](http://www.iitb.ac.in). Only those links having '.iitb.ac.in' were considered.
###Extracting keywords
All words from the url as well as title were used as keywords. Also to compensate for the lack of enough keywords, edged N-grams of these words were used.
###Creating the database
The data was then arranged as 'keyword-list_of_links' table.<br>
Also pageranks were calculated using most primitive version of google's pageranking algorithm. [Learn more](https://en.wikipedia.org/wiki/PageRank)
###Searching
The user input is split in words and a list of urls is retrieved from the data. The list is then sorted first according to their pageranks then according to the number of times that link appears in the list.<br><br>
**The code for first 3 parts can be found in the [SearchEngine](https://github.com/adityapb/searchEngine) project.**
##For setting up server
The server must have python, `pyenchant` module and `django:v1.7.4` installed<br>
For setting up in localhost, run `python manage.py runserver`
