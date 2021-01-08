from data.movie import Movie
import pandas as pd
import sys

movie = Movie('1754656')
df = pd.DataFrame([s.to_dict() for s in movie.reviews])

df.to_csv(str(sys.path[0]) + '/files/movie.csv')


