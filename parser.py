from bs4 import BeautifulSoup
import requests
import openpyxl

class Rating:
    def __init__(self, movie_title, rating, date):
        self.movie_title = movie_title
        self.rating = rating
        self.date = date


def get_user_ratings(user_id=2054122):
    user_url = f'https://www.kinopoisk.ru/user/2054122/votes/'
    response = requests.get(user_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('div', class_='profileFilmsList')
    entries = table.find_all('div', class_='item')

    ratings = []
    for entry in entries:
        movie_title = entry.find('div', class_='nameRus').text.strip()
        rating = entry.find('div', class_='vote').text.strip()
        date = entry.find('div', class_='date').text
        ratings.append(Rating(movie_title, rating, date))

    return ratings


def save_data_to_excel(data, filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Название фильма', 'Рейтинг', 'Дата оценки'])
    for rating in data:
        ws.append([rating.movie_title, rating.rating, rating.date])
    wb.save(filename)