# -*- coding: iso-8859-15 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8:........C@@@
# @@@@@@@@@@@@@@88@@@@@@@@@@@@@@@@@@@@@@88@@@@@@@@@@888@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O:...........:C@
# @       .@O        O@8         C@@O        o@@@:       cO                   oc       8o   .@@.   @c....:O@@:....:@
# @     .:c8    CO    O8    :o    O8    oO    C@.   :8.   :::.    ..::.     ::Cc    ..:8o    o@:   @o....:8@@:....:@
# @    c@@@O    OO    C8    c@    OO    o8    c@.   :@.   :@@C    O@@@@.   :@@@c    8@@@@@@@@@@@@: @@@@@@@@@O.....:@
# @     ..oO    OO    C8         .@O    o@@@@@@@.   :@.   :@@C    O@@@@.   :@@@c    :C8@@@o O@@ccC @@@@@@@O.......c@
# @       oO    OO    C8         C@O    o.    c8.   :@.   :@@8OOCo8@@@@.   :@@@8@@@@@@O@@@@@@@8C:  @@@@@C.......o@@@
# @    c@@@O    OO    C8    c8    OO    oO    c@.   :@.  o@@@@@@@@@@@@@@@@@@@@@o    8@@@o ..o      @@@C......:C@@@@@
# @    c@@@O    CO    C8    c8    OO    o@.   c@.   :@..o8@@@@@@@@@@@@@@@@Oc@@@c    8@@@o   oo     @C......:O@@@@@@@
# @    c@@@@    ..    88    c8    O@.   .:    c@c    :o@@@@@@@@@@@@@@@@@@@@@@@@Ooc::   Co   o@.    @c....:O@@@@@@@@@
# @    c@@@@@o      o@@8    c@    O@@o    cc  c@@O.  c@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:  Co   o@O    @c....:O8@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:C@:C:..:C.:.:c.:.@o.............:@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.:o o.oo o ooCc.oC@c.............:@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# bleedReinforcements.py -- links cps together
#
#  ©2013 Papillon for Forgotten Honor
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd
from game import scoringCommon
from game.gameplayPlugin import base, hookProxy
from game.scoringCommon import hasPilotKit


class fht_bleedReinforcements(base):
    def __init__(self, bleedCpAxis, bleedCpAllied, alliedCpsForAxisBleed = 3, axisCpsForAlliedBleed = 3):
        try:
            fhtd.bleedCPAxis = bleedCpAxis
            fhtd.bleedCPAllied = bleedCpAllied
            fhtd.alliedCPsForAxisBleed = alliedCpsForAxisBleed
            fhtd.axisCPsForAlliedBleed = axisCpsForAlliedBleed
        except Exception, e:
            fht.Debug("Exception in fht_bleedReinforcements.init(): " + str(e))

            
      
        
    def round_start(self, hooker):
        try:
            self.hooker = hooker
            self.hooker.register('ControlPointChangedOwner', self.onCPChanged)
        except Exception, e:
            fht.Debug("Exception in fht_bleedReinforcements.round_start(): " + str(e))
        
    def onCPChanged(self, cp, team):
        try:           
            if cp.templateName in [ self.bleedCpAxis, self.bleedCpAllied ] or team is -1:
                return

            areaValues = { 1: 0, 2: 0 }
            for cp in fhtd.sortedCPs:
                owner = int(cp.cp_getParam('team'))
                if owner in areaValues.keys():
                    areaValues[owner] +=  getattr(cp, "areaValue" + str(owner), 0)


            alliedBleedCP = utils.getNamedCP(self.bleedCpAllied)        
            alliedBleedTeam = int(alliedBleedCP.cp_getParam('team'))
            
            axisBleedCP = utils.getNamedCP(self.bleedCpAxis)        
            axisBleedTeam = int(axisBleedCP.cp_getParam('team'))

            #Rule 1: Axis > 100 AreaValue, Allied < 100 AreaValue --> Allied Reinforcements
            if areaValue1 > 100 and areaValue2 < 100:

                if alliedBleedTeam == 0:
                    utils.cp_setTeam(alliedBleedCP, 2, 0)
                    
                    utils.sayAll("Activated Allied bleed (R1)")
                if axisBleedTeam == 1:
                    utils.cp_setTeam(axisBleedCP, 0, 0)
                    if DEBUG: print 'bleedReinforcements: De-Activated Axis Bleed reinforcements'
                    utils.sayAll("De-Activated Axis bleed (R1)")


            #Rule 2: Allied control at least the necessary flags for Axis bleed --> Activate axis bleed
            if areaValue2 > 100 and areaValue1 < 100:
                if axisBleedTeam == 0:
                    utils.cp_setTeam(axisBleedCP, 1, 0)
                    if DEBUG: print 'bleedReinforcements: Activated Axis bleed reinforcements'
                    utils.sayAll("Activated Axis bleed (R2)")
                if alliedBleedTeam == 2:
                    utils.cp_setTeam(alliedBleedCP, 0, 0)
                    if DEBUG: print 'bleedReinforcements: De-Activated Allied bleed reinforcements'
                    utils.sayAll("De-Activated Allied bleed (R2)")

            #Rule 3: no bleed --> deactivate all bleed reinforcements
            if (areaValue1 < 100 and areaValue2 < 100) or (areaValue1 > 100 and areaValue2 > 100):
                if alliedBleedTeam == 2:
                    utils.cp_setTeam(alliedBleedCP, 0, 0)
                    if DEBUG: print 'bleedReinforcements: De-Activated Allied bleed reinforcements'
                    utils.sayAll("De-Activated Allied bleed (R3)")
                if axisBleedTeam == 1:
                    utils.cp_setTeam(axisBleedCP, 0, 0)
                    if DEBUG: print 'bleedReinforcements: De-Activated Axis bleed reinforcements'
                    utils.sayAll("De-Activated Axis bleed (R3)")
        except Exception, e:
            fht.Debug("Exception in fht_bleedReinforcements.round_start(): " + str(e))
            

