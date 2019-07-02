
rs_dingbat = [r'[\u2700-\u27bf]']
rs_regional = [r'(?:[\U0001F1E6-\U0001F1FF]){2}']
rs_surr_pair = [r'[\U00010000-\U0010FFFF]']

keycap = [r'[\u0023\u002a\u0030-\u0039]\ufe0f?\u20e3']
misc_symbols = [r'[\u2600-\u26FF]']
cjk_letters_and_months = [
  r'\u3299',
  r'\u3297'
]
cjk_symbols_and_punctuation = [
  r'\u303d',
  r'\u3030'
]
enclosed_alphanumerics = [
  r'\u24c2'
]
enclosed_alphanumeric_supplement = [
  r'[\U0001F170-\U0001F171]',
  r'[\U0001F17E-\U0001F17F]',
  r'\U0001F18E',

  r'[\U0001F191-\U0001F19A]',

  r'[\U0001F1E6-\U0001F1FF]'
]
enclosed_ideographic_supplement = [
  r'[\U0001F201-\U0001F202]',
  r'\U0001F21A',
  r'\U0001F22F',
  r'[\U0001F232-\U0001F23A]',
  r'[\U0001F250-\U0001F251]'
]
general_punctuation = [
  r'\u203c',
  r'\u2049'
]
geometric_shapes = [
  r'[\u25aa-\u25ab]',
  r'\u25b6',
  r'\u25c0',
  r'[\u25fb-\u25fe]'
]
latin1_supplement = [
  r'\u00a9',
  r'\u00ae'
]
letter_like_symbols = [
  r'\u2122',
  r'\u2139'
]
mahjong_tiles = [
  r'\U0001F004'
]
misc_symbols_and_arrows = [
  r'\u2b05',
  r'\u2b06',
  r'\u2b07',
  r'\u2b1b',
  r'\u2b1c',
  r'\u2b50',
  r'\u2b55'
]
misc_technical = [
  r'\u231a',
  r'\u231b',
  r'\u2328',
  r'\u23cf',
  r'[\u23e9-\u23f3]',
  r'[\u23f8-\u23fa]'
]
playing_cards = [
  r'\U0001F0CF'
]
supplemental_arrows = [
  r'\u2934',
  r'\u2935'
]
arrows = [
  r'[\u2190-\u21ff]'
]
supplemental = list()
for x in (
  rs_dingbat,
  rs_regional,
  rs_surr_pair,

  keycap,
  cjk_letters_and_months,
  cjk_symbols_and_punctuation,
  enclosed_alphanumerics,
  enclosed_alphanumeric_supplement,
  enclosed_ideographic_supplement,
  general_punctuation,
  geometric_shapes,
  latin1_supplement,
  letter_like_symbols,
  mahjong_tiles,
  misc_symbols,
  misc_symbols_and_arrows,
  misc_technical,

  playing_cards,
  supplemental_arrows,
  arrows
):
    supplemental.extend(x)

pattern = '(?:' + '|'.join(supplemental) + ')'
