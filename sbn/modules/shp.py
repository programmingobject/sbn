# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R


"shopping list"


__author__ = "Bart Thate <skullbonesandnumber@gmail.com>"


import time


from .. import Object
from .. import find, fntime, laps, write


class Shop(Object):

    def __init__(self):
        super().__init__()
        self.txt = ''

    def size(self):
        return len(self.__dict__)

    def length(self):
        return len(self.__dict__)


def got(event):
    if not event.args:
        return
    selector = {'txt': event.args[0]}
    for obj in find('shop', selector):
        obj.__deleted__ = True
        write(obj)
        event.reply('ok')


def shp(event):
    if not event.rest:
        nmr = 0
        for obj in find('shop'):
            lap = laps(time.time()-fntime(obj.__oid__))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply("no shops")
        return
    obj = Shop()
    obj.txt = event.rest
    write(obj)
    event.reply('ok')
