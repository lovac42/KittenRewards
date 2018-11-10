# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/KittenRewards
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2

from aqt import mw
from anki.hooks import wrap
from aqt.mediasrv import RequestHandler
import anki.sched, anki.schedv2
from anki.utils import isMac, isLin
import random, os, re
# from aqt.utils import showWarning, showText


IMG_EXT = re.compile(r'\.(?:jpe?g|gif|png|tiff|bmp)$', re.I) #Perl FTW! <3

RES_DIR = 'kitten_rewards'
CATS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), RES_DIR))
CATS_IMGS = [i for i in os.listdir(CATS_DIR) if IMG_EXT.search(i)]


def finishedMsg(self, _old):
    image_path = RES_DIR+'/'+random.choice(CATS_IMGS)
    msg="""<b>
Congratulations! You have finished this deck for now.
</b><br><img src='%s' style="max-width:100%%"/><br><br>%s
"""%(image_path,self._nextDueMsg())
    return (_(msg))

anki.sched.Scheduler.finishedMsg = wrap(anki.sched.Scheduler.finishedMsg, finishedMsg, 'around')
anki.schedv2.Scheduler.finishedMsg = wrap(anki.schedv2.Scheduler.finishedMsg, finishedMsg, 'around')



# Replace /user/collection.media folder with actual addon path
def _redirectWebExports(self, path, _old):
    targetPath = os.path.join(os.getcwd(), RES_DIR, '')
    if path.startswith(targetPath):
        return os.path.join(CATS_DIR, path[len(targetPath):])
    return _old(self,path)

RequestHandler._redirectWebExports = wrap(RequestHandler._redirectWebExports, _redirectWebExports, 'around')
