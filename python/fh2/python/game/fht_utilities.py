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
#   fht_utilities.py - global functions that are used by fht plugins.

import bf2, host, bf2.Timer, random, math, sys, string, os, default, new, re, time, conParser
from game.stats.constants import *
import game.utilities as utils
import game.fht_data as fhtd
import game.fht_settings as fhts
import game.gamemodes.gpm_cq as gpm
rcon = utils.rconExec
debugFileName = "mods/fh2/fht/fhtdebug.log"
errorFileName = "mods/fh2/fht/fhterrors.log"


def getPluginObjects():
    Debug("fht_utilities.getPluginObjects")
    try:
        Debug("fht_utilities.getPluginObjects")
        fhtd.fhtPluginObjects = {}
        fhtd.allPluginObjects = {}
        fhtd.kitLimiters = {}
        for p in gpm.g_plugin.loaded_plugins:
            fhtd.allPluginObjects[p.__class__.__name__] = p
            Debug(p.__class__.__name__)
            if "fht_" in p.__class__.__name__.lower():
                fhtd.fhtPluginObjects[p.__class__.__name__] = p
            if "limit" in p.__class__.__name__.lower():
                if hasattr(p, "info"):
                    team = p.info.team
                    slot = p.info.slot
                    try:
                        fhtd.kitLimiters[team][slot] = p
                    except Exception, e:
                        fhtd.kitLimiters[team] = {}
                        fhtd.kitLimiters[team][slot] = p
                    
    except Exception, e:
        Debug("Failed to get plugin Objects" + str(e))
    Debug("fht_utilities.getPluginObjects done")

def Debug(msg):
        msg = str(msg)
        if "exception" in msg.lower():
            errorFile = open(errorFileName, "a")
            d = time.strftime("%Y-%m-%d %H:%M:%S")
            errorFile.write(d + ": " + msg + "\n")
            errorFile.close()
            if not fhts.debugging:
                adminPM(msg)
        if fhts.debugging:
                host.rcon_invoke('echo "DEBUG: %s"' % msg)
                host.rcon_invoke('game.sayall "DEBUG: %s"' % msg)
                print msg
                debugFile = open(debugFileName, "a")
                d = time.strftime("%Y-%m-%d %H:%M:%S")
                debugFile.write(d + ": " + msg + "\n")                
                debugFile.close()                   
        if fhts.isDedicated:
                for p in fhtd.debugUsers:
                        personalMessage(msg, p)

def deleteThing(thing, hide = False):
    try:
        ids = utils.listObjectsOfTemplate(thing.templateName.lower())
        for id in ids:
            utils.rconExec("object.active id" + str(id))
            pos = utils.rconExec("object.absolutePosition")
            pos = pos.split("/")
            pos = [ float(x) for x in pos ]
            pos = tuple(pos)
            if pos is (0.0, 0.0, 0.0):
                continue
            if sameTransform(pos, thing.getPosition()):
                if hide:
                    thing.setPosition(utils.denormalise(thing.getPosition(), (0.0, -50.0, 0.0)))
                utils.deleteObject(id)
                return
    except Exception, e:
        Debug("Exception in fht.deleteThing(): " + str(e))

def reloadMap():
    try:
        currentMapID = utils.rconExec("admin.currentLevel").strip()
        utils.rconExec("admin.nextLevel %s" % str(currentMapID))
        utils.rconExec('admin.runNextLevel')
    except Exception, e:
        Debug("Exception in fht.reloadMap(): " + str(e)) 


def sameTransform(x, y):
    if math.fabs(x[0] - y[0]) < 0.20000000000000001 and math.fabs(x[1] - y[1]) < 0.20000000000000001:
        return math.fabs(x[2] - y[2]) < 0.20000000000000001
    else:
        return False

def getControlPoints():
    Debug("fht_utilities.getControlPoints")
    try:
        import game.gamemodes.gpm_cq
        fhtd.cpList = game.gamemodes.gpm_cq.g_controlPoints
    except:
        fhtd.cpList = []
    try:
        if not len(fhtd.cpList):
            fhtd.cpList = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
        for cp in fhtd.cpList:
            utils.active(cp.templateName)
            cp.cpID = int(utils.rconExec("ObjectTemplate.controlPointId"))
            cp.areaValue1 = int(utils.templateProperty('areaValueTeam1'))
            cp.areaValue2 = int(utils.templateProperty('areaValueTeam2'))
            cp.showOnMinimap = int(utils.templateProperty('showonminimap'))
    except Exception, e:
        Debug("Exception in fht.getControlPoints(): " + str(e)) 
    Debug("fht_utilities.getControlPoints done")

def getSpawnPoints():
    Debug("fht_utilities.getSpawnPoints")
    try:
        fhtd.spList = []
        fhtd.spCPIds = []
        fhtd.spList = bf2.objectManager.getObjectsOfType('dice.bf.SpawnPoint')
        for sp in fhtd.spList:
            utils.active(sp.templateName)
            sp.cpID = int(utils.templateProperty('setControlPointId'))
            fhtd.spCPIds.append(sp.cpID)
            if not (utils.templateProperty('setGroup')).isdigit():
                sp.spawnGroup = None
            else: 
                sp.spawnGroup = int(utils.templateProperty('setGroup'))
    except Exception, e:
        Debug("Exception in fht.getSpawnPoints(): " + str(e)) 
    Debug("fht_utilities.getSpawnPoints done")

def getSpawners():
    Debug("fht_utilities.getSpawners")
    try:
        fhtd.objectSpawners = []
        fhtd.depSpawners = []
        fhtd.objectSpawners = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ObjectSpawner')
        for s in fhtd.objectSpawners:
            if not utils.reasonableObject(s):
                continue
            
            #Debug("spawner: " + s.templateName) 
            utils.active(s.templateName)
            #Debug("active: " + s.templateName) 
            s.templates = []
            #Debug("templates: " + s.templateName) 
            script = utils.printScriptTillItFuckingWorks()
            #Debug("script: " + s.templateName) 
            parser = conParser.ConParser()
            #Debug("parser: " + s.templateName) 
            parser.run_string(script)
            #Debug("run_string: " + s.templateName) 
            script_lines = utils.printScriptTillItFuckingWorks().lower().splitlines()
           
            for line in script_lines:
                words = line.split()
                if len(words) == 0 or words[0] != 'objecttemplate.setobjecttemplate':
                    continue
                #Debug("0: " + words[0]) 
                #Debug("1: " + words[1]) 
                #Debug("2: " + words[2]) 
                s.templates.append(words[2])
                         
                if s in fhtd.depSpawners:
                    continue
                elif words[2].lower() in fhts.emplacements.keys():
                    fhtd.depSpawners.append(s)
            s.id = getId(s)    
            #Debug("s.id: " + s.id) 
            utils.activeObject(s.id)
            s.cpID = utils.rconExec("Object.getControlPointId")
            #Debug("s.cpID: " + s.cpID) 
    except Exception, e:
        Debug("Exception in fht.getSpawners(): " + str(e)) 	
    Debug("fht_utilities.getSpawners done")

def setCPSpawnPoints():
    Debug("fht_utilities.setCPSpawnPoints")
    try:
        cpSpawnPoints = { }   
        for cp in fhtd.cpList:
            if not cp.cpID in fhtd.spCPIds:
                continue
            else:
                cpSpawnPoints[cp.cpID] = cp.getPosition()
        for sp in fhtd.spList:
            if not sp.spawnGroup:
                cpSpawnPoints[sp.cpID] = sp.getPosition()
        fhtd.cpSpawnPoints = cpSpawnPoints
        for key in cpSpawnPoints.keys():
            Debug(str(key))
            Debug(str(cpSpawnPoints[key]))
    except Exception, e:
        Debug("Exception in fht.setCPSpawnPoints(): " + str(e))        
    Debug("fht_utilities.setCPSpawnPoints done")

def rot_X(w):
    w = math.radians(w)
    cos_w = math.cos(w)
    sin_w = math.sin(w)
    return [
        [1.0, 0.0, 0.0],
        [0.0, cos_w, -sin_w],
        [0.0, sin_w, cos_w]
        ]


def rot_Y(w):
    w = math.radians(w)
    cos_w = math.cos(w)
    sin_w = math.sin(w)
    return [
        [cos_w, 0.0, sin_w],
        [0.0, 1.0, 0.0],
        [-sin_w, 0.0, cos_w]
        ]


def rot_Z(w):
    w = math.radians(w)
    cos_w = math.cos(w)
    sin_w = math.sin(w)
    return [
        [cos_w, -sin_w, 0.0],
        [sin_w, cos_w, 0.0],
        [0.0, 0.0, 1.0]
        ]


def rotateVector(rot, v):
    if rot[0]:
        v = matMultVec(rot_Y(rot[0]), v)
    if rot[1]:
        v = matMultVec(rot_X(rot[1]), v)
    if rot[2]:
        v = matMultVec(rot_Z(rot[2]), v)
    return v


def scalarProd(u, v):
     sum = 0
     for i in xrange(len(u)):
            sum += u[i] * v[i]
     return sum

def matMultVec(m, v):
     return [ scalarProd(r, v) for r in m ]


def squadMessage(ref, msg, team = None):
    if team:
        for p in bf2.playerManager.getPlayers():
            if p.getTeam() is team and p.getSquadId() is ref:
                personalMessage(msg, p)
    else:
        for p in bf2.playerManager.getPlayers():
            if p.getTeam() is ref.getTeam() and p.getSquadId() is ref.getSquadId():
                personalMessage(msg, p)


def personalMessage(msg, p):
    if int(host.rcon_invoke("sv.internet").strip()) == 1:
            host.sgl_sendTextMessage(p.index, 14, 1, msg, 0 )
    else:
            host.rcon_invoke('game.sayall "%s"' % msg)

def adminPM(msg, p = None):
    try:
        if p:
            msg += " [" + p.getName() + "]"

        if fhts.isDedicated:
            for p in bf2.playerManager.getPlayers():
                try:
                    if p.hash is "":
                        pass
                except:
                    Debug("Playerhash-variable isn't set, player isn't inited, initiating now")
                    playerInit(p)

                if p.hash is "":
                    tHash = getPlayerHash(p.getName())
                    if not tHash:
                        Debug("Hash not found. Not sending a PM to " + p.getName())
                    else:
                        Debug("Hash found, setting it now")
                        p.hash = tHash

                if p.hash is not "" and fhts.fht_adminHashes.has_key(p.hash):
                    if not fhts.fht_adminHashes[p.hash] > fhts.fht_adminPowerLevels["setlive"]:
                        personalMessage(msg, p)     
        else:
            utils.sayAll(msg)
    except Exception, e:
        Debug("Exception in fht.adminPM(): " + str(e)) 

# Init the player
def playerInit(p):
	try:
		p.teamswitch = 0
		p.die = 0
		p.killreason = ""
		p.hash = ""
	except:
		Debug("Exception in PlayerInit()")

# Get the cd key hash of a player
def getPlayerHash(playerName):
	try:
		Debug("Entered GetPlayerHash")
		playerData = host.rcon_invoke("admin.listplayers").strip().split("\n")

		i = 0
		while i < len(playerData):
			name = playerData[i].split(" - ")
			name = name[1].split(" is ")

			# Playername found yes/no
			if name[0] == playerName:
				Debug("Playerhash and playername found")

				# Now search for the hash
				hash = playerData[i+1].split("hash: ")
				return hash[1].strip()

			# I'm adding two, because player data consists of two lines
			i += 2

		# If you get here, the hash wasn't found
		Debug("No player hash found?")
		return False
	except:
		Debug("Exception in GetPlayerHash")
		return False

def nearestCP(origin, onlyTeam = 0, forSpawn = False):
    minDis = -1
    cpClose = None
    try:
        for cp in fhtd.cpList:
            utils.active(cp.templateName)
            if forSpawn and not cp.cpID in fhtd.spCPIds:
                continue
            if ( not onlyTeam or onlyTeam is cp.cp_getParam('team')) and int(utils.templateProperty('showOnMinimap')):
                newDis = utils.vectorDistance(origin, cp.getPosition())
                if (minDis is -1) or (newDis <= minDis):
                    minDis = newDis
                    cpClose = cp
    except Exception, e:
        Debug("Exception in fht.nearestCP(): " + str(e))
    return cpClose, minDis

def nearestSP(origin, onlyTeam = 0):
        try:
            cp, distance = nearestCP(origin, onlyTeam, True)
            pos = fhtd.cpSpawnPoints[cp.cpID]
            return pos, distance
        except Exception, e:
            Debug("Exception in fht.nearestSP(): " + str(e))
            return (0.0, 0.0, 0.0), -1

def getId(obj):
    ids = []
    for i in utils.listObjectsOfTemplate(obj.templateName.lower()):
        ids.append(i)
    for id, thing in zip(ids, bf2.objectManager.getObjectsOfTemplate(obj.templateName.lower())):
        if thing is obj:
            return id
    return None

def playersInSquad(team, squadid):
    players = bf2.playerManager.getPlayers()
    squadmembers = []
    for p in players:
        if p.isValid() and p.getTeam() == team and p.getSquadId() == squadid:
            squadmembers.append(p)
    return squadmembers

def isAllowedAttackVehicleType(v):
    if v.templateName.lower() in fhts.customAllowedAttackVehicles:
        return True
    elif getVehicleType(v.templateName.lower()) in fhts.allowedAttackVehicleTypes:
        return True
    else:
        return False

def isMainBaseVehicleType(v):
    if v.templateName.lower() in fhts.customMainBaseVehicles:
        return True
    elif getVehicleType(v.templateName.lower()) in fhts.mainBaseVehicleTypes:
        return True
    else:
        return False

def isMonitoredVehicleType(v):
    if v.templateName.lower() in fhts.customMonitorVehicles:
        return True
    elif getVehicleType(v.templateName.lower()) in fhts.monitorVehicleTypes:
        return True
    else:
        return False

def isAllowedVehicleType(v):
    if v.templateName.lower() in fhts.customVehicle:
        return True
    elif getVehicleType(v.templateName.lower()) in fhts.allowedVehicleTypes:
        return True
    else:
        return False

def isAllowedWeaponType(w):
    if w.templateName.lower() in fhts.customWeapons:
        return True
    elif getWeaponType(w.templateName.lower()) in fhts.allowedWeaponTypes:
        return True
    else:
        return False


def getRedeployables():
    list = [ x['current'] for x in fhtd.depRegister.values() ]
    for l in list:
        if not l or not utils.reasonableObject(l):
            list.remove(l)
    return list

def inSplashZone(thing):
    activeDepList = getRedeployables()
    for obj in activeDepList:
        if not utils.reasonableObject(obj):
            continue
        else:
            if utils.isInRange(thing.getPosition(), obj.getPosition(), fhts.artyUnsafeRadius):
                return True
    return False

def findPlayer(playerName):
	matches = 0
	p_good = ""
	try:
		for p in bf2.playerManager.getPlayers():
			if p.getName().lower().find(playerName.lower()) != -1:
				p_good = p
				matches += 1
				if matches > 1:
					return "more"

		if matches == 0:
			return "none"
		else:
			return p_good
	except:
		Debug("Exception in FindPlayer()")
		return "none"

def sortCPs():
    Debug("fht_utilities.sortCPs")
    try:
        cpList = fhtd.cpList
        mbList = fhtd.mainBases
        cpListExt = []
        mbListExt = []
        for cp in cpList:
            if not utils.reasonableObject(cp) or not cp.showOnMinimap:
                continue
            if cp.cp_getParam('unableToChangeTeam'):
                mbListExt.append( (cp, cp.getPosition()[2]) )
            else:
                cpListExt.append( (cp, cp.getPosition()[2]) )                

        def getKey(item):
            return item[1]

        def mysorted(iterable, key, reverse=0):
            temp = [(key(x), x) for x in iterable]
            temp.sort()
            if reverse:
                return [temp[i][1] for i in xrange(len(temp) - 1, -1, -1)]
            return [t[1] for t in temp]

        cpListSort = mysorted(cpListExt, key=getKey, reverse=True)
        mbListSort = mysorted(mbListExt, key=getKey, reverse=True)

        fhtd.sortedMBs = []
        for item in mbListSort:
            fhtd.sortedMBs.append(item[0])
            
        fhtd.sortedCPs = []
        for item in cpListSort:
            fhtd.sortedCPs.append(item[0])
    except:
        Debug("Exception in sortCPs")
    Debug("fht_utilities.sortCPs done")

def getSortedCP(no, mainBases = False):
    if mainBases:
        sorList = fhtd.sortedMBs
    else:
        sorList = fhtd.sortedCPs

    if len(sorList) < int(no) or int(no) < 1:
        return None
    else:
        return sorList[int(no)-1]
