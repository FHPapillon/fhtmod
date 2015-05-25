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
# fht_admin.py -- Handles ingame Admin commands and admin drone.
#
# by Harmonikater for Forgotten Honor 
import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time
from game.gameplayPlugin import base, setDefaultTicketLossPerMin, getDefaultTicketLossPerMin
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd

def newHasPilotKit(player):
    if not player.isAlive():
        return False

    if player.getVehicle().templateName.lower() in game.fht_settings.droneTemplate.lower():
        return True
    
    if player.getKit() is None:
        return False
    
    kt = getKitType(player.getKit().templateName)
    if kt == KIT_TYPE_PILOT:
        return True
    else:
        return False

class fht_admin(base):
 
    def __init__(self, *args, **kwargs):
        try:
            self.hooker = None
##            self.readScore()
            if "mapCenter" in kwargs:
                fhts.mapCenter = kwargs["mapCenter"]
            if int(utils.rconExec("sv.internet").strip()):
                fhts.isDedicated = True
            else:
                fhts.isDedicated = False

            self.fht_adminCommands = {
                    "adminpm":                      self.adminCall,
            ##        "clear":                        self.clearScores,
                    "cpchange":                     self.changeCPTeam,
                    "fhtdebugme":                      self.debugPlayer,
                    "fhtdebug":                     self.debugGlobal,
                    "drone":		            self.droneCreate,
                    "plugin":                       self.enablePlugin,
                    "exit":		            self.droneExit,
            ##        "exec":                         self.executeRconFile,
                    "getvalue":                     self.getValue,
                    "help":                         self.textHelp,
                    "import":                       self.reloadSettings,
                    "kick":                         self.playerKick,
                    "k":                            self.playerKick,
                    "kitlimit":                     self.changeKitLimits,
                    "live": 		            self.textLive,
                    "mainbase":                     self.selectMainBaseLink,
                    "location":		            self.findLocation,
                    "md5check":                     self.md5Check,
                    "md5time":                      self.md5Time,
                    "mbchange":                     self.mainBaseUpdate,
                    "mbteam":                       self.mainBaseTeam,
                    "perimeter":                    self.textPerimeter,
                    "rank":                         self.setPermission,
                    "rcon":                         self.rconCommand,
                    "rp":                           self.rallyLink,
                    "rally":                        self.rallyLink,
                    "rallypoint":                   self.rallyLink,
                    "rr":                           self.rallyResetLink,
                    "resetrally":                   self.rallyResetLink,
                    "score":			    self.textScore,
                    "shuffle":                      self.shuffleLink,
                    "scoremod":		            self.setScoreMod,
                    "setbleed":                     self.setBleedRate,
                    "setlive": 		            self.activeRound,
                    "setvalue":                     self.setValue,
                    "teleport":	                    self.droneTeleport,
                    "tele":	        	    self.droneTeleport
            }                
                

        except Exception, e:
            fht.Debug("Exception in fht_admin.init(): " + str(e))            
       
                
    
    def round_start(self, hooker):
        try: 
            self.hooker = hooker
            hooker.register('ExitVehicle', self.onVehicleExited)
            hooker.register('EnterVehicle', self.onVehicleEntered)
            hooker.register('ChatMessage', self.onChatMessage)
            host.registerGameStatusHandler(self.onGameStatusChanged)
            self.fhtPyOverrides()
##            self.readScore()
        except Exception, e:
            fht.Debug("Exception in fht_admin.round_start(): " + str(e))            

    def fhtPyOverrides(self):
        try:
            from game.scoringCommon import hasPilotKit
            hasPilotKit.func_code = newHasPilotKit.func_code

            import limitKit
            limitKit.LARGE_SQUAD_SIZE = 10

            import vehicleMetadata as vMd
            vMd.artillery_info['lefh18_fht'] = (dict(barrel = 'lefh18_fht_gun', azimuth = 'lefh18_fht_remotecam_azi_req', elevation = 'lefh18_fht_remotecam_elev_req', camera = 'lefh18_fht_remotecam_holder', velocity = 480.0, gravitymod = 10.0, elevation_offset = -0.25, indicator = 'lefh18_fht_remotecam_targetind', static = True))
            vMd.artillery = vMd.artillery_info.keys()

            import game.stats.constants as st
            st.weaponTypeMap['wrench'] = st.WEAPON_TYPE_NONLETHAL
            st.weaponTypeMap['no73atgrenade'] = st.WEAPON_TYPE_EXPLOSIVE
            st.weaponTypeMap['wrench_pack'] = st.WEAPON_TYPE_ATGUN
            st.vehicleTypeMap['mc205'] = st.VEHICLE_TYPE_AIR
            st.vehicleTypeMap['lefh18_fht'] = st.VEHICLE_TYPE_ARTILLERY
            
        except Exception, e:
            fht.Debug("Exception in fht_admin.fhtPyOverrides(): " + str(e))
         

    def onGameStatusChanged(self, status):
        try:    
            if status is bf2.GameStatus.Playing:
                fhtd.roundStarted = False    
        except Exception, e:
            fht.Debug("Exception in fht_admin.onGameStatusChanged(): " + str(e))

    def shuffleLink(self, cmd, args, p):
        try:
            shuffle = fhtd.fhtPluginObjects['fht_flagShuffle']
            shuffle.hooker = self.hooker
            shuffle.shuffleCPs()
        except Exception, e:
            fht.Debug("Exception in fht_admin.shuffleLink(): " + str(e))



    def round_end(self, hooker):
        try:
            if fhtd.isLive:
                rounds = fhtd.roundsPlayed + 1
##                axis = bf2.gameLogic.getTickets(1)
##                allied = bf2.gameLogic.getTickets(2)
##                self.writeScore(rounds, axis, allied)
                fhtd.isLive = False
        except Exception, e:
            fht.Debug("Exception in fht_admin.round_end(): " + str(e))
            

    def onVehicleEntered(self, p, v, *args):
        try:
            if fhts.droneTemplate in v.templateName.lower():
                prevent = False
                if fhts.isDedicated:
                    try:
                        if p.teamswitch is "":
                            pass
                    except:
                        fht.playerInit(p)
                    if p.hash is "":
                        tHash = fht.getPlayerHash(p.getName())
                        if tHash is False:
                            prevent = True
                        else:
                            p.hash = tHash
                    if not fhts.fht_adminHashes.has_key(p.hash):
                        prevent = True
                    elif fhts.fht_adminHashes[p.hash] > fhts.fht_adminPowerLevels['drone']:
                        prevent = True
                if prevent:
                    fht.Debug("Admin doesn't have enough rights to use admin drone!")
                    fht.personalMessage("§C1001You do not have permission to use this vehicle!", p)                            
                    fht.deleteThing(utils.rootParent(p.getVehicle()))                    
        except Exception, e:
            fht.Debug("Exception in fht_admin.onVehicleEntered(): " + str(e))    

    def onVehicleExited(self, p, v):
        try:
            if fhts.droneTemplate in v.templateName.lower():
                if utils.reasonableObject(v):
                    fht.deleteThing(v)
                    self.hooker.later(1, self.clearDrones, v.getPosition())
                if not getattr(p, 'safeDroneExit', True):
                    p.safeDroneExit = True
                    return
                pos = v.getPosition()
                p.getDefaultVehicle().setPosition((pos[0], 0.0, pos[2]))
        except Exception, e:
            fht.Debug("Exception in fht_admin.onVehicleExited(): " + str(e))  



    def clearDrones(self, pos):
        try:
            for obj in bf2.objectManager.getObjectsOfTemplate(fhts.droneTemplate):
                if utils.isInRange(obj.getPosition(), pos, 20.0):
                    if not len(obj.getOccupyingPlayers()):
                        fht.deleteThing(obj)
        except Exception, e:
            fht.Debug("Exception in fht_admin.clearDrones(): " + str(e))  

    def changeCPTeam(self, cmd, args, p):
        try:
            teams = { 'neutral': 0, 'axis': 1, 'allies': 2 }
            fht.Debug(len(args))
            fht.Debug(args[0].isdigit())
            fht.Debug(args[1] in teams)
            fht.Debug(args[0])
            fht.Debug(args[1])
            if not len(args) is 2 or not args[0].isdigit() or not args[1] in teams:
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify the flag number 1,2,... (North - South)", p)
                fht.personalMessage("§C1001 and the team to set it to (neutral/axis/allies)", p)
                return
            else:
                cp = fht.getSortedCP(args[0])
                fht.Debug(cp)
                if not cp:
                    fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify the flag number 1,2,... (North - South)", p)
                    fht.personalMessage("§C1001 and the team to set it to (neutral/axis/allies)", p)
                else:
                    utils.cp_setTeam(cp, teams[args[1]], 1)           
        except Exception, e:
            fht.Debug("Exception in fht_admin.changeCPTeam(): " + str(e)) 


    def activeRound(self, cmd, args, p):
        try:
            if fhtd.isLive:
                fht.personalMessage(("Round has already been called Live."), p)
            elif fhtd.roundStarted:
                fht.adminPM(("You cannot call a round live after round start, please restart."), p)
            else:
                fhtd.isLive = True
                utils.rconExec('game.sayall "?LIVE"')
                fht.adminPM("Round has been called live by: ", p)
                fhtd.axisStartTickets = bf2.gameLogic.getTickets(1)
                fhtd.alliedStartTickets = bf2.gameLogic.getTickets(2)
        except Exception, e:
            fht.Debug("Exception in fht_admin.clearDrones(): " + str(e))


    def setTickets(self, cmd, args, p):
        try:        
            teams = { "axis": 1, "allies": 2 }
            if not len(args) is 2 or not args[0].lower() in teams.keys() or not args[1].isdigit():
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a team (axis/allies) and the new bleed rate.", p)
            else:
                setDefaultTicketLossPerMin(teams[args[0].lower()], int(args[1]))
        except Exception, e:
            fht.Debug("Exception in fht_admin.setBleedRate(): " + str(e))


    def setBleedRate(self, cmd, args, p):
        try:
            teams = { "axis": 1, "allies": 2 }
            if not len(args) is 2 or not args[0].lower() in teams.keys() or not args[1].isdigit():
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a team (axis/allies) and the new bleed rate.", p)
            else:
                setDefaultTicketLossPerMin(teams[args[0].lower()], int(args[1]))
                utils.updateTicketLoss()
        except Exception, e:
            fht.Debug("Exception in fht_admin.setBleedRate(): " + str(e))


    def changeKitLimits(self, cmd, args, p):
        try:
            try:
                teams = [ "1", "2" ]
                slots = [ "0", "1", "2", "3", "4", "5" ]
                if not len(args) is 3 or not args[0] in teams or not args[1] in slots:
                    raise ValueError
                else:
                    team = int(args[0])
                    slot = int(args[1])
                    limit = float(args[2])
            except ValueError:
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a team 1/2 (axis/allied),", p)
                fht.personalMessage("§C1001a slot(1-5) and the new limit (e.g. 0.15)", p)
                return

            if not team in fhtd.kitLimiters:
                fht.personalMessage("§C1001Cannot change a non-existant kit limit.", p)
            else:
                if not slot in fhtd.kitLimiters[team]:
                    fht.personalMessage("§C1001Cannot change a non-existant kit limit.", p)
                else:
                    fhtd.kitLimiters[team][slot].info.limit = limit
                    
        except Exception, e:
            fht.Debug("Exception in fht_admin.changeKitLimits(): " + str(e))
                

    def setPermission(self, cmd, args, p):
        try:
            if not fhts.isDedicated:
                return
            else:
                args[1] = args[1].lower()
                ranks = {
                    "root":         0,
                    "admin":        1,
                    "hq":           2,
                    "co":           3,
                    "none":         777,
                }
                if len(args) is not 2 or not args[1] in ranks.keys():
                    fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a name and a rank (Admin/HQ/CO/None)", p)
                else:
                    foundP = fht.findPlayer(args[0])
                    if foundP is "none":
                        fht.personalMessage("§C1001Sorry, no matching player found for '" + args[0] + "'", p)
                    elif foundP is "more":
                        fht.personalMessage("§C1001Multiple players found that match '" + args[0] + "'", p)
                    else:
                        if foundP is p:
                            fht.personalMessage("§C1001You cannot change your own rank.", p)
                            return
                        elif fhts.fht_adminHashes[p.hash] > ranks[args[1]]:
                            fht.personalMessage("§C1001You cannot assign a rank higher then your own.", p)
                            return
                        elif fhts.fht_adminHashes[p.hash] > fhts.fht_adminPowerLevels["setlive"]:
                            if foundP.getTeam() is not p.getTeam():
                                fht.personalMessage("§C1001You do not have permission to rank players on the enemy team!", p)
                                return
                        else:
                            try:
                                if foundP.teamswitch is "":
                                    pass
                            except:
                                fht.playerInit(foundP)
                            if foundP.hash is "":
                                tHash = fht.getPlayerHash(foundP.getName())
                                if not tHash:
                                    fht.personalMessage("§C1001Couldn't assign rank to player '" + foundP.getName() + "'", p)                                    
                                    return
                                else:
                                    foundP.hash = tHash
                            if fhts.fht_adminHashes.has_key(foundP.hash) and not fhts.fht_adminHashes[foundP.hash] > fhts.fht_adminHashes[p.hash]:
                                fht.personalMessage("§C1001You can only assign a new rank to a player beneath your rank.", p)
                            else:
                                fhts.fht_adminHashes[foundP.hash] = ranks[args[1]]
        except Exception, e:
            fht.Debug("Exception in fht_admin.setPermission(): " + str(e))             


    def playerKick(self, cmd, args, p):
        try:
            if len(args) < 2:
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a name and a reason", p)
            else:
                i = 1
                reason = ""
                while i < len(args):
                    reason += str(args[i] + " ")
                    i += 1
                foundP = fht.findPlayer(args[0])
                if foundP is "none":
                    fht.personalMessage("§C1001Sorry, no matching player found for '" + args[0] + "'", p)
                elif foundP is "more":
                    fht.personalMessage("§C1001Multiple players found that match '" + args[0] + "'", p)
                else:
                    if fhts.isDedicated and fhts.fht_adminHashes[p.hash] > fhts.fht_adminPowerLevels["setlive"]:
                        if foundP.getTeam() is not p.getTeam():
                            fht.personalMessage("§C1001You do not have permission to kick players on the enemy team!", p)
                            return
                    elif fhts.isDedicated and fhts.fht_adminHashes[p.hash] > fhts.fht_adminPowerLevels["mainbase"]:
                        if foundP.getSquad() is not p.getSquad():
                            fht.personalMessage("§C1001You do not have permission to kick players outside your squad!", p)
                            return                        
                    fht.adminPM("§C1001" + foundP.getName() + " has been kicked, " + reason, p)
                    utils.sayAll("§C1001KICKING PLAYER %s, %s"%(foundP.getName(), reason))
                    utils.rconExec('admin.kickPlayer %d' % foundP.index)
        except Exception, e:
            fht.Debug("Exception in fht_admin.playerKick(): " + str(e)) 

    def setScoreMod(self, cmd, args, p):
        try:
            if not len(args):
                admMsg = ("Score Modifier is currently set to %i%%"%(fhts.scoreMod))                            
                fht.personalMessage(admMsg, p)
            else:
                if not args[0].isdigit() or not len(args) is 1:
                    fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify the new score modifier in %.", p)                                    
                else:
                    fhts.scoreMod = int(args[0])
                    admMsg = ("Score Modifier has been set to %i%% by "%(int(fhts.scoreMod)))                            
                    fht.adminPM(adm_msg, p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.setScoreMod(): " + str(e)) 



    def md5Check(self, cmd, args, p):
        try:
            if not len(args) or not args[0].isdigit():
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please select parameters 1 (enabled) or 0 (disabled).", p)
            else:
                if int(args[0]):
                    utils.rconExec("pb_sv_load pbsvuser.cfg")
                else:
                    utils.rconExec("pb_sv_md5toolempty")
        except Exception, e:
            fht.Debug("Exception in fht_admin.md5Check(): " + str(e)) 

                
    def md5Time(self, cmd, args, p):
        try:
            if not len(args) or not args[0].isdigit():
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify the new time in whole seconds (limited between 10 and 300).", p)
            else:
                if int(args[0]) > 300:
                    time = 300
                elif int(args[0]) < 10:
                    time = 10
                else:
                    time = int(args[0])
                utils.rconExec(("pb_sv_md5toolfreq " + str(time)))
                admMsg = ("Interval between md5 checks has been set to %s seconds."%(str(time)))                            
                fht.adminPM(admMsg, p)                                
        except Exception, e:
            fht.Debug("Exception in fht_admin.md5Time(): " + str(e)) 

                            
    def rconCommand(self, cmd, args, p):
        try:
            if len(args):
                rcon = ""
                for arg in args:
                    rcon = rcon + arg + " "
                            
                output = utils.rconExec(rcon)
                if output is not "":
                    fht.personalMessage(output, p)
            else:
                fht.personalMessage("§C1001Please specify a command to send.", p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.rconCommand(): " + str(e)) 

    def droneExit(self, cmd, args, p):
        try:
            if not fhts.droneTemplate in p.getVehicle().templateName.lower():
                fht.personalMessage("§C1001You can only this use command while in an admin drone.", p)
            else:            
                p.safeDroneExit = False
                fht.personalMessage("§C1001You have decided not to be removed back to the ground on exit. Proceed with caution.", p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.droneExit(): " + str(e)) 

    def mainBaseUpdate(self, cmd, args, p):
        try:
            if not len(args) is 2 or ( args[0].isdigit() and args[1].isdigit() and int(args[0]) < 1 ):
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify the main base (1,2,... from North to South)", p)
                fht.personalMessage("§C1001and amount (negative to decrease).", p)
            else:
                cp = fht.getSortedCP(args[0], True)
                if cp:
                    amount = float(args[1])
                    if ( cp.safeRadius + amount ) < 50.0:
                        fht.personalMessage("§C1001Minimum safe radius is 50m.", p)
                        amount = 50.0 - cp.safeRadius
                    mBKC = fhtd.fhtPluginObjects['fht_mainBaseKillCheck']
                    mBKC.hooker = self.hooker
                    mBKC.updateMainBaseSize(cp, amount)
                else:
                    fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify the main base (1,2,... from North to South)", p)
                    fht.personalMessage("§C1001and amount (negative to decrease).", p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.updateMainBaseSize(): " + str(e))

    def selectMainBaseLink(self, cmd, args, p):
        try:
            if not fhtd.fhtPluginObjects.has_key('fht_flagShuffle'):
                fht.personalMessage("Mainbase Selection is not available on this map.", p)
            else:
                shuffle = fhtd.fhtPluginObjects['fht_flagShuffle']
                shuffle.hooker = self.hooker
                shuffle.mainBaseSelection(cmd, args, p)           
        except Exception, e:
            fht.Debug("Exception in fht_admin.selectMainBaseLink(): " + str(e)) 

    def mainBaseTeam(self, cmd, args, p):
        try:
            if not fhtd.fhtPluginObjects.has_key('fht_flagShuffle'):
                fht.personalMessage("Mainbase Selection is not available on this map.", p)
            else:
                if len(args) is 1 and ( args[0].isdigit()):
                    team = int(args[1])
                    if team == 1 or team == 2:
                        shuffle = fhtd.fhtPluginObjects['fht_flagShuffle']                        
                        shuffle.mbTeam = team
                        if team ==1:
                            shuffle.flagTeam = 2
                        else:
                            shuffle.flagTeam = 1
                        fht.adminPM("%s has set the mainbase team to %s."%(p.getName(), team), p)
                    else:
                       fht.personalMessage("Only 1 or 2 are possible as team", p)
                else:
                   fht.personalMessage("Exactly one parameter is allowed: 1 or 2", p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.mainBaseTeam(): " + str(e)) 

    def reloadSettings(self, cmd, args, p):
        try:
            import game.fht_settings as fhtsreload
            reload(fhtsreload)
            for key in fhts.__dict__.keys():
                fhts.__dict__[key] = fhtsreload.__dict__[key]
            fhtd.deployerKits = [ x['kit'].lower() for x in fhts.emplacements.values() ]
            fht.adminPM("§C1001FHT settings have been reloaded.", p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.reloadSettings(): " + str(e))  


    def droneCreate(self, cmd, args, p):
        try:
            if not p.isAlive() or p.isManDown():
                return False
            else:
                if p.getVehicle().getParent():
                    fht.personalMessage("§C1001You cannot be in a vehicle while requesting an admin drone.", p)
                else:
                    pos = p.getDefaultVehicle().getPosition()
                    offset = fht.rotateVector(p.getDefaultVehicle().getRotation(), (1.0, 0.5, 0.0))
                    pos = utils.denormalise(pos, offset)
                    utils.createObject(fhts.droneTemplate, pos, p.getDefaultVehicle().getRotation(), 0, 120)
                    self.hooker.later(10, self.clearDrones, pos)
                    fht.adminPM("Admin drone has been requested.", p)                                  
        except Exception, e:
            fht.Debug("Exception in fht_admin.droneCreate(): " + str(e))  

    def droneTeleport(self, cmd, args, p):
        try:
            if not len(args) or not hasattr(args[0], 'lower'):
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a target player or the Grid reference in format C5", p)
            else:
                args = args[0]
                if not fhts.droneTemplate in p.getVehicle().templateName.lower():
                    fht.personalMessage("§C1001You can only this use command while in an admin drone.", p)
                else:
                    if not p.isAlive() or p.isManDown():
                        fht.personalMessage("§C1001You have to be alive to use this command.", p)
                    else:
                        target = None
                        if len(args) is 2 and args[1].isdigit():
                            size = bf2.gameLogic.getWorldSize()[0]
                            grids = ( int( ord(args[0].lower()) - 96), int(args[1]) )
                            if ( grids[0] < 1 or grids[0] > 8 ) or ( grids[1] < 1 or grids[1] > 8 ):
                                fht.personalMessage("§C1001You have to specify a grid square on the Map (A 1 to H 8).", p)
                            else:
                                fht.Debug("DroneTeleport(): Map Coordinates found.")
                                x = fhts.mapCenter[0]
                                z = fhts.mapCenter[2]
                                x = x - ( size / 16) + ( ( size / 8 ) * ( grids[0] - 4 ) )
                                z = z + ( size / 16) - ( ( size / 8 ) * ( grids[1] - 4 ) )
                                target = (float(x), 0.0, float(z))
                        else:
                            foundP = fht.findPlayer(args)
                            if foundP is "none":
                                fht.personalMessage("§C1001Sorry, no matching player found for '" + args[0] + "'", p)
                            elif foundP is "more":
                                fht.personalMessage("§C1001Multiple players found that match '" + args[0] + "'", p)
                            else:
                                if not foundP.isAlive() or foundP.isManDown():
                                    fht.personalMessage("§C1001" + foundP.getName() + " is currently dead or down", p)
                                else:                                                    
                                    target = foundP.getDefaultVehicle().getPosition()
                                    target = ( target[0], target[1] + 5.0, target[2] )
                        if target:
                                drone = p.getVehicle()
                                drone.setPosition(target)
        except Exception, e:
            fht.Debug("Exception in fht_admin.droneTeleport(): " + str(e))

    def rallyLink(self, cmd, args, p):
##        try:
            rallies = fhtd.fhtPluginObjects['fht_deploySpawnPoint']
            rallies.hooker = self.hooker
            rallies.onRemoteCommand(p.index, "FHT_SL_deploying_spawnpoint")
##        except Exception, e:
##            fht.Debug("Exception in fht_admin.rallyLink(): " + str(e))

    def rallyResetLink(self, cmd, args, p):
##        try:
            rallies = fhtd.fhtPluginObjects['fht_deploySpawnPoint']
            rallies.hooker = self.hooker
            rallies.resetRally(p)
##        except Exception, e:
##            fht.Debug("Exception in fht_admin.rallyResetLink(): " + str(e))


    def adminCall(self, cmd, args, p):
        try:
            i = 0
            reason = ""
            while i < len(args):
                reason += str(args[i] + " ")
                i += 1
            fht.adminPM(reason, p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.adminCall(): " + str(e))


    def getValue(self, cmd, args, p):
        try:
            if not len(args) is 1:
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a object in fht_settings.py.", p)                
            else:
                if not "game." in args[0]:
                    module = args[0].split(".")[0]
                    object = args[0].replace(module + ".", "")
                    module = "game.plugins." + module
                    fht.Debug(module)
                    fht.Debug(object)
                else:
                    object = args[0].split(".")[-1].replace(".", "")
                    module = args[0].replace("." + object, "")
                    fht.Debug(module)
                    fht.Debug(object)
                try:
                    oldVal = eval(args[0])
                except:
                    try:
                        oldVal = getattr(sys.modules[module], object)
                    except Exception, e:
                        fht.Debug(str(e))
                        fht.personalMessage("§C1001" + args[0] + " not found.", p)
                        return

                needType = type(oldVal)
                typeName = str(needType).split("'")
                typeName = typeName[len(typeName)-2]
                fht.personalMessage("§C1001" + module + "." + object + " currently set to " + str(oldVal) + " (Type: " + typeName + ")", p)
                return
        except Exception, e:
            fht.Debug("Exception in fht_admin.getValue(): " + str(e)) 

    def setValue(self, cmd, args, p):
        try:
            if not len(args) is 2:
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify a module's object and the value to set it to.", p)                
            else:
                if not "game." in args[0]:
                    module = args[0].split(".")[0]
                    object = args[0].replace(module + ".", "")
                    module = "game.plugins." + module
                    fht.Debug(module)
                    fht.Debug(object)
                else:
                    object = args[0].split(".")[-1].replace(".", "")
                    module = args[0].replace("." + object, "")
                    fht.Debug(module)
                    fht.Debug(object)
                try:
                    oldVal = eval(args[0])
                except:
                    try:
                        oldVal = getattr(sys.modules[module], object)
                    except:
                        fht.personalMessage("§C1001" + args[0] + " not found.", p)
                        return
                                            
                needType = type(oldVal)
                arg = None
                try:
                    arg = eval(args[1])
                    givType = type(arg)
                    if not givType is needType:
                        raise Exception
                    else:
                        setattr(sys.modules[module], object, arg)

                except Exception, e:
                    fht.Debug(str(e))
                    typeName = str(needType).split("'")
                    typeName = typeName[len(typeName)-2]
                    givTypeName = str(givType).split("'")
                    givTypeName = givTypeName[len(givTypeName)-2]                    
                    fht.personalMessage("§C1001" + args[0] + " requires a " + typeName + " argument. (" + givTypeName + " was given)", p)
                    return
                fht.adminPM("§C1001" + args[0] + " has been set to " + str(arg), p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.setValue(): " + str(e))         

    def enablePlugin(self, cmd, args, p):
        try:
            fhtPlugins = {
                "redeps":       "doRedeployables",
                "killcheck":    "doMainBaseCheck",
                "rallies":      "doRallies"
                }
            params = [ "0", "1" ]
            if not len(args) is 2 or not args[0].lower() in fhtPlugins or not args[1] in params:
                fht.personalMessage("§C1001Incorrect usage of '" + cmd + "'. Please specify one of the following plugins: redeps, killcheck, rallies and a parameter 1/0 (on/off).", p)
            else:
                param = int(args[1])
                plugin = args[0].lower()
                if not getattr(fhts, fhtPlugins[plugin]) is param:
                    setattr(fhts, fhtPlugins[plugin], param)
                    if not param:
                        fht.adminPM((plugin + " plugin has been disabled."), p)
                        if "rallies" in plugin:
                            rallies = fhtd.fhtPluginObjects['fht_deploySpawnPoint']
                            rallies.hooker = self.hooker
                            rallies.shutOff()
                        if "redeps" in plugin:
                            redeps = fhtd.fhtPluginObjects['fht_reDeployables']
                            redeps.hooker = self.hooker
                            redeps.shutOff()                          
                    else:
                        fht.adminPM((plugin + " plugin has been enabled."), p)
                        if "killcheck" in plugin:
                            mBKC = fhtd.fhtPluginObjects['fht_mainBaseKillCheck']
                            mBKC.hooker = self.hooker
                            for cp in fhtd.mainBases:
                                mBKC.updateMainBaseSize(cp, 0.0)
                        if "rallies" in plugin:
                            rallies = fhtd.fhtPluginObjects['fht_deploySpawnPoint']
                            rallies.hooker = self.hooker
                            rallies.createFallbacks()
                else:
                    if not param:
                        fht.personalMessage((args[0].lower() + " plugin is already disabled."), p)
                    else:
                        fht.personalMessage((args[0].lower() + " plugin is already enabled."), p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.enablePlugin(): " + str(e))                    


    def debugPlayer(self, cmd, args, p):
        try:
            if not len(args) is 1 or not args[0] in [ "0", "1" ]:
                fht.personalMessage("§C1001Please specify a parameter (0/1) ", p)
            else:
                if int(args[0]):
                    if not p in fhtd.debugUsers:
                        fhtd.debugUsers.append(p)
                        fht.personalMessage("§C1001Turned on debug messages for " + p.getName(), p)
                else:
                    if p in fhtd.debugUsers:
                        fhtd.debugUsers.remove(p)
                        fht.personalMessage("§C1001Turned off debug messages for " + p.getName(), p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.debugPlayer(): " + str(e))   


    def debugGlobal(self, cmd, args, p):
        try:
            if not len(args) is 1 or not args[0] in [ "0", "1" ]:
                fht.personalMessage("§C1001Please specify a parameter (0/1) ", p)
            else:
                bVar = bool(int(args[0]))
                if fhts.debugging is bVar:
                    fht.personalMessage("Global debugging is already set to " + str(bVar), p)
                else:
                    fhts.debugging = bVar
                    fht.adminPM("§C1001Global debugging has been set to " + str(bVar), p)                    
        except:
                fht.Debug("Exception in PythonDebug")
            
    
    def onChatMessage(self, playerID, msgText, channel, flags):
        try:
            if len(msgText) > 1 and playerID != -1:
                msgText = msgText.replace("HUD_TEXT_CHAT_TEAM", "")
                msgText = msgText.replace("HUD_TEXT_CHAT_SQUAD", "")
                msgText = msgText.replace("HUD_TEXT_CHAT_DEADPREFIX", "")
                msgText = msgText.replace("HUD_CHAT_DEADPREFIX", "")
                if msgText.startswith("*"):
                        msgText = msgText.replace("*", "", 1)
                if msgText.startswith(" "):
                        msgText = msgText.replace(" ", "", 1)

                if not msgText.startswith(fhts.fht_commandSymbol):
                    rallyCommands = [ "rp", "rally", "rallypoint", "rr", "resetrally" ]
                    if not msgText.lower() in rallyCommands:
                        return False

                command = msgText.split(" ")[0].replace(fhts.fht_commandSymbol, "", 1)
                fht.Debug("Found command is %s" %(command))
                if not self.fht_adminCommands.has_key(command):
                    fht.Debug("The entered command %s was not a fht command" %(command))
                    return False

                p = bf2.playerManager.getPlayerByIndex(playerID)
                if fhts.isDedicated and fhts.fht_adminPowerLevels[command] != 777:
                    fht.Debug("Server is dedicated, proceeding with hash checks")
                        
                    try:
                        if p.teamswitch == "":
                            pass
                    except:
                        fht.Debug("Playervariables aren't set, initiating now")
                        fht.playerInit(p)

                    if p.hash == "":
                        fht.Debug("Player has no hash set, finding it now")
                        tHash = fht.getPlayerHash(p.getName())
                        if not tHash:
                            return False
                        else:
                            fht.Debug("Hash found, setting it now")
                            p.hash = tHash

                    if not fhts.fht_adminHashes.has_key(p.hash):
                        fht.Debug("The player's hash doesn't match an admin's hash")
                        return False
                    fht.Debug("Hash found!")
                    if fhts.fht_adminHashes[p.hash] > fhts.fht_adminPowerLevels[command]:
                        fht.Debug("Admin doesn't have enough rights to execute this command!")
                        fht.personalMessage("§C1001You do not have sufficient rights to execute this command", p)
                        return False
                else:
                    fht.Debug("Server is not dedicated (or an 'open' command was used), not performing hash check!")
                    
                fht.Debug("Executing command now...")
                args = msgText.replace(fhts.fht_commandSymbol + command, "", 1).strip().split()
                self.fht_adminCommands[command](command, args, p)                  
                fht.Debug("Done executing %s" %(command))
                
        except Exception, e:
            fht.Debug("Exception in fht_admin.onChatMessage(): " + str(e)) 

    def findLocation(self, cmd, args, p):
        try:
            if not p.isAlive() or p.isManDown():
                return False
            else:
                pos = p.getDefaultVehicle().getPosition()
                fht.personalMessage("Location: %f, %f, %f"%(pos[0], pos[1], pos[2]), p)                         
        except Exception, e:
            fht.Debug("Exception in fht_admin.findLocation(): " + str(e))   


    def textLive(self, cmd, args, p):
        try:
            if fhtd.isLive:
                fht.personalMessage("Round is live.", p)
                utils.rconExec('game.sayall "?Round is LIVE."')
            else:
                fht.personalMessage("Round is NOT live.", p)
                utils.rconExec('game.sayall "?Round is NOT live."')
        except Exception, e:
            fht.Debug("Exception in fht_admin.textLive(): " + str(e))  


    def textPerimeter(self, cmd, args, p):
        try:
            found = 0
            for player in bf2.playerManager.getPlayers():
                if hasattr(player, 'enterPerimeterAt') and player.enterPerimeterAt:
                    team = ''
                    time = float(host.timer_getWallTime() - player.enterPerimeterAt)
                    found += 1
                    if player.getTeam() == 2: team = 'axis'
                    if player.getTeam() == 1: team = 'allied'
                    fht.personalMessage("%s is inside the %s main base perimeter; entered %.0f seconds ago. Artylike Objects destroyed: %i"%(player.getName(), team, time, player.ArtyDestroyed), p)
            if found == 0:
                fht.personalMessage("Currently no players in enemy main base (including perimeter).", p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.textPerimeter(): " + str(e))  

                    
    def textHelp(self, cmd, args, p):
        try:
            fht.personalMessage("§C1001Custom fht commands:", p)
            i = 0
            keys = ""
            for key in self.fht_adminCommands:
                if fhts.isDedicated and fhts.fht_adminPowerLevels[key] != 777:
                    try:
                        if p.teamswitch == "":
                            pass
                    except:
                        fht.playerInit(p)
                    if p.hash == "":
                        tHash = fht.getPlayerHash(p.getName())
                        if not tHash:
                            return False
                        else:
                            p.hash = tHash
                    if not fhts.fht_adminHashes.has_key(p.hash) or fhts.fht_adminHashes[p.hash] > fhts.fht_adminPowerLevels[key]:
                        continue
                i += 1
                if keys is not "":
                    keys += ", "
                keys += fhts.fht_commandSymbol + key
                if i is 8:
                    fht.personalMessage("§C1001" + keys, p)
                    keys = ""
                    i = 0
            if i > 0:
                fht.personalMessage("§C1001" + keys, p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.textHelp(): " + str(e)) 


    def textScore(self, cmd, args, p):
        try:
            fht.personalMessage("This feature is not available right now.", p)
        except Exception, e:
            fht.Debug("Exception in fht_admin.textScore(): " + str(e)) 

    def textScore(self, cmd, args, p):
            try:
                    if not fhtd.roundsPlayed or not self.axisstart or not self.alliedstart:
                        fht.personalMessage("No Live Rounds have been played yet.", p)
                        return
                    axis_rvp = ( float(self.axis_wins) / float(self.rounds_played) ) * RVP
                    adf.Debug("Axis RVP: %i" %axis_rvp)
                    axis_tvp = ( float(self.axis_tickets) / float( self.rounds_played * self.axisstart ) ) * TVP
                    adf.Debug("Axis RVP: %i" %axis_tvp)

                    allied_rvp = ( float(self.allied_wins) / float(self.rounds_played) ) * RVP
                    adf.Debug("Allies RVP: %i" %allied_rvp)
                    allied_tvp = ( float(self.allied_tickets) / float( self.rounds_played * self.alliedstart ) ) * TVP
                    adf.Debug("Allies TVP: %i" %allied_tvp)

                    axis_score = round((axis_rvp + axis_tvp)*(float(self.scoremod)/float(100.0)))
                    allied_score = round((allied_rvp + allied_tvp)*(float(self.scoremod)/float(100.0)))

                    if self.rounds_played == 1:
                        s = ""
                    else:
                        s = "s"

                    msg = "Total Remaining Tickets after %i Round%s: §C1001Axis: %i    Allies:  %i"%(self.rounds_played, s, self.axis_tickets, self.allied_tickets)
                    fht.personalMessage(msg, p)
                    
                    msg2 = "Projected Battle Score after %i Round%s: §C1001Axis: %.0f    Allies:  %.0f"%(self.rounds_played, s, axis_score, allied_score)
                    fht.personalMessage(msg2, p)
            except:
                    adf.Debug("Execption in TextScore()")



    def WriteScore(self, rds, axis, allies):
        try:
                            loggingFile = open(loggingFileName, "a")
                            
                            d = time.strftime("%Y-%m-%d %H:%M:%S")
                            message = ("Round %i Axis: %i Allies: %i ScoreMod: %i written %s\n" %(rds, axis, allies, self.scoremod, d))
                            loggingFile.write(message)

                            loggingFile.close()

                            persistentFile = open(persistentFileName, "a")
                            mapname = bf2.gameLogic.getMapName()
                            persistent_message = ("Map: %s, Round %i, Axis: %i out of %i, Allies: %i out of %i, Score Modifier: %i automatically written on %s\n" %(mapname, rds, axis, self.axisstart, allies, self.alliedstart, self.scoremod, d))                            
                            persistentFile.write(persistent_message)

                            persistentFile.close()

                            self.ReadScore()
        except Exception, e:
            fht.Debug("Exception in fht_admin.textScore(): " + str(e)) 


    def clearScores(self, cmd, args, p):
            try:
                    loggingFile = open(fhts.loggingFileName, "w")
                    loggingFile.close()
                    
                    adm_msg = ("Battle Scores have been cleared.")
                    fht.AdminPM(adm_msg, p)

                    self.ReadScore()
                    
            except:
                    fht.Debug("Execption in ClearScores()")
##


    def readScore(self):
        try:
            loggingFile = open(fhts.scoreFileName, "r")

            self.axis_tickets = 0
            self.axis_wins = 0
            self.allied_tickets = 0
            self.allied_wins = 0
            self.rounds_played = 0
                            
            for line in loggingFile:
                args = line.strip().split()
                rds = args[1]
                axis = args[3]
                allied = args[5]
                self.scoremod = int(args[7])

                if self.rounds_played < int(rds):
                    self.rounds_played = int(rds)

                    self.axis_tickets += int(axis)
                    self.allied_tickets += int(allied)

                if int(axis) > int(allied):
                    self.axis_wins += 1
                elif int(axis) < int(allied):
                    self.allied_wins += 1                                    
                                    
            loggingFile.close()

        except Exception, e:
            fht.Debug("Exception in fht_admin.readScore(): " + str(e))
