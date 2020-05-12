import requests
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediaMixr.settings')

import django
django.setup()
from accounts.models import *
from recommendation.models import *
import random
genres = [
              'Action/Adventure',
              'Action/Adventure',
              'Action/Adventure',
              'Horror',
              'Horror',
              'Horror',
              'Fantasy',
              'Fantasy',
              'Fantasy',
              'Science Fiction',
              'Science Fiction',
              'Science Fiction',
              'Sports',
              'Sports',
              'Sports',
              'Mystery',
              'Mystery',
              'Mystery',
              'Historical Fiction',
              'Historical Fiction',
              'Historical Fiction',
              'Steampunk',
              'Steampunk',
              'Steampunk',
              'Military Fiction',
              'Military Fiction',
              'Military Fiction'
    ]


def add_tvshows():
    tv_shows = ['The Flash',
                'Jack Ryan',
                'Agents of S.H.I.E.L.D',
                'The Terror',
                'The Walking Dead',
                'Black Mirror',
                'The Witcher',
                'Game of Thrones',
                'The Last Kingdom',
                'The Mandalorian',
                'Doctor Who',
                'The Expanse ',
                'NFL Sunday',
                'Around the Horn',
                'SportsCenter',
                'True Detective',
                'Criminal Minds ',
                'Sherlock',
                'Vikings',
                'Outlander',
                'Medici',
                'Carnival Row',
                'Sanctuary',
                'Penny Dreadful',
                'The Last Ship',
                'The Brave',
                'SEAL Team']
    publishers = ['CW',
                  'Amazon',
                  'ABC',
                  'AMC',
                  'AMC',
                  'Netflix',
                  'Netflix',
                  'HBO',
                  'Netflix',
                  'Disney +',
                  'BBC',
                  'Amazon',
                  'FOX',
                  'ESPN',
                  'ESPN',
                  'HBO',
                  'CBS',
                  'BBC',
                  'Netflix',
                  'STARZ',
                  'Big Light',
                  'Amazon',
                  'SyFy',
                  'Showtime',
                  'TNT',
                  'Universal',
                  'CBS']
    interest = Interest.objects.get(name='TV Shows')
    for show, publisher, genre_name in zip(tv_shows,publishers,genres):
        genre = Genre.objects.get(name = genre_name)
        s = Media(title=show, creator=publisher,genre=genre, type=interest)
        print('adding TV shows')
        s.save()

def add_books():
    books = ["The Way of Shadows",
             "Six of Crows",
             "Divergent",
             "The Necronomicon",
             "Christine",
             "The Exorcist",
             "The Name of the Wind",
             "Assassin's Apprentice",
             "The Last Wish",
             "Ender's Game",
             "Dune",
             "Foundation",
             "The Great American Novel",
             "The Boys of Summer",
             "Where Dreams Die Hard",
             "Hound of the Baskervilles",
             "Murder on the Orient Express ",
             "Rebecca",
             "A Gentleman in Moscow",
             "A Rising Man",
             "Alias Grace",
             "Airman",
             "His Dark Materials",
             "The Lies of Locke Lamora",
             "The Things They Carried",
             "Patriot Games",
             "All Quiet on the Western Front",]
    authors = ["Brent Weeks",
               "Leigh Bardugo",
               "Veronica Roth",
               "H.P. Lovecraft",
               "Stephen King",
               "William Peter Blatty",
               "Patrick Rothfuss",
               "Robin Hobb",
               "Andrzej Sapkowski",
                "Orson Scott Card",
                "Frank Herbert",
                "Isaac Asimov",
               "Philip Roth",
               "Roger Kahn",
               "Carlton Stowers",
               "Arthur Conan Doyle",
               "Agatha Christie",
               "Daphne du Maurier",
                "Amor Towles",
                "Abir Mukherjee",
                "Margaret Atwood",
                "Eoin Colfer",
                "Philip Pullman",
                "Scott Lynch",
               "Tim O'Brien",
               "Tom Clancy",
               "Erich Maria Remarque",
               ]
    interest = Interest.objects.get(name='Books')
    for book, author,genre_name in zip(books,authors, genres):
        genre = Genre.objects.get(name = genre_name)
        b = Media(title=book, creator=author, genre=genre, type=interest)
        print('adding books')
        b.save()

def add_movies():
    movies = ['Avengers: Infinity War',
              'Mad Max:Fury Road',
              'Mission Impossible',
              'A Quiet Place',
              'Get Out',
              'It',
              'The Lord of the Rings',
              "Pan’s Labyrinth",
              'The Princess Bride',
              'The Martian',
              'Blade Runner 2049',
              'Interstellar',
              'Moneyball',
              'The Blindside',
              'Miracle',
              'Gone Girl',
              'Wind River',
              'Zodiac',
              'First Man',
              'The King’s Speech',
              'The Darkest Hour',
              'Hugo ',
              'Van Helsing',
              'The Goldan Compass',
              'Full Metal Jacket',
              'American Sniper',
              'War Horse']
    studios = ['Marvel',
               'WB Studios',
               'Skydance'
               'Platinum Dunes',
               'Blumhouse',
               'New Line Cinema',
               'New Line Cinema',
               'WB',
               'Act III Communications',
               'Scott Free Productions',
               'Columbia Pictures',
               'Legendary Pictures',
               'Plan B Entertainment',
               'Alcon Entertainment',
               'Buena Vista Pictures',
               'Regency Enterprises',
               'Acacia Entertainment ',
               'Pheonix Pictures',
               'Universal Pictures',
               'Momentum Pictures',
               'Perfect World Pictures',
               'GK Films',
               'Sommers Company',
               'New Line Cinema',
               'Harrier Films',
               'Village Roadshow Pictures',
               'Touchstone Pictures']
    interest = Interest.objects.get(name='Movies')
    for movie,studio,genre_name in zip(movies,studios, genres):
        genre = Genre.objects.get(name = genre_name)
        m = Media(title=movie, creator=studio, genre=genre, type=interest)
        print('adding movies')
        m.save()

def add_games():
    games = ['Uncharted',
             'Tomb Raider',
             'Infamous',
             'Silent Hill',
             'Amnesia',
             'Dead Space',
             'The Witcher 3: Wild Hunt',
             'The Legend of Zelda: Breath of the Wild',
             'Dragon’s Dogma',
             'Deus Ex: Human Revolution',
             'Mass Effect',
             'No Man’s Sky',
             'FIFA',
             'MLB: The Show',
             'Madden NFL',
             'Alan Wake',
             'Heavy Rain',
             'LA Noire',
             'Assassin’s Creed',
             'Command and Conquer',
             'Valiant Hearts: The Great War',
             'Dishonored',
             'Bioshock',
             'The Order: 1886',
             'Call of Duty: Modern Warfare',
             'Medal of Honor',
             'Red Orchestra 2']
    developer = ['Sony',
                 'SQUARE ENIX',
                 'Suckerpunch',
                 'Konami',
                 'Frictional Games',
                 'EA',
                 'CD Projekt RED',
                 'Nintendo',
                 'Capcom',
                 'Eidos Montreal',
                 'Bioware',
                 'Hello Games',
                 'EA',
                 'Sony',
                 'EA',
                 'Remedy Entertainment',
                 'Quantic Dream',
                 'Rockstar Games',
                 'Ubisoft',
                 'EA',
                 'Ubisoft',
                 'Arcane Studios',
                 '2K',
                 'Sony',
                 'Infinity Ward',
                 'Danger Close Games',
                 'Tripwire Interactive',
                 ]
    interest = Interest.objects.get(name='Video Games')
    for game, developer,genre_name in zip(games,developer,genres):
        genre = Genre.objects.get(name = genre_name)
        vg = Media(title=game, creator=developer, genre=genre, type=interest)
        print('adding video games')
        vg.save()

def add_interests():
    interests = ['Books', 'Movies', 'TV Shows', 'Video Games']
    for interest in interests:
        i = Interest(name = interest)
        print('adding interests')
        i.save()

def add_genres():
    genres = ['Action/Adventure', 'Horror', 'Fantasy', 'Science Fiction', 'Sports', 'Mystery', 'Historical Fiction','Steampunk','Military Fiction']
    for genre in genres:
        g = Genre(name = genre)
        print('adding genres')
        g.save()

add_interests()
add_genres()

add_books()
add_movies()
add_tvshows()
add_games()
