import typing as t
import os
import random


PATH = os.path.dirname(__file__)
ADJECTIVE_PATH = os.path.join(PATH, 'adjectives.txt')
NOUN_PATH = os.path.join(PATH, 'nouns.txt')


class NameGenerator(object):

    def __init__(self):
        self._adjectives = [] #type: t.List[str]
        self._nouns = [] #type: t.List[str]

        with open(ADJECTIVE_PATH, 'r') as f:
            self._adjectives[:] = (
                line.rstrip()
                for line in
                f.readlines()
            )
        with open(NOUN_PATH, 'r') as f:
            self._nouns[:] = (
                line.rstrip()
                for line in
                f.readlines()
            )

    def get_name(self, seed: int=None) -> str:
        if seed is not None:
            previous_state = random.getstate()
            random.seed(seed)

        name = '-'.join(
            (
                random.choice(self._adjectives),
                *random.sample(self._nouns, 2)
            )
        )

        if seed is not None:
            random.setstate(previous_state)

        return name
