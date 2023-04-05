Twitter Scraping with MongoDB and Streamlit

Basic workflow and execution of project Twitter Scraping 

# all needed packages and lib
import all required packages and lib such as 

streamlit , pandas , json , pymongo , snscrape.modules.twitter , datatime , time , image and st_lottie

# MongoDB client connection is done
mongoDB client connection by pymongo.MongoClient

# animation hello
animation of hello by loading of json file & using st_lottie package 

# animation snow fall
snow falling animation by loading css file by using class as local_css and load the animation

main block 

# page header
giving the header name by st.markdown and editing the color , size and text 
# menu
adding menu as Twitter Scraping , About and Version 

selection of menu 

# loading of animation hello 
loaded the animation on right side of the screen 


when twitter scraping is selected then it display with 3 sub tab as Search , Display , Download 

# tab sub menu
as per selection of sub menu 
# tab1 search box
in Search allows user to enter the form deteails by hashtag or keyword , time frame and no of tweets click on submit button to fetch the data 
this will fetch the data only less than 1000 tweets 

A loading bar will appare once it finishes 

# tab2 display
It will show how many data as been fetehed 

in display sub menu it display all the feteched data as a dataframe by this we can able to sort in A-Z or Z-A formats 

# tab3 download
In download tab it will allow user to download in csv or json format 

loading bar appears for downloading 

Demo video link: https://drive.google.com/file/d/1vhtkpj8yz9tfPJaBeOtSnvOWU0s3UTbd/view?usp=sharing 
