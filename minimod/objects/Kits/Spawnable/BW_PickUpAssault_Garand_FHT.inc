
include ../geoms.con
ObjectTemplate.create Kit BW_PickUpAssault_Garand_FHT
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.kitType Assault
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry kitmesh_thompsonm1a1
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
ObjectTemplate.addTemplate no4grenade
ObjectTemplate.addTemplate millsbomb-3
ObjectTemplate.addTemplate m1garand
ObjectTemplate.addTemplate m1garandbayonet
ObjectTemplate.addTemplate dressing_gb
include ../debug.con
rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.ammoSound S_Resupply
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		"HUD_TEXT_MENU_SPAWN_KIT_ASSAULT"
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons-FH2\kit_SMG_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons-FH2\kit_SMG.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound			S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.6

rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

