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

# nobel_winners = tuple(filter(lambda x: x.nobel, scientists))
# pprint(nobel_winners)

# pprint(tuple(filter(lambda x: True, scientists)))

# nobel_physicists = tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists))

# pprint(nobel_physicists)

def nobel_chemist_filter(record):
    return record.field == 'chemistry' and record.nobel 

# nobel  = tuple(filter(nobel_chemist_filter, scientists))
# pprint(nobel)

nobel_tuple = tuple(x for x in scientists if x.nobel)
pprint(nobel_tuple)

apple = 1