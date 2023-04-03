Twitter Scraping with MongoDB and Streamlit

Basic workflow and execution of project Twitter Scraping 

import all required packages and lib such as 

streamlit , pandas , json , pymongo , snscrape.modules.twitter , datatime , time , image and st_lottie

mongoDB client connection by pymongo.MongoClient

animation of hello by loading of json file & using st_lottie package 

snow falling animation by loading css file by using class as local_css 

main block 

giving the header name by st.markdown and editing the color , size and text 

adding menu as Twitter Scraping , About and Version 

selection of menu 

when main menu is selected then it display with 3 sub tab as Search , Display , Download 

as per selection of sub menu 

in Search allows user to enter the form deteails by hashtag or keyword , time frame and no of tweets click on submit button to fetch the data 
this will fetch the data only less than 1000 tweets 

A loading bar will appare once it finishes 

It will show how many data as been fetehed 

in display sub menu it display all the feteched data as a dataframe by this we can able to sort in A-Z or Z-A formats 

In download tab it will allow user to download in csv or json format 











Demo video link1:  https://drive.google.com/file/d/1cBIDjZSL8cnfRjFCSBFZEAx79JYFUgKS/view?usp=sharing

Demo video link 2: https://drive.google.com/file/d/1o500mRYG_t_S-91GMOCk2SooOQ6YFhuT/view?usp=sharing
