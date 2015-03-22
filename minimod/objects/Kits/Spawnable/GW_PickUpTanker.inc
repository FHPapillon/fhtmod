
include ../geoms.con
ObjectTemplate.create Kit GW_PickUpTanker
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.kitType Assault
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry kitmesh_mp34
ObjectTemplate.geometry.kit c_kit_smgassault	
ObjectTemplate.geometry.dropGeom c_drop_smgassault
ObjectTemplate.collisionMesh kit_collision
ObjectTemplate.physicsType Point
ObjectTemplate.hasCollisionPhysics 1
ObjectTemplate.hasMobilePhysics 0
ObjectTemplate.mapMaterial 0 material 76
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 4

rem -------------------------------------
ObjectTemplate.addTemplate heer_knife
ObjectTemplate.addTemplate mp34
ObjectTemplate.addTemplate wrench
ObjectTemplate.addTemplate Dienstglas-i5
ObjectTemplate.addTemplate dressing_de
include ../debug.con
rem -------------------------------------
ObjectTemplate.createComponent Ability
ObjectTemplate.ability.hasRepairingAbility 1
ObjectTemplate.abilityRestoreRate 0.05
ObjectTemplate.abilityInVehicleRadius 0
ObjectTemplate.abilityInVehicleStrength 0.0
ObjectTemplate.abilityInVehicleMaterial 73

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.ammoSound S_Resupply
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		"HUD_TEXT_MENU_SPAWN_KIT_ASSAULT"
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons\kit_Engineer_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons\kit_Engineer.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"

ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound		S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.6

rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

