import os

class Config:
    SECRET_KEY = 'Secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///zatyshok.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # отримати безкоштовно: https://aistudio.google.com/app/apikey
    GEMINI_API_KEY = 'Secret_key'
    # координати Львова для погодного API
    WEATHER_LAT = 49.8397
    WEATHER_LON = 24.0297
