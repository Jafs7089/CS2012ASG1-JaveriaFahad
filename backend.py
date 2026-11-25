import csv
import json
from abc import ABC, abstractmethod
from datetime import datetime


class InvalidTransactionError(Exception):
    pass


class Transaction(ABC):
    def __init__(self, city, date, time, amount, status):
        self._city = city
        self._date = date
        self._time = time
        self.amount = amount
        self._status = status

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value