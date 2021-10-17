import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import pyautogui
from plyer import notification
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('recognition is on....')
        recognizer.pause_threshold = 0.7
        voice = re
