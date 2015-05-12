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
# NMMN      +mMMNMMNy` :MMMs sMMM/ .hMMMMMMm/  self.onMMNMMNy`  mMMMM-/MMMMh  -MMMMMMMh  hMMM- .NMMy  yMMM: dMMM. .hMMMNMMN+  hMMM- .NMMy  +NMMNMMMh. -MMMh sMMM+    
# -+++-------:+ooo+:----+++/--+++/---/oooo/:----:+ooo+:-   mMMMM-/MMMMh  .ssssssso::+sss:::+ss+::+sss/:osss:::/+yhyyo/:::osss/::+sso:::/syyyy+/::/ssso//ss/-    
# `+++++++++++++++++++++++++++++++++++++++++++++++++++++`  /shNM-/MNhs:  .::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::      
#                                                             . `.                                                                                             
#
# fht_reDeployables.py -- allows relocation of static emplacements
#
#  ©2014 Harmonikater for Forgotten Honor
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time
from game.gameplayPlugin import base
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd
import fht_testModule

test = True

class fht_testing(base):


    def __init__(self, *args, **kwargs):
        fht.Debug("Got here")
        self.hooker = None
        self.waiting = None
        self.testObject = fht_testModule.testObject(kwargs)
        fht.Debug("Created Test Object")
    
    def bf2_init(self, hooker):
        try:
            self.testObject.bf2_init(hooker)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def bf2_deinit(self, hooker):
        try:
            self.testObject.bf2_init(hooker)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)       

    def round_end(self, hooker):
        try:
            self.testObject.round_end(hooker)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)       

    def round_start(self, hooker, *args, **kwargs):
        self.hooker = hooker
        fht.Debug("Calling Round Start")        
        self.testObject.hooker = hooker
        host.registerGameStatusHandler(self.onGameStatusChanged)
        hooker.register('ControlPointChangedOwner', self.onControlPointChangedOwner)
        hooker.register('PlayerTeamDamagePoint', self.onPlayerTeamDamagePoint)
        hooker.register('PlayerUnlocksResponse', self.onPlayerUnlocksResponse)
        hooker.register('PlayerStatsResponse', self.onPlayerStatsResponse)
        hooker.register('PlayerGiveAmmoPoint', self.onPlayerGiveAmmoPoint)
        hooker.register('DeployGrapplingHook', self.onDeployGrapplingHook)
        hooker.register('TicketLimitReached', self.onTicketLimitReached)
        hooker.register('ConsoleSendCommand', self.onConsoleSendCommand)
        hooker.register('ChangedSquadLeader', self.onChangedSquadLeader)
        hooker.register('PlayerChangedSquad', self.onPlayerChangedSquad)
        hooker.register('PlayerChangeWeapon', self.onPlayerChangeWeapon)
        hooker.register('PlayerRepairPoint', self.onPlayerRepairPoint)
        hooker.register('PlayerChangeTeams', self.onPlayerChangeTeams)
        hooker.register('ChangedCommander', self.onChangedCommander)
        hooker.register('PlayerDisconnect', self.onPlayerDisconnect)
        hooker.register('TimeLimitReached', self.onTimeLimitReached)
        hooker.register('VehicleDestroyed', self.onVehicleDestroyed)
        hooker.register('PlayerHealPoint', self.onPlayerHealPoint)
        hooker.register('DeployTactical', self.onDeployTactical)
        hooker.register('PlayerRevived', self.onPlayerRevived)
        hooker.register('PlayerConnect', self.onPlayerConnect)
        hooker.register('DeployZipLine', self.onDeployZipLine)
        hooker.register('RemoteCommand', self.onRemoteCommand)
        hooker.register('ClientCommand', self.onClientCommand)
        hooker.register('EnterVehicle', self.onEnterVehicle)
        hooker.register('PlayerKilled', self.onPlayerKilled)
        hooker.register('PlayerBanned', self.onPlayerBanned)
        hooker.register('PlayerKicked', self.onPlayerKicked)
        hooker.register('ExitVehicle', self.onExitVehicle)
        hooker.register('PlayerSpawn', self.onPlayerSpawn)
        hooker.register('PlayerDeath', self.onPlayerDeath)
        hooker.register('PlayerScore', self.onPlayerScore)
        hooker.register('ChatMessage', self.onChatMessage)
        hooker.register('PickupKit', self.onPickupKit)
        hooker.register('DropKit', self.onDropKit)
        hooker.register('Reset', self.onReset)
        
        hooker.register('ChatMessage', self.reloadModule)

        try:
            self.testObject.round_start(hooker)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e) 
        

    def reloadModule(self, playerID, msgText, channel, flags):
        if len(msgText) > 1 and playerID != -1:
            if "!reset" in msgText:
                if test:
                    import fht_testModule as test_reload
                    reload(test_reload)
                    newTestObject = test_reload.testObject()
                    self.testObject = newTestObject
                    self.testObject.hooker = self.hooker
                    fht.Debug("Reloaded Test Module and Object")  


    def onGameStatusChanged(self, status):
        try:
            self.testObject.onGameStatusChanged(status)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerConnect(self, player):
        try:
            self.testObject.onPlayerConnect(player)
        except AttributeError, e: pass

        except TypeError, e: fht.Debug(e)

    def onPlayerSpawn(self, player, soldier):
        try:
            self.testObject.onPlayerSpawn(player, soldier)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onRemoteCommand(self, playerId, cmd):           
        try:
            self.testObject.onRemoteCommand(playerId, cmd)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
     
    def onPlayerChangeTeams(self, playerObject, humanHasSpawned):
        try:
            self.testObject.onPlayerChangeTeams(playerObject, humanHasSpawned)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerChangeWeapon(self, playerObject, oldWeaponObject, newWeaponObject):
        try:
            self.testObject.onPlayerChangeWeapon(playerObject, oldWeaponObject, newWeaponObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
     
    def onPlayerChangedSquad(self, playerObject, oldSquadID, newSquadID):
        try:
            self.testObject.onPlayerChangedSquad(playerObject, oldSquadID, newSquadID)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
     
    def onPlayerScore(self, playerObject, difference):
        try:
            self.testObject.onPlayerScore(playerObject, difference)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerHealPoint(self, givingPlayerObject, receivingSoldierObject):
        try:
            self.testObject.onPlayerHealPoint(givingPlayerObject, receivingSoldierObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerRepairPoint(self, givingPlayerObject, receivingVehicleObject):
        try:
            self.testObject.onPlayerRepairPoint(givingPlayerObject, receivingVehicleObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerGiveAmmoPoint(self, givingPlayerObject, receivingPhysicalObject):
        try:
            self.testObject.onPlayerGiveAmmoPoint(givingPlayerObject, receivingPhysicalObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerTeamDamagePoint(self, playerObject, victimSoldierObject):
        try:
            self.testObject.onPlayerTeamDamagePoint(playerObject, victimSoldierObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerKilled(self, victimPlayerObject, attackerPlayerObject, weaponObject, assists, victimSoldierObject):
        try:
            self.testObject.onPlayerKilled(victimPlayerObject, attackerPlayerObject, weaponObject, assists, victimSoldierObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
     
    def onPlayerRevived(self, revivedPlayerObject, medicPlayerObject):
        try:
            self.testObject.onPlayerRevived(revivedPlayerObject, medicPlayerObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerDeath(self, playerObject, soldierObject):
        try:
            self.testObject.onPlayerDeath(playerObject, soldierObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
     
    def onEnterVehicle(self, player, vehicle, freeSoldier = False):
        try:
            self.testObject.onEnterVehicle(player, vehicle, freeSoldier = False)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onExitVehicle(self, player, vehicle):
        try:
            self.testObject.onExitVehicle(player, vehicle)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerBanned(self, playerObject, times, type):
        try:
            self.testObject.onPlayerBanned(playerObject, times, type)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
     
    def onPlayerKicked(self, playerObject):
        try:
            self.testObject.onPlayerKicked(playerObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
     
    def onPlayerDisconnect(self, playerObject):
        try:
            self.testObject.onPlayerDisconnect(playerObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onVehicleDestroyed(self, vehicleObject, attackerObject):
        try:
            self.testObject.onVehicleDestroyed(vehicleObject, attackerObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPickupKit(self, playerObject, kitObject):
        try:
            self.testObject.onPickupKit(playerObject, kitObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onDropKit(self, playerObject, kitObject):
        try:
            self.testObject.onDropKit(playerObject, kitObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onReset(self, data):
        try:
            self.testObject.onReset(data)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onValidatePlayerNameResponse(self, realNick, oldNick, realPID, oldPID, player):
        try:
            self.testObject.onValidatePlayerNameResponse(realNick, oldNick, realPID, oldPID, player)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
  
    def onChangedCommander(self, teamID, oldCommanderPlayerObject, newCommanderPlayerObject):
        try:
            self.testObject.onChangedCommander(teamID, oldCommanderPlayerObject, newCommanderPlayerObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onChangedSquadLeader(self, squadID, oldLeaderPlayerObject, newLeaderPlayerObject):
        try:
            self.testObject.onChangedSquadLeader(squadID, oldLeaderPlayerObject, newLeaderPlayerObject)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)  

    def onControlPointChangedOwner(self, controlPointObject, attackingTeamID):
        try:
            self.testObject.onControlPointChangedOwner(controlPointObject, attackingTeamID)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onTimeLimitReached(self, value):
        try:
            self.testObject.onTimeLimitReached(value)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onTicketLimitReached(self, team, limitID):
        try:
            self.testObject.onTicketLimitReached(team, limitID)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
  
    def onConsoleSendCommand(self, command, args):
        try:
            self.testObject.onConsoleSendCommand(command, args)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onClientCommand(self, command, issuerPlayerObject, args):
        try:
            self.testObject.onClientCommand(command, issuerPlayerObject, args)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
  
    def onPlayerUnlocksResponse(self, succeeded, player, unlocks):
        try:
            self.testObject.onPlayerUnlocksResponse(succeeded, player, unlocks)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onChatMessage(self, playerId, text, channel, flags):
        try:
            self.testObject.onChatMessage(self, playerId, text, channel, flags)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onPlayerStatsResponse(self, succeeded, player, response):
        try:
            self.testObject.onPlayerStatsResponse(succeeded, player, response)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
  
    def onDeployGrapplingHook(self, player):
        try:
            self.testObject.onDeployGrapplingHook(player)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onDeployZipLine(self, player):
        try:
            self.testObject.onDeployZipLine(player)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)

    def onDeployTactical(self, player):
        try:
            self.testObject.onDeployTactical(player)
        except AttributeError, e: pass
        except TypeError, e: fht.Debug(e)
