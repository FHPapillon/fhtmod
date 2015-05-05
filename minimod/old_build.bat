REM Create fht_common_client.zip
7z a -tzip fht_common_client.zip -r sound\*
7z a -tzip fht_common_client.zip -r textures\*

REM Create fht_menu_client.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\menu" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\fht_menu_client" /E /ZB /COPY:DAT /R:0 /W:0
7z a -tzip fht_menu_client.zip -r .\fht_menu_client\*
rmdir /s /q fht_menu_client

REM Create fht_client_soldiers.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\soldiers" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Soldiers" /E /ZB /COPY:DAT /R:0 /W:0
7z a -tzip fht_client_soldiers.zip -r Soldiers\*
rmdir /s /q Soldiers

REM Create fht_objects_vehicles_server.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\vehicles" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Vehicles" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.samples
7z a -tzip fht_objects_vehicles_server.zip -r Vehicles\*
rmdir /s /q Vehicles

REM Create fht_objects_vehicles_client_textures.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\vehicles" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Vehicles" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.bundledmesh *.samples
7z a -tzip fht_objects_vehicles_client_textures.zip -r Vehicles\*
rmdir /s /q Vehicles

REM Create fht_objects_vehicles_client.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\vehicles" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Vehicles" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_vehicles_client.zip -r Vehicles\*
rmdir /s /q Vehicles

REM Create fht_objects_statics_server.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\StaticObjects" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\StaticObjects" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.samples
7z a -tzip fht_objects_statics_server.zip -r StaticObjects\*
rmdir /s /q StaticObjects

REM Create fht_objects_statics_client_textures.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\StaticObjects" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\StaticObjects" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.samples *.bundledmesh
7z a -tzip fht_objects_statics_client_textures.zip -r StaticObjects\*
rmdir /s /q StaticObjects

REM Create fht_objects_statics_client.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\StaticObjects" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\StaticObjects" /E /ZB /COPY:DAT /R:0 /W:0 /xf  *.inc *.ai *.collisionmesh *.con *.tweak *.dds *.samples
7z a -tzip fht_objects_statics_client.zip -r StaticObjects\*
rmdir /s /q StaticObjects

REM Create fht_objects_server.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\Common" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Common" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples
7z a -tzip fht_objects_server.zip -r Common\*
rmdir /s /q Common
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\Kits" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Kits" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples
7z a -tzip fht_objects_server.zip -r Kits\*
rmdir /s /q Kits
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\Weapons" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Weapons" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.dds *.bundledmesh *.wav *.samples
7z a -tzip fht_objects_server.zip -r Weapons\*
rmdir /s /q Weapons

REM Create fht_objects_client.zip
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\Common" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Common" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.samples
7z a -tzip fht_objects_client.zip -r Common\*
rmdir /s /q Common
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\Kits" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Kits" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.samples
7z a -tzip fht_objects_client.zip -r Kits\*
rmdir /s /q Kits
robocopy.exe "C:\Users\Timo\Documents\FHT\fhtmod\minimod\objects\Weapons" "C:\Users\Timo\Documents\FHT\fhtmod\minimod\Weapons" /E /ZB /COPY:DAT /R:0 /W:0 /xf *.staticmesh *.inc *.ai *.collisionmesh *.con *.tweak *.samples
7z a -tzip fht_objects_client.zip -r Weapons\*
rmdir /s /q Weapons

ping 192.0.2.2 -n 1 -w 60000 > nul

