

include ../geoms.con
ObjectTemplate.create Kit UW_NCO_fht_rifle
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.kitType Assault
ObjectTemplate.aiTemplate Assault
ObjectTemplate.geometry UW_kits
ObjectTemplate.geometry.kit c_kit_nco
ObjectTemplate.geometry.dropGeom c_drop_nco
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.setHasCollisionPhysics 1
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 6
rem -------------------------------------
ObjectTemplate.addTemplate m1garand
ObjectTemplate.addTemplate AN_M8_SmokeGrenade
ObjectTemplate.addTemplate colt1911
ObjectTemplate.addTemplate m3binoculars
ObjectTemplate.addTemplate m3_knife
ObjectTemplate.addTemplate carlisle_dressing-nco
include ../debug.con
rem -------------------------------------

rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair
ObjectTemplate.abilityHud.ammoSound S_Resupply

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		"NCO"
ObjectTemplate.vehicleHud.miniMapIcon		"Ingame\Kits\Icons-FH2\kit_NCO_outline.tga"
ObjectTemplate.vehicleHud.vehicleIcon		"Ingame\Kits\Icons-FH2\kit_NCO.tga"
ObjectTemplate.vehicleHud.spottedIcon 		"Ingame\Player\Icons\Minimap\mini_Soldier.dds"
ObjectTemplate.vehicleHud.pantingSound		S_SprintBreath
ObjectTemplate.vehicleHud.injurySound		S_Injury
ObjectTemplate.vehicleHud.vehicleType 		7

ObjectTemplate.sprintStaminaDissipationFactor 0.6


rem ---BeginComp:Radio ---
ObjectTemplate.createComponent Radio
ObjectTemplate.Radio.spottedMessage	"infantry_spotted"
rem ---EndComp ---

