from .main import Cysgor


def get_score(text):
    cysgor = Cysgor(text)
    return cysgor.find_errors().score


def get_mistakes(text):
    cysgor = Cysgor(text)
    return cysgor.find_errors().mistakes
