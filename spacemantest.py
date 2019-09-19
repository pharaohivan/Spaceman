import unittest
from spaceman import is_word_guessed
from spaceman import get_guessed_word
from spaceman import is_guess_in_word



class spaceman_test(unittest.TestCase):

    def test_is_word_guessed(self):
        assert is_word_guessed('dog', 'cat') is False

    def test_get_guessed_word(self):
        assert get_guessed_word('cat', ['t','a']) == "_ a t "

    def test_is_guess_in_word(self):
        assert is_guess_in_word('a', ['c', 'a', 't']) is True






if __name__ == '__main__':
    unittest.main()
