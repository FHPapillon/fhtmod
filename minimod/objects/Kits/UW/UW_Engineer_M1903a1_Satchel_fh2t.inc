

include ../geoms.con
ObjectTemplate.create Kit UW_Engineer_M1903a1_Satchel_fh2t
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.kitType Engineer
ObjectTemplate.aiTemplate Engineer
ObjectTemplate.geometry kitmesh_m1903a1_compob
ObjectTemplate.geometry.kit c_kit_engineer
ObjectTemplate.geometry.dropGeom c_drop_engineer
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.setHasCollisionPhysics 1
ObjectTemplate.cullRadiusScale 6

rem -------------------------------------
ObjectTemplate.addTemplate M1903a1
ObjectTemplate.addTemplate m3_knife
ObjectTemplate.addTemplate britsatchel
ObjectTemplate.addTemplate wrench
ObjectTemplate.addTemplate carlisle_dressing
include ../debug.con
rem -------------------------------------
ObjectTemplate.createComponent Ability
ObjectTemplate.ability.hasRepairingAbility 1
ObjectTemplate.abilityRestoreRate 0.05
ObjectTemplate.abilityInVehicleRadius 0
ObjectTemplate.abilityInVehicleStrength 0.0
ObjectTemplate.abilityInVehicleMaterial 73

rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair
ObjectTemplate.abilityHud.ammoSound S_Resupply

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		"ENGINEER"
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons\kit_Engineer_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons\kit_Engineer.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound		S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.2


rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

