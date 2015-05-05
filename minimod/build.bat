REM Create fht_common_client.zip
7z a -tzip fht_common_client.zip -r sound\* 
7z a -tzip fht_common_client.zip -r textures\*
7z a -tzip fht_common_client.zip -r terrain\*

REM Create fht_common_server.zip
7z a -tzip fht_common_server.zip -r sound\*.con

REM Create fht_menu_client.zip
robocopy.exe ".\menu" ".\fht_menu_client" /E /ZB /COPY:DAT /R:0 /W:0
ping 192.0.2.2 -n 1 -w 10000 > nul
7z a -tzip fht_menu_client.zip -r .\fht_menu_client\*
ping 192.0.2.2 -n 1 -w 10000 > nul
rmdir /s /q fht_menu_client

REM Create fht_soldiers_client.zip
robocopy.exe ".\objects\soldiers" ".\Soldiers" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.con *.tweak
7z a -tzip fht_soldiers_client.zip -r Soldiers\*
rmdir /s /q Soldiers

REM Create fht_soldiers_server.zip
robocopy.exe ".\objects\soldiers" ".\Soldiers" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.skinnedmesh *.dds
7z a -tzip fht_soldiers_server.zip -r Soldiers\*
rmdir /s /q Soldiers

REM Create fht_objects_vehicles_server.zip
robocopy.exe ".\objects\vehicles" ".\Vehicles" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.samples
7z a -tzip fht_objects_vehicles_server.zip -r Vehicles\*
rmdir /s /q Vehicles

REM Create fht_objects_vehicles_client_textures.zip
robocopy.exe ".\objects\vehicles" ".\Vehicles" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.bundledmesh *.samples
robocopy.exe ".\objects\weapons" ".\Weapons" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.bundledmesh *.samples
7z a -tzip fht_objects_vehicles_client_textures.zip -r Vehicles\*
7z a -tzip fht_objects_vehicles_client_textures.zip -r Weapons\*
rmdir /s /q Vehicles
rmdir /s /q Weapons

REM Create fht_objects_vehicles_client.zip
robocopy.exe ".\objects\vehicles" ".\Vehicles" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_vehicles_client.zip -r Vehicles\*
rmdir /s /q Vehicles

REM Create fht_objects_statics_server.zip
robocopy.exe ".\objects\StaticObjects" ".\StaticObjects" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.samples
7z a -tzip fht_objects_statics_server.zip -r StaticObjects\*
rmdir /s /q StaticObjects

REM Create fht_objects_statics_client_textures.zip
robocopy.exe ".\objects\StaticObjects" ".\StaticObjects" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.samples *.bundledmesh
robocopy.exe ".\objects\Common" ".\Common" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.samples *.bundledmesh
7z a -tzip fht_objects_statics_client_textures.zip -r StaticObjects\*
7z a -tzip fht_objects_statics_client_textures.zip -r Common\*
rmdir /s /q StaticObjects
rmdir /s /q Common

REM Create fht_objects_statics_client.zip
robocopy.exe ".\objects\StaticObjects" ".\StaticObjects" /E /ZB /COPY:DAT /R:0 /W:0 /xf  *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_statics_client.zip -r StaticObjects\*
rmdir /s /q StaticObjects

REM Create fht_objects_server.zip
robocopy.exe ".\objects\Common" ".\Common" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples

ping 192.0.2.2 -n 1 -w 10000 > nul
7z a -tzip fht_objects_server.zip -r Common\*
ping 192.0.2.2 -n 1 -w 10000 > nul
rmdir /s /q Common
ping 192.0.2.2 -n 1 -w 10000 > nul
robocopy.exe ".\objects\Kits" ".\Kits" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples
7z a -tzip fht_objects_server.zip -r Kits\*
rmdir /s /q Kits
robocopy.exe ".\objects\Weapons" ".\Weapons" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples
7z a -tzip fht_objects_server.zip -r Weapons\*
rmdir /s /q Weapons
robocopy.exe ".\objects\Roads" ".\Roads" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples *.dat
7z a -tzip fht_objects_server.zip -r Roads\*
rmdir /s /q Roads
robocopy.exe ".\objects\vegitation" ".\vegitation" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples
7z a -tzip fht_objects_server.zip -r vegitation\*
rmdir /s /q vegitation

REM Create fht_objects_client.zip
robocopy.exe ".\objects\Common" ".\Common" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_client.zip -r Common\*
rmdir /s /q Common
robocopy.exe ".\objects\Kits" ".\Kits" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_client.zip -r Kits\*
rmdir /s /q Kits
robocopy.exe ".\objects\Weapons" ".\Weapons" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_client.zip -r Weapons\*
rmdir /s /q Weapons
robocopy.exe ".\objects\Roads" ".\Roads" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_client.zip -r Roads\*
rmdir /s /q Roads
robocopy.exe ".\objects\vegitation" ".\vegitation" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_client.zip -r vegitation\*
rmdir /s /q vegitation

ping 192.0.2.2 -n 1 -w 60000 > nul

