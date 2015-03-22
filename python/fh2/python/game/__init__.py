# File: _ (Python 2.3)

import sys
if sys.version_info == (2, 3, 4, 'final', 0):
    is_bf2 = True
else:
    is_bf2 = False
    sys.path += [
        'python',
        'python_dummy',
        '../../python']
from game.log import log
fhlog = log()
import readConfig
config = readConfig.config()
if is_bf2:
    config.read('mods/fh2/fh2.cfg')
    fhlog.post_init()
    sublog = fhlog.peon(__name__)

dbg_level = config.get('debug_level')
if dbg_level and dbg_level.lower() == 'debug':
    is_debug = True
else:
    is_debug = False

def newTimerOnTrigger(self):
    
    try:
        self.targetFunc(self.data)
    except:
        sublog.exception('onTrigger exception')
        self.destroy()


if is_bf2:
    import bf2
    bf2.Timer.onTrigger = newTimerOnTrigger


try:
    import bf2.stats.stats
    from game.stats.stats import fh2stats_init
    bf2.stats.stats.init = fh2stats_init
    print 'patched stat functions [python/game/__init__.py]'
except Exception:
    e = None

if is_bf2:
    import host
    
    try:
        spam_treshold = float(host.rcon_invoke('sv.radioMaxSpamFlagCount'))
        host.rcon_invoke('sv.radioMaxSpamFlagCount %s' % spam_treshold * 2.0)
    except Exception:
        e = None

sys.path.append('admin/ad_framework/')
import ad_init
