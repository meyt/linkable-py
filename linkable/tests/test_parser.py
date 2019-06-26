import pytest
from linkable import Linkable, LinkableList

matches = [
    [
        'one linear demo with #hashtag',
        'one linear demo with <a href="/hashtag/#hashtag">#hashtag</a>',
        dict(hashtags=1, emails=0, urls=0, mentions=0)
    ],
    [
        'یک متن با محتوای #یونیکد',
        'یک متن با محتوای <a href="/hashtag/#یونیکد">#یونیکد</a>',
        dict(hashtags=1, emails=0, urls=0, mentions=0)
    ],
    [
        'یک متن با لینک https://example.com',
        'یک متن با لینک <a href="https://example.com">https://example.com</a>',
        dict(hashtags=0, emails=0, urls=1, mentions=0)
    ],
    [
        'a link https://example.com',
        'a link <a href="https://example.com">https://example.com</a>',
        dict(hashtags=0, emails=0, urls=1, mentions=0)
    ],
    [
        'link https://example.com and @ mention @mention',
        'link <a href="https://example.com">https://example.com</a> '
        'and @ mention <a href="/@mention">@mention</a>',
        dict(hashtags=0, emails=0, urls=1, mentions=1)
    ],
    [
        'link https://example.com and @ mention @mention و یک #tag_ and'
        ' email@x.co',
        'link <a href="https://example.com">https://example.com</a> and '
        '@ mention <a href="/@mention">@mention</a> و یک '
        '<a href="/hashtag/#tag_">#tag_</a> and <a href="mailto:email@x.co">'
        'email@x.co</a>',
        dict(hashtags=1, emails=1, urls=1, mentions=1)
    ],
    [
        'a link with https://example.com\n@newline_mention',
        'a link with <a href="https://example.com">https://example.com</a>'
        '\n<a href="/@newline_mention">@newline_mention</a>',
        dict(hashtags=0, emails=0, urls=1, mentions=1)
    ],
    [
        'a link with https://example.com\r\n@newline_mention',
        'a link with <a href="https://example.com">https://example.com</a>'
        '\r\n<a href="/@newline_mention">@newline_mention</a>',
        dict(hashtags=0, emails=0, urls=1, mentions=1)
    ],
    [
        'one linear demo with (#hashtag)',
        'one linear demo with (<a href="/hashtag/#hashtag">#hashtag</a>)',
        dict(hashtags=1, emails=0, urls=0, mentions=0)
    ],
    [
        'one linear demo with google.com URL',
        'one linear demo with <a href="http://google.com">google.com</a> URL',
        dict(hashtags=0, emails=0, urls=1, mentions=0)
    ],
    [
        'is this a #hashtag?',
        'is this a <a href="/hashtag/#hashtag">#hashtag</a>?',
        dict(hashtags=1, emails=0, urls=0, mentions=0)
    ],
    [
        'brackets (@a) {#b} 《@c》 ⟨@d⟩ [@e]?',
        'brackets '
        '(<a href="/@a">@a</a>) '
        '{<a href="/hashtag/#b">#b</a>} '
        '《<a href="/@c">@c</a>》 '
        '⟨<a href="/@d">@d</a>⟩ '
        '[<a href="/@e">@e</a>]?',
        dict(hashtags=1, emails=0, urls=0, mentions=4)
    ],
    [
        'guillemets ‹@a› <@b> «#c»?',
        'guillemets '
        '‹<a href="/@a">@a</a>› '
        '<<a href="/@b">@b</a>> '
        '«<a href="/hashtag/#c">#c</a>»?',
        dict(hashtags=1, emails=0, urls=0, mentions=2)
    ],
    [
        'quotations ‘@a’ “@b” \'#c\' "@d" „@e“ “@f”',
        'quotations '
        '‘<a href="/@a">@a</a>’ '
        '“<a href="/@b">@b</a>” '
        '\'<a href="/hashtag/#c">#c</a>\' '
        '"<a href="/@d">@d</a>" '
        '„<a href="/@e">@e</a>“ '
        '“<a href="/@f">@f</a>”'
        ,
        dict(hashtags=1, emails=0, urls=0, mentions=5)
    ],
    [
        'is this a #hashtag? #or_hashtag!!!!!',
        'is this a <a href="/hashtag/#hashtag">#hashtag</a>? '
        '<a href="/hashtag/#or_hashtag">#or_hashtag</a>!!!!!',
        dict(hashtags=2, emails=0, urls=0, mentions=0)
    ],
    [
        'is this a ###hashtag? #or_hashtag!!!!!',
        'is this a ##<a href="/hashtag/#hashtag">#hashtag</a>? '
        '<a href="/hashtag/#or_hashtag">#or_hashtag</a>!!!!!',
        dict(hashtags=2, emails=0, urls=0, mentions=0)
    ],
    # Tags should separate with spaces
    [
        'is this a#hashtag?',
        'is this a#hashtag?',
        dict(hashtags=0, emails=0, urls=0, mentions=0)
    ],
    [
        'is this #hashtag#another',
        'is this #hashtag#another',
        dict(hashtags=0, emails=0, urls=0, mentions=0)
    ],
    # Start with hashtag
    [
        '#hashtag is coming...',
        '<a href="/hashtag/#hashtag">#hashtag</a> is coming...',
        dict(hashtags=1, emails=0, urls=0, mentions=0)
    ],
    [
        '#hashtag! is coming...',
        '<a href="/hashtag/#hashtag">#hashtag</a>! is coming...',
        dict(hashtags=1, emails=0, urls=0, mentions=0)
    ]
]


# noinspection PyTypeChecker
@pytest.mark.parametrize('text, output, attributes', matches)
def test_parser(text, output, attributes: dict):
    assert Linkable(text) == output
    assert Linkable(text).__repr__() == output

    linkable_list = LinkableList(text)
    assert len(linkable_list.hashtags) == attributes['hashtags']
    assert len(linkable_list.mentions) == attributes['mentions']
    assert len(linkable_list.emails) == attributes['emails']
    assert len(linkable_list.urls) == attributes['urls']
    assert len(linkable_list.links) == sum(
        map(lambda x: attributes[x], attributes.keys())
    )
