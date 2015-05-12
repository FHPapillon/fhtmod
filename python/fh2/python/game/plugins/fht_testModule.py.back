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
# fht_testModule
#
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time
from game.gameplayPlugin import base
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd



##  For registering Events, use the function names as given below. Do not register new handlers in here!
##  Reload the module ingame by typing !reset
##
##
##            fh2 events:       init (!not __init__!), bf2_init, bf2_deinit, round_start, round_end
##
##            GameStatusHandler:  onGameStatusChanged
##            'ControlPointChangedOwner': onControlPointChangedOwner
##            'PlayerTeamDamagePoint': onPlayerTeamDamagePoint
##            'PlayerUnlocksResponse': onPlayerUnlocksResponse
##            'PlayerStatsResponse': onPlayerStatsResponse
##            'PlayerGiveAmmoPoint': onPlayerGiveAmmoPoint
##            'DeployGrapplingHook': onDeployGrapplingHook
##            'TicketLimitReached': onTicketLimitReached
##            'ConsoleSendCommand': onConsoleSendCommand
##            'ChangedSquadLeader': onChangedSquadLeader
##            'PlayerChangedSquad': onPlayerChangedSquad
##            'PlayerChangeWeapon': onPlayerChangeWeapon
##            'PlayerRepairPoint': onPlayerRepairPoint
##            'PlayerChangeTeams': onPlayerChangeTeams
##            'ChangedCommander': onChangedCommander
##            'PlayerDisconnect': onPlayerDisconnect
##            'TimeLimitReached': onTimeLimitReached
##            'VehicleDestroyed': onVehicleDestroyed
##            'PlayerHealPoint': onPlayerHealPoint
##            'DeployTactical': onDeployTactical
##            'PlayerRevived': onPlayerRevived
##            'PlayerConnect': onPlayerConnect
##            'DeployZipLine': onDeployZipLine
##            'RemoteCommand': onRemoteCommand
##            'ClientCommand': onClientCommand
##            'EnterVehicle': onEnterVehicle
##            'PlayerKilled': onPlayerKilled
##            'PlayerBanned': onPlayerBanned
##            'PlayerKicked': onPlayerKicked
##            'ExitVehicle': onExitVehicle
##            'PlayerSpawn': onPlayerSpawn
##            'PlayerDeath': onPlayerDeath
##            'PlayerScore': onPlayerScore
##            'ChatMessage': onChatMessage
##            'PickupKit': onPickupKit
##            'DropKit': onDropKit
##            'Reset': onReset

def extract_cameras(obj):
    utils.active(obj.templateName)
    type = utils.getType()
    if type == 'camera':
        return [
            obj.templateName]
    else:
        out = []
        for c in obj.getChildren():
            out += extract_cameras(c)
        
        return out


class testObject:

    def __init__(self):
        self.mgRegister = []

    def round_start(self, hooker):
        self.hooker = hooker

    def onPlayerSpawn(self, p, pBody):
        try:
            fht.Debug(p.getName())
            p.currentMGDeployment = None
            p.cancelMGDep = False
            p.hasPendingMG = False
        except Exception, e:
            fht.Debug("Exception in fht_testModule.onPlayerSpawn(): " + str(e)) 


    def getCount(self, p):
        try:
            for (wName, count) in p.score.bulletsFired:
                if (fhts.depMGWeapon in wName.lower()):
                    return int(count)
        except Exception, e:
            fht.Debug("Exception in fht_testModule.checkCount(): " + str(e))                     
        

    def onPlayerChangeWeapon(self, p, wFrom, wTo):
        try:
            if p.getDefaultVehicle().getParent():
                fht.Debug("Ignoring inside vehicle")
                return

            if wFrom and 'm1919a6' in wFrom.templateName.lower():
                p.cancelMGDep = False                

            if wTo and 'm1919a6' in wTo.templateName.lower():
                fht.Debug("Need Cancel!")
                p.cancelMGDep = True
                mg = p.currentMGDeployment
                if utils.reasonableObject(mg):
                    if not len(mg.getOccupyingPlayers()):
                        if mg in self.mgRegister:
                            self.mgRegister.remove(mg)                        
                        fht.deleteThing(mg)
                        fht.Debug("Changed back: Delete old one")
                        mg = None
                else:
                    mg = None
            
            if wTo and fhts.depMGWeapon in wTo.templateName.lower():
                p.depMGLastCount = self.getCount(p)
                
            if wFrom and fhts.depMGWeapon in wFrom.templateName.lower():
                if p.getKit().templateName.lower() in fhts.depMachineGuns.keys():
                    if self.getCount(p) > p.depMGLastCount:
                        pPos = p.getDefaultVehicle().getPosition()
                        self.hooker.later(fhts.depMGDelay, self.checkMarkers, p, pPos)
                        fht.Debug("Checking Markers")
        except Exception, e:
            fht.Debug("Exception in fht_testModule.onPlayerChangeWeapon(): " + str(e))                     

                    
    def checkMarkers(self, p, pPos):
        try:
            mg = p.currentMGDeployment
            if utils.reasonableObject(mg):
                if not len(mg.getOccupyingPlayers()):
                    self.mgRegister.remove(mg)                        
                    fht.deleteThing(mg)
                    fht.Debug("Changed back: Delete old one")
                    mg = None
                else:
                    return
            for obj in bf2.objectManager.getObjectsOfTemplate(fhts.depMGProjectile):
                if utils.reasonableObject(obj):
                    pos = obj.getPosition()
                    rot = obj.getRotation()
                    team = p.getTeam()
                    kitName = p.getKit().templateName.lower()
##                    template = fhts.depMachineGuns[kitName]
                    template = 'm1919a6_emplaced'
                    try:
                        test = utils.verifyTemplateExistence("PlayerControlObject", template)
                        test = True
                    except:
                        test = False
                    if test:
                        rot = utils.layFlat(rot)
                        rot[0] =  rot[0] + 180.0
                        if math.fabs( pPos[0] - pos[0] ) > 1.0:
                            fht.deleteThing(obj)
                            continue
                        if math.fabs( pPos[2] - pos[2] ) > 1.0:
                            fht.deleteThing(obj)
                            continue
                        fht.Debug("Vertical distance: %.3f"%(pPos[1] - pos[1]))
                        if not ( pPos[1] - pos[1] ) < 0.16 or not ( pPos[1] - pos[1] ) > -0.45:
                            fht.Debug("Too far away in vertical")
                            fht.deleteThing(obj)
                            continue
                        pos = list(pos)
                        pos[1] = pos[1] - 0.05
                        utils.createObject(template, pos, rot, team, 9999)
                        p.hasPendingMG = True
                        self.hooker.later(0.5, self.registerMG, template, pos, rot, team, p)
                        fht.deleteThing(obj)
                    else:
                        fht.Debug("Test Failed")
        except Exception, e:
            fht.Debug("Exception in fht_testModule.checkMarkers(): " + str(e))

    def registerMG(self, template, pos, rot, team, p):
        try:
            for mg in bf2.objectManager.getObjectsOfTemplate('m1919a6_emplaced'):
                if not mg in self.mgRegister:
                    if fht.sameTransform(pos, mg.getPosition()):
                        if not p.cancelMGDep:
                            self.mgRegister.append(mg)
                            p.currentMGDeployment = mg
                            mg.owner = p
                            mg.team = team
                            triggerId = bf2.triggerManager.createRadiusTrigger(mg, self.onRadioTrigger, '<<PCO>>', 0.75,  (1, 2, 3))
                        else:
                            fht.deleteThing(mg, True)
        except Exception, e:
            fht.Debug("Exception in fht_testModule.registerMG(): " + str(e))

    def onRadioTrigger(self, triggerId, mg, vehicle, enter, userData):
        try:
            fht.Debug(enter)
            if mg:
                for p in vehicle.getOccupyingPlayers():
                    pBody = p.getDefaultVehicle()
                    if p.getTeam() is mg.team:
                        if enter:
                            return
                        else:
                            if p is mg.owner:
                                if not len(mg.getOccupyingPlayers()):
                                    self.mgRegister.remove(mg)
                                    fht.deleteThing(mg)
                                    fht.Debug("Changed back: Delete old one")
                            else:
                                fht.Debug("but not owner?")
                                
##                    else:
##                        if enter:
##                            if not [p, pBody] in rally.enemies:
##                                if not hasPilotKit(p):
##                                    rally.enemies.append([p, pBody])
##                        else:
##                            if [p, pBody] in rally.enemies:
##                                rally.enemies.remove([p, pBody])

        except Exception, e:
            fht.Debug("Exception in fht_testModule.onRadioTrigger(): " + str(e))            

    def onExitVehicle(self, player, vehicle):
        try:
            if vehicle.templateName.lower() in 'm1919a6_emplaced':
                fht.Debug("Counts as exit")
                fht.deleteThing(vehicle, True)
        except Exception, e:
            fht.Debug("Exception in fht_testModule.onExitVehicle(): " + str(e))  

    def onEnterVehicle(self, player, vehicle, freeSoldier = False):
        try:

            if vehicle.templateName.lower() in 'm1919a6_emplaced':
                if hasattr(vehicle, 'owner'):
                    if not vehicle.owner is player:
                        player.getDefaultVehicle.setDamage(24)
                    else:
                        fht.Debug("owner entered. all good")

            

            
            if not fhts.testDone:
                ignore_subs = '25pdr mortar gwr34'.split()
                for pco in bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject'):
                    cams = extract_cameras(pco)
                    for cam in cams:
                        do_it = 1
                        for x in ignore_subs:
                            if x in cam.lower():
                                do_it = 0
                                continue
                        
                        if do_it:
                            utils.active(cam)
                            utils.rconExec('ObjectTemplate.CVMChase 1')
                            utils.rconExec('ObjectTemplate.CVMFrontChase 1')
                            utils.rconExec('ObjectTemplate.CVMFlyBy 1')
                            continue
                fhts.testDone = True
                fht.Debug("Bindair Dundat")
        except Exception, e:
            fht.Debug("Exception in fht_testModule.onEnterVehicle(): " + str(e))                 

















                
