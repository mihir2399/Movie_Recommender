# Movie_Recommender
Movie Recommendation System
This project implements a movie recommendation system using a combination of text processing and machine learning techniques to provide personalized movie suggestions based on various attributes of movies. The system leverages metadata including movie overviews, genres, keywords, cast, and crew to calculate similarities between movies and recommend the most relevant ones.

Overview
The recommendation system is built on the following core steps:

Data Preparation:

The dataset includes movies with attributes such as movie_id, title, overview, genres, keywords, cast, and crew.
Casting Information: Extracts the names of the top three cast members from the cast data.
Director Information: Identifies the director(s) from the crew data.
Overview Processing: Converts the movie overview into a list of words for further analysis.
Tag Concatenation: Combines the processed overview, genres, keywords, cast, and crew into a unified set of tags for each movie.
Text Processing:

Lowercasing: Standardizes text by converting all tags to lowercase.
Stemming: Reduces words to their root forms using the Porter Stemmer to enhance similarity detection.
Vectorization:

Utilizes the Bag of Words model to convert text tags into numerical vectors. This method captures the frequency of words and enables the comparison of movies based on their textual content.
Similarity Calculation:

Computes the cosine similarity between movie vectors to measure how similar different movies are based on their tags.
Recommendation Function:

The core functionality of the recommendation system. It searches for the specified movie in the dataset, calculates similarity scores with other movies, and suggests the top 5 most similar movies.
Example
For instance, when querying for "The Avengers," the system might recommend films such as "Iron Man 3," "Avengers: Age of Ultron," and other related titles based on their textual similarity.

Usage
To use the recommendation system, simply call the recommend function with the name of the movie you are interested in. The system will output a list of movies that are similar to the specified one, helping you discover new films that match your taste.

