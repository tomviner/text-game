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
    response = "This was not as edible as it looked!"

class Pythonist(items.Actor):
    pass

class Seat(items.Item):
    pass

class Mug(items.Item):
#    mobile = True
#    response = "That is not your mug, the name says 'Nicholas Tollervey'."
    pass

class Shirt(items.Item):
    pass

class Dojo(items.Room):
    pass

class Restaurant(items.Room):
    pass

class Reception(items.Room):
    pass

class PresentationRoom(items.Room):
    pass

game = game.createFromScript(open('script.xml'), locals())
game.actor = Player.inst
interface.runGame(game)
