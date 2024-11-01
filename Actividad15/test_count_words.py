# test_count_words.py

from count_words import CountWords

def test_two_words_ending_with_s():
    words = CountWords().count("dogs cats")
    assert words == 2

def test_no_words_at_all():
    words = CountWords().count("dog cat")
    assert words == 0

def test_words_that_end_in_r():
    words = CountWords().count("car bar")
    assert words == 2

def test_mixed_endings():
    words = CountWords().count("car cats")
    assert words == 2

def test_word_ending_with_s_at_end():
    words = CountWords().count("cats")
    assert words == 1

def test_non_alpha_characters():
    words = CountWords().count("dogs, cats.")
    assert words == 2

def test_empty_string():
    words = CountWords().count("")
    assert words == 0

def test_only_non_alpha():
    words = CountWords().count("!!!")
    assert words == 0

def test_word_notfinishinrs():
    words = CountWords().count("carrot,chicken")
    assert words == 0

def test_word_withdifferentwords():
    words = CountWords().count("chicken, cats, rabbit ")
    assert words == 1