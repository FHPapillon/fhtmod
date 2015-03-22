

include ../geoms.con
ObjectTemplate.create Kit BW_RifleAssaultPara
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.kitType Assault
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry bw_kits
ObjectTemplate.geometry.kit c_kit_airman
ObjectTemplate.geometry.dropGeom c_drop_pilot
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.setHasCollisionPhysics 1
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 6
rem -------------------------------------
ObjectTemplate.addTemplate BritishParachuteLauncher
ObjectTemplate.addTemplate webleymk6-i3
ObjectTemplate.addTemplate no4
ObjectTemplate.addTemplate Sykes_knife
ObjectTemplate.addTemplate no77smoke
ObjectTemplate.addTemplate dressing_gb
include ../debug.con
rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair
ObjectTemplate.abilityHud.ammoSound S_Resupply

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		RIFLEMAN
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons-FH2\kit_para_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons-FH2\kit_para.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound			S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.6


rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

