import typing as t
import os
import random


PATH = os.path.dirname(__file__)
ADJECTIVE_PATH = os.path.join(PATH, 'adjectives.txt')
NOUN_PATH = os.path.join(PATH, 'nouns.txt')


class NameGenerator(object):

    def __init__(self):
        self._adjectives = self._load_words(ADJECTIVE_PATH)
        self._nouns = self._load_words(NOUN_PATH)

    @classmethod
    def _load_words(cls, path: str) -> t.List[str]:
        with open(path, 'r') as f:
            return [
                line.rstrip()
                for line in
                f.readlines()
            ]

    def _get_name(self) -> str:
        return '-'.join(
            (
                random.choice(self._adjectives),
                *random.sample(self._nouns, 2),
            )
        )

    def get_name(self, seed: int = None) -> str:
        if seed is None:
            return self._get_name()

        previous_state = random.getstate()
        random.seed(seed)

        try:
            return self._get_name()
        finally:
            random.setstate(previous_state)
