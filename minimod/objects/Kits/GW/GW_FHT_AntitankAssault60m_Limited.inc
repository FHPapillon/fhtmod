

include ../geoms.con
ObjectTemplate.create Kit GW_FHT_AntitankAssault60m_Limited
ObjectTemplate.saveInSeparateFile 1
ObjectTemplate.networkableInfo KitInfo
ObjectTemplate.kitType AT
ObjectTemplate.aiTemplate AT
ObjectTemplate.geometry kitmesh_panzerfaust60m
ObjectTemplate.geometry.kit c_kit_at
ObjectTemplate.geometry.dropGeom c_drop_at
ObjectTemplate.setHasCollisionPhysics 1
ObjectTemplate.dropHeadwear helmet
ObjectTemplate.cullRadiusScale 6

rem -------------------------------------
ObjectTemplate.addTemplate HJ_knife
ObjectTemplate.addTemplate WaltherP38-i3
ObjectTemplate.addTemplate panzerfaust60m
ObjectTemplate.addTemplate dressing_de
include ../debug.con
rem -------------------------------------

rem -------------------------------------

ObjectTemplate.createComponent AbilityHud
ObjectTemplate.abilityHud.ammoSound S_Resupply
ObjectTemplate.abilityHud.healingSound S_Heal
ObjectTemplate.abilityHud.repairingSound S_Repair

ObjectTemplate.createComponent VehicleHud
ObjectTemplate.vehicleHud.hudName 		"PANZERABWEHRSOLDAT (LIMITED)"
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

