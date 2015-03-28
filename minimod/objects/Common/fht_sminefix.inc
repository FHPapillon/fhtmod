rem ***** Change arming delay to prevent laying smines while running
rem ***** Make deployment longer-running
rem ***** include changed animation

ObjectTemplate.activeSafe GenericFireArm smine
ObjectTemplate.fire.fireLaunchDelay 3
ObjectTemplate.fire.fireStartDelay CRD_UNIFORM/1/1/0
ObjectTemplate.animationSystem1P objects/weapons/handheld/explosives/SMine/FHTAnimationSystem1p.inc
ObjectTemplate.activeSafe GenericFireArm smine_gb
ObjectTemplate.fire.fireLaunchDelay 3
ObjectTemplate.fire.fireStartDelay CRD_UNIFORM/1/1/0
ObjectTemplate.animationSystem1P objects/weapons/handheld/explosives/SMine/FHTAnimationSystem1p.inc
ObjectTemplate.activeSafe GenericFireArm apminem2
ObjectTemplate.fire.fireLaunchDelay 3
ObjectTemplate.fire.fireStartDelay CRD_UNIFORM/1/1/0
ObjectTemplate.animationSystem1P objects/weapons/handheld/explosives/SMine/FHTAnimationSystem1p.inc

ObjectTemplate.activeSafe GenericFireArm smine
objectTemplate.delayToUse 3.0
objectTemplate.fire.fireStartDelay 5
ObjectTemplate.fire.fireLaunchDelay 3
ObjectTemplate.activeSafe GenericFireArm apminem2
objectTemplate.delayToUse 3.0
objectTemplate.fire.fireStartDelay 5
ObjectTemplate.fire.fireLaunchDelay 3
ObjectTemplate.activeSafe GenericFireArm smine_gb
objectTemplate.delayToUse 3.0
objectTemplate.fire.fireStartDelay 5
ObjectTemplate.fire.fireLaunchDelay 3


ObjectTemplate.activeSafe GenericProjectile apminem2_Projectile
ObjectTemplate.armingDelay 0.3
ObjectTemplate.activeSafe GenericProjectile smine_Projectile
ObjectTemplate.armingDelay 0.3
ObjectTemplate.activeSafe GenericProjectile smine_gb_Projectile
ObjectTemplate.armingDelay 0.3  