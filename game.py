#!/usr/bin/env python


from pyf import items, game, interface, props

class Game(game.Game):
    pass

class Room(items.Room):
    pass

class Player(items.Actor):
    pass

class Furnace(items.Item):
    pass

class Burger(items.Item):
    pass

class Pythonist(items.Actor):
    pass

class Seat(items.Item):
    pass

class Mug(items.Item):
    mobile = True
    response = "That is not your mug, the name says 'Nicholas Tollervey'."

class Shirt(items.Item):
    pass

game = game.createFromScript(open('script.xml'), locals())
game.actor = Player.inst
interface.runGame(game)
