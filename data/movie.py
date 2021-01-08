import imdb
import random

ia = imdb.IMDb()


class Movie:
    title = ''
    description = ''
    cover_url = ''
    release_date = ''
    reviews = []
    rating = ''
    reviews_raw = []

    def __init__(self, movie_id):
        movie_info = ia.get_movie(movie_id)
        self.title = movie_info.data['original title']
        self.description = movie_info.data['plot outline']
        self.cover_url = movie_info.data['cover url']
        self.release_date = movie_info.data['original air date']
        self.rating = movie_info.data['rating']
        self.reviews_raw = ia.get_movie(movie_id, ['reviews'])['reviews']
        self._parse_reviews()

    def _parse_reviews(self):
        for item in self.reviews_raw:
            r = Review(item['content'], item['title'], item['author'], item['date'], item['rating'],
                       item['helpful'], item['not_helpful'])
            if not type(r.rating) is int:
                r.rating = int(random.randrange(1, 10))
            self.reviews.append(r)


class Review:
    content = ''
    title = ''
    author = ''
    date = ''
    rating = ''
    helpful = 0
    not_helpful = 0

    def __init__(self, content, title, author, date, rating, helpful, not_helpful):
        self.content = content
        self.title = title
        self.author = author
        self.date = date
        self.rating = rating
        self.helpful = helpful
        self.not_helpful = not_helpful

    def to_dict(self):
        return {
            'content': self.content,
            'title': self.title,
            'author': self.author,
            'date': self.date,
            'rating': self.rating,
            'helpful': self.helpful,
            'not_helpful': self.not_helpful
        }


