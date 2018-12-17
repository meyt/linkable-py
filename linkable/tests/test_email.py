import pytest
from linkable.validators import validate_email


valid_items = (
    'email@here.com',
    'weirder-email@here.and.there.com',
    'email@[127.0.0.1]',
    'example@valid-----hyphens.com',
    'example@valid-with-hyphens.com',
    'test@domain.with.idn.tld.उदाहरण.परीक्षा',
    'تست@example.co'
)

invalid_items = (
    '',
    'abc',
    'abc@',
    'abc@bar',
    'a @x.cz',
    'abc@.com',
    'something@@somewhere.com'
)


@pytest.mark.parametrize('item', valid_items)
def test_valid_email(item):
    assert validate_email(item)


@pytest.mark.parametrize('item', invalid_items)
def test_invalid_email(item):
    assert not validate_email(item)
