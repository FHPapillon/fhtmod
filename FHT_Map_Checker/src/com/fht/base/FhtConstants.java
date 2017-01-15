package com.fht.base;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public interface FhtConstants {
	public static String gpo_name = "GamePlayObjects.con";
	public static String clientArchives = "//ClientArchives.con";
	public static String map_desc_file_path = "//info//";
	public static String serverArchives = "//ServerArchives.con";
	public static String fh2_path = "C://Program Files (x86)//EA GAMES//Battlefield 2//mods//fh2//levels//";
	public static String localization_path = "C://Program Files (x86)//EA GAMES//Battlefield 2//mods//fh2//localization//german//fht_maps_cmp.txt";
	public static String name_tag_in_desc = "<name>";
	public static String name_tag_close_in_desc = "</name>";
	public static String tmp = "//tmp.con";
	public static String init = "//init.con";
	public static String team_1 = "gameLogic.setTeamName 1";
	public static String team_2 = "gameLogic.setTeamName 2";
	public static String kit = "gameLogic.setKit";
	public static String mapdata = "//mapdata.py";
	public static String gamePlayObjects_64 = "//GameModes//gpm_cq//64//GamePlayObjects.con";
	public static String gamePlayObjects_32 = "//GameModes//gpm_cq//32//GamePlayObjects.con";
	public static String gamePlayObjects_16 = "//GameModes//gpm_cq//16//GamePlayObjects.con";	
	public static final List<String> clientArchiveLines = Collections.unmodifiableList( Arrays.asList( 
			"fileManager.mountArchive fht/fht_common_client.zip Common", 
			"fileManager.mountArchive fht/fht_menu_client.zip Menu", 
			"fileManager.mountArchive fht/fht_objects_statics_client.zip Objects", 
			"fileManager.mountArchive fht/fht_objects_statics_client_textures.zip Objects",
			"fileManager.mountArchive fht/fht_objects_vehicles_client.zip Objects", 
			"fileManager.mountArchive fht/fht_objects_vehicles_client_textures.zip Objects"));
	public static final List<String> serverArchiveLines = Collections.unmodifiableList( Arrays.asList( 
			"fileManager.mountArchive fht/fht_objects_server.zip Objects", 
			"fileManager.mountArchive fht/fht_objects_statics_server.zip Objects", 
			"fileManager.mountArchive fht/fht_objects_vehicles_server.zip Objects"));

	public static final List<String> tmpLines = Collections.unmodifiableList( Arrays.asList( 
			"run ClientArchives.con", 
			"run ServerArchives.con", 
			"run ../../objects/Common/CommonSpawners.con", 
			"run ../../objects/Common/FewerGrenades.con", 
			"run ../../objects/Common/fht_mod.con", 
			"run ../../objects/Common/NoSquadSpawn.inc"));
	
	
	public static final List<String> initLines = Collections.unmodifiableList( Arrays.asList(""));
	public static final List<String> gpoLines = Collections.unmodifiableList( Arrays.asList(""));		
	
	public static final String createControlPoint = "ObjectTemplate.create ControlPoint";
	public static final String controlPointID = "ObjectTemplate.controlPointId";
	public static final String objectControlPointID = "Object.setControlPointId";
	public static final String objectSpawner = "ObjectTemplate.create ObjectSpawner";
	public static final String objectTemplate1 = "ObjectTemplate.setObjectTemplate 1";
	public static final String objectTemplate2 = "ObjectTemplate.setObjectTemplate 2";
	public static final String objectCreate = "Object.create";
	public static final String cpRadius = "ObjectTemplate.radius ";
	public static final String cpTeam = "ObjectTemplate.team";
	public static final String cpTimeToGetControl = "ObjectTemplate.timeToGetControl";
	public static final String cpTimeToLoseControl= "ObjectTemplate.timeToLoseControl";
	public static final String cpAreaValueTeam1 = "ObjectTemplate.areaValueTeam1";
	public static final String cpAreaValueTeam2 = "ObjectTemplate.areaValueTeam2";
	public static final String cpShowOnMinimap = "ObjectTemplate.showOnMinimap";
	public static final String cpIsUnstrategicControlPoint = "ObjectTemplate.isUnstrategicControlPoint";
	public static final String cpUnableToChangeTeam = "ObjectTemplate.unableToChangeTeam";
	public static final String objectMinSpawnDelay = "ObjectTemplate.minSpawnDelay";
	public static final String objectMaxSpawnDelay = "ObjectTemplate.maxSpawnDelay";	
	public static final String objectTimeToLive = "ObjectTemplate.TimeToLive";	
	public static final String objectTeamlocked = "ObjectTemplate.teamOnVehicle";	
	public static final String objectMaxNrOfObjectSpawned = "ObjectTemplate.maxNrOfObjectSpawned";	
	public static final String numberOfTickets = "gameLogic.setDefaultNumberOfTicketsEx ";
	public static final String fh2VehicleImageLinkPrefix = "http://forgottenhope.warumdarum.de/imagesfh2/vehicles/";
	public static final String cmpVehicleImageLinkPrefix = "http://files.forgottenhonor.com/fh2/FH2_Maps/Images/";
	public static final String smallgif = "small.gif";
	public static final String bigjpg = "big.jpg";
}


