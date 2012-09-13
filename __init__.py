print 'imported me: ailling_randombot'

from brplatform.api.bots import DataBot
import bots


DataBot.register(bots.RandomBot)
#DataBot.register(bots.RandomFloatBot)
DataBot.register(bots.RandomIntBot)
