from linkable import patterns, validators
from linkable.helpers import LazyAttribute


class Linkable:
    _validators_list = (
        'hashtag',
        'mention',
        'email',
        'url'
    )

    def __init__(self, text, mention_style: str='twitter'):
        self.mention_style = mention_style
        self.text = text
        self.validators = dict(
            email=validators.validate_email,
            url=validators.validate_url,
            hashtag=validators.validate_hashtag,
            mention=(
                validators.validate_twitter_mention
                if self.mention_style == 'twitter' else
                validators.validate_github_mention
            )
        )

    def __str__(self):
        return self.replaced_text

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other

    @LazyAttribute
    def replaced_text(self):
        return self.replace_links(self.text)

    def replace_links(self, text):
        result = patterns.word_pattern.sub(
            self.replacer, text)
        result = patterns.word_between_punctuations.sub(
            self.replacer, result)
        return result

    def replacer(self, match):
        value = match.group()

        hashtag_match = patterns.hashtag_with_end_punctuations.match(value)
        if (
            hashtag_match is not None and
            self.validators['hashtag'](hashtag_match.group(1))
        ):
            return patterns.hashtag_with_end_punctuations.sub(
                lambda x: self.replace_hashtag(x.group()), value
            )

        for validator_name in self._validators_list:
            if self.validators[validator_name](value) is not False:
                return getattr(
                    self, 'replace_%s' % validator_name
                )(value)
        return value

    def replace_hashtag(self, value):
        return '<a href="/hashtag/{value}">{value}</a>'.format(value=value)

    def replace_mention(self, value):
        return '<a href="/{value}">{value}</a>'.format(value=value)

    def replace_url(self, value):
        url = value
        if patterns.url_scheme_pattern.match(url) is None:
            url = 'http://' + url
        return '<a href="{url}">{value}</a>'.format(url=url, value=value)

    def replace_email(self, value):
        return '<a href="mailto:{value}">{value}</a>'.format(value=value)


class LinkableList(Linkable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hashtags = []
        self.mentions = []
        self.urls = []
        self.emails = []
        self.replace_links(self.text)

    def replace_mention(self, value):
        self.mentions.append(value)
        return super().replace_mention(value)

    def replace_hashtag(self, value):
        self.hashtags.append(value)
        return super().replace_hashtag(value)

    def replace_email(self, value):
        self.emails.append(value)
        return super().replace_email(value)

    def replace_url(self, value):
        self.urls.append(value)
        return super().replace_url(value)

    @property
    def links(self):
        return self.hashtags + self.mentions + self.urls + self.emails
