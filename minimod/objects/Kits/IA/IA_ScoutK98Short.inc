

include ../geoms.con
ObjectTemplate.create Kit IA_ScoutK98Short
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.kitType Assault
ObjectTemplate.geometry kitmesh_m91carcano_carbine_dienstglass
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry.kit c_kit_lmg
ObjectTemplate.geometry.dropGeom c_drop_lmg
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.setHasCollisionPhysics 1
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 4

rem -------------------------------------
ObjectTemplate.addTemplate m91carcanocarbine
ObjectTemplate.addTemplate dienstglas
ObjectTemplate.addTemplate m91carcanocarbinebayonet
ObjectTemplate.addTemplate smine
ObjectTemplate.addTemplate nebeleihandgranate42
ObjectTemplate.addTemplate dressing_it
include ../debug.con
rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair
ObjectTemplate.abilityHud.ammoSound S_Resupply

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 			"RICOGNITORE"
ObjectTemplate.vehicleHud.miniMapIcon			"Ingame\Kits\Icons-FH2\kit_scout_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon			"Ingame\Kits\Icons-FH2\kit_scout.tga"
ObjectTemplate.vehicleHud.spottedIcon 			"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound			S_SprintBreath
ObjectTemplate.vehicleHud.injurySound			S_Injury
ObjectTemplate.vehicleHud.vehicleType 			7

ObjectTemplate.sprintStaminaDissipationFactor 0.2

rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---
