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
# fht_reDeployables.py -- allows relocation of static emplacements
#
#  ©2014 Harmonikater for Forgotten Honor
import bf2, host, bf2.Timer, random, math
from game.gameplayPlugin import base
import game.utilities as utils
import game.fht_utilities as fht
import game.fht_settings as fhts
import game.fht_data as fhtd


class fht_reDeployables(base):

    def __init__(self, *args, **kwargs):
        try:
            self.hooker = None
            fhtd.depRegister = {}
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.init(): " + str(e))            



    def round_start(self, hooker):
        try:
            self.hooker = hooker
            fhtd.deployerKits = [ x['kit'].lower() for x in fhts.emplacements.values() ]
            hooker.register('PlayerChangeWeapon', self.onWeaponChanged)
            hooker.register('PickupKit', self.onKitPickUp)
            hooker.register('DropKit', self.onKitDrop)
            hooker.register('EnterVehicle', self.onVehicleEntered)
            hooker.register('VehicleDestroyed', self.onVehicleDestroyed)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.round_start(): " + str(e))


    def onVehicleEntered(self, p, v, free):
        try:
            if fhts.doRedeployables:
                vln = v.templateName.lower()
                if v.templateName.lower() in fhts.emplacements.keys():
                    if not hasattr(v, 'DID'):
                        for s in fhtd.depSpawners:
                            if vln in s.templates and utils.isInRange(v.getPosition(), s.getPosition(), 1.0):
                                if not hasattr(s, 'depAssigned') or not s.depAssigned:
                                    n = 0
                                    while (vln + '_' + str(n)) in fhtd.depRegister:
                                        n += 1
                                    DID = vln + '_' + str(n)
                                    fhtd.depRegister[DID] = dict(name = vln, pos = v.getPosition(), rot = v.getRotation(), active = True, current = v)
                                    v.DID = DID
                                    self.spawnDeployerKit(v, DID)
                                    fht.Debug("fht_reDeployables.py: Found %s (late), setting DID: %s" %(vln, DID))
                                    s.depAssigned = True
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.onVehicleEntered(): " + str(e))               


    def spawnDeployerKit(self, obj, DID):
        try:
            if fhts.doRedeployables:
                fht.Debug("Spawning Kit on " + str(DID))
                kitname = fhts.emplacements[obj.templateName.lower()]['kit']
                offset = (0.0, 1.0, -1.0)
                pos = utils.denormalise(obj.getPosition(), fht.rotateVector(obj.getRotation(), offset))
                utils.createObject(kitname, pos, obj.getRotation(), 0, 9999)
                self.hooker.later(fhts.depRegisterDelay, self.assignDID, kitname, pos, DID)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.spawnDeployerKit(): " + str(e))            
        

    def assignDID(self, template, pos, DID, kit = None, attempt = 0):
        try:
            if fhts.doRedeployables:
                found = False
                for obj in bf2.objectManager.getObjectsOfTemplate(template):
                    if not utils.reasonableObject(obj) or ( hasattr(obj, 'DID') and obj.DID is not DID ):
                        continue
                    if fht.sameTransform(pos, obj.getPosition()):
                        if not ( hasattr(obj, 'DID') and obj.DID is DID ):
                            found = True
                            obj.DID = DID
                            if kit:
                                fhtd.depRegister[DID]['active'] = True
                                fhtd.depRegister[DID]['current'] = obj
                    elif template in fhtd.deployerKits:
                        self.hooker.later(fhts.depRegisterDelay*2.0, self.deleteUnassignedKit, obj)
                if not found:
                    fht.Debug("fht_reDeployables.assignDID: %s not found on %d. attempt" %(template, attempt + 1))
                    if template in fhtd.deployerKits:
                        if attempt > fhts.depMaxAttempts:
                            return
                        offset = (0.0, 0.05, -0.5)
                        rot = fhtd.depRegister[DID]['rot']
                        pos = utils.denormalise(pos, fht.rotateVector(rot, offset))
                        utils.createObject(template, pos, rot, 0, 9999)
                        attempt += 1
                        self.hooker.later(fhts.respawnAttemptInterval, self.assignDID, template, pos, DID, attempt)
                        return
                    if pos is fhtd.depRegister[DID]['pos']:
                        self.hooker.later(fhts.respawnAttemptInterval, self.respawnEmplacement, DID)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.assignDID(): " + str(e))  






    def onWeaponChanged(self, p, wfrom, wto):
        try:   
            if fhts.doRedeployables:              
                if p.getKit() and (p.getKit().templateName.lower() in fhtd.deployerKits):
                    if wto and (wto.templateName.lower() in fhts.packWeapon):
                        p.monitorPacking = True
                        p.packActive = False
                        p.packLastCount = 0
                        self.monitorPacker(p)
                        fht.Debug("fht_reDeployables.onWeaponChanged(): Monitoring %s for packing." %p.getName())
                    else:
                        p.monitorPacking = False
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.onWeaponChanged(): " + str(e)) 
                

    def monitorPacker(self, p):
        try:
            fht.Debug("Entered fht_reDeployables.monitorPacker")
            if fhts.doRedeployables:
                if p.monitorPacking and p.isAlive():
                    kit = p.getKit()
                    if not hasattr(kit, 'DID'):
                        fht.Debug("fht_reDeployables.monitorPacker(): %s has a kit with no DID." %p.getName())
                        return
                    DID = kit.DID
                    info = fhts.emplacementInfo[(fhts.emplacements[fhtd.depRegister[DID]['name']]['type'])]
                    for (wName, count) in p.score.bulletsFired:
                        if (wName.lower() == fhts.packWeapon) and (int(count) > p.packLastCount):
                            p.packLastCount = int(count)
                            if not p.packActive:
                                template = fhtd.depRegister[DID]['name']
                                if fhtd.depRegister[DID]['active']:
                                    for obj in bf2.objectManager.getObjectsOfTemplate(template):
                                        if utils.reasonableObject(obj) and utils.isInRange(p.getDefaultVehicle().getPosition(), obj.getPosition(), fhts.packRadius):
                                            self.packEmplacementLoop(obj, p, count, p.getKit(), host.timer_getWallTime(), template, False)
                                            break

                                else:
                                    fht.Debug("%s , your kit has no active Deployment. Building." %p.getName())
                                    for marker in bf2.objectManager.getObjectsOfTemplate(fhts.requestObject):
                                        if utils.reasonableObject(marker) and utils.isInRange(marker.getPosition(), p.getDefaultVehicle().getPosition(), fhts.packRadius):
                                            if utils.isInRange(marker.getPosition(), fhtd.depRegister[DID]['pos'], info['radius']):
                                                self.packEmplacementLoop(marker, p, count, p.getKit(), host.timer_getWallTime(), template, True)
                                                break
                                            else:
                                                fht.Debug("%s is trying to deploy outside the allowed radius. Deleting marker as indication." %p.getName())
                                                fht.deleteThing(marker)
                    self.hooker.later(10, self.monitorPacker, p)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.monitorPacker(): " + str(e))

    def packEmplacementLoop(self, obj, p, startCount, kit, start, template, build):
        try:
            if fhts.doRedeployables:
                if ( not utils.reasonableObject(obj) ) or ( not p.isValid() ):
                    return
                if p.monitorPacking and p.isAlive():
                    info = fhts.emplacementInfo[(fhts.emplacements[template]['type'])]
                    p.packActive = True
                    if (not utils.isInRange(p.getDefaultVehicle().getPosition(), obj.getPosition(), fhts.packRadius)) or (not p.monitorPacking):
                        p.packActive = False
                        fht.Debug("%s moved too far away. Stopping Deployment." %p.getName())
                        return
                    if p.isAlive() and utils.reasonableObject(obj):
                        end = host.timer_getWallTime()
                        fht.Debug("%s : Time Passed: %i" %(p.getName(), int(end-start)))
                        if end - start > info['delay']*2:
                            fht.Debug("Time Limit reached by %s. Start again." %p.getName())
                            p.packActive = False
                            return
                        elif end - start > info['delay']:
                            for (weapon, count) in p.score.bulletsFired:
                                if (weapon.lower() == fhts.packWeapon):
                                    fht.Debug("Bullets fired by %s in interval: %f" %(p.getName(), count - startCount))
                                    fht.Debug("Should be at least: %f" %((fhts.depRPS*float(info['delay'])*fhts.depCorrFactor)))
                                    if ((count - startCount) > (fhts.depRPS*float(info['delay'])*fhts.depCorrFactor)):                
                                        if build:
                                            fht.Debug("%s : Build is True." %p.getName())
                                            self.buildEmplacement(obj, template, p, kit)
                                            p.packActive = False
                                            return
                                        else:
                                            fht.Debug("%s : Build is False." %p.getName())
                                            self.hooker.later(info['respawn'], self.respawnEmplacement, obj.DID)
                                            p.packActive = False
                                            fht.deleteThing(obj, True)
                                            fhtd.depRegister[obj.DID]['active'] = False
                                            fhtd.depRegister[obj.DID]['current'] = None
                                            p.packActive = False
                                            return
                        else:
                            self.hooker.later(5, self.packEmplacementLoop, obj, p, startCount, kit, start, template, build)
                        return
                p.packLastCount = 0
                p.packActive = False
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.packEmplacementLoop(): " + str(e))

    def buildEmplacement(self, m, template, p, kit):
        try:
            if fhts.doRedeployables:
                info = fhts.emplacementInfo[(fhts.emplacements[template]['type'])]
                pos = m.getPosition()
                rot = m.getRotation()
                if 'flatten' in info:
                    rot = utils.layFlat(rot)
                pos = utils.xform(pos, fht.rotateVector(rot, ( 0.0, fhts.emplacements[template].get('offset', 0.0) - fhts.crateHeight, 0.0)))
                utils.createObject(template, pos, rot, 0, 9999)
                self.hooker.later(fhts.depRegisterDelay, self.assignDID, template, pos, kit.DID, kit)
                fht.deleteThing(m)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.buildEmplacement(): " + str(e))                


            

    def onKitPickUp(self, p, kit):
        try:
            if fhts.doRedeployables:
                if kit.templateName.lower() in fhtd.deployerKits:
                    p.DID = kit.DID
                    fht.Debug("fht_reDeployables.onKitPickUp: %s picked up Deployer kit on %s." %(p.getName(), kit.DID))
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.onKitPickUp(): " + str(e))  

            
    def onKitDrop(self, p, kit):
        try:
            if fhts.doRedeployables:
                if kit.templateName.lower() in fhtd.deployerKits:
                    p.monitorPacking = False
                    self.hooker.later(fhts.depRegisterDelay, fht.deleteThing, kit)
                    if fhtd.depRegister[p.DID]['active']:
                        obj = fhtd.depRegister[p.DID]['current']
                        if not utils.reasonableObject(obj):
                            fhtd.depRegister[p.DID]['current'] = None
                            fhtd.depRegister[p.DID]['active'] = False
                        else:
                            self.spawnDeployerKit(obj, p.DID)
                            return
                    template = fhtd.depRegister[p.DID]['name']
                    info = fhts.emplacementInfo[(fhts.emplacements[template]['type'])]                        
                    self.hooker.later(info['respawn'], self.respawnEmplacement, p.DID)                 
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.onKitDrop(): " + str(e))
            

    def deleteUnassignedKit(self, kit):
        try:
            if kit:
                if hasattr(kit, 'DID'):
                    return
                else:
                    fht.deleteThing(kit)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.deleteUnassignedKit(): " + str(e))  






    def onVehicleDestroyed(self, v, p):
        try:
            if not fhts.doRedeployables: return
            if v.templateName.lower() in fhts.emplacements.keys():
                if hasattr(v, 'DID'):
                    pos = fhtd.depRegister[v.DID]['pos']
                    if not fht.sameTransform(v.getPosition(), pos):
                        self.hooker.later(fhts.wreckTTL, self.deleteEmplacement, v)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.onVehicleDestroyed(): " + str(e))          

    def deleteEmplacement(self, v):
        try:
            if not fhts.doRedeployables: return
            info = fhts.emplacementInfo[(fhts.emplacements[v.templateName.lower()]['type'])]
            if utils.reasonableObject(v):
                if len(v.getOccupyingPlayers()) or ( v.hasArmor and not v.getIsWreck() ):
                    return
                else:
                    if hasattr(v, 'DID'):
                        self.hooker.later((info['respawn'] - fhts.wreckTTL), self.respawnEmplacement, v.DID)
                        for kit in bf2.objectManager.getObjectsOfTemplate(fhts.emplacements[v.templateName.lower()]['kit']):
                            if not hasattr(kit, 'DID'):
                                self.hooker.later(fhts.depRegisterDelay*2.0, self.deleteUnassignedKit, kit)
                            elif (kit.DID is v.DID) and not kit.getParent():
                                fht.deleteThing(kit)                                
                    fhtd.depRegister[v.DID]['current'] = None
                    fhtd.depRegister[v.DID]['active'] = False
                    fht.deleteThing(v)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.deleteEmplacement(): " + str(e))          

    def respawnEmplacement(self, DID, shutOff = False):
        try:
            if ( not fhts.doRedeployables or fhtd.depRegister[DID]['active'] ) and not shutOff: return
            template = fhtd.depRegister[DID]['name']
            pos = fhtd.depRegister[DID]['pos']
            rot = fhtd.depRegister[DID]['rot']

            kitname = fhts.emplacements[template]['kit']        
            for kit in bf2.objectManager.getObjectsOfTemplate(kitname):
                if not utils.reasonableObject(kit):
                    continue
                elif not hasattr(kit, 'DID'):
                    fht.Debug("Found a kit with no DID!")
                    self.hooker.later(fhts.depRegisterDelay*2.0, self.deleteUnassignedKit, kit)                
                elif kit.DID is DID:
                    fht.Debug("No respawn on %s , the deployer kit is still active." %DID)
                    return
            if self.checkPlayers(DID):
                fht.Debug("No respawn on %s , the deployer kit is still being used by a player." %DID)
                return
                
            utils.createObject(template, pos, rot, team = 0, ttl = 9999)
            if shutOff:
                return
            self.hooker.later(fhts.depRegisterDelay, self.assignDID, template, pos, DID, True)
        
            offset = (0.0, 1.0, -1.0)
            pos = utils.denormalise(pos, fht.rotateVector(rot, offset))
            utils.createObject(kitname, pos, rot, 0, 9999)
            self.hooker.later(fhts.depRegisterDelay, self.assignDID, kitname, pos, DID)
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.respawnEmplacement(): " + str(e))  

    def checkPlayers(self, DID):
        try:
            if not fhts.doRedeployables: return  
            for p in bf2.playerManager.getPlayers():
                if p.isValid() and p.isAlive() and not p.isManDown():
                    if p.getKit() and p.getKit().templateName.lower() in fhtd.deployerKits:
                        if hasattr(p, 'DID') and p.DID is DID:
                            return True
            return False
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.checkPlayers(): " + str(e))   


               
    def round_end(self, hooker):
        self.hooker = None
        fhtd.depRegister = []
        for s in fhtd.depSpawners:
            s.depAssigned = False


    def shutOff(self):
        try:
            for p in bf2.playerManager.getPlayers():
                if p.isValid() and p.isAlive() and not p.isManDown():
                    if p.getKit() and p.getKit().templateName.lower() in fhtd.deployerKits:
                        p.getVehicle().setDamage(0.00001)
                        p.getDefaultVehicle().setDamage(0.00001)
            for kitname in fhtd.deployerKits:
                for kit in bf2.objectManager.getObjectsOfTemplate(kitname):
                    if not kit.getParent():
                        fht.deleteThing(kit)
            for key in fhtd.depRegister.keys():
                fht.Debug(key)
                if not fhtd.depRegister[key]['active']:
                    fht.Debug("Not active")
                    self.respawnEmplacement(key, True)
                else:
                    fht.Debug("active")
                    obj = fhtd.depRegister[key]['current']
                    pos = fhtd.depRegister[key]['pos']
                    rot = fhtd.depRegister[key]['rot']                      
                    if not utils.reasonableObject(obj):
                        self.respawnEmplacement(key, True)
                    else:
                        if not fht.sameTransform(pos, obj.getPosition()):
                            fht.deleteThing(obj, True)
                            self.respawnEmplacement(key, True)

            for s in fhtd.depSpawners:
                s.depAssigned = False
        except Exception, e:
            fht.Debug("Exception in fht_reDeployables.shutOff(): " + str(e)) 
            
                        
                  
                
