import pytest
from linkable.validators import validate_hashtag
from linkable.tests.helpers.unicode_emoji import emoji
from linkable.tests.helpers.unicode_emoji_sequences import emoji_sequences

valid_items = (
    '#lorem',
    '#LOREM',
    '#نمیشود',
    '#گنجشک',
    '#می‌شود',
    '#the_quick_brown_fox_jumps_over_the_lazy_dog',
    '#Lorem_a',
    '#\uD83D\uDCA9',
    '＃lorem_ipsum'
)


invalid_items = (
    '#5',
    '#d-a',
    '#~!@#$%^&*()_+',
    '#',
    '##',
    '##lorem',
    '####lorem',
    '#️⃣false',
    '＃＃',
    '＃##️⃣',
    '###️⃣',
    '#@',
    '#!@$%^&*('
)


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation_emoji = ['‼', '〽', '〰', '⁉', '‼']
punctuation = ['*', '#']


@pytest.mark.parametrize('item', valid_items)
def test_valid_hashtag(item):
    assert validate_hashtag(item)


@pytest.mark.parametrize('item', invalid_items)
def test_invalid_hashtag(item):
    assert not validate_hashtag(item)


@pytest.mark.parametrize('item', emoji)
def test_hashtag_with_emoji(item):
    item = chr(item)
    exclusions = numbers + punctuation_emoji + punctuation
    if item in exclusions:
        return

    assert validate_hashtag('#%s' % item)


@pytest.mark.parametrize('item', emoji_sequences)
def test_hashtag_with_emoji_sequences(item):
    assert validate_hashtag('#%s' % item)
