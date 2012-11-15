# -*- coding: utf-8 -*-

"""
    Mamanger
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from flaskext.script import Manager
from application import app


######################################################
###
### Manager
###
######################################################

manager = Manager(app)


######################################################
###
### Commands
###
######################################################


######################################################
###
### Run
###
######################################################

if __name__ == "__main__":
    manager.run()
