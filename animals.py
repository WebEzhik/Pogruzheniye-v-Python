#!/usr/bin/python
# -*- coding: latin-1 -*-
import argparse
import logging
from logging.handlers import RotatingFileHandler


class AnimalCreationError(Exception):
    pass


class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("??? ??????????? ????????.")


class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def display_info(self):
        print(f"??? ???? ?? ????? {self.name}. ??? ????? ? {self.habitat}.")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def display_info(self):
        print(f"??? ????? ?? ????? {self.name}. ?? ?????? ??????? ?????????? {self.wingspan}.")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, **kwargs):
        if animal_type == "Fish":
            return Fish(name, kwargs.get("habitat"))
        elif animal_type == "Bird":
            return Bird(name, kwargs.get("wingspan"))
        elif animal_type == "Animal":
            return Animal(name)
        else:
            raise AnimalCreationError(f"??? ????????? '{animal_type}' ?? ??????????????.")


def configure_logging():
    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = RotatingFileHandler("animals.log", maxBytes=100000, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(log_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def parse_args():
    parser = argparse.ArgumentParser(description="??????? ? ??????? ?????????? ? ????????")
    parser.add_argument("animal_type", help="??? ?????????: Fish, Bird ??? Animal")
    parser.add_argument("name", help="??? ?????????")
    parser.add_argument("--habitat", help="????? ???????? (???? ????)")
    parser.add_argument("--wingspan", help="?????? ??????? (???? ?????)")

    return parser.parse_args()


def main():
    configure_logging()

    args = parse_args()
    animal_type = args.animal_type
    name = args.name
    habitat = args.habitat
    wingspan = args.wingspan

    try:
        animal = AnimalFactory.create_animal(animal_type, name, habitat=habitat, wingspan=wingspan)
        logging.info(f"???????? ???????: {animal_type} ?? ????? {name}")
        animal.display_info()

    except AnimalCreationError as e:
        logging.error(f"?????? ??? ???????? ?????????: {e}")
        print(f"?????? ??? ???????? ?????????: {e}")


if __name__ == "__main__":
    main()

# ??????: python animals.py Bird ???? --wingspan "2 ?????"