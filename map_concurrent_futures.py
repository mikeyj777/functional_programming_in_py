import os
import collections
# import multiprocessing
import concurrent.futures
import time
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

def transform(x):
    t0 = time.time()
    pid = os.getpid()
    time.sleep(1)
    res = {'name': x.name, 'age': 2024 - x.born}
    pprint(f'pid: {pid}. start time{t0}')
    return res

if __name__ == '__main__':

    t0 = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(transform, scientists)

    t1 = time.time()

    pprint(f'multi-process time: {t1-t0} seconds') 

    t0 = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(transform, scientists)

    t1 = time.time()

    pprint(f'multi-thread time: {t1-t0} seconds')     