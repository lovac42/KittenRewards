# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/KittenRewards
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1

from aqt import mw
from anki.hooks import wrap
from anki.sched import Scheduler
# from aqt.utils import showWarning, showText
import random, os


RES_DIR = 'kitten_rewards'
CATS_DIR = os.path.join(mw.pm.addonFolder(), RES_DIR)
CATS_IMGS = [i for i in os.listdir(CATS_DIR) if i.endswith(".jpg")]


def finishedMsg(self, _old):
    image_path = os.path.join(CATS_DIR, random.choice(CATS_IMGS))
    msg="""<b>
Congratulations! You have finished this deck for now.
</b><br><img src='%s' style="max-width:100%%"/><br><br>%s
"""%(image_path,self._nextDueMsg())
    return (_(msg))

Scheduler.finishedMsg = wrap(Scheduler.finishedMsg, finishedMsg, 'around')
