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
- Jupyter notebook

## Install
```bash
$ python3 -m venv env
$ pip install -r requirements.txt 
```

## Usage

### Data analysis scripts
The data analysis plots are generated through Python scripts.
Theses scripts can be run by using the following cmd:
```bash
$ python <script_name.py>
```
The output plots are stored in outputs/ directory.
The details of various data analysis scripts are summarized in a table below.

| File Name | Description | Outputs | 
| --- | ------------ | ------ |
| age_rating_trends.py | Plots the trends of age rating groups on various variables | rating_vs_num_list_users.jpeg, rating_vs_num_episodes.jpeg, rating_vs_average_episode_duration.jpeg, rating_vs_mean.jpeg, rating_vs_rank.jpeg, rating_count.jpeg, rating_vs_popularity.jpeg, rating_num_anime_vs_year.jpeg  |        
| most_viewed_anime_trends.py | Plots number of animes produced of each media type and viewership of animes based on media type| animes_based_on_media_type_trends.jpeg, media_type_trends_based_on_users.jpeg |
| anime_count_vs_year.py | Plots the number of anime released every year | num_anime_vs_year.jpeg  |      
| rank_vs_popularity.py | Analyzes correlation between rank and popularity | rank_vs_popularity.jpg, rank_vs_popularity_first100.jpg|
| anime_vs_related.py | Calculates the Pearson Correlation Coefficient of the rating and number of viewers of an anime with respect to the same for related anime. The calculation is done in 2 parts considering 4000 anime in each for efficient computation. | The Pearson Correlation Coefficient and p-value are output directly on the terminal |         
| source_trends.py | Plots anime trends based on source over years and rank vs. popularity | source_count.jpeg, source_num_anime_vs_year.jpeg, source_vs_popularity.jpeg, source_vs_rank_and_pop.jpeg |
| distribution_of_ratings.py | Plots the frequency of each rating as given by the viewers to various anime. | distribution_of_scores.jpg |  
| source_vs_popularity_rating.py | Plots popularity, ranking and average rating trends based on source of anime | source_vs_popularity.jpg, source_vs_ranking.jpg, source_vs_average_rating.jpg |
| starting_date_vs_rating.py | Plots the rating trends of animes with respect to the their starting year | all-2.jpeg, choosy-2.jpeg |
| genre_analysis.py | Plots genre-wise anime count and users. Also generates a comparative plot for production count vs viewer count for each genre| most_common_genre.jpg, most_watched_genre.jpg, genre_popularity_vs_number.jpg |           
| studio_production_trends.py | Plots the number of animes produced by studio over time which is given as input though a list in the code| plot_anime_vs_year.jpeg|
| genre_pop_time_analysis.py | Plots the year-wise number of viewers of genres | genre_popularity_time_analysis.jpg |  
| studio_trends.py | Plots the number of animes produced by studios, viewership(average number of viewers of each anime) of studios, average rating of animes produced by studios | plot_animes.jpeg, plot_users.jpeg, plot_rating.jpeg, plot_users_top_studios.jpeg, plot_rating_top_studios.jpeg|
| genre_trend.py | Plots genre trends year-wise, similarity in rank and popularity | genre_count.jpeg, genre_num_anime_vs_year.jpeg, genre_vs_popularity.jpeg, genre_vs_rank_and_pop.jpeg |              
| length_of_anime_trends.py | Plots the average rating of anime over time belonging to different categories based on number of episode. Also outputs csv files containing aggregate data for anime belonging to different categories based on number of episodes. | length-of-anime-trends.csv (excludes OVA, Specials and Music), length-of-anime-trends-untrimmed.csv, all-3-len-anime{episode range}.jpeg, choosy-3-len-anime{episode range}.jpeg where episode range lies in {0-9, 10-19, 20-29, 30-49, 50-99, 100-199, 200-499, 500-999, 1000+}|  


### Recommendation systems
#### SVD
We used item-based collaborative filtering with Singular Value Decomposition to build our recommendation system. Collaborative filtering is a method to predict a rating for a user item pair based on the history of ratings given by the user to the item. We used the SVD matrix factorisation to find the user-rating matrix and used cosine similarity for finding best matches. We make use of CUDA from PyTorch for faster implementation of SVD.
##### Usage
*File*: SVD_recommender.ipynb <br />
*Get recommendations*: Go to the cell labelled __Make Recommendations__ . Add the anime name you want recommendations for in `anime_name` variable in the cell, numbr of recommndations in `top_n` variable in the cell and run the cell. The recommendations will be printed below the cell.

#### KNN
We used item-based collaborative filtering with KNN to build our recommendation system. KNN is a non-parametric, lazy learning method. It uses a database in which the data points are separated into several clusters to make inferences for new samples. We used cosine similarity for the nearest neighbor search.
##### Usage
*File*: KNN_recommender.ipynb <br />
*Get recommendations*: Go to the cell labelled __Make Recommendations__ . Add the anime name you want recommendations for in `my_favourite` variable in the cell, and run the cell. The recommendations will be printed below the cell.

#### ALS
The Alternating Least Square (ALS) algorithm is a matrix factorization approach that runs in parallel. ALS is built for large-scale collaborative filtering tasks and is implemented in Apache Spark ML. ALS does a decent job of dealing with the Ratings-data's scalability and sparseness, and it's simple and scales well to very big datasets.
##### Usage
*File*: ALS_recommender.ipynb <br />
*Get recommendations*: Go to the cell labelled __Make Recommendations__ . Add the anime name you want recommendations for in `my_anime_list` variable in the cell, and run the cell. The recommendations will be printed below the cell.

#### TF-IDF 
Term Frequency — Inverse Document Frequency (TF-IDF) based recommendation systems are content based recommenders. This method primarily uses the synopsis of an anime to provide recommendation by assigning importance to words mentioned in synopsis with more importance to words mentioned less commonly among all synopsis.

##### Usage
*File*: tf_idf_syn_gen_rate.py <br />
*Get recommendations*: Run the following bash command replacing <anime_name_i> (i is a number) by the name of the anime for which you want recommendations. The anime name should be the same as it is on MyAnimeList. Recommendations for multiple anime can be obtained by entering multiple names separated by a whitespace.
```bash
$ python3 tf_idf_syn_gen_rate.py "<anime_name_1>" "<anime_name_2>" ... "<anime_name_n>"
``` 
The above recommender uses the synopsis, genre and rating of an anime to make suggestion. You can also use tf_idf_synopsis_recommender.py for only synopsis based recommendation and tf_idf_syn_genre_recommender.py for only synopsis and genre based recommendation.

## Data
The dataset we used for our project is the [MyAnimeList](https://myanimelist.net/) dataset. To retrieve the data corresponding to each anime and users on MyAnimeList, we used the official MyAnimeList API, the documentation for it can be found at [MAL API](https://myanimelist.net/apiconfig/references/api/v2).

The data we obtained can be found [here](https://drive.google.com/drive/folders/1asYoWIx1hm156rqrCEhDpxjV0ldF3CYD?usp=sharing).

The data files need to be put in the data directory in order to run the scripts.

### Data retrieval Scripts
- __Scraping Valid Anime IDs:__ Valid anime IDs can be found [here](https://myanimelist.net/info.php?search=\%25\%25\%25&go=relationids&divname=relationGen1). 
script used to scrape the data is *extract_valid_anime_ids.py*
- __Fetch Anime Data:__ *fetch_api.py* fetches anime data from anime IDs.
- __Fetch Username Data:__ *username_fetch.py* Fetches list of usernames using BFS on friend list of a root user. Since the official MAL API doesn't currently provide support for fetching friend list of a user, we had to use an unofficial API whose documentation can be found at [Jikan API](https://jikan.moe/).
- __Fetch User Data:__ *user_data_fetch.py* fetches the details of users from username.
  