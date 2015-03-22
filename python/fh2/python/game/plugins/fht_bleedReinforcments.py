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
import bf2, host, bf2.Timer, random
from game.gameplayPlugin import base
import game.utilities

DEBUG = 1

class fht_bleedReinforcments(base):
    def __init__(self, bleedCpAxis, bleedCpAllied, alliedCpsForAxisBleed, axisCpsForAlliedBleed):       
        self.bleedCpAxis = bleedCpAxis
        self.bleedCpAllied = bleedCpAllied
        self.alliedCpsForAxisBleed = alliedCpsForAxisBleed
        self.axisCpsForAlliedBleed = axisCpsForAlliedBleed
      
        if DEBUG: print 'bleedReinforcments: bleedCpAxis = %s, bleedCpAllied = %s, alliedCpsForAxisBleed = %i, axisCpsForAlliedBleed = %i'%(self.bleedCpAxis, self.bleedCpAllied, self.alliedCpsForAxisBleed, self.axisCpsForAlliedBleed)
        
    def round_start(self, hooker):
        hooker.register('ControlPointChangedOwner', self.cpchanged)
    
    def cpchanged(self, cpchanging, top):
        cPsAxisControlled = 0
        cPsAlliedControlled = 0
        numberOfRelvantCps = 0
        areaValue1 = 0
        areaValue2 = 0
        team = cpchanging.cp_getParam('team')

        #ignore changes at the bleed cps
        cp_name = cpchanging.templateName
        if cp_name == self.bleedCpAxis:
            return
        if cp_name == self.bleedCpAllied:
            return
        
        if team == -1: return
        if DEBUG: print 'bleedReinforcments: cpchanged', cpchanging.templateName, 'to', team
        #Iterate through all CPs and count per team how many each team holds
        #Ignore non-capturable Mainbases, flags that are not visible on the minimap
        cps = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
        for cp in cps:
            cp_name = cp.templateName
            if DEBUG: print 'bleedReinforcments: checking', cp_name
            
            game.utilities.active(cp_name)
            #Discard Mainbases
            mainbase = int(game.utilities.templateProperty('unableToChangeTeam'))
            if mainbase == 1:
                #skip mainbase
                if DEBUG: print 'bleedReinforcments: skipped Mainbases', cp_name
                continue

            #Discard flags that are not visible on the minimap
            mainbase = int(game.utilities.templateProperty('showOnMinimap'))
            if mainbase == 0:
                #skip non-minimap-flags
                if DEBUG: print 'bleedReinforcments: skipped non-minimap flag', cp_name
                continue
           
            numberOfRelvantCps += 1
            team = int(cp.cp_getParam('team'))
            av1 = int(game.utilities.templateProperty('areaValueTeam1'))
            av2 = int(game.utilities.templateProperty('areaValueTeam2'))
            if DEBUG: print 'bleedReinforcments: team of CP', team
            if team == 1:
                areaValue1 = areaValue1 + av1
                cPsAxisControlled+=1
            if team == 2:
                areaValue2 = areaValue2 + av2
                cPsAlliedControlled+=1

        alliedBleedCP = game.utilities.getNamedCP(self.bleedCpAllied)        
        alliedBleedTeam = int(alliedBleedCP.cp_getParam('team'))
        if DEBUG: print 'alliedBleedTeam: ', alliedBleedTeam
        
        axisBleedCP = game.utilities.getNamedCP(self.bleedCpAxis)        
        axisBleedTeam = int(axisBleedCP.cp_getParam('team'))
        if DEBUG: print 'axisBleedTeam: ', axisBleedTeam
        
        if DEBUG: print 'bleedReinforcments: Axis control ', cPsAxisControlled, ' Allies control ', cPsAlliedControlled
        if DEBUG: print 'bleedReinforcments: Axis control areaValue', areaValue1, ' Allies control areaValue2', areaValue2
        if DEBUG: print 'bleedReinforcments: Axis bleeds when ', self.alliedCpsForAxisBleed, ' Allies bleeds when ', self.axisCpsForAlliedBleed 

        #Rule 1: Axis > 100 AreaValue, Allied < 100 AreaValue --> Allied Reinforcements
        if areaValue1 > 100 and areaValue2 < 100:
            if alliedBleedTeam == 0:
                game.utilities.cp_setTeam(alliedBleedCP, 2, 0)
                if DEBUG: print 'bleedReinforcments: Activated Allied bleed reinforcements'
                game.utilities.sayAll("Activated Allied bleed (R1)")
            if axisBleedTeam == 1:
                game.utilities.cp_setTeam(axisBleedCP, 0, 0)
                if DEBUG: print 'bleedReinforcments: De-Activated Axis Bleed reinforcements'
                game.utilities.sayAll("De-Activated Axis bleed (R1)")


        #Rule 2: Allied control at least the necessary flags for Axis bleed --> Activate axis bleed
        if areaValue2 > 100 and areaValue1 < 100:
            if axisBleedTeam == 0:
                game.utilities.cp_setTeam(axisBleedCP, 1, 0)
                if DEBUG: print 'bleedReinforcments: Activated Axis bleed reinforcements'
                game.utilities.sayAll("Activated Axis bleed (R2)")
            if alliedBleedTeam == 2:
                game.utilities.cp_setTeam(alliedBleedCP, 0, 0)
                if DEBUG: print 'bleedReinforcments: De-Activated Allied bleed reinforcements'
                game.utilities.sayAll("De-Activated Allied bleed (R2)")

        #Rule 3: no bleed --> deactivate all bleed reinforcements
        if (areaValue1 < 100 and areaValue2 < 100) or (areaValue1 > 100 and areaValue2 > 100):
            if alliedBleedTeam == 2:
                game.utilities.cp_setTeam(alliedBleedCP, 0, 0)
                if DEBUG: print 'bleedReinforcments: De-Activated Allied bleed reinforcements'
                game.utilities.sayAll("De-Activated Allied bleed (R3)")
            if axisBleedTeam == 1:
                game.utilities.cp_setTeam(axisBleedCP, 0, 0)
                if DEBUG: print 'bleedReinforcments: De-Activated Axis bleed reinforcements'
                game.utilities.sayAll("De-Activated Axis bleed (R3)")

