
include ../geoms.con
ObjectTemplate.create Kit BA_PickUpAntitankBoysCommando
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.kitType Assault
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry kitmesh_boys
ObjectTemplate.geometry.kit c_kit_at
ObjectTemplate.geometry.dropGeom c_drop_at
ObjectTemplate.collisionMesh kit_collision
ObjectTemplate.physicsType Point
ObjectTemplate.hasCollisionPhysics 1
ObjectTemplate.hasMobilePhysics 0
ObjectTemplate.mapMaterial 0 material 76
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 6

rem -------------------------------------
ObjectTemplate.addTemplate boys
ObjectTemplate.addTemplate No69Grenade
ObjectTemplate.addTemplate webleymk6
ObjectTemplate.addTemplate Sykes_knife
ObjectTemplate.addTemplate dressing_gb
include ../debug.con
rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.ammoSound S_Resupply
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		"HUD_TEXT_MENU_SPAWN_KIT_ASSAULT"
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons-FH2\kit_atrifle_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons-FH2\kit_atrifle.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound			S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.6

rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

