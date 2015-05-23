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
# fht_emergencyCode.py -- Backup module that can be executed at runtime to change code at runtime.
#
# by Harmonikater for Forgotten Honor 
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time, inspect
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd





#           # Example for changing an ingame chat command in fht_admin:

#           # Import the class.
from game.plugins.fht_admin import fht_admin

#           # Define the new Method to replace the old.
def findLocation(self, cmd, args, p):
    try:
        if not p.isAlive() or p.isManDown():
            return False
        else:
            pos = p.getDefaultVehicle().getPosition()
            fht.personalMessage("Location: %f, %f, %f"%(pos[0], pos[1], pos[2]), p)

#            # Let's add a new Line here.
            
            fht.Debug("This Message was added at runtime.")
            
    except Exception, e:
        fht.Debug("Exception in fht_admin.findLocation(): " + str(e))   

function = findLocation
instance = fhtd.fhtPluginObjects['fht_admin']

#           # Now we can replace the old method with the new updated code.
fhtd.fhtPluginObjects['fht_admin'].findLocation = new.instancemethod(function, instance, fht_admin)

#           # If the old method is stored in any other locations we need to replace it here also.
#           # In this case, the command is linked through the fht_adminCommands dict, so change it in there as well.
fhtd.fhtPluginObjects['fht_admin'].fht_adminCommands["location"] = new.instancemethod(function, instance, fht_admin)




#           # Let's assume now we're changing a method that's registered to a BF2 engine event.

from game.plugins.fht_deploySpawnPoint import fht_deploySpawnPoint
from game import scoringCommon

def onVehicleDestroyed(self, rally, attacker):
    try:
        if "m4" in rally.templateName.lower():
            fht.Debug("The rally plugin doesn't care that a sherman was destroyed!")
        else:
            if not fhts.doRallies: return
            if fhts.rallyTemplatePrefix in rally.templateName.lower():
                if rally in fhtd.dspRegister:
                    fhtd.dspRegister.remove(rally)
                if not rally.templateName.lower()[-1:].isdigit():
                    return
                self.markerDaemon.add(rally.templateName.lower(), "fht_rally_active_dummy", (0.0, 0.0, 0.0), team = rally.team)
                fht.Debug("Rally " + rally.templateName.lower() + " was destroyed.")
                spTemplate = fhts.rallyTemplatePrefix + '_' + str(rally.team) + '_' + str(rally.squad) + fhts.rallySpawnSuffix
                utils.active(spTemplate)
                utils.rconExec('ObjectTemplate.setOnlyForAI 0')  
                if not attacker == None:

                    teamName = bf2.gameLogic.getTeamName(rally.team)
                    template = ((fhts.rallyTemplatePrefix + '_') + teamName)
                    self.hooker.later(0.01, self.dummySpawn, template, rally.pos, rally.getRotation(), rally.team)
                    
                    if rally.team is attacker.getTeam():
                        scoringCommon.addScore(attacker, scoringCommon.SCORE_SUICIDE, scoringCommon.RPL)
                        bf2.gameLogic.sendGameEvent(attacker, 11, 1)
                    else:
                        scoringCommon.addScore(attacker, 3, scoringCommon.SKILL)
                        bf2.gameLogic.sendGameEvent(attacker, 10, 5)
                
    except Exception, e:
        fht.Debug("Exception in fht_deploySpawnPoint.onVehicleDestroyed(): " + str(e))             
            
function = onVehicleDestroyed
instance = fhtd.fhtPluginObjects['fht_deploySpawnPoint']


#           # Since the old method was already registered to the hooker, we need to deregister it first:
instance.hooker.deregister('VehicleDestroyed', instance.onVehicleDestroyed)

#           # Then we replace the instance's method like above:
instance.onVehicleDestroyed = new.instancemethod(function, instance, fht_deploySpawnPoint)

#           # Now we reregister the updated method.
instance.hooker.register('VehicleDestroyed', instance.onVehicleDestroyed)
