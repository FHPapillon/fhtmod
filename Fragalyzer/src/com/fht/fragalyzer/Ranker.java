package com.fht.fragalyzer;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import com.fht.fragalyzer.types.EventType;
import com.fht.fragalyzer.types.KillType;
import com.fht.fragalyzer.types.KitType;
import com.fht.fragalyzer.types.PlayerStats;
import com.fht.fragalyzer.types.StatScope;
import com.fht.fragalyzer.types.VehicleType;
import com.fht.fragalyzer.types.WeaponType;
import com.hp.gagawa.java.elements.A;
import com.hp.gagawa.java.elements.Body;
import com.hp.gagawa.java.elements.Div;
import com.hp.gagawa.java.elements.H1;
import com.hp.gagawa.java.elements.H2;
import com.hp.gagawa.java.elements.H4;
import com.hp.gagawa.java.elements.Head;
import com.hp.gagawa.java.elements.Html;
import com.hp.gagawa.java.elements.Img;
import com.hp.gagawa.java.elements.Table;
import com.hp.gagawa.java.elements.Td;
import com.hp.gagawa.java.elements.Text;
import com.hp.gagawa.java.elements.Title;
import com.hp.gagawa.java.elements.Tr;

public class Ranker {

	private String basePath;
	private StatScope scope;
	private String scopeName;
	private Html report;
	private int td_counter;
	private Tr tr;
	private Table table;

	private HashMap<String, Integer> killRanking;
	private HashMap<String, Integer> deathsRanking;
	private HashMap<String, Integer> tkRanking;
	private HashMap<String, Double> kdrRanking;

	private HashMap<String, Integer> cpCapRanking;

	private HashMap<String, Integer> cpCapAassistRanking;

	private HashMap<String, Integer> cpDefendRanking;

	private HashMap<String, Integer> cpNeutralizeRanking;

	private HashMap<String, Integer> cpNeutralizeAssistRanking;

	private HashMap<VehicleType, HashMap<String, Integer>> vehicleTypeRanking;
	private HashMap<WeaponType, HashMap<String, Integer>> weaponTypeRanking;
	private HashMap<String, HashMap<KitType, Integer>> weaponRanking;

	public Ranker(String basePath) {
		super();
		this.setBasePath(basePath);
		setKillRanking(new HashMap<>());
		setDeathsRanking(new HashMap<>());
		setTkRanking(new HashMap<>());
		setCpCapRanking(new HashMap<>());
		setCpCapAassistRanking(new HashMap<>());
		setCpDefendRanking(new HashMap<>());
		setCpNeutralizeAssistRanking(new HashMap<>());
		setCpNeutralizeRanking(new HashMap<>());
		setVehicleTypeRanking(new HashMap<>());
		setWeaponTypeRanking(new HashMap<>());
		setWeaponRanking(new HashMap<>());
		setReport(new Html());
		Head head = new Head();
		getReport().appendChild(head);
		setTd_counter(0);
		tr = new Tr();
		table = new Table();
	}

	/*
	 * Per player, count his CP actions
	 */
	private PlayerStats countCPStuff(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();

		LogEntry logEntry;
		int cpCaptures = 0;
		int cpCaptureAssists = 0;
		int cpDefends = 0;
		int cpNeutralizes = 0;
		int cpNeutralizeAssists = 0;

		while (it.hasNext()) {
			logEntry = it.next();
			if (logEntry.getEventType().equals(EventType.SCORE)) {
				switch (logEntry.getCpEvent()) {
				case cpCaptures:
					cpCaptures++;
					break;
				case cpAssists:
					cpCaptureAssists++;
					break;
				case cpDefends:
					cpDefends++;
					break;
				case cpNeutralizes:
					cpNeutralizes++;
					break;
				case cpNeutralizeAssists:
					cpNeutralizeAssists++;
					break;
				default:
					break;
				}
			}

		}

		stats.setFlagCaps(cpCaptures);
		stats.setFlagCapAssists(cpCaptureAssists);
		stats.setFlagDefends(cpDefends);
		stats.setFlagNeutralizeAssist(cpNeutralizeAssists);
		stats.setFlagNeutralizes(cpNeutralizes);
		getCpCapRanking().put(stats.getPlayerName(), new Integer(stats.getFlagCaps()));
		getCpCapAassistRanking().put(stats.getPlayerName(), new Integer(stats.getFlagCapAssists()));
		getCpDefendRanking().put(stats.getPlayerName(), new Integer(stats.getFlagDefends()));
		getCpNeutralizeRanking().put(stats.getPlayerName(), new Integer(stats.getFlagNeutralizes()));
		getCpNeutralizeAssistRanking().put(stats.getPlayerName(), new Integer(stats.getFlagNeutralizeAssist()));

		// System.out.println("Player " + cpCaptures + " " + cpCaptureAssists +
		// " " + cpNeutralizeAssists + " " +cpNeutralizes + " " + cpDefends + "
		// " + stats.getPlayerName());

		return stats;
	}

	/*
	 * Per player, count how often he was killed
	 */
	private PlayerStats countDeaths(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();

		LogEntry logEntry;
		int deaths = 0;

		while (it.hasNext()) {
			logEntry = it.next();
			if (logEntry.getEventType().equals(EventType.KILL) && !logEntry.getKillType().equals(KillType.SUICIDE)
					&& logEntry.getVictim().equals(stats.getPlayerName())) {
				deaths++;
			}

		}

		stats.setDeaths(deaths);
		getDeathsRanking().put(stats.getPlayerName(), new Integer(stats.getDeaths()));

		return stats;
	}

	/*
	 * Per player, count the kills with a special WeaponType
	 */
	private PlayerStats countEnemies(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();
		HashMap<String, Integer> opponents = new HashMap<>();

		LogEntry logEntry;

		while (it.hasNext()) {
			logEntry = it.next();
			if (logEntry.getEventType().equals(EventType.KILL) && !logEntry.getKillType().equals(KillType.SUICIDE)
					&& logEntry.getVictim().equals(stats.getPlayerName())) {
				// System.out.println(logEntry.getAttackerWeaponType() + ": " +
				// logEntry.getWeapon());
				if (opponents.containsKey(logEntry.getPlayer()))
					opponents.put(logEntry.getPlayer(),
							new Integer(opponents.get(logEntry.getPlayer()).intValue() + 1));
				else
					opponents.put(logEntry.getPlayer(), new Integer(1));
			}

		}

		stats.setEnemies(opponents);

		return stats;
	}

	/*
	 * Per player, count how many kills he had without TKs and Suicides
	 */
	private PlayerStats countKills(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();

		LogEntry logEntry;
		int kills = 0;

		while (it.hasNext()) {
			logEntry = it.next();
			if (isRealKill(logEntry) && logEntry.getPlayer().equals(stats.getPlayerName())) {
				kills++;
			}

		}

		stats.setKills(kills);
		getKillRanking().put(stats.getPlayerName(), new Integer(stats.getKills()));

		return stats;
	}

	/*
	 * Per player, count how often he teamkilled
	 */
	private PlayerStats countTeamKills(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();

		LogEntry logEntry;
		int tks = 0;

		while (it.hasNext()) {
			logEntry = it.next();
			if (!logEntry.getKillType().equals(KillType.SUICIDE) && logEntry.isTeamkill()) {
				tks++;
			}

		}

		stats.setTeamKills(tks);
		getTkRanking().put(stats.getPlayerName(), new Integer(stats.getTeamKills()));

		return stats;
	}

	/*
	 * Per player, count the kills with a special VehicleType
	 */
	private PlayerStats countVehicleKills(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();
		HashMap<String, Integer> vehicleKill = new HashMap<>();
		HashMap<VehicleType, Integer> vehicleTypeKill = new HashMap<>();
		HashMap<String, Integer> vehicleTypeKillRankingForVehicleType;
		LogEntry logEntry = null;

		while (it.hasNext()) {
			logEntry = it.next();
			if (logEntry.getPlayer().equals(stats.getPlayerName()) && isRealKill(logEntry)) {
				switch (logEntry.getKillType()) {
				case VEHICLE_INF:
				case VEHICLE_VEHICLE:
					if (vehicleKill.containsKey(logEntry.getAttackerVehicleName()))
						vehicleKill.put(logEntry.getAttackerVehicleName(),
								new Integer(vehicleKill.get(logEntry.getAttackerVehicleName()).intValue() + 1));
					else
						vehicleKill.put(logEntry.getAttackerVehicleName(), new Integer(1));
					if (vehicleTypeKill.containsKey(logEntry.getAttackerVehicleType()))
						vehicleTypeKill.put(logEntry.getAttackerVehicleType(),
								new Integer(vehicleTypeKill.get(logEntry.getAttackerVehicleType()).intValue() + 1));
					else
						vehicleTypeKill.put(logEntry.getAttackerVehicleType(), new Integer(1));

					if (!getVehicleTypeRanking().containsKey((logEntry.getAttackerVehicleType())))
						vehicleTypeKillRankingForVehicleType = new HashMap<>();
					else
						vehicleTypeKillRankingForVehicleType = getVehicleTypeRanking()
								.get(logEntry.getAttackerVehicleType());

					if (!vehicleTypeKillRankingForVehicleType.containsKey(logEntry.getPlayer()))
						vehicleTypeKillRankingForVehicleType.put(logEntry.getPlayer(), new Integer(1));
					else
						vehicleTypeKillRankingForVehicleType.put(logEntry.getPlayer(), new Integer(
								vehicleTypeKillRankingForVehicleType.get(logEntry.getPlayer()).intValue() + 1));

					getVehicleTypeRanking().put(logEntry.getAttackerVehicleType(),
							vehicleTypeKillRankingForVehicleType);
					break;
				default:
					break;
				}

			}
		}

		stats.setVehicleNameKills(vehicleKill);
		stats.setVehicleTypeKills(vehicleTypeKill);

		return stats;
	}

	private PlayerStats countVictims(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();
		HashMap<String, Integer> opponents = new HashMap<>();

		LogEntry logEntry;

		while (it.hasNext()) {
			logEntry = it.next();
			if (isRealKill(logEntry) && !logEntry.getVictim().equals(stats.getPlayerName())) {
				// System.out.println(logEntry.getAttackerWeaponType() + ": " +
				// logEntry.getWeapon());
				if (opponents.containsKey(logEntry.getVictim()))
					opponents.put(logEntry.getVictim(),
							new Integer(opponents.get(logEntry.getVictim()).intValue() + 1));
				else
					opponents.put(logEntry.getVictim(), new Integer(1));
			}

		}

		stats.setVictims(opponents);

		return stats;
	}

	/*
	 * Per player, count the kills with a special WeaponType
	 */
	private PlayerStats countWeaponKills(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();
		HashMap<String, Integer> weaponKill = new HashMap<>();
		HashMap<WeaponType, Integer> weaponTypeKill = new HashMap<>();
		HashMap<String, Integer> weaponTypeKillRankingForVehicleType;
		

		LogEntry logEntry;

		while (it.hasNext()) {
			logEntry = it.next();
			if (logEntry.getPlayer().equals(stats.getPlayerName()) && isRealKill(logEntry)) {
				switch (logEntry.getKillType()) {
				case INF_INF:
				case INF_VEHICLE:
					// Count weapon Kills
					if (weaponKill.containsKey(logEntry.getWeaponName()))
						weaponKill.put(logEntry.getWeaponName(),
								new Integer(weaponKill.get(logEntry.getWeaponName()).intValue() + 1));
					else
						weaponKill.put(logEntry.getWeaponName(), new Integer(1));

					// Count weaponType kills
					if (weaponTypeKill.containsKey(logEntry.getAttackerWeaponType()))
						weaponTypeKill.put(logEntry.getAttackerWeaponType(),
								new Integer(weaponTypeKill.get(logEntry.getAttackerWeaponType()).intValue() + 1));
					else
						weaponTypeKill.put(logEntry.getAttackerWeaponType(), new Integer(1));

					if (!getWeaponTypeRanking().containsKey((logEntry.getAttackerWeaponType())))
						weaponTypeKillRankingForVehicleType = new HashMap<>();
					else
						weaponTypeKillRankingForVehicleType = getWeaponTypeRanking()
								.get(logEntry.getAttackerWeaponType());

					if (!weaponTypeKillRankingForVehicleType.containsKey(logEntry.getPlayer()))
						weaponTypeKillRankingForVehicleType.put(logEntry.getPlayer(), new Integer(1));
					else
						weaponTypeKillRankingForVehicleType.put(logEntry.getPlayer(), new Integer(
								weaponTypeKillRankingForVehicleType.get(logEntry.getPlayer()).intValue() + 1));

					getWeaponTypeRanking().put(logEntry.getAttackerWeaponType(), weaponTypeKillRankingForVehicleType);
					

				
					break;
				default:
					break;
				}
			}

		}

		stats.setWeaponNameKills(weaponKill);
		stats.setWeaponTypeKills(weaponTypeKill);

		return stats;
	}

	private HashMap<String, PlayerStats> createPlayerStats(HashMap<String, PlayerStats> playerEvents) {
		// Walk over each player
		HashMap<String, PlayerStats> stats = playerEvents;
		for (Map.Entry<String, PlayerStats> entry : stats.entrySet()) {
			String player = entry.getKey();
			PlayerStats playerStats = entry.getValue();

			// Count number of kill per Weapon
			playerStats = countWeaponKills(playerStats);

			// Count number of kill per Vehicle
			playerStats = countVehicleKills(playerStats);

			// Count number of victims
			playerStats = countVictims(playerStats);

			// Count number of enemies
			playerStats = countEnemies(playerStats);

			// Count number of kills
			playerStats = countKills(playerStats);

			// Count number of deaths
			playerStats = countDeaths(playerStats);

			// Count number of TKs
			playerStats = countTeamKills(playerStats);

			// Count number of CP Things
			playerStats = countCPStuff(playerStats);

			if (playerStats.getDeaths() > 0)
				playerStats.setKdrRatio((double) playerStats.getKills() / (double) playerStats.getDeaths());
			getKdrRanking().put(playerStats.getPlayerName(), new Double(playerStats.getKdrRatio()));

			stats.put(player, playerStats);
		}

		return stats;
	}

	private void dumpVehicleTypeRank(String name, HashMap<VehicleType, HashMap<String, Integer>> ranks, FileWriter fw) {

		for (Map.Entry<VehicleType, HashMap<String, Integer>> entry : ranks.entrySet()) {
			try {
				fw.write(dumpRank(FragalyzerConstants.vehicleTypeNames.get(entry.getKey()), entry.getValue()) + ",");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

	}

	private void dumpWeaponTypeRank(String name, HashMap<WeaponType, HashMap<String, Integer>> ranks, FileWriter fw) {

		for (Map.Entry<WeaponType, HashMap<String, Integer>> entry : ranks.entrySet()) {
			try {
				fw.write(dumpRank(FragalyzerConstants.weaponTypeNames.get(entry.getKey()), entry.getValue()) + ",");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

	}

	private String dumpRank(String name, HashMap<String, Integer> ranks) {
		JSONObject obj, event;
		JSONArray list;
		obj = new JSONObject();
		list = new JSONArray();
		for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(ranks).entrySet()) {
			event = new JSONObject();
			event.put(entry.getKey(), entry.getValue());
			list.add(event);
		}
		obj.put(name, list);
		
		appendToHTLMReport(name, getScope().name(), ranks);
		
		return obj.toJSONString();
	}

	private String dumpRankDouble(String name, HashMap<String, Double> ranks) {

		DecimalFormat df = new DecimalFormat("##.##");
		df.setRoundingMode(RoundingMode.CEILING);

		JSONObject obj, event;
		JSONArray list;
		obj = new JSONObject();
		list = new JSONArray();
		for (Map.Entry<String, Double> entry : MapUtil.sortByValueDesc(ranks).entrySet()) {
			event = new JSONObject();
			event.put(entry.getKey(), String.format(df.format(entry.getValue().doubleValue())));
			list.add(event);
		}
		obj.put(name, list);
		return obj.toJSONString();
	}
	
	private void appendToHTLMReport(String map_round, String scope, HashMap<String, Integer> ranks){
		
		
		Title title = new Title();
		title.appendChild(new Text(map_round + " " + getScopeName()));
		getReport(). appendChild(title);

		Body body = new Body();

		Table table = new Table();
		Tr tr = new Tr();
		Td td = new Td();

//		H1 h1 = new H1();
//		h1.appendChild(new Text(scope));
//		body.appendChild(h1);

		
		table = new Table();
	
		H2 h2 = new H2();
		h2.appendChild(new Text(map_round));
		body.appendChild(h2);

		for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(ranks).entrySet()) {
			 tr = new Tr();
			 //tr = new Tr();
			 table.appendChild(tr);
			 td = new Td();
			 td.appendChild(new Text(entry.getKey()));
			 tr.appendChild(td);		
			 td = new Td();
			 td.appendChild(new Text(entry.getValue()));
			 tr.appendChild(td);
		}
		body.appendChild(table);
		getReport().appendChild(body);

	}
	
	private void appendPlayerStats(String player, PlayerStats stats){



		Body body = new Body();

		Table table = new Table();
		Tr tr = new Tr();
		Td td = new Td();

		H1 h1 = new H1();
		h1.appendChild(new Text("Stats for: " + player));
		body.appendChild(h1);

		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Kills"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getKills()));

		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Deaths"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getDeaths()));
		
		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Teamkills"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getTeamKills()));		

		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Flag Captures"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getFlagCaps()));					
		

		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Flag Capture Assists"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getFlagCapAssists()));						


		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Flag Neutralizes"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getFlagNeutralizes()));					
		

		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Flag Neutralize Assits"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getFlagNeutralizeAssist()));					
		

		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Flag Defends"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(stats.getFlagDefends()));					
		
		H4 h2 = new H4();
		h2.appendChild(new Text(FragalyzerConstants.vehicletypekills));
		
		body.appendChild(table);
		body.appendChild(h2);
		table = new Table();

		for (Map.Entry<VehicleType, Integer> entry : MapUtil.sortByValueDesc(stats.getVehicleTypeKills()).entrySet()) {
			 tr = new Tr();
			 //tr = new Tr();
			
			 td = new Td();
			 td.appendChild(new Text(FragalyzerConstants.vehicleTypeNames.get(entry.getKey())));
			 tr.appendChild(td);		
			 td = new Td();
			 td.appendChild(new Text(entry.getValue()));
			 tr.appendChild(td);
			 table.appendChild(tr);
		}
		body.appendChild(table);	
		
		h2 = new H4();
		h2.appendChild(new Text(FragalyzerConstants.vehiclekill));

		body.appendChild(h2);
		table = new Table();

		for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getVehicleNameKills()).entrySet()) {
			 tr = new Tr();
			 //tr = new Tr();
			
			 td = new Td();
			 td.appendChild(new Text(entry.getKey()));
			 tr.appendChild(td);		
			 td = new Td();
			 td.appendChild(new Text(entry.getValue()));
			 tr.appendChild(td);
			 table.appendChild(tr);
		}
		body.appendChild(table);			
		
		
		h2 = new H4();
		h2.appendChild(new Text(FragalyzerConstants.weaponkill));

		body.appendChild(h2);
		table = new Table();

		for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getWeaponNameKills()).entrySet()) {
			 tr = new Tr();
			 //tr = new Tr();
			
			 td = new Td();
			 td.appendChild(new Text(entry.getKey()));
			 tr.appendChild(td);		
			 td = new Td();
			 td.appendChild(new Text(entry.getValue()));
			 tr.appendChild(td);
			 table.appendChild(tr);
		}
		body.appendChild(table);		
		
		h2 = new H4();
		h2.appendChild(new Text(FragalyzerConstants.enemies));

		body.appendChild(h2);
		table = new Table();

		for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getEnemies()).entrySet()) {
			 tr = new Tr();
			 //tr = new Tr();
			
			 td = new Td();
			 td.appendChild(new Text(entry.getKey()));
			 tr.appendChild(td);		
			 td = new Td();
			 td.appendChild(new Text(entry.getValue()));
			 tr.appendChild(td);
			 table.appendChild(tr);
		}
		body.appendChild(table);				
		
		h2 = new H4();
		h2.appendChild(new Text(FragalyzerConstants.victims));

		body.appendChild(h2);
		table = new Table();

		for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getVictims()).entrySet()) {
			 tr = new Tr();
			 //tr = new Tr();
			
			 td = new Td();
			 td.appendChild(new Text(entry.getKey()));
			 tr.appendChild(td);		
			 td = new Td();
			 td.appendChild(new Text(entry.getValue()));
			 tr.appendChild(td);
			 table.appendChild(tr);
		}
		body.appendChild(table);				
		
		getReport().appendChild(body);

	}
		
	
	private Tr getTr(){
		int c = getTd_counter();
		c++;
		if (getTd_counter()== 8){
			tr = new Tr();
			c = 1;
			
		}
		setTd_counter(c);
		return tr;
	}

	private void dumpRanks(HashMap<String, PlayerStats> playerEvents, String name) {

		// Getting a Set of Key-value pairs
		Set<Entry<String, PlayerStats>> entrySet = playerEvents.entrySet();

		String player;
		PlayerStats stats;
		JSONArray list;

		// Obtaining an iterator for the entry set
		Iterator<Map.Entry<String, PlayerStats>> it = entrySet.iterator();
		JSONObject obj, event;

		FileWriter fw = null;
		String line = new String();
		try {
			fw = new FileWriter(getBasePath() + "//" + getScope() + "_" + name + "_stats.json");
			fw.append(System.getProperty("line.separator")); // e.g.
			fw.write("[");

			fw.write(dumpRank(FragalyzerConstants.killrankings, getKillRanking()) + ",");
			fw.write(dumpRank(FragalyzerConstants.deathrankings, getDeathsRanking()) + ",");
			fw.write(dumpRank(FragalyzerConstants.tkrankings, getTkRanking()) + ",");
			fw.write(dumpRank(FragalyzerConstants.cpcapassistranking, getCpCapAassistRanking()) + ",");
			fw.write(dumpRank(FragalyzerConstants.cpcapranking, getCpCapRanking()) + ",");
			fw.write(dumpRank(FragalyzerConstants.cpdefendranking, getCpDefendRanking()) + ",");
			fw.write(dumpRank(FragalyzerConstants.cpneutralizeassistranking, getCpNeutralizeAssistRanking()) + ",");
			fw.write(dumpRank(FragalyzerConstants.cpneutralizeranking, getCpNeutralizeRanking()) + ",");
			fw.write(dumpRankDouble(FragalyzerConstants.kdrranking, getKdrRanking()) + ",");
			dumpVehicleTypeRank(FragalyzerConstants.vehicletype, getVehicleTypeRanking(), fw);
			dumpWeaponTypeRank(FragalyzerConstants.weapontype, getWeaponTypeRanking(), fw);

			while (it.hasNext()) {

				obj = new JSONObject();
				event = new JSONObject();
				list = new JSONArray();
				Map.Entry<String, PlayerStats> me = it.next();
				/*
				 * fw = new FileWriter(basePath + "//stats_" +
				 * me.getKey().replaceAll("[^A-Za-z0-9]", "") + ".json");
				 * fw.append(System.getProperty("line.separator")); // e.g.
				 * fw.write("[");
				 */
				player = me.getKey();
				stats = me.getValue();

				obj.put("player", player);
				obj.put("kills", stats.getKills());
				obj.put("deaths", stats.getDeaths());
				obj.put("teamkills", stats.getTeamKills());
				obj.put("cpcaps", stats.getFlagCaps());
				obj.put("cpcapassists", stats.getFlagCapAssists());
				obj.put("cpdefends", stats.getFlagDefends());
				obj.put("cpneutralizes", stats.getFlagNeutralizes());
				obj.put("cpneutralizeassists", stats.getFlagNeutralizeAssist());
				
				appendPlayerStats(player, stats);

				list = new JSONArray();
				for (Map.Entry<VehicleType, Integer> entry : MapUtil.sortByValueDesc(stats.getVehicleTypeKills())
						.entrySet()) {
					event = new JSONObject();
					event.put(FragalyzerConstants.vehicleTypeNames.get(entry.getKey()), entry.getValue());
					list.add(event);
					
					
				}
				obj.put("vehicletypekills", list);

				list = new JSONArray();
				for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getWeaponNameKills())
						.entrySet()) {
					event = new JSONObject();
					event.put(entry.getKey(), entry.getValue());
					list.add(event);
				}
				obj.put("weaponkill", list);

				list = new JSONArray();
				for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getVehicleNameKills())
						.entrySet()) {
					event = new JSONObject();
					event.put(entry.getKey(), entry.getValue());
					list.add(event);
				}
				obj.put("vehiclekill", list);

				list = new JSONArray();
				for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getVictims()).entrySet()) {
					event = new JSONObject();
					event.put(entry.getKey(), entry.getValue());
					list.add(event);
				}
				obj.put("victims", list);

				list = new JSONArray();
				for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(stats.getEnemies()).entrySet()) {
					event = new JSONObject();
					event.put(entry.getKey(), entry.getValue());
					list.add(event);
				}
				obj.put("enemies", list);

				line = obj.toJSONString();
				if (it.hasNext())
					line = line + ",";
				fw.write(line);

				/*
				 * fw.write(obj.toJSONString());
				 * 
				 * fw.append(System.getProperty("line.separator")); // e.g.
				 * fw.write("]"); // "\n" fw.close();
				 */
			}

			fw.append(System.getProperty("line.separator")); // e.g.
			fw.write("]"); // "\n"
			fw.close();
			
		} catch (IOException e) {
			System.err.println("Konnte Datei nicht erstellen");
		} finally {
			if (fw != null)
				try {
					fw.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
		}
		
		try {
			fw = new FileWriter(getBasePath() + "//" + getScope() + "_" + getScopeName() + "_stats.html");
			fw.write(getReport().write());
			fw.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();

		}		

	}

	public String getBasePath() {
		return basePath;
	}

	public HashMap<String, Integer> getCpCapAassistRanking() {
		return cpCapAassistRanking;
	}

	public HashMap<String, Integer> getCpCapRanking() {
		return cpCapRanking;
	}

	public HashMap<String, Integer> getCpDefendRanking() {
		return cpDefendRanking;
	}

	public HashMap<String, Integer> getCpNeutralizeAssistRanking() {
		return cpNeutralizeAssistRanking;
	}

	public HashMap<String, Integer> getCpNeutralizeRanking() {
		return cpNeutralizeRanking;
	}

	public HashMap<String, Integer> getDeathsRanking() {
		return deathsRanking;
	}

	public HashMap<String, Double> getKdrRanking() {
		return kdrRanking;
	}

	public HashMap<String, Integer> getKillRanking() {
		return killRanking;
	}

	public StatScope getScope() {
		return scope;
	}

	public HashMap<String, Integer> getTkRanking() {
		return tkRanking;
	}

	private boolean isRealKill(LogEntry logEntry) {
		return logEntry.getEventType().equals(EventType.KILL) && !logEntry.getKillType().equals(KillType.SUICIDE)
				&& !logEntry.isTeamkill();
	}

	public void rank(ArrayList<LogEntry> logEntries, String name, StatScope scope) {
		setScope(scope);
		setScopeName(name);
		Iterator<LogEntry> it = logEntries.iterator();
		setReport(new Html());
		tr = new Tr();
		table = new Table();
		setTd_counter(0);
		LogEntry kill;

		setKillRanking(new HashMap<>());
		setDeathsRanking(new HashMap<>());
		setTkRanking(new HashMap<>());
		setKdrRanking(new HashMap<>());
		setCpCapRanking(new HashMap<>());
		setVehicleTypeRanking(new HashMap<>());
		setWeaponTypeRanking(new HashMap<>());

		PlayerStats stats = new PlayerStats();
		HashMap<String, PlayerStats> playerEvents = new HashMap<>();
		LogEntry logEntry;
		while (it.hasNext()) {
			logEntry = it.next();

			if (logEntry.getEventType().equals(EventType.KILL) || logEntry.getEventType().equals(EventType.SCORE)) {

				kill = logEntry;

				// Add to player's eventlist
				if (!playerEvents.containsKey(kill.getPlayer())) {
					stats = new PlayerStats();
					stats.setPlayerName(kill.getPlayer());
				} else {
					stats = playerEvents.get(kill.getPlayer());
				}

				stats.getEvents().add(kill);
				playerEvents.put(kill.getPlayer(), stats);

				if (logEntry.getEventType().equals(EventType.KILL)) {
					if (!playerEvents.containsKey(kill.getVictim())) {
						stats = new PlayerStats();
						stats.setPlayerName(kill.getVictim());
					} else {
						stats = playerEvents.get(kill.getVictim());
					}

					stats.getEvents().add(kill);
					playerEvents.put(kill.getVictim(), stats);
				}

			}

		}

		playerEvents = createPlayerStats(playerEvents);

		dumpRanks(playerEvents, name);

	}

	public void setBasePath(String basePath) {
		this.basePath = basePath;
	}

	public void setCpCapAassistRanking(HashMap<String, Integer> cpCapAassistRanking) {
		this.cpCapAassistRanking = cpCapAassistRanking;
	}

	public void setCpCapRanking(HashMap<String, Integer> cpCapRanking) {
		this.cpCapRanking = cpCapRanking;
	}

	public void setCpDefendRanking(HashMap<String, Integer> cpDefendRanking) {
		this.cpDefendRanking = cpDefendRanking;
	}

	public void setCpNeutralizeAssistRanking(HashMap<String, Integer> cpNeutralizeAssistRanking) {
		this.cpNeutralizeAssistRanking = cpNeutralizeAssistRanking;
	}

	public void setCpNeutralizeRanking(HashMap<String, Integer> cpNeutralizeRanking) {
		this.cpNeutralizeRanking = cpNeutralizeRanking;
	}

	public void setDeathsRanking(HashMap<String, Integer> deathsRanking) {
		this.deathsRanking = deathsRanking;
	}

	public void setKdrRanking(HashMap<String, Double> kdrRanking) {
		this.kdrRanking = kdrRanking;
	}

	public void setKillRanking(HashMap<String, Integer> killRanking) {
		this.killRanking = killRanking;
	}

	public void setScope(StatScope scope) {
		this.scope = scope;
	}

	public void setTkRanking(HashMap<String, Integer> tkRanking) {
		this.tkRanking = tkRanking;
	}

	public HashMap<VehicleType, HashMap<String, Integer>> getVehicleTypeRanking() {
		return vehicleTypeRanking;
	}

	public void setVehicleTypeRanking(HashMap<VehicleType, HashMap<String, Integer>> vehicleTypeRanking) {
		this.vehicleTypeRanking = vehicleTypeRanking;
	}

	public HashMap<WeaponType, HashMap<String, Integer>> getWeaponTypeRanking() {
		return weaponTypeRanking;
	}

	public void setWeaponTypeRanking(HashMap<WeaponType, HashMap<String, Integer>> weaponTypeRanking) {
		this.weaponTypeRanking = weaponTypeRanking;
	}

	public HashMap<String, HashMap<KitType, Integer>> getWeaponRanking() {
		return weaponRanking;
	}

	public void setWeaponRanking(HashMap<String, HashMap<KitType, Integer>> weaponRanking) {
		this.weaponRanking = weaponRanking;
	}

	public String getScopeName() {
		return scopeName;
	}

	public void setScopeName(String scopeName) {
		this.scopeName = scopeName;
	}

	public Html getReport() {
		return report;
	}

	public void setReport(Html report) {
		this.report = report;
	}

	public int getTd_counter() {
		return td_counter;
	}

	public void setTd_counter(int td_counter) {
		this.td_counter = td_counter;
	}

}