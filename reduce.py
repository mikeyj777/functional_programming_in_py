from functools import reduce
import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

scientists = (
    Scientist(name='Ada Lovelace', field='mathematics', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='mathematics', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada May', field='chemistry', born=1845, nobel=True),
    Scientist(name='Katherine Johnson', field='medicine', born=1917, nobel=True),
    Scientist(name='Sir Arthur Faust', field='physics', born=1877, nobel=False),
)

names_and_ages = tuple(map(lambda x: {'name': x.name, 'age': 2024 - x.born}, scientists))

pprint('\n')
pprint(names_and_ages)

tot_age = reduce(lambda acc, val: acc + val['age'], names_and_ages, 0)

print('\n', tot_age)

# group by field

fields = set(s.field for s in scientists)
d_dict = dict.fromkeys(fields, [])
