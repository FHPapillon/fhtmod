# -*- coding: iso-8859-15 -*-
# ````````````````````````````````````````````````     hMMMMMMMM-:MMMMMMMMy                                                                                     
# +oooooooooooosssooooooooosssoooooooosssssoooooossssoo/MMMMMMMM-/MMMMMMMM:osssssssssssssssssssssssssssssssssssssyyyssssssssssssssssssssssyysssssssssssssss-    
# yhhhhhhh  .ohdddhs-  -hhhhhhy+`   :yddddy+`  .ohdddhs-/++NMMMM-/MMMMm++ohhhhhhho  ohho  .hhh+  +hhh- ohhh`  :shddhy/`  ohho  .hhh+  `+yhddhs-  .hhhhhhs/`     
# NMMMmmmm `mMMMhmMMN- :MMMNdMMMm` +MMMdhMMMy `mMMMhmMMN-  mMMMM-/MMMMh  -MMMNmmmy  hMMM+ -MMMy  yMMM: dMMM. /MMMmhMMMh  hMMM+ -MMMy  dMMMhmMMM: -MMMNdNMMm`    
# NMMN     `MMMm sMMM/ :MMMs dMMM. sMMM/`mdy+ `MMMd sMMM:  mMMMM-/MMMMh  -MMMh      hMMMN:-MMMy  yMMM: dMMM. oMMM+ NMMN  hMMMM:-MMMy  NMMN oMMM+ -MMMh hMMM-    
# NMMMooo- `MMMm sMMM/ :MMMy`dMMM. sMMM/-:--. `MMMd sMMM:  mMMMM-/MMMMh  -MMMd+++`  hMMMMN+MMMy  yMMM+-dMMM. oMMM+ NMMN  hMMMMN+MMMy  NMMN oMMM+ -MMMh`hMMM-    
# NMMMMMMo `MMMm sMMM/ :MMMNdMMMd  sMMM/NMMMd `MMMd sMMM:  mMMMM-/MMMMh  -MMMMMMM:  hMMMMMNMMMy  yMMMMNMMMM. oMMM+ NMMN  hMMMMMNMMMy  NMMN oMMM+ -MMMNdNMMm`    
# NMMN---` `MMMm sMMM/ :MMMMMMM+`  sMMM/+MMMm `MMMd sMMM:  mMMMM-/MMMMh  -MMMh---`  hMMMyMMMMMy  yMMMyomMMM. oMMM+ NMMN  hMMMyMMMMMy  NMMN oMMM+ -MMMMMMMo`     
# NMMN     `MMMm sMMM/ :MMMdNMMd`  sMMM/`MMMm `MMMd sMMM:  mMMMM-/MMMMh  -MMMy      hMMM-yMMMMy  yMMM: dMMM. oMMM+ NMMN  hMMM-yMMMMy  NMMN oMMM+ -MMMdNMMd`     
# NMMN     `MMMN-yMMM/ :MMMs/MMMs  sMMMo:MMMm `MMMm-hMMM:  mMMMM-/MMMMh  -MMMd///-  hMMM-`dMMMy  yMMM: dMMM. oMMMs:MMMN  hMMM-`dMMMy  NMMN-sMMM+ -MMMh/MMMy     
# NMMN      +mMMNMMNy` :MMMs sMMM/ .hMMMMMMm/  oNMMNMMNy`  mMMMM-/MMMMh  -MMMMMMMh  hMMM- .NMMy  yMMM: dMMM. .hMMMNMMN+  hMMM- .NMMy  +NMMNMMMh. -MMMh sMMM+    
# -+++-------:+ooo+:----+++/--+++/---/oooo/:----:+ooo+:-   mMMMM-/MMMMh  .ssssssso::+sss:::+ss+::+sss/:osss:::/+yhyyo/:::osss/::+sso:::/syyyy+/::/ssso//ss/-    
# `+++++++++++++++++++++++++++++++++++++++++++++++++++++`  /shNM-/MNhs:  .::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::      
#                                                             . `.                                                                                             
#
# fht_hotFixer
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time
from game.gameplayPlugin import base
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd


class fht_hotFixer(base):
 
    def __init__(self, templateCode = "", objectCode = "", *args, **kwargs):
        try:
            self.hooker = None
            self.templateCode = templateCode
            self.objectCode = objectCode
        except Exception, e:
            fht.Debug("Exception in fht_hotFixer.init(): " + str(e))  
    
    def round_start(self, hooker):
        try:
            self.hooker = hooker
            self.hooker.later(fhts.startDelay, self.runCode)
        except Exception, e:
            fht.Debug("Exception in fht_hotFixer.round_start(): " + str(e))

    def round_end(self, hooker):
        try:
            self.hooker = None
        except Exception, e:
            fht.Debug("Exception in fht_hotFixer.round_start(): " + str(e))            

    def runCode(self):
        try:
            if not self.templateCode is "":
                template = "mapdataHotFixDummyTemplate"
                try:
                    utils.verifyTemplateExistence("ObjectSpawner", template)
                    fht.Debug("Dummy Template Exists. Hotfix from mapdata has already been called.")
                except:
                    fht.Debug("Dummy Template not found. Running hotfix code.")
                    for x in self.templateCode.split('\n'):
                        utils.rconExec(x)
                    utils.rconExec('ObjectTemplate.create ObjectSpawner %s' % template)
                    utils.rconExec('ObjectTemplate.activeSafe ObjectSpawner %s' % template)
                    utils.rconExec('ObjectTemplate.hasMobilePhysics 0')

            if not self.objectCode is "":
                spawner = "mapdataHotFixDummySpawner"
                
                output = utils.rconExec('Object.listObjectsOfTemplate %s' % spawner)
                if not output is "":
                    fht.Debug("Dummy Spawner Exists. Hotfix from mapdata has already been called.")
                    return
                else:      
                    fht.Debug("Dummy Spawner not found. Running hotfix code.")
                    for x in self.objectCode.split('\n'):
                        utils.rconExec(x)
                    utils.rconExec('ObjectTemplate.create ObjectSpawner %s' % spawner)
                    utils.rconExec('ObjectTemplate.activeSafe ObjectSpawner %s' % spawner)
                    utils.rconExec('ObjectTemplate.hasMobilePhysics 0')
                    utils.rconExec('Object.create %s' % spawner)
                    utils.rconExec('Object.Object.absolutePosition 100.000/300.000/20.000')
                    utils.rconExec('Object.rotation 100.000/20.000/10.000')
                
        except Exception, e:
            fht.Debug("Exception in fht_hotFixer.round_start(): " + str(e))        
                    



