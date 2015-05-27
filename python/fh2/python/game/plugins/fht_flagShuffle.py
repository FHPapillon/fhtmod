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
# fht_flagShuffle.py -- Allows for some variety in flag layouts
#
# CC BY-SA 2014 -- by Papillon and Harmonikater for Forgotten Honor 
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time
from game.gameplayPlugin import base
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd


class fht_flagShuffle(base):
 
    def __init__(self, noOfCPs = 0, excludeCPs = [], unusedCPs = [], flagTeam = None, mbTeam = None, mbChoices = [], mbOpName = None, *args, **kwargs):
        try:
            self.noOfCPs = int(noOfCPs)
            self.flagTeam = flagTeam
            self.mbTeam = mbTeam
            self.mbChoices = mbChoices
            self.mbOpName = mbOpName
            self.excludeCPs = [ int(x) for x in excludeCPs ]
            self.unusedCPs = [ int(x) for x in unusedCPs ]
            self.hooker = None
            fhtd.mbSelected = False
            self.selectingTeam = mbTeam
            self.shuffleThese = []
            self.activeCPs = []
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.init(): " + str(e))            
    
    def round_start(self, hooker):
        fht.Debug("fht_flagShuffle.round_start()")
        fhtd.mbSelected = False
        try:
            self.hooker = hooker
            if self.noOfCPs:
                self.hooker.later(3, self.getCandidates)
                self.hooker.later(5, self.setTeamCPs)
                self.hooker.later(5, fht.sortCPs)
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.round_start(): " + str(e))
        fhtd.mbSelected = False

    def round_end(self, hooker):
        fhtd.mbSelected = False
        try:
            self.hooker = None
##            fht.Debug(self.noOfCPs)
##            if self.noOfCPs:
##                fht.Debug("Do the FHT Shuffle.")
##                self.shuffleCPs()
##                fht.reloadMap()
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.round_end(): " + str(e))
        self.mbSelected = False
    def setTeamCPs(self):
        try:
            for cp in fhtd.cpList:
                if cp.cpID in self.unusedCPs:
                    utils.cp_setTeam(cp, 0, 0)
                elif cp in self.shuffleThese:
                    if cp in self.activeCPs:
                        utils.cp_setTeam(cp, self.flagTeam, 0)
                    else:
                        utils.cp_setTeam(cp, 0, 0)                    
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.setTeamCPs(): " + str(e))

    def getCandidates(self):
        try:
            fht.Debug("Entered Candidates")
            fht.Debug(len(fhtd.cpList))
            self.shuffleThese = []
            for cp in fhtd.cpList:
                if not utils.reasonableObject(cp) or cp.cpID in self.excludeCPs:
                    continue
                else:
                    fht.Debug("Registered cp: " + cp.templateName)
                    self.shuffleThese.append(cp)
                    utils.activeSafe("ControlPoint", cp.templateName)
                    
                    cp.showOnMinimap = int(utils.rconExec("ObjectTemplate.showOnMinimap"))
                    cp.unableToChangeTeam = int(utils.rconExec("ObjectTemplate.unableToChangeTeam"))
                    cp.areaValueTeam1 = int(utils.rconExec("ObjectTemplate.areaValueTeam1"))
                    cp.areaValueTeam2 = int(utils.rconExec("ObjectTemplate.areaValueTeam2"))

                    fht.Debug(cp.templateName)
                    fht.Debug(cp.showOnMinimap)
                    fht.Debug(cp.unableToChangeTeam)
                    fht.Debug(cp.areaValueTeam1)
                    fht.Debug(cp.areaValueTeam2)

                    if cp.showOnMinimap and not cp.unableToChangeTeam and cp.areaValueTeam1 and cp.areaValueTeam2:
                        fht.Debug("Active")
                        self.activeCPs.append(cp)
                        cp.shuffleIsActive = True
                    else:
                        cp.shuffleIsActive = False
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.getCandidates(): " + str(e))
        

    def mainBaseSelection(self, cmd, args, p):
        try:
            pTeam = p.getTeam()
            if not self.mbTeam: 
                fht.personalMessage("Mainbase Selection is not available on this map.", p)
                return
            elif not pTeam is self.selectingTeam:
                fht.personalMessage("Your team is not entitled to Mainbase Selection", p)
                return
            elif fhtd.mbSelected:
                fht.personalMessage("A Mainbase has already been selected", p)
                return
            else:
                try:
                    choice = int(args[0]) - 1
                except:
                    fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify the target mainbase as 1,2,... (from North to South)", p)
                    return
                mbName = self.mbChoices[choice]
                mb = utils.getNamedCP(mbName)
                utils.cp_setTeam(mb, self.mbTeam, True)
                utils.sayTeam("%s has selected the main base at %s."%(p.getName(), mbName), self.mbTeam)
                fht.adminPM("%s has selected the main base at %s."%(p.getName(), mbName), p)
                
                mbOp = utils.getNamedCP(self.mbOpName)
                utils.cp_setTeam(mbOp, self.flagTeam, True)
                fhtd.mbSelected = True
                mBCK = fhtd.fhtPluginObjects.get('fht_mainBaseKillCheck', None)
                if mBCK:
                    mBCK.findMainBases() 
                fht.getControlPoints() 
                fht.getSpawnPoints()
                fht.setCPSpawnPoints()
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.mainBaseSelection(): " + str(e)) 
    
    def shuffleCPs(self):
        try:
            if not len(self.shuffleThese):
                self.getCandidates()
            self.activeCPs = []
            while not len(self.activeCPs) > self.noOfCPs:
                n = False
                while not n:
                    n = random.randint(1, len(self.shuffleThese))
                    if not self.shuffleThese[n-1] or self.shuffleThese[n-1] in self.activeCPs:
                        n = False
                    fht.Debug(n)
                        
                cp = self.shuffleThese[n-1]
                self.activeCPs.append(cp)
                self.flipCP(cp, forceActive = True)
                fht.Debug("Flip: " + cp.templateName)

            for cp in fhtd.cpList:
                if ( cp.cpID in self.unusedCPs ) or ( cp in self.shuffleThese and not cp in self.activeCPs ):
                    self.flipCP(cp, forceInactive = True)
                    
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.shuffleCPs(): " + str(e))
            


    def flipCP(self, cp, forceActive = False, forceInactive = False):
        try:
            if forceActive and not forceInactive:
                bVar = True
            elif forceInactive and not forceActive:
                bVar = False
            else:
                bVar = bool(cp.shuffleIsActive)
            utils.activeSafe("ControlPoint", cp.templateName)
            fht.Debug("objecttemplate.activesafe controlpoint " + cp.templateName)

            utils.rconExec("ObjectTemplate.showOnMinimap " + str(int(not(bVar))))
            fht.Debug("ObjectTemplate.showOnMinimap " + str(int(not(bVar))))
            
            utils.rconExec("ObjectTemplate.unableToChangeTeam " + str(int(bVar)))
            fht.Debug("ObjectTemplate.unableToChangeTeam " + str(int(bVar)))
            
            utils.rconExec("ObjectTemplate.areaValueTeam1 " + str(35*int(not(bVar))))
            fht.Debug("ObjectTemplate.areaValueTeam1 " + str(35*int(not(bVar))))

            utils.rconExec("ObjectTemplate.areaValueTeam2 " + str(35*int(not(bVar))))
            fht.Debug("ObjectTemplate.areaValueTeam2 " + str(35*int(not(bVar))))
            
            cp.shuffleIsActive = not bVar
            fht.Debug(cp.shuffleIsActive)
        except Exception, e:
            fht.Debug("Exception in fht_flagShuffle.flipCP(): " + str(e))             
