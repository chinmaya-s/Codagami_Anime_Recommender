# Anime Data Analysis and Recommendation System

## Authors
### Group-15

| Name | Roll no | Email | 
| --------- | ----- | -------- |
| Chinmaya Singal | 180207 | chinmaya@iitk.ac.in |
| Dipesh Khandelwal  | 180249 | dipeshk@iitk.ac.in |
| Rythm Agarwal | 180636 | rythm@iitk.ac.in |
| Sakshi | 180653 | sakshisa@iitk.ac.in |
| Sarthak Dubey | 180674 | srthkdb@iitk.ac.in |

## Description
This is the project of group-15 for the course CS685. In this project, we have analysed the data available on [MyAnimeList](https://myanimelist.net/) and tried to get some insights related to the growth of anime over time, genres, studios, etc. Along with that, we have also built anime recommendation systems using different models to provide both content based and collaborative filtering based recommendations to users.
Steps to create python virtual environment

## Requirements
- Python 3.8.10
- Java (openjdk version 1.8.0_292) (Only for ALS recommendation system)
- Python modules are listed in requirements.txt

## Install
```bash
$ python3 -m venv env
$ pip install -r requirements.txt 
```

## Usage

### Data retrieval scripts

### Data analysis scripts
The data analysis plots are generated through Python scripts.
Theses scripts can be run by using the following cmd:
```bash
$ python <script_name.py>
```
The output plots are stored in outputs/ directory.
The details of various data analysis scripts are summarized in a table below.

| File Name | Description | Outputs | 
| --- | ----------- | ---- |
| age_rating_trends.py | Plots the trends of age rating groups on various variables | rating_vs_num_list_users.jpeg, rating_vs_num_episodes.jpeg, rating_vs_average_episode_duration.jpeg, rating_vs_mean.jpeg, rating_vs_rank.jpeg, rating_count.jpeg, rating_vs_popularity.jpeg, rating_num_anime_vs_year.jpeg  |        
| most_viewed_anime_trends.py | | |
| anime_count_vs_year.py | Plots the number of anime released every year | num_anime_vs_year.jpeg  |      
| rank_vs_popularity.py | | |
| anime_vs_related.py | | |         
| source_trends.py | | |
| distribution_of_ratings.py | | |  
| source_vs_popularity_rating.py | | |
| starting_date_vs_rating.py | | |
| genre_analysis.py | | |           
| studio_production_trends.py | | |
| genre_pop_time_analysis.py | | |  
| studio_trends.py | | |
| genre_trend.py | | |              
| length_of_anime_trends.py | | |   


### Recommendation systems

## Data

## Project Structure
