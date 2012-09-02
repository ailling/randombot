from brplatform.api.bots import DataBot

import random


class RandomBot(DataBot):
    def run(self):
        print 'randombot running'
        rnd = {'random_float': random.random() * 5.0, 'random_int': random.randint(0,5)}
        self.StoreData(rnd)
        return True

class RandomFloatBot(DataBot):
    def run(self):
        print 'RandomFloatBot running'
        return self.StoreData({'random_float': random.random() * 5.0})

class RandomIntBot(DataBot):
    def run(self):
        print 'RandomIntBot running'
        return self.StoreData({'random_int': random.randint(0,5)})
