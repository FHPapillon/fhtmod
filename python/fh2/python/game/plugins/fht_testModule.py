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
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd
from game import markerDaemon
from game import scoringCommon
from game.gameplayPlugin import base, hookProxy
from game.scoringCommon import hasPilotKit



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

class testObject:

        
    def __init__(self, def_loc_team1 = (0.0, 0.0, 0.0), def_loc_team2 = (0.0, 0.0, 0.0), *args, **kwargs):
        try:
            fhtd.dspRegister = []
            self.hooker = None
            self.markerDaemon = markerDaemon.start()
            fhtd.revivalCenter = [(0, 0, 0), def_loc_team1, def_loc_team2]
            self.shutOff(True)

##            #Calculate ttl. Apparently minimum ttl is 2:00 (120 secs) which are added to the value given in ttl
##            #So, ensure that the map-defined ttl is done (if possible)
##            #If a time of < 120 secs is giventtl is set to 0 so that 120 applies
##            for this in [ fhts.rallyTTL, fhts.rallyTTLSL ]:
##                if this < 120.0:
##                    this = 0.0
##                else:           
##                    this = this - 120.0
            
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.__init__(): " + str(e))

    def round_start(self, hooker):
        try:
            self.hooker = hooker
            #hooker.register('RemoteCommand', self.onRemoteCommand)
            #hooker.register('PlayerSpawn', self.onPlayerSpawn)
            #hooker.register('VehicleDestroyed', self.onVehicleDestroyed)
            self.shutOff(True)
            if not fhts.doRallies: return
            #self.createFallbacks()
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.round_start(): " + str(e))

    def createFallbacks(self):
        try:
            if not fhts.doRallies: return
            if not fhtd.revivalCenter[1] is (0.0, 0.0, 0.0):
                template = fhts.rallyTemplatePrefix + '_' + bf2.gameLogic.getTeamName(1) + '_0'
                utils.createObject(template, fhtd.revivalCenter[1], (0.0, 0.0, 0.0), 1, 99999)
                self.hooker.later(fhts.rallyRegisterDelay, self.updateRegister, fhtd.revivalCenter[1], template, 1, None)

            if not fhtd.revivalCenter[2] is (0.0, 0.0, 0.0):
                template = fhts.rallyTemplatePrefix + '_' + bf2.gameLogic.getTeamName(2) + '_0'
                utils.createObject(template, fhtd.revivalCenter[2], (0.0, 0.0, 0.0), 2, 99999)
                self.hooker.later(fhts.rallyRegisterDelay, self.updateRegister, fhtd.revivalCenter[2], template, 2, None)
             
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.createFallbacks(): " + str(e))                 
        
    def onVehicleDestroyed(self, rally, attacker):
        try:
            if not fhts.doRallies: return
            if fhts.rallyTemplatePrefix in rally.templateName.lower():
                if rally in fhtd.dspRegister:
                    fhtd.dspRegister.remove(rally)
                try:
                    self.markerDaemon.remove(rally.templateName.lower())
                except:
                    pass
                if not rally.templateName.lower()[-1:].isdigit():
                    return
                fht.Debug("Rally " + rally.templateName.lower() + " was destroyed.")
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

    def dummySpawn(self, template, pos, rot, team):
        try:
            if not fhts.doRallies: return            
            utils.createObject(template, pos, rot, team)
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.dummySpawn(): " + str(e))   

    def resetRally(self, p):
        try:
            if not fhts.doRallies or not p.isValid(): return    
            pSquad = p.getSquadId()
            fht.Debug("SquadID: " + str(pSquad))
            if not pSquad: return
            pTeam = p.getTeam()
            fht.Debug("pTeam: " + str(pTeam))

            for r in fhtd.dspRegister:
                if not utils.reasonableObject(r):
                    fhtd.dspRegister.remove(r)
                    fht.Debug("Unreasonable removed")
                elif not hasattr(r, 'pos'):
                    fhtd.dspRegister.remove(r)
                    fht.Debug("Unassigned removed")
                    fht.deleteThing(r)
                    try:
                        self.markerDaemon.remove(r.templateName.lower())
                    except:
                        pass
                else:
                    if r.team is pTeam:
                        if r.squad is pSquad:
                            if fhts.testRallyDisable:
                                self.forceDisable(r)
                                return
                            if r.isDisabled:
                                fht.personalMessage("%s: Your squad's rally is currently disabled!"%(p.getName()), p)
                                return                            
                            rTemplate = r.templateName.lower()
                            rPos = r.pos
                            rRot = r.getRotation()
                            rTeam = r.team
                            rSquad = r.squad
                            rSL = r.sL
                            if rSL:
                                fht.Debug("SL dep")
                                info = self.lastDeploySLOnly
                                if r.time:
                                    last = r.time
                                else:
                                    last = info[pTeam][pSquad]
                                rTTL = fhts.rallyTTLSL - host.timer_getWallTime() + last
                                ttl = fhts.rallyTTLSL
                            else:
                                info = self.lastDeploy
                                if r.time:
                                    last = r.time
                                else:
                                    last = info[pTeam][pSquad]                                
                                rTTL = fhts.rallyTTL - host.timer_getWallTime() + last
                                ttl = fhts.rallyTTL
                            fht.Debug(r.time)
                            fht.Debug(str(rTTL) + " time: " + str(host.timer_getWallTime()) + " info: " + info[0] + " " + str(info[pTeam][pSquad]))
                            fhtd.dspRegister.remove(r)
                            fht.deleteThing(r)
                            try:
                                self.markerDaemon.remove(r.templateName.lower())
                            except:
                                pass
                            fht.Debug("deleted")
                            utils.createObject(rTemplate, rPos, rRot, rTeam, ttl)
                            fht.Debug("created")
                            self.hooker.later(fhts.rallyRegisterDelay, self.updateRegister, rPos, rTemplate, rTeam, rSquad, rSL, rTTL, last)
                            return
            fht.personalMessage("%s: Your squad does not have a rally."%(p.getName()), p)
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.resetRally(): " + str(e))   

    def shutOff(self, resetOnly = False):
        try:
            now = host.timer_getWallTime() - fhts.waitTimeRally
            self.lastRun = {}
            
            self.lastDeploy = [
                "Normal",
                ["", now, now, now, now, now, now, now, now, now, now],
                ["", now, now, now, now, now, now, now, now, now, now]
            ]

            now = host.timer_getWallTime() - fhts.waitTimeRallySL
            self.lastDeploySLOnly = [
                "SL",
                ["", now, now, now, now, now, now, now, now, now, now],
                ["", now, now, now, now, now, now, now, now, now, now]
            ]
            for r in fhtd.dspRegister:
                if utils.reasonableObject(r):
                    try:
                        self.markerDaemon.remove(r.templateName.lower())
                    except:
                        pass
                    fht.deleteThing(r)
                fhtd.dspRegister.remove(r)
            fhtd.dspRegister = []
            if resetOnly:
                return
            teams = [ 0, 1, 2]
            squads = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
            for team in teams:
                tName = bf2.gameLogic.getTeamName(team)
                for squad in squads:
                    rTemplate = (((fhts.rallyTemplatePrefix + '_') + tName) + '_') + str(squad)
                    rTemplate = rTemplate.lower()
                    try:
                        self.markerDaemon.remove(rTemplate)
                    except:
                        pass
                    for rally in bf2.objectManager.getObjectsOfTemplate(rTemplate):
                        if not utils.reasonableObject(rally):
                            continue
                        else:
                            try:
                                self.markerDaemon.remove(rally.templateName.lower())
                            except:
                                pass
                            fht.deleteThing(rally)
               

        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.shutOff(): " + str(e))            
            
    def onRemoteCommand(self, pId, cmd):
        try:
            if not fhts.doRallies: return
            if not cmd == "FHT_SL_deploying_spawnpoint":    return
            timeNow = host.timer_getWallTime()
            if pId in self.lastRun.keys():
                if (timeNow - self.lastRun[pId]) < 3.0:	return
            self.lastRun[pId] = timeNow
            
            if pId is -1:
                pId = 255
            p =  bf2.playerManager.getPlayerByIndex(pId)
            
            if not p.isValid() or not p.isAlive():    return   

            fht.Debug("This Happened")

            pBody = p.getDefaultVehicle()
            pPos =  pBody.getPosition()
            pTeam = p.getTeam()
            pSquad = p.getSquadId()

            if pBody.getParent() or not p.getSquadId() or hasPilotKit(p):	return       
            
            rSL = False
            nearbySquadPs = 0
            for sP in fht.playersInSquad(pTeam, pSquad):
                if sP.isValid() and sP.isAlive():
                    sPV = sP.getVehicle()
                    if utils.isInRange(pPos, sPV.getPosition(), fhts.maxDistanceToSquadMember):
                        if not hasPilotKit(p):
                            nearbySquadPs += 1
            if nearbySquadPs < fhts.minSquadPsNear:
                if p.isSquadLeader():
                    info = self.lastDeploySLOnly
                    wTime = fhts.waitTimeRallySL - host.timer_getWallTime() + info[pTeam][pSquad]
                    if wTime > 0:
                        fht.personalMessage("You cannot deploy a squadleader rally - previous deployment too recent, retry in %.1f seconds"%(wTime), p)
                        return
                    ttl = fhts.rallyTTLSL
                    msg = "%s deployed a squadleader rally for your squad. It will be up for %.0f seconds. Next squadleader rally deployment possible in %.0f seconds"%(p.getName(), ttl, fhts.waitTimeRallySL)
                    rSL = True

                else:
                    fht.squadMessage(p, "%s: You cannot deploy a rally - not enough squad members nearby (%d nearby, %d required)"%(p.getName(), nearbySquadPs, fhts.minSquadPsNear))
                    return
            else:
                info = self.lastDeploy
                wTime = fhts.waitTimeRally - host.timer_getWallTime() + info[pTeam][pSquad]
                if wTime > 0:
                    fht.squadMessage(p, "Your squad cannot deploy a rally - previous deployment too recent, retry in %.1f seconds"%(wTime))
                    return
                ttl = fhts.rallyTTL
                msg = "%s deployed a rally for your squad. It will be up for %.0f seconds. Next rally deployment possible in %.0f seconds"%(p.getName(), ttl, fhts.waitTimeRally)


            cp, dis = fht.nearestCP(pPos)
            if cp:
                utils.active(cp.templateName.lower())
                disMin = float(cp.getTemplateProperty('radius')) + fhts.minDisFlag
                if dis < disMin:
                    fht.squadMessage(p, "%s: You cannot deploy a rally here - too close to flag (%.1fm away, %dm required)"%(p.getName(), dis, disMin))
                    return

            if fhts.doMainBaseCheck:
                for mB in fhtd.mainBases:
                    if mB.team and mB.team != pTeam:
                        if utils.isInRange(pPos, mB.getPosition(), mB.safeRadius*math.sqrt(2) + fhts.mainBaseBuffer):
                            fht.squadMessage(p, "%s: You cannot deploy a rally inside the enemy main base perimeter."%(p.getName()))
                            return                    
                  
            for r in fhtd.dspRegister:
                if not utils.reasonableObject(r):
                    fhtd.dspRegister.remove(r)
                elif not hasattr(r, 'pos'):
                    try:
                        self.markerDaemon.remove(r.templateName.lower())
                    except:
                        pass
                    fhtd.dspRegister.remove(r)
                    fht.deleteThing(r)                    
                else:
                    if r.team == pTeam:
                        if r.squad:
                            if not r.squad is pSquad:
                                rDis = utils.vectorDistance(pPos, r.pos)
                                if rDis < fhts.minDisTeamSP:
                                    fht.squadMessage(p, "%s: You cannot deploy a rally here - too close to fireteam %s's rally. (%.1fm away, %dm required)"%(p.getName(), str(r.squad), rDis, fhts.minDisTeamSP))
                                    return
                            else:
                                try:
                                    self.markerDaemon.remove(r.templateName.lower())
                                except:
                                    pass
                                fhtd.dspRegister.remove(r)
                                fht.deleteThing(r)
                            
            pTName = bf2.gameLogic.getTeamName(pTeam)
            rTemplate = (((fhts.rallyTemplatePrefix + '_') + pTName) + '_') + str(pSquad)
            rTemplate = rTemplate.lower()
            rPos = utils.denormalise(pPos, fhts.rallyDeployPosition)
            utils.createObject(rTemplate, rPos, (0.0, 0.0, 0.0), pTeam, ttl)
            info[pTeam][pSquad] = host.timer_getWallTime()
            fht.Debug("Should have written info at " + str(host.timer_getWallTime()))
            fht.Debug("Is actually: " + str(info[pTeam][pSquad]))
            fht.squadMessage(p, msg)
            self.hooker.later(fhts.rallyRegisterDelay, self.updateRegister, rPos, rTemplate, pTeam, pSquad,  rSL, None, host.timer_getWallTime() )
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.onRemoteCommand():" + str(e))
    
    
    def updateRegister(self, pos, template, team, squad = None, rSL = False, rTTL = None, time = None):
        try:
            if not fhts.doRallies: return
            for rally in bf2.objectManager.getObjectsOfTemplate(template):
                if utils.reasonableObject(rally) and not rally in fhtd.dspRegister:
                    cPos = rally.getPosition()
                    if fht.sameTransform(pos, cPos):
                        if squad:
                            triggerId = bf2.triggerManager.createRadiusTrigger(rally, self.onRadioTrigger, '<<PCO>>', fhts.rallyRadius,  (1, 2, 3))
                            rally.triggerId = triggerId
                            rally.friends = []
                            rally.enemies = []
                        rally.time = time
                        rally.missedSpawns = 0
                        fhtd.dspRegister.append(rally)
                        rally.isDisabled = False
                        rally.squad = squad
                        rally.team = team
                        rally.pos = rally.getPosition()
                        rally.sL = rSL
                        if not squad:
                            squad = "0"
                        self.markerDaemon.add(rally.templateName.lower(), "fht_rally_marker_" + str(squad), cPos, team = rally.team)
                        if rTTL and rTTL > 0.0:
                            self.hooker.later(rTTL, self.clearRally, rally)
                    else:
                        fht.Debug("Found an unregistered rally.")
                        self.clearRally(rally, True)
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.updateRegister(): " + str(e))

    def clearRally(self, rally, unRegistered = False):
        try:
            if utils.reasonableObject(rally):
                if unRegistered and rally in fhtd.dspRegister and hasattr(rally, 'pos'):
                    return
                try:
                    self.markerDaemon.remove(rally.templateName.lower())
                except:
                    pass
                fht.deleteThing(rally)
            else:
                fht.Debug("Rally was already destroyed before rTTL expired")
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.clearRally(): " + str(e))

    def onPlayerSpawn(self, p, pBody):
        try:
            if not fhts.doRallies: return
            if pBody.getParent() or p.isAIPlayer():	return
                
            pTeam = p.getTeam()
            pPos =  pBody.getPosition()
            pSquad = p.getSquadId()

            for rally in fhtd.dspRegister:
                
                if not utils.reasonableObject(rally):
                    fhtd.dspRegister.remove(rally)
                    continue
                elif not hasattr(rally, 'pos'):
                    try:
                        self.markerDaemon.remove(rally.templateName.lower())
                    except:
                        pass
                    fhtd.dspRegister.remove(rally)
                    fht.deleteThing(rally)
                    continue
                elif rally.team is pTeam:
                    if (utils.vectorDistance(rally.pos, pPos)) <= 12:
                        if not pSquad:
                            self.correctSpawn(p, rally.squad, 1)
                            return
                        if pSquad != rally.squad:  
                            pSquadHasDSP = False
                            for r in fhtd.dspRegister:
                                if not utils.reasonableObject(r):
                                    fhtd.dspRegister.remove(r)
                                    continue
                                elif not hasattr(r, 'pos'):
                                    try:
                                        self.markerDaemon.remove(rally.templateName.lower())
                                    except:
                                        pass
                                    fhtd.dspRegister.remove(rally)
                                    fht.deleteThing(rally)
                                    continue
                                elif r.team is pTeam and r.squad is pSquad:
                                    pSquadHasDSP = True
                                    if not r.isDisabled:
                                        if not rally.squad:
                                            msg = "You were moved to your squad rally."
                                        else:
                                            msg = "You selected the wrong rally (squad %d). You were moved to your squad rally."%(rally.squad)
                                        fht.personalMessage(msg, p)
                                        pBody.setPosition(r.pos)
                                        r.missedSpawns += 1
                                        if fhts.fixRallyAfter < r.missedSpawns:
                                            self.resetRally(p)
                                        return                                
                                    else:
                                        self.correctSpawn(p, rally.squad, 2)
                                        return
                            if not pSquadHasDSP:
                                self.correctSpawn(p, rally.squad, 3)
                                return
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.onPlayerSpawn(): " + str(e))

    def forceDisable(self, rally):
        try:
            spTemplate = fhts.rallyTemplatePrefix + '_' + str(rally.team) + '_' + str(rally.squad) + fhts.rallySpawnSuffix
            if not rally.isDisabled:
                utils.active(spTemplate)
                utils.rconExec('ObjectTemplate.setOnlyForAI 1')
                fht.squadMessage(rally.squad, "Your rally has been disabled by enemy presence.", rally.team)
                rally.isDisabled = True
                self.markerDaemon.add(rally.templateName.lower(), "fht_rally_marker_" + str(rally.squad) + "_alt", rally.pos, team = rally.team)
                return
            if rally.isDisabled:
                utils.active(spTemplate)
                utils.rconExec('ObjectTemplate.setOnlyForAI 0')
                rally.isDisabled = False
                self.markerDaemon.add(rally.templateName.lower(), "fht_rally_marker_" + str(rally.squad), rally.pos, team = rally.team)
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.forceDisable(): " + str(e))        
    	    	        
    def correctSpawn(self, p, rSquad, case = 0):
        try:
            pTeam = p.getTeam()
            pBody = p.getDefaultVehicle()
            pPos = pBody.getPosition()
        
            msg = ""
            if case is 1:
                if not rSquad:
                    msg = "You are not in a squad, you were moved to the next flag."
                else:
                    msg = "You selected the wrong rally (squad " + str(rSquad) + ". You are not in a squad, you were moved to the next flag."
            if case is 2:
                msg = "You selected the wrong rally (squad " + str(rSquad) + "). Your squad rally is disabled, you were moved to the next flag."
            if case is 3:
                if not rSquad:
                    msg = "Your squad does not have a rally, you were moved to the next flag."
                else:
                    msg = "You selected the wrong rally (squad " + str(rSquad) + "). Your squad does not have a rally, you were moved to the next flag."

            if msg:
                fht.personalMessage(msg, p)
                
            tPos, dis = fht.nearestSP(pPos, pTeam)
            if dis is -1:            
                tPos = fhtd.revivalCenter[pTeam]
                if tPos is (0.0, 0.0, 0.0):
                    pBody.setDamage(0.01)
                    utils.sayAll('fht_deploySpawnPoint.py: spawn error detected for %s. Please report the error if it persists.'%p.getName())
                    return                    
            pBody.setPosition(tPos)
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.correctSpawn(): " + str(e))         
    
    def round_end(self, hooker):
        try:
            self.hooker = None
            self.shutOff(True)
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.round_end(): " + str(e))               

    def onRadioTrigger(self, triggerId, rally, vehicle, enter, userData):
        try:
            if not fhts.doRallies: return
            if vehicle:    
                for p in vehicle.getOccupyingPlayers():
                    pBody = p.getDefaultVehicle()
                    if p.getTeam() is rally.team:
                        if enter:
                            if not [p, pBody] in rally.friends:
                                if not hasPilotKit(p):
                                    rally.friends.append([p, pBody])
                        else:
                            if [p, pBody] in rally.friends:
                                rally.friends.remove([p, pBody])                     
                    else:
                        if enter:
                            if not [p, pBody] in rally.enemies:
                                if not hasPilotKit(p):
                                    rally.enemies.append([p, pBody])
                        else:
                            if [p, pBody] in rally.enemies:
                                rally.enemies.remove([p, pBody])

            for fP, fPBody  in rally.friends:
                if not fP.isValid() or not fP.isAlive() or fP.isManDown() or not utils.reasonableObject(fPBody):
                    rally.friends.remove([fP, fPBody])

            for eP, ePBody in rally.enemies:
                if not eP.isValid() or not eP.isAlive() or eP.isManDown() or not utils.reasonableObject(ePBody):
                    rally.enemies.remove([eP, ePBody])
                               
            spTemplate = fhts.rallyTemplatePrefix + '_' + str(rally.team) + '_' + str(rally.squad) + fhts.rallySpawnSuffix
            if len(rally.enemies):
                if ( len(rally.enemies) > len(rally.friends) ) or ( len(rally.enemies) > 3 ):
                    if not rally.isDisabled:
                        utils.active(spTemplate)
                        utils.rconExec('ObjectTemplate.setOnlyForAI 1')
                        fht.squadMessage(rally.squad, "Your rally has been disabled by enemy presence.", rally.team)
                        rally.isDisabled = True
                        self.markerDaemon.add(rally.templateName.lower(), "fht_rally_marker_" + str(rally.squad) + "_alt", rally.pos, team = rally.team)
                    return
            if rally.isDisabled:
                utils.active(spTemplate)
                utils.rconExec('ObjectTemplate.setOnlyForAI 0')
                rally.isDisabled = False
                self.markerDaemon.add(rally.templateName.lower(), "fht_rally_marker_" + str(rally.squad), rally.pos, team = rally.team)
        except Exception, e:
            fht.Debug("Exception in fht_deploySpawnPoint.onRadioTrigger(): " + str(e))













                
