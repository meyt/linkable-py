import re
from os.path import join, dirname


class Emoji:

    def __init__(self, code_points, name=None):
        self.code_points = code_points
        self.name = name

    def __repr__(self):
        return ''.join([chr(x) for x in self.code_points])


class Emojies(list):

    def load_from_testfile(self, filename=None):
        # https://unicode.org/Public/emoji/12.0/emoji-test.txt
        this_dir = dirname(__file__)
        stuff_dir = join(dirname(this_dir), 'stuff')
        filename = filename or join(stuff_dir, 'emoji-test.txt')

        self.clear()

        with open(filename, 'r') as f:
            for line in f.readlines():
                exploded = line.split(';')
                if len(exploded) <= 1:
                    continue

                code_points = str(re.sub(r'\s\s+', " ", exploded[0]))
                code_points = code_points.strip().split(' ')
                if code_points[0] == '#':
                    continue
                code_points = list(map(lambda x: int(x, 16), code_points))
                comment = exploded[1].split('#')[1]
                comment = str(re.sub('[^a-zA-Z0-9,: -]+', '', comment))
                comment = comment.strip()

                self.append(
                    Emoji(code_points, comment)
                )
