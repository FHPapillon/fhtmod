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
# fht_mainBaseKillCheck
#
# CC BY-SA 2014 -- by Harmonikater for Forgotten Honor 
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time
from game.gameplayPlugin import base
from game.stats.constants import *
from game import markerDaemon
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd
import vehicleMetadata as vMd

    

class fht_mainBaseKillCheck(base):
 
    def __init__(self, *args, **kwargs):
        try:
            fht.Debug("mbkc happened")
            self.hooker = None
            self.markerDaemon = markerDaemon.start()
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.init(): " + str(e))        
    
    def round_start(self, hooker):
        fht.Debug("fht_mainBaseKillCheck.round_start()" )
        try: 
            self.hooker = hooker
            hooker.register('PlayerSpawn', self.onPlayerSpawn)
            hooker.register('PlayerKilled', self.onPlayerKilled)
            hooker.register('PlayerChangeWeapon', self.onWeaponChange)
            hooker.register('PickupKit', self.onKitPickUp)
            hooker.register('VehicleDestroyed', self.onVehicleDestroyed)
            hooker.register('ExitVehicle', self.onVehicleExit)
            hooker.register('EnterVehicle', self.onVehicleEnter)   
            self.hooker.later(fhts.startDelay, self.initData)               
            fhtd.watchList = []
            fhtd.safeList = []
            fht.Debug("fht_mainBaseKillCheck.round_start() done" )
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.round_start(): " + str(e))         

    def round_end(self, hooker):
        try:
            fht.Debug("fht_mainBaseKillCheck.round_end self.hooker = None  " )
            self.hooker = None
            fht.Debug("fht_mainBaseKillCheck.round_end self.hooker = None is done  " )
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.round_end(): " + str(e))      
        fht.Debug("fht_mainBaseKillCheck.round_end finished" )

    def initData(self):
        fht.Debug("fht_mainBaseKillCheck.initData()" )
        try:
            cp = fhtd.cpList[0]
            test = cp.cp_getParam('team')
            test2 = cp.cpID
            self.hooker.later(fhts.startDelay, self.reDrawMarkers)
            fht.Debug("Not getting stuff.")
        except:
            fht.Debug("New Map. Getting Objects.")
            fht.getPluginObjects()
            fht.getControlPoints()
            fht.getSpawnPoints()
            fht.getSpawners()
            fht.setCPSpawnPoints()
            fht.sortCPs()
            mbCheck = fhtd.fhtPluginObjects.get('fht_flagShuffle', None)
            if not (mbCheck and mbCheck.mbTeam):
                self.hooker.later(fhts.startDelay, self.findMainBases)

    def confirmList(self, p, safe = False):
        try:
            if not p or not p.isValid:
                return False
            if safe: cp = p.ownMainBase
            else: cp = p.mainBaseEntered
            if not cp or not utils.reasonableObject(cp):
                return False
            pPos = p.getDefaultVehicle().getPosition()
            pPos = (pPos[0], 0.0, pPos[2])
            cPos = cp.getPosition()
            cPos = (cPos[0], 0.0, cPos[2])
            if not utils.isInRange(pPos, cPos, (cp.safeRadius*math.sqrt(2) + 50.0)*fhts.mBCKCorrFactor):
                if safe:
                    fhtd.safeList = list(fhtd.safeList)
                    if p in fhtd.safeList: fhtd.safeList.remove(p)
                else:
                    fhtd.watchList = list(fhtd.watchList)
                    if p in fhtd.watchList: fhtd.watchList.remove(p)
                return False
            if ( pPos[0] > cp.corners[0][0] ) or ( pPos[0] < cp.corners[2][0] ) or ( pPos[2] > cp.corners[0][2] ) or ( pPos[0] < cp.corners[2][2] ):
                return "PASS"
            return True
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.confirmList(): " + str(e))  

    def findMainBases(self):
        try:
            fhtd.mainBases = []
            for cp in fhtd.cpList:
                utils.active(cp.templateName)
                if cp.cp_getParam('unableToChangeTeam') and cp.cp_getParam('team') and int(utils.templateProperty('showOnMinimap')):
                    if cp.templateName.lower() in fhts.notMainBase:
                        continue
                    match = False
                    if len(fhts.forceMainBase):
                        for cpName, cpRadius in fhts.forceMainBase:
                            if cpName.lower() is cp.templateName.lower():
                                radius = cpRadius
                                match = True
                                break
                    if not match:
                        radius = self.getBaseSize(cp)
                    cp.safeRadius = radius
                    cp.team = cp.cp_getParam('team')                        
                    self.drawMarker(cp, cp.safeRadius)
                    fhtd.mainBases.append(cp)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.findMainBases(): " + str(e))          

    def reDrawMarkers(self):
        try:
            for cp in fhtd.mainBases:
                self.drawMarker(cp, cp.safeRadius)
            return True
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.reDrawMarkers(): " + str(e))
            return False

    def drawMarker(self, cp, radius):
        try:
            cPos = cp.getPosition()
            cNE = (cPos[0] + radius, 0.0, cPos[2] + radius)
            cSE = (cPos[0] + radius, 0.0, cPos[2] - radius)
            cSW = (cPos[0] - radius, 0.0, cPos[2] - radius)
            cNW = (cPos[0] - radius, 0.0, cPos[2] + radius)            
            cp.mbTriggerID = bf2.triggerManager.createRadiusTrigger(cp, self.onCPTrigger, '<<PCO>>', radius*math.sqrt(2) + fhts.mainBaseBuffer, (1, 2, 3))
            self.markerDaemon.add(cp.templateName + "_NE", "uncap_ne", cNE)
            self.markerDaemon.add(cp.templateName + "_SE", "uncap_se", cSE)
            self.markerDaemon.add(cp.templateName + "_SW", "uncap_sw", cSW)
            self.markerDaemon.add(cp.templateName + "_NW", "uncap_nw", cNW)
            cp.corners = ( cNE, cSE, cSW, cNW )
            return True
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.drawMarkers(): " + str(e))
            return False

    def updateMainBaseSize(self, cp, amount):
        try:
            bf2.triggerManager.destroy(cp.mbTriggerID)
            radius = cp.safeRadius + amount
            cp.safeRadius = radius
            self.drawMarker(cp, cp.safeRadius)               
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.updateMainBaseSize(): " + str(e))             

    def getBaseSize(self, cp):
        try:
            utils.active(cp.templateName)
            cpID = utils.rconExec("ObjectTemplate.controlPointId")
            size = 50.0
            if not len(fhtd.objectSpawners):
                objectSpawners = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ObjectSpawner')
                fhtd.objectSpawners = objectSpawners
            for s in fhtd.objectSpawners:
                if not utils.reasonableObject(s):
                    continue
                if int(str(s.cpID).strip()) == int(str(cp.cpID).strip()):
                    cpPos = ( cp.getPosition()[0], 0.0, cp.getPosition()[2] )
                    spPos = ( s.getPosition()[0], 0.0, s.getPosition()[2] )
                    distance = utils.vectorDistance(cpPos, spPos)
                    if  distance + fhts.mainBaseBuffer > size:
                        size = distance + fhts.mainBaseBuffer
            
            if size > fhts.maxMainbaseSize:
                size = fhts.maxMainbaseSize
            fht.Debug("Final Size for " + cp.templateName + ": " + str(size))
            return size
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.getBaseSize(): " + str(e))        

    def onPlayerSpawn(self, p, pBody):
        try:
            if p in fhtd.watchList:
                fhtd.watchList.remove(p)
            p.punishWeapon = False
            p.punishVehicle = False
            p.punishKit = False
            p.punishWrench = False
            p.enterWithVehicle = None
            p.enterPerimeterAt = None
            p.artyDestroyed = 0
            if not fhtd.roundStarted:
                fhtd.roundStarted = True
        except:
            fht.Debug("Exception in fht_mainBaseKillCheck.onPlayerSpawn(): " + str(e)) 

    def onCPTrigger(self, triggerId, cp, v, enter, userData):
        try:
            if cp.isValid():
                if v:
                    psInV = v.getOccupyingPlayers()
                    for p in psInV:
                        if cp.cp_getParam('team') and cp.cp_getParam('team') != p.getTeam():
                            pV = utils.rootParent(p.getVehicle())
                            fhtd.watchList = list(fhtd.watchList)
                            if enter:
                                p.mainBaseEntered = cp
                                if not p in fhtd.watchList:
                                    fhtd.watchList.append(p)
                                    p.enterWithKit = p.getKit().templateName.lower()
                                    if p.getDefaultVehicle().getParent():
                                        p.enterWithVehicle = pV.templateName.lower()               
                                if p.getDefaultVehicle().getParent():
                                    if not fht.isAllowedVehicleType(pV):
                                        if not fht.isAllowedAttackVehicleType(pV):
                                            self.punishInfringement(p, 'punishVehicle', pV.templateName)
                                else:                             
                                    self.onWeaponChange(p, None, p.getPrimaryWeapon())
                            else:
                                if p in list(fhtd.watchList):
                                    p.punishWeapon = False
                                    fhtd.watchList.remove(p)
                                    if pV.templateName.lower() in p.enterWithVehicle:
                                        p.punishVehicle = False
                        if cp.cp_getParam('team') is p.getTeam():
                            fhtd.safeList = list(fhtd.safeList)
                            if enter:
                                if not p in fhtd.safeList:
                                    fhtd.safeList.append(p)
                                p.ownMainBase = cp
                            else:
                                if p in fhtd.safeList:                                
                                    fhtd.safeList.remove(p)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.onCPTrigger(): " + str(e)) 

    def onVehicleDestroyed(self, v, a, reRun = False):
        try:
            if not fhts.doMainBaseCheck or not a: return
            else:
                if fht.isMainBaseVehicleType(v):
                    if not v in fhtd.mainBaseVehicles:
                        fhtd.mainBaseVehicles.append(v)
                    a.artyDestroyed += 1
            if a in fhtd.watchList:
                confirm = self.confirmList(a)
                if confirm and not confirm is "PASS":
                    if fht.isMonitoredVehicleType(v):
                        if not utils.rootParent(a.getVehicle()).templateName.lower() in fhts.droneTemplate:
                            if not hasattr(v, 'isOccupied') or not  v.isOccupied:
                                if not fht.inSplashZone(v):
                                    if not reRun:
                                        self.hooker.later(fhts.mBCKRepeatDelay, self.onVehicleDestroyed, v, a, True)
                                        return
                                    else:   
                                        fht.personalMessage("%s: You are not allowed to destroy empty planes or armoured vehicles inside the enemy main base." %(a.getName()), a)
                                        fht.adminPM("Player %s has destroyed %s inside the enemy main base." %(a.getName(), v.templateName), a)
                                        a.punishVehicle = True
                                        self.killPlayer(a)
            else:
                if fht.isMonitoredVehicleType(v):
                    if not utils.rootParent(a.getVehicle()).templateName.lower() in fhts.droneTemplate:                    
                        if not hasattr(v, 'isOccupied') or not  v.isOccupied:         
                            for cp in fhtd.mainBases:
                                if cp.cp_getParam('team') and cp.cp_getParam('team') != a.getTeam():
                                    p_pos = v.getPosition()
                                    p_pos = ( p_pos[0], 0.0, p_pos[2] )
                                    cp_pos = ( cp.getPosition()[0], 0.0, cp.getPosition()[2] )
                                    if utils.isInRange(cp_pos, p_pos, cp.safeRadius*math.sqrt(2)):

                                        if ( p_pos[0] > cp.corners[0][0] ) or ( p_pos[0] < cp.corners[2][0] ) or ( p_pos[2] > cp.corners[0][2] ) or ( p_pos[0] < cp.corners[2][2] ):
                                            fht.Debug("Pass")
                                            return 
                                        if not self._near_Artillery(v):
                                            if not rerun:
                                                rerun = True
                                                self.hooker.later(REPEAT_DELAY, self.onVehicleDestroyed, v, a, rerun)
                                                return
                                            else:   
                                                msg = ("%s: You are not allowed to destroy empty planes or armoured vehicles inside the enemy main base." %(a.getName()))
                                                adf.personalMessage(msg, a)
                                                adm_msg = ("Player %s has destroyed %s inside the enemy main base." %(a.getName(), v.templateName))
                                                ad_admin.adminPM(adm_msg, a)
                                                a.punishVehicle = True
                                                self.killPlayer(a)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.onVehicleDestroyed(): " + str(e)) 


    def onPlayerKilled(self, v, a, weapon, assists, vBody, reRun = False):
        try:
            if not fhts.doMainBaseCheck: return
            if a and v and not utils.rootParent(a.getVehicle()).templateName.lower() in fhts.droneTemplate:
                if v.getTeam() != a.getTeam():
                    vVehicle = utils.rootParent(v.getVehicle())
                    if fht.isMainBaseVehicleType(vVehicle):
                        a.artyDestroyed += 1
                    if v in fhtd.safeList:
                        confirm = self.confirmList(v, True)
                        if confirm and not confirm is "PASS":
                            if not fht.inSplashZone(vVehicle):
                                if not reRun:
                                    self.hooker.later(fhts.mBCKRepeatDelay, self.onPlayerKilled, v, a, weapon, assists, vBody, True)
                                    return
                            if not a.getDefaultVehicle().getParent():
                                if weapon and not fht.isAllowedWeaponType(weapon):
                                    fht.personalMessage("%s: You are not allowed kill enemies inside their main Base with this weapon." %(a.getName()), a)
                                    fht.adminPM("Player %s has killed %s inside the enemy main base with %s." %(a.getName(), v.getName(), weapon.templateName), a)                    
                                    self.killPlayer(a)
                            else:
                                aVehicle = utils.rootParent(a.getVehicle())
                                if not fht.isAllowedAttackVehicleType(aVehicle):
                                    if not fht.isMainBaseVehicleType(vVehicle) and not fht.inSplashZone(vVehicle):
                                        fht.personalMessage("%s: You are not allowed kill enemies inside their main Base with this Vehicle." %(a.getName()), a)
                                        fht.adminPM("Player %s has killed %s inside the enemy main base with %s." %(a.getName(), v.getName(), aVehicle.templateName), a)
                                        a.punishVehicle = True
                                        self.killPlayer(a)
                        return
                    if a in fhtd.safeList:
                        if getWeaponType(weapon.templateName.lower()) is WEAPON_TYPE_UNKNOWN:
                            if v in fhtd.watchList:
                                confirm = self.confirmList(v)
                                if confirm and not confirm is "PASS":
                                    return
                            confirm = self.confirmList(a, True)
                            if confirm and not confirm is "PASS":
                                if a.getDefaultVehicle().getParent():
                                    if not fht.isMainBaseVehicleType(utils.rootParent(a.getVehicle())):
                                        a.punishVehicle = True
                                        fht.personalMessage("%s: You are not allowed to shoot out of your Main Base with this vehicle." %(a.getName()), a)
                                        fht.adminPM(adm_msg, "Player %s has destroyed %s with %s from inside his own main base." %(a.getName(), v.getName(), a.getVehicle().templateName))
                                        self.killPlayer(a)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.onPlayerKilled(): " + str(e)) 


    def onKitPickUp(self, p, kit):
        try:
            if p in fhtd.watchList:
                confirm = self.confirmList(p)
                if not confirm or confirm is "PASS":
                    return
                elif kit:
                    if kit.templateName.lower() is  p.enterWithKit.lower():
                        p.punishKit = False
                    else:
                        self.punishInfringement(p, 'punishKit', kit.templateName)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.onKitPickUp(): " + str(e)) 

    def onWeaponChange(self, p, wfrom, wto):
        try:
            if wto and wto.templateName.lower() in fhts.wrenches:   
                if p.getDefaultVehicle().getParent():
                    self.punishInfringement(p, 'punishWrench')
                return
            if wfrom and wfrom.templateName.lower() in fhts.wrenches:
                p.punishWrench = False
            if p in fhtd.watchList:
                if p.getDefaultVehicle().getParent() or not self.confirmList(p):
                    return
                elif wto and not fht.isAllowedWeaponType(wto):
                    self.punishInfringement(p, 'punishWeapon', wto.templateName)
                else:
                    p.punishWeapon = False
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.onWeaponChange(): " + str(e)) 

    def onVehicleEnter(self, p, v, freeWeapon):
        try:
            v.isOccupied = True
            if freeWeapon and p.getPrimaryWeapon() and p.getPrimaryWeapon().templateName.lower() in fhts.wrenches:
                p.punishWrench = True
                self.punishInfringement(p, 'punishWrench')                 
            if p in fhtd.watchList:
                confirm = self.confirmList(p)
                if ( not confirm ) or ( confirm is "PASS" ):
                    return
                elif not fht.isAllowedVehicleType(v):
                    self.punishInfringement(p, 'punishVehicle', v.templateName)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.onVehicleEnter(): " + str(e)) 

    def onVehicleExit(self, p, v):
        try:
            if not len(v.getOccupyingPlayers()):
                v.isOccupied = False
            if p.isAlive() and not p.isManDown():
                p.punishWrench = False
            if p in fhtd.watchList:
                p.punishVehicle = False
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.onVehicleExit(): " + str(e)) 

    def punishInfringement(self, p, type, info = ""):
        try:
            if not fhts.doMainBaseCheck: return
            if type is 'punishKit':
                msg = ("%s: You are not allowed to take any kit from inside the enemy main base. Switch back to your old kit NOW!" %(p.getName()))
                adm_msg = ("Player %s has picked up a kit %s inside enemy main base." %(p.getName(), info))
            elif type is 'punishWeapon':
                msg = ("%s: You are not allowed to use %s inside the enemy main base (perimeter). Change your weapon NOW!" %(p.getName(), info))
                adm_msg = ("Player %s is using weapon %s inside enemy main base." %(p.getName(), info))
            elif type is 'punishWrench':
                msg = ("%s: You are not allowed to repair vehicles from outside seats. Exit the vehicle or change to another Weapon NOW!" %(p.getName()))
                adm_msg = ("Player %s is repairing vehicle from outside seat." %(p.getName()))                
            elif type is 'punishVehicle':
                msg = ("%s: You are not allowed to use this %s inside the enemy main base (perimeter). Exit NOW!" %(p.getName(), info))
                adm_msg = ("Player %s has entered/driven %s inside the enemy main base (perimeter)." %(p.getName(), info))                
            fht.personalMessage(msg, p)
            fht.adminPM(adm_msg, p)
            setattr(p, type, True)
            self.hooker.later(fhts.warnLength, self.bleedOffender, p, type)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.punishInfringement(): " + str(e)) 

    def bleedOffender(self, p, type):
        try:
            if not p.isValid():
                return
            elif getattr(p, type, False):
                if p.isAlive() and not p.isManDown():
                    pBody = p.getDefaultVehicle()
                    
                    if pBody.getParent() and p.enterWithVehicle and type is 'punishVehicle':
                        if p in fhtd.watchList:
                            if not self.confirmList(p) and utils.rootParent(p.getVehicle()).templateName.lower() in p.enterWithVehicle:
                                p.punishVehicle = False
                                return
                    if type is 'punishWeapon':
                        if ( not self.confirmList(p) ):
                            return
                    HP = pBody.getDamage()
                    if HP > 20:
                        pBody.setDamage(HP - 20)
                        self.hooker.later(1, self.bleedOffender, p, type)
                    else:
                        self.killPlayer(p)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.bleedOffender(): " + str(e)) 

    def killPlayer(self, p):
        try:
            if p.isAlive() and not p.isManDown():
                p.getDefaultVehicle().setDamage(0.01)
                self.hooker.later(3, self.confirmKill, p)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.killPlayer(): " + str(e)) 

    def confirmKill(self, p):
        try:
            if p.getDefaultVehicle() and p.getDefaultVehicle().getParent():
                if hasattr(p, 'punishVehicle') and p.punishVehicle:
                    if p.isAlive() and not p.isManDown():
                        host.rcon_invoke('admin.kickPlayer %d' % p.index)
        except Exception, e:
            fht.Debug("Exception in fht_mainBaseKillCheck.confirmKill(): " + str(e)) 
