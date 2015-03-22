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
# fht_settings.py -- Set constants for fht plugins
from game.stats.constants import *

startDelay = 1.0
debugging = False

doRallies = True
doRedeployables = True
doMainBaseCheck = True
doShuffle = True

#-------------------------------
#    fht_deploySpawnPoint.py
#-------------------------------
maxDistanceToSquadMember = 10
minSquadPsNear = 2
rallyRegisterDelay = 0.1
rallyDeployPosition = (0.0, -1.0, 0.0)	        # SP position relative to SL position (to fix floating SP objects)
rallyTemplatePrefix = "fht_radio_rp"            # name of the deployable spawn point object template for team 0 (dummy, not used), 1 and 2 respectively
rallySpawnSuffix = "_SpawnPoint"                # note that the object template(s) must be already defined in .con files and known to the map
rallyRadius = 10.0
waitTimeRally = 120.0
waitTimeRallySL = 240.0
minDisTeamSP = 20.0
minDisFlag = 10.0
rallyTTL = 600.0
rallyTTLSL = 120.0
fixRallyAfter = 3
testRallyDisable = False

#-------------------------------
#    fht_admin.py
#-------------------------------

campaign = 16
scoreMod = 100
scoreModifiers = {
        1: 1.0, 2: 1.0, 3: 1.0, 4: 1.1, 5: 1.1, 6: 1.1, 7: 1.2, 8: 1.2, 9: 1.2, 10: 1.5, 11: 1.5, 12: 2.0, 13: 2.0
        }
mapCenter = (0.0, 0.0, 0.0)

fht_adminHashes = {		            # 0: Superuser, 1: Admin, 2: HQ, 3: CO
	"31b339ad9b2c21da0006f2f06153319c":		0,							# Pappilon
        "1e9c1159bbaf428726ff595b83e7f156":             0,                                                      # Harmonikater        
	"39fb681b6ea6792958b1eb19cb6a5a93":		0,							# Gunhead
	"8621c6338942ef8cf287f096acec670c":		1,							# [FH] Viktor2a5
	"e36365a13d5a6d2a20a8dfaa2ef46667":		1,							# Deek
	"c8f89719181af36144d5cffe5fe1bb8f":		1,							# Quicksilver


	"844ccf50139aca36914c608f46d7337f":		2,							# Erwin
        "eead04a074f3eb1f440e3668f9b7eed3":             2,                                                      # Wualy
        "0fc5efdd137b4bd97409f798b095f0c5":             3,                                                      # Beyers
        "74bccd98d4892acfaa28ec43aa6a9d3c":             3,                                                      # Malleus
        "9c04c1f9b631cb0e3f38e28b39ca0d89":             3,                                                      # Surfbird
        "ec5959288c81f78ce837867694664c49":             3,                                                      # theUgg     

        "22a94fc25377056c2ea8c628c2dc06d3":             2,                                                      # Oberst_S
        "18b5d9bf7f8a17bfc1747cede9e88ece":             3,                                                      # Odium
        "3c7f908b662c4b4768cc71ebc9f35288":             3,                                                      # Sandre
        "e879c5882eda922429fb9d17afacfbd9":             3,                                                      # Tutvys
        "63b63324851c0fbe6d86dc532f6b86a1":             3,                                                      # Hawk2k9      
}

fht_commandSymbol = "!"

droneTemplate = 'fht_drone'
roundsPlayed = 0
RVP = 100.0
TVP = 50.0           
isDedicated = True
scoreFileName = "mods/fh2/fht/fhtScores.log"
loggingFileName = "battle_scores.txt"
persistentFileName = "all_scores.txt"


fht_adminPowerLevels = {	    # Rights management. The lower the powerlevel, the more power one has. 
				    # 0: Superuser, 1: Admin, 2: HQ, 3: CO, 777: Open


	# Text messages
	"help":			777,								# Show help about custom commands.												
	"location":		0,								# Show current location in map coordinates.
        "perimeter":            1,                                                              # Shows which players are currently inside enemy main base perimeter.

	# Battle Control
##	"clear":	    	1,								# Clear Round Scores at start of battle.
        "scoremod":  		1,								# Read out/Adjust Scoring modifier for this battle.
        "setlive":  		1,								# Count this round in scores and send messages.
        "kick":                 2,                                                              # Kick Player from Server (0 - all players, 1 - players on team)
        "k":                    3,                                                              #   --""--
        "rank":                 2,                                                              # Give (temporary) Power levels to a player.
        "cpchange":             1,                                                              # Change owner of a flag.
        "setbleed":             0,                                                              # Change bleed rate of a team.
        "kitlimit":             0,                                                              # Add/Change kitlimit of a slot.

        # Server control
        "rcon":                 0,                                                              # Send rcon commands through chat.
        "setvalue":             0,                                                              # Change a value in fht_settings ingame.
        "getvalue":             0,                                                              # Get a value in fht_settings ingame.
        "md5check":             0,                                                              # Enable/Disable md5 checks.
        "md5time":              0,                                                              # Set Interval between each md5 check.

	# Drone Commands
	"drone":		1,				                                # Create Admin Drone		    
	"exit":			1,								# Turn off safe exit for current drone use.
        "teleport":		1,				                                # Move Drone to player/grid square.
        "tele":		        1,				                                #   --""--

        # HQ Commands
        "mainbase":             2,                                                              # Choose a mainbase if Mainbase Selection is supported.
        "adminpm":              2,                                                              # Send a Message to all admins.

        # Plugins
        "import":               0,                                                              # Re-import settings for specified or all FHT plugins.
        "plugin":               0,                                                              # Enable specified FHT plugin.
        "mbchange":             1,                                                              # In-/Decrease Size of a MainBase
        "fhtdebugme":           1,                                                              # Turn on personal fht debug messages.
        "fhtdebug":             1,                                                              # Turn on global fht debug messages.
        "shuffle":              0,                                                              # Shuffle Flags
    
	# Open commands									        # Please note that 777 is a fixed value for "open" commands! This means everybody on the server can use them
        "live":  		777,								# Shows whether the round is live.												        
	"score":		777,								# Shows the battlescore.
##	"standings":		777,								# Shows the campaign score.
        "rp":                   777,                                                            # Deploys Squad Rally Point.
        "rally":                777,                                                            #   --""--
        "rallypoint":           777,                                                            #   --""--
        "rr":                   0,                                                            # Resets the rally point, to fix spawnpoint disappearing
        "resetrally":           0,                                                            #   --""--
}       


#-------------------------------
#    fht_mainBaseKillCheck.py
#-------------------------------

notMainBase = []
forceMainBase = zip([],[])



perimeterTriggerTime = 120.0
mainBaseBuffer = 50.0
warnLength = 5.0
maxMainbaseSize = 150.0
allowedVehicleTypes = [ VEHICLE_TYPE_TRANSPORT, VEHICLE_TYPE_BICYCLE, VEHICLE_TYPE_PARACHUTE ]
allowedWeaponTypes = [ WEAPON_TYPE_MINEFLAG, WEAPON_TYPE_TARGETING, WEAPON_TYPE_MINEDET, WEAPON_TYPE_GOLD, WEAPON_TYPE_SMOKE, WEAPON_TYPE_EXPLOSIVE, WEAPON_TYPE_CLOSE, WEAPON_TYPE_NONLETHAL ]
monitorVehicleTypes = [ VEHICLE_TYPE_HEAVYARMOR, VEHICLE_TYPE_MEDIUMARMOR, VEHICLE_TYPE_LIGHTARMOR, VEHICLE_TYPE_AIR, VEHICLE_TYPE_APC, VEHICLE_TYPE_ARMOREDCAR ]
mainBaseVehicleTypes = [ VEHICLE_TYPE_ANTIAIR, VEHICLE_TYPE_RADIO, VEHICLE_TYPE_ARTILLERY, VEHICLE_TYPE_ATGUN, VEHICLE_TYPE_MACHINEGUN ]
allowedAttackVehicleTypes = [ VEHICLE_TYPE_AIR ]

# Custom Exceptions
customWeapons = []
customVehicle = [ 'fht_drone' ]
customMonitorVehicles = []
customMainBaseVehicles = [ 'fht_drone' ]
customAllowedAttackVehicles = [ 'fht_drone' ]
wrenches = [ 'wrench', 'wrench-i5' ]
artyUnsafeRadius = 15.0
mBCKRepeatDelay = 3.0
mBCKCorrFactor = 1.05
 

#-------------------------------
#    fht_redeploybles.py
#-------------------------------
requestObject = 'fht_deploy_marker'
packRadius = 3.0
wreckTTL = 30.0
depRegisterDelay = 0.1
packWeapon = 'wrench_pack'
depRPS = 0.5
depCorrFactor = 0.8
respawnAttemptInterval = 5.0
crateHeight = 0.05
depMaxAttempts = 3

emplacementInfo = {
    'light_at': dict(radius = 1000.0, respawn = 60.0, delay = 10.0),
    'medium_at': dict(radius = 1000.0, respawn = 90.0, delay = 4.0), 
    'heavy_at': dict(radius = 1000.0, respawn = 120.0, delay = 20.0),
    'artillery': dict(radius = 1000.0, respawn = 90.0, delay = 20.0, flatten = True),
    'aa_gun': dict(radius = 1000.0, respawn = 60.0, delay = 10.0)}

emplacements = {
    'flak18': dict(kit = 'flak18_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'flak18_fr': dict(kit = 'flak18_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'flak18_pg': dict(kit = 'flak18_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'flak18ns': dict(kit = 'flak18ns_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'flak18ns_fr': dict(kit = 'flak18ns_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'flak18ns_fr_two': dict(kit = 'flak18ns_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'flak18ns_pg': dict(kit = 'flak18ns_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'flak37': dict(kit = 'flak37_deployer_kit', type = 'aa_gun', offset = 0.15862),
    'flak38': dict(kit = 'flak38_deployer_kit', type = 'aa_gun', offset = 0.15862),
    'flak38_france': dict(kit = 'flak38_deployer_kit', type = 'aa_gun', offset = 0.15862),
    'flak38_pan': dict(kit = 'flak38_deployer_kit', type = 'aa_gun', offset = 0.15862),
    'flak38_win': dict(kit = 'flak38_deployer_kit', type = 'aa_gun', offset = 0.15862),
    'flak43': dict(kit = 'flak43_deployer_kit', type = 'aa_gun', offset = 0.15862),
    'flakvierling_ard': dict(kit = 'flakvierling_deployer_kit', type = 'aa_gun', offset = 0.0),
    'flakvierling_win': dict(kit = 'flakvierling_deployer_kit', type = 'aa_gun', offset = 0.0),
    'flakvierling38': dict(kit = 'flakvierling_deployer_kit', type = 'aa_gun', offset = 0.0),
    'flakvierling38_pan': dict(kit = 'flakvierling_deployer_kit', type = 'aa_gun', offset = 0.0),
    'flakvierling38_france': dict(kit = 'flakvierling_deployer_kit', type = 'aa_gun', offset = 0.0),
    'lefh18': dict(kit = 'lefh18_deployer_kit', type = 'artillery', offset = 0.32984),
    'lefh18_fht': dict(kit = 'lefh18_deployer_kit', type = 'artillery', offset = 0.32984),
    'lefh18_france': dict(kit = 'lefh18_deployer_kit', type = 'artillery', offset = 0.32984),
    'nebelwerfer': dict(kit = 'nebelwerfer_deployer_kit', type = 'artillery', offset = 0.45105),
    'nebelwerfer_ard': dict(kit = 'nebelwerfer_deployer_kit', type = 'artillery', offset = 0.45105),
    'nebelwerfer_pan': dict(kit = 'nebelwerfer_deployer_kit', type = 'artillery', offset = 0.45105),
    'nebelwerfer_win': dict(kit = 'nebelwerfer_deployer_kit', type = 'artillery', offset = 0.45105),
    'pak35_static': dict(kit = 'pak35_deployer_kit', type = 'light_at', offset = 0.28022),
    'pak35_europe_static': dict(kit = 'pak35_deployer_kit', type = 'light_at', offset = 0.28022),
    'pak35_greece_static': dict(kit = 'pak35_deployer_kit', type = 'light_at', offset = 0.28022),
    'pak35_static_pzg40': dict(kit = 'pak35_deployer_kit', type = 'light_at', offset = 0.28022),
    'pak38_static': dict(kit = 'pak38_deployer_kit', type = 'medium_at', offset = 0.46081),
    'pak38_static_fr': dict(kit = 'pak38_deployer_kit', type = 'medium_at', offset = 0.46081),
    'pak38_static_pg': dict(kit = 'pak38_deployer_kit', type = 'medium_at', offset = 0.46081),
    'pak40_static': dict(kit = 'pak40_deployer_kit', type = 'medium_at', offset = 0.55926),
    'pak40_static_ard': dict(kit = 'pak40_deployer_kit', type = 'medium_at', offset = 0.55926),
    'pak40_static_win': dict(kit = 'pak40_deployer_kit', type = 'medium_at', offset = 0.55926),
    'pak40_static_wp': dict(kit = 'pak40_deployer_kit', type = 'medium_at', offset = 0.55926),
    'pak40_static_ws': dict(kit = 'pak40_deployer_kit', type = 'medium_at', offset = 0.55926),
    'sig33': dict(kit = 'sig33_deployer_kit', type = 'artillery', offset = 0.0),
    'wurfgerat41': dict(kit = 'wurfgerat_deployer_kit', type = 'artillery', offset = 0.0),
    'wurfgerat41_alt': dict(kit = 'wurfgerat_deployer_kit', type = 'artillery', offset = 0.0),
    '2pdr': dict(kit = '2pdr_deployer_kit', type = 'light_at', offset = 0.05989),
    '25pdr': dict(kit = '25pdr_deployer_kit', type = 'artillery', offset = 0.45446),
    '25pdr_mkiv': dict(kit = '25pdr_mkiv_deployer_kit', type = 'artillery', offset = 0.45446),
    '6pdr_mkiv_static': dict(kit = '6pdr_mkiv_deployer_kit', type = 'medium_at', offset = 0.35379),
    '6pdr_static': dict(kit = '6pdr_deployer_kit', type = 'medium_at', offset = 0.35379),
    'bofors40mm': dict(kit = 'bofors_deployer_kit', type = 'aa_gun', offset = 0.39018),
    'bofors40mm_eu': dict(kit = 'bofors_deployer_kit', type = 'aa_gun', offset = 0.39018),
    'breda_35_20mm': dict(kit = 'breda35_deployer_kit', type = 'aa_gun', offset = 0.20093),
    'cannone_da_47_32_static': dict(kit = 'cannone47_deployer_kit', type = 'light_at', offset = 0.27944),
    'schneider_1913': dict(kit = 'schneider_1913_deployer_kit', type = 'artillery', offset = 0.0),
    '37mm_m3_static': dict(kit = '37mm_deployer_kit', type = 'light_at', offset = 0.68505),
    '57mm_m1_atgun_static': dict(kit = '57mm_deployer_kit', type = 'medium_at', offset = 0.35731),
    '57mm_m1_atgun_win_static': dict(kit = '57mm_deployer_kit', type = 'medium_at', offset = 0.35731),
    '76mm_m5_atgun_static': dict(kit = '76mm_deployer_kit', type = 'medium_at', offset = 0.50392),
    '76mm_m5_atgun_static_win': dict(kit = '76mm_deployer_kit', type = 'medium_at', offset = 0.50392),
    '90mm_aa_at_m1': dict(kit = '90mm_deployer_kit', type = 'heavy_at', offset = 0.13377),
    '90mm_aa_at_m2': dict(kit = '90mm_deployer_kit', type = 'heavy_at', offset = 0.13377),
    'm2a1_howitzer_105mm': dict(kit = 'm2a1_deployer_kit', type = 'artillery', offset = 0.50630),
    'm2a1_howitzer_105mm_win': dict(kit = 'm2a1_deployer_kit', type = 'artillery', offset = 0.50630),
    'm33': dict(kit = 'm33_deployer_kit', type = 'aa_gun', offset = 0.10989),
    'm51': dict(kit = 'm51_deployer_kit', type = 'aa_gun', offset = 0.21151),
    'm51_win': dict(kit = 'm51_deployer_kit', type = 'aa_gun', offset = 0.21151)}

	#-------------------------------
#    fht_machineGuns.py
#-------------------------------

# bar18a2_slow -> convert
# boys -> maybe convert
# breda30 -> convert
# brenmk1 -> convert
# fg42_deployed -> convert
# fg42_zf_deployed -> convert
# lewishandheld -> test (lewis_bipod)
# m1919a6 -> should work fine, just rename some
# mg34bipod -> test (mg34_bipod)
# mg42bipod -> fix crashes (mg42_bipod)
# pzb39 -> maybe convert
# zb26_deployed -> convert


depMachineGuns = {
    
    'gw_lmg_mg42_limited': 'mg42_bipod',
    'gs_lmg_mg42_limited': 'mg42_bipod',
    'ga_pickupsupportmg42': 'mg42_bipod',
    'gw_pickupsupportmg42': 'mg42_bipod',
    'uw_pickupsupportm1919a6': 'm1919a6_emplaced',
    'uw_lmg_m1919a6_limited': 'm1919a6_emplaced'
    }

depMGWeapon = 'carlisle_dressing'
depMGProjectile = 'carlisle_dressing_projectile'
depMGDelay = 2.0
testDone = False