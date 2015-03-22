

include ../geoms.con
ObjectTemplate.create Kit UW_RifleAssault_FHT
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.kitType Assault
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry kitmesh_m1garand
ObjectTemplate.geometry.kit c_kit_rifleassault
ObjectTemplate.geometry.dropGeom c_drop_rifleassault
ObjectTemplate.setHasCollisionPhysics 1
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 4	

rem -------------------------------------
ObjectTemplate.addTemplate mk2pineapple
ObjectTemplate.addTemplate m1903a1
ObjectTemplate.addTemplate m1903a1bayo
ObjectTemplate.addTemplate carlisle_dressing
include ../debug.con
rem -------------------------------------

rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.ammoSound S_Resupply
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		"RIFLEMAN"
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons-FH2\kit_rifle_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons-FH2\kit_rifle.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound		S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.6

rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

