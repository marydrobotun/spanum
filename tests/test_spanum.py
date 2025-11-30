import csv
import pytest
from spanum.numbers_to_words import number_to_words
from spanum.words_to_numbers import words_to_number


def load_test_data():
    data = []
    with open("tests/test_data.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            number = int(row["number"])
            words = row["words"]
            data.append((number, words))
    return data


@pytest.mark.parametrize("number,words", load_test_data())
def test_number_to_words(number, words):
    assert number_to_words(number) == words


@pytest.mark.parametrize("number,words", load_test_data())
def test_words_to_number(number, words):
    assert words_to_number(words) == number
