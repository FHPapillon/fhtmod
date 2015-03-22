
include ../geoms.con
ObjectTemplate.create Kit UW_PickUpTanker
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.kitType Engineer
ObjectTemplate.aiTemplate Engineer
ObjectTemplate.geometry kitmesh_m3greasegun
ObjectTemplate.geometry.kit c_kit_tanker
ObjectTemplate.geometry.dropGeom 0
ObjectTemplate.collisionMesh kit_collision
ObjectTemplate.physicsType Point
ObjectTemplate.hasCollisionPhysics 1
ObjectTemplate.hasMobilePhysics 0
ObjectTemplate.mapMaterial 0 material 76
ObjectTemplate.cullRadiusScale 4

rem -------------------------------------
ObjectTemplate.addTemplate m3binoculars
ObjectTemplate.addTemplate m3greasegun
ObjectTemplate.addTemplate m3_knife
ObjectTemplate.addTemplate wrench-i5
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
ObjectTemplate.vehicleHud.hudName 		"TANK CREW"
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons\kit_engineer_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons\kit_engineer.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound			S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.2


rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

