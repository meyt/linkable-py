import pytest
from linkable.validators import validate_github_mention, validate_twitter_mention


valid_global_mentions = [
  '@a',
  '@lorem',
  '@LOREM',
  '@with5'
]

invalid_global_mentions = [
  '@~!@#$%^&*()_+',
  '@',
  '@@',
  '@!@$%^&*(',
  '@یونیکد',
  '@🤵🏻'
]

valid_mentions = {
  'twitter': valid_global_mentions + [
    '@the_quick_brown_fox_jumps_over_the_lazy_dog',
    '@with_number5',
    '@with_5'
  ],
  'github': valid_global_mentions + [
    '@the-quick-brown-fox-jumps-over-the-lazy-dog',
    '@50cent'
  ]
}

invalid_mentions = {
  'twitter': invalid_global_mentions + [
    '@lorem-ipsum',
    '@50cent',
    '@with5-',
    '@-dash',
    '@dash-',
    '@dash-dash--'
  ],
  'github': invalid_global_mentions + [
    '@lorem_ipsum',
    '@_underscore',
    '@underscore_',
    '@underscore__'
  ]
}


@pytest.mark.parametrize('item', valid_mentions['github'])
def test_valid_github_mention(item):
    assert validate_github_mention(item)


@pytest.mark.parametrize('item', invalid_mentions['github'])
def test_invalid_github_mention(item):
    assert not validate_github_mention(item)


@pytest.mark.parametrize('item', valid_mentions['twitter'])
def test_valid_twitter_mention(item):
    assert validate_twitter_mention(item)


@pytest.mark.parametrize('item', invalid_mentions['twitter'])
def test_invalid_twitter_mention(item):
    assert not validate_twitter_mention(item)
