# Different statistics are available and can be applied to columns with 
# numerical data. Operations in general exclude missing data and operate 
# across rows by default.

# MEAN

import pandas as pd

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")

# MEAN
mean_of_movie_length = movies["Length"].mean()

print("The mean of length of the movies is",mean_of_movie_length,"minutes")

print("The mean of length of the movies is (rounded)",round(mean_of_movie_length,1),"minutes")

# MEDIAN
median_of_movie_length = movies["Length"].median()

print("The median of length of the movies is (rounded)",round(median_of_movie_length,1),"minutes")

# The aggregating statistic can be calculated for multiple 
# columns at the same time.
# describe() function is used to achieve it.

aggregate_stats = movies.describe()
print("The aggegate statistics for the movie statistics ", aggregate_stats)

# Aggegate statistics for length of movies
aggregate_stats_length = movies["Length"].describe()
print("The aggegate statistics for the Length of movie ", round(aggregate_stats_length,1))

# Aggegate statistics for length and rating of movies
aggregate_stats_rating = movies["Rating"].describe()
print("The aggegate statistics: Rating ", round(aggregate_stats_rating,1))

# Aggregating statistics grouped by category

movie_by_director = movies[["Genre","Rating"]].groupby("Genre").mean()
print(movie_by_director)

"""
Concepts learned
 - mean()
"""