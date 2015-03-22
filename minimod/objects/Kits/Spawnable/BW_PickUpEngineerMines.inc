
include ../geoms.con
ObjectTemplate.create Kit BW_PickUpEngineerMines
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.kitType Engineer
ObjectTemplate.aiTemplate Engineer
ObjectTemplate.geometry kitmesh_no4_markivmine
ObjectTemplate.geometry.kit c_kit_engineer
ObjectTemplate.geometry.dropGeom c_drop_engineer
ObjectTemplate.collisionMesh kit_collision
ObjectTemplate.physicsType Point
ObjectTemplate.hasCollisionPhysics 1
ObjectTemplate.hasMobilePhysics 0
ObjectTemplate.mapMaterial 0 material 76
ObjectTemplate.cullRadiusScale 4

rem -------------------------------------
ObjectTemplate.addTemplate no4_short
ObjectTemplate.addTemplate Sykes_knife
ObjectTemplate.addtemplate britsatchel
ObjectTemplate.addTemplate wrench
ObjectTemplate.addTemplate mineflag_gb
ObjectTemplate.addTemplate minedetector
ObjectTemplate.addTemplate dressing_gb
include ../debug.con
rem -------------------------------------
ObjectTemplate.createComponent Ability
ObjectTemplate.ability.hasRepairingAbility 1
ObjectTemplate.abilityRestoreRate 0.05
ObjectTemplate.abilityInVehicleRadius 0
ObjectTemplate.abilityInVehicleStrength 0.0
ObjectTemplate.abilityInVehicleMaterial 73

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
ObjectTemplate.vehicleHud.injurySound			S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.2


rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

