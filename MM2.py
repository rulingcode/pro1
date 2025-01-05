from mongoengine import *

import ClientFile

connect('parif')


class Setting(Document):
    LastId = IntField()
    MainBalance = IntField()


def IdGenerator() -> str:
    dev = Setting.objects.first()
    if dev is None:
        dev = Setting()
        dev.LastId = 206
        dev.MainBalance = 0
    dev.LastId += 1
    dev.save()
    return str(dev.LastId)


def ChangeMainBalance(amount: int) -> int:
    dev = Setting.objects.first()
    dev: Setting
    dev.MainBalance = dev.MainBalance + amount
    dev.save()
    return dev.MainBalance
