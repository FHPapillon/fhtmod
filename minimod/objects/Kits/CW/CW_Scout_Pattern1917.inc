

include ../geoms.con
ObjectTemplate.create Kit CW_Scout_Pattern1917
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.kitType Assault
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry kitmesh_no4_binoculars
ObjectTemplate.geometry.kit c_kit_scout
ObjectTemplate.geometry.dropGeom c_drop_scout
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.setHasCollisionPhysics 1
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 4

rem -------------------------------------
ObjectTemplate.addTemplate m1917enfield
ObjectTemplate.addTemplate no2_binocs
ObjectTemplate.addTemplate Sykes_knife
ObjectTemplate.addTemplate smine_gb
ObjectTemplate.addTemplate no77smoke
ObjectTemplate.addTemplate dressing_gb
include ../debug.con
rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair
ObjectTemplate.abilityHud.ammoSound S_Resupply

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 			"RECON"
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
