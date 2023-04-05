# all needed packages and lib
import streamlit as st
import pandas as pd
import numpy as np
import json
from streamlit_lottie import st_lottie
import time
import pymongo
from pymongo import MongoClient
from datetime import date
import snscrape.modules.twitter as sntwitter
from PIL import Image

# MongoDB client connection is done
client = pymongo.MongoClient("mongodb://localhost:27017/")
tweetdb = client.shanmu
tweetdb_main = tweetdb.project1_twitterscraping.py

# animation hello
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
lottie_coding = load_lottiefile("welcome.json")

# animation snow fall
# class for css file
def local_css(file_name):
   with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

# load the animation 
animation_symbol = "*"
st.markdown(
   f"""
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   <div class="snowflake">{animation_symbol}</div>
   """,
   unsafe_allow_html=True
)
def main():
  
  # page header
  # change of color , size and text 
  st.markdown(
        f"""    
        <h3 style='color: #CA74F3; font-size: 48px;'>Twitter Scraping</h3>    
        """,
        unsafe_allow_html=True)
  
  # menu
  tweets = 0
  menu = ["Twitter Scraping","About","Version"]
  choice = st.sidebar.selectbox("Menu",menu)

  # Menu 1 is Main Menu page 
  if choice=="Twitter Scraping":
    right_col , left_col = st.columns(2)
    # animation hello  
    with left_col:
     st_lottie(
     lottie_coding,
     speed=5,
     reverse=False,
     loop=True,
     quality="high",
     height = 350,
     width = 550,
     key = "coding",
     )
    with right_col:
   # tab sub menu
     tab1, tab2, tab3 = st.tabs(["Search", "Display", "Download"]) # total 3 sub menus
     with tab1:  
      # to change the color and size of sub menus
      st.markdown(
         f"""    
         <h3 style='color: #2A0AF7; font-size: 48px;'>Search</h3>    
         """,
         unsafe_allow_html=True)
      st.markdown(
         f"""    
         <h3 style='color: #F70A41; font-size: 30px;'>Tweet searching Form</h3>    
         """,
         unsafe_allow_html=True)
      
       # Search box 
       # Every time after the last tweet the database will be cleared for updating new scraping data
      tweetdb_main.delete_many({})

       # Form for collecting user input for twitter scrape
      with st.form(key='form1'):

      # Hashtag input
        query = st.text_input('Hashtag or keyword')

      # No of tweets for scraping
        st.write("Enter the limit for the Data Scraping: Maximum limit is 1000 tweets")
        limit = st.number_input('Insert a number',min_value=0,max_value=1000,step=5)

      # From date to end date for scraping
        st.write("Enter the Starting date to scrap the tweet data")
        start = st.date_input('Start date')
        end = st.date_input('End date')

      # Submit button to scrap
        submit_button = st.form_submit_button(label="Submit")
      if submit_button:
        st.success(f"Tweet hashtag {query} received for scraping".format(query))

        # loading progress for fectching
        'Fectching the data....'
        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
        # Update the progress bar with each iteration.
         latest_iteration.text(f'Fectching the data {i+1}')
         bar.progress(i + 1)
         time.sleep(0.03)
        '...Data fectched successfully!!!'

      # TwitterSearchScraper will scrape the data and insert into MongoDB database
      for tweet in sntwitter.TwitterSearchScraper(f'from:{query} since:{start} until:{end}').get_items():
        # To verify the limit if condition is set
         if tweets == limit:
          break
         # Stores the tweet data into MongoDB until the limit is reached
         else:      
          new = {"date":tweet.date,"id":tweet.id, "url":tweet.url, "tweet_content":tweet.content,"user":tweet.user.username,"replycount":tweet.replyCount,"retweetcount":tweet.retweetCount,"language":tweet.lang,"source":tweet.source,"like_count":tweet.likeCount}
          tweetdb_main.insert_one(new)
          tweets += 1

      # Display the total tweets scraped
      df = pd.DataFrame(list(tweetdb_main.find()))
      cnt = len(df)
      st.success(f"Total number of tweets scraped for the input query is := {cnt}".format(cnt))
    with tab2:
       st.markdown(
        f"""    
        <h3 style='color: #F7F30A; font-size: 48px;'>Display</h3>    
        """,
        unsafe_allow_html=True)
       # Save the documents in a dataframe
       df = pd.DataFrame(list(tweetdb_main.find()))
       #Dispaly the document 
       st.dataframe(df)   
    with tab3:
      col1, col2 = st.columns(2)
      # Download the scraped data as CSV
      with col1:
          st.write("Download the tweet data as CSV File")
          # save the documents in a dataframe
          df = pd.DataFrame(list(tweetdb_main.find()))
          # Convert dataframe to csv
          df.to_csv('twittercsv.csv')
          def convert_df(data):
           # Cache the conversion to prevent computation on every rerun
           return df.to_csv().encode('utf-8')
          csv = convert_df(df)
          st.download_button(
                        label="Download data as CSV",
                        data=csv,
                        file_name='twitercsv.csv',
                        mime='text/csv',
                        )
          st.success("Successfully Downloaded data as CSV")
          # loading progress for downloading
          'Downloading the data of CSV....'
          # Add a placeholder
          latest_iteration = st.empty()
          bar = st.progress(0)
          for i in range(100):
          # Update the progress bar with each iteration.
              latest_iteration.text(f'Downloading the data of CSV {i+1}')
              bar.progress(i + 1)
              time.sleep(0.01)
          '...CSV Data donwloaded successfully!!!'
          
      # Download the scraped data as JSON
      with col2:
         st.write("Download the tweet data as JSON File")
         # Convert dataframe to json string instead as json file 
         twtjs = df.to_json(default_handler=str).encode()
        # Create Python object from JSON string data
         obj = json.loads(twtjs)
         js = json.dumps(obj, indent=4)
         st.download_button(
                        label="Download data as JSON",
                        data=js,
                        file_name='twtjs.js',
                        mime='text/js',
                        
                        )
         st.success("Successfully Downloaded data as JSON")
         # loading progress for downloading
         'Downloading the data of JSON ....'
         # Add a placeholder
         latest_iteration = st.empty()
         bar = st.progress(0)
         for i in range(100):
             # Update the progress bar with each iteration.
             latest_iteration.text(f'Downloading the data of JSON {i+1}')
             bar.progress(i + 1)
             time.sleep(0.01)
         '...JSON Data donwloaded successfully!!!'
  elif choice=="About":
    st_lottie(
     lottie_coding,
     speed=5,
     reverse=False,
     loop=True,
     quality="high",
     height = 350,
     width = 550,
     key = "coding",
     )
    st.markdown(
        f"""    
        <h3 style='color: #F63366; font-size: 18px;'>About</h3>    
        """,
        unsafe_allow_html=True)  
    # Info about Twitter Scrapper
    with st.expander("Twitter Scrapper"):
      st.write('''Twitter Scrapper (or Twitter Scraper) is a type of web scraping tool used to extract data from Twitter, 
                    a popular social media platform. A Twitter scraper uses automated bots to collect large amounts of
                    data from Twitter, such as tweets, user profiles, hashtags, etc.
                    Twitter scrapers can be used for a wide range of applications, such as sentiment analysis, 
                    brand monitoring, market research, and social media analytics. By extracting data from Twitter, 
                    businesses and organizations can gain insights into consumer behavior, market trends, and public opinion''')
      # Info about Snscraper
    with st.expander("Snscraper"):
      st.write('''Snsrape Python packages used for web scraping social media platforms, including Twitter, 
                    Instagram, and facebook etc. when this module is used as twitter then this lib will fetch the data from the twitter
                    which is given by user''')
    # Info about MongoDB database
    with st.expander("MongoDB"):
      st.write('''MongoDB is a popular open-source, document-oriented NoSQL database that is used to store and manage 
                    unstructured and semi-structured data. MongoDB uses a document data model, which means that data is stored
                    in flexible, JSON-like documents, making it easy to handle and scale data..
                    when the user enters the data in the streamlit it will fetch the data through the sntwitter 
                    and display the content as dataframe ''')
    # Info about Streamlit framework
    with st.expander("Streamlit"):
      st.write('''Streamlit is a popular open-source Python library used for building interactive web applications and data visualizations. 
                    It allows you to create custom web applications with just a few lines of Python code. Streamlit provides a simple 
                    and intuitive way to create web applications by providing ready-to-use UI components and easy-to-use APIs..''')
    with st.expander("Project Video"):
      video = st.checkbox('show video')
      if video:
        img = open(r'C:\Users\shanm\Videos\Captures\Project1_twitterscraping.mp4','rb')
        st.video(img,format='video/mp4')
  elif choice=="Version": 
    st_lottie(
     lottie_coding,
     speed=5,
     reverse=False,
     loop=True,
     quality="high",
     height = 350,
     width = 550,
     key = "coding",
     )
    st.markdown(
        f"""    
        <h3 style='color: #F63366; font-size: 18px;'>Version</h3>    
        """,
        unsafe_allow_html=True) 
    # Info about Version
    with st.expander("Version"):
      st.write('''
                Project Tittle - Twitter Scrapping   

                Project By - Shanmugavel S  

                Streamlit  Version  - V1.20.0      

                Streamlit Project Version - 1.0.0 completion of project                                                           

                Streamlit Project Version - 1.0.1 adding of animation

                Streamlit Project Version - 1.0.2 adding of snowfall 

                Streamlit Project Version - 1.0.3 adding progress bar for fetching the data and downloading the data  

                Streamlit Project Version - 1.0.4 adding of video

                Streamlit Project Version - 1.0.5 moving animation to right side of screen
                ''')         
# call the function
main()