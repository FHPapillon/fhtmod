package com.fht.fragalyzer;

import java.io.FileWriter;
import java.io.IOException;
import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import javax.print.attribute.HashPrintJobAttributeSet;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import com.fht.fragalyzer.types.EventType;
import com.fht.fragalyzer.types.KillType;
import com.fht.fragalyzer.types.PlayerStats;
import com.fht.fragalyzer.types.StatScope;
import com.fht.fragalyzer.types.VehicleType;
import com.fht.fragalyzer.types.WeaponType;

public class Ranker {
	
	private String basePath;
	private StatScope scope;
	
	private HashMap<String, Integer> killRanking;
	private HashMap<String, Integer> deathsRanking;
	private HashMap<String, Integer> tkRanking;	
	private HashMap<String, Double> kdrRanking;

	private HashMap<String, Integer> cpCapRanking;

	private HashMap<String, Integer> cpCapAassistRanking;

	private HashMap<String, Integer> cpDefendRanking;

	private HashMap<String, Integer> cpNeutralizeRanking;

	private HashMap<String, Integer> cpNeutralizeAssistRanking;

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
		
		System.out.println("Player  " + cpCaptures + " " + cpCaptureAssists + " " + cpNeutralizeAssists + " " +cpNeutralizes + " " + cpDefends + " " + stats.getPlayerName());

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
			if (logEntry.getEventType().equals(EventType.KILL)&&!logEntry.getKillType().equals(KillType.SUICIDE) && logEntry.getVictim().equals(stats.getPlayerName())) {
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
			if (logEntry.getEventType().equals(EventType.KILL)&&!logEntry.getKillType().equals(KillType.SUICIDE) && logEntry.getVictim().equals(stats.getPlayerName())) {
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
	 * Per player, count how many kills he had
	 */
	private PlayerStats countKills(PlayerStats stats) {
		Iterator<LogEntry> it = stats.getEvents().iterator();
		
		LogEntry logEntry;
		int kills = 0;

		while (it.hasNext()) {
			logEntry = it.next();
			if (!logEntry.getKillType().equals(KillType.SUICIDE) && logEntry.getPlayer().equals(stats.getPlayerName())) {
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
		LogEntry logEntry = null;

		while (it.hasNext()) {
			logEntry = it.next();
			if (logEntry.getPlayer().equals(stats.getPlayerName())) {
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
			if (logEntry.getEventType().equals(EventType.KILL)&&!logEntry.getKillType().equals(KillType.SUICIDE) && !logEntry.getVictim().equals(stats.getPlayerName())) {
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
		LogEntry logEntry;

		while (it.hasNext()) {
			logEntry = it.next();
			if (logEntry.getPlayer().equals(stats.getPlayerName())) {
				switch (logEntry.getKillType()) {
				case INF_INF:
				case INF_VEHICLE:
					// System.out.println(logEntry.getAttackerWeaponType() + ":
					// " +
					// logEntry.getWeapon());
					if (weaponKill.containsKey(logEntry.getWeaponName()))
						weaponKill.put(logEntry.getWeaponName(),
								new Integer(weaponKill.get(logEntry.getWeaponName()).intValue() + 1));
					else
						weaponKill.put(logEntry.getWeaponName(), new Integer(1));
					if (weaponTypeKill.containsKey(logEntry.getAttackerWeaponType()))
						weaponTypeKill.put(logEntry.getAttackerWeaponType(),
								new Integer(weaponTypeKill.get(logEntry.getAttackerWeaponType()).intValue() + 1));
					else
						weaponTypeKill.put(logEntry.getAttackerWeaponType(), new Integer(1));
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

			// Count number of kill per WeaponType
			playerStats = countWeaponKills(playerStats);

			// Count number of kill per VehicleType
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
				playerStats.setKdrRatio((double)playerStats.getKills() / (double)playerStats.getDeaths());
			getKdrRanking().put(playerStats.getPlayerName(), new Double(playerStats.getKdrRatio()));

			stats.put(player, playerStats);
		}

		return stats;
	}

	private void dumpRanks(HashMap<String, PlayerStats> playerEvents, String name) {

		// Getting a Set of Key-value pairs
		Set entrySet = playerEvents.entrySet();

		String player;
		PlayerStats stats;
		JSONArray list;

		// Obtaining an iterator for the entry set
		Iterator<Map.Entry<String, PlayerStats>> it = entrySet.iterator();
		JSONObject obj, event;
		

		DecimalFormat df = new DecimalFormat("##.##");
		df.setRoundingMode(RoundingMode.CEILING);

		
		FileWriter fw = null;
		String line = new String();
		try {
			fw = new FileWriter(getBasePath() + "//" + getScope() + "_" + name +  "_stats.json");
			fw.append(System.getProperty("line.separator")); // e.g.
			fw.write("[");
			obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getKillRanking())
					.entrySet()) {
				event = new JSONObject();
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("killrankings",list);
			line = obj.toJSONString();
			fw.write(line + ",");
			
			obj = new JSONObject();

			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getDeathsRanking())
					.entrySet()) {
				event = new JSONObject();
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("deathrankings", list);
			line = obj.toJSONString();
			fw.write(line + ",");		
			
			obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getTkRanking())
					.entrySet()) {
				event = new JSONObject();
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("tkrankings", list);
			line = obj.toJSONString();
			fw.write(line + ",");	
			
			obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Double> entry : MapUtil.sortByValueDesc(getKdrRanking())
					.entrySet()) {
				event = new JSONObject();
				
				event.put(entry.getKey(), String.format(df.format(entry.getValue().doubleValue())));
				list.add(event);
			}
			obj.put("kdrranking", list);
			line = obj.toJSONString();
			fw.write(line + ",");			
			
			obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getCpCapRanking())
					.entrySet()) {
				event = new JSONObject();
				
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("cpcapranking", list);
			line = obj.toJSONString();
			fw.write(line + ",");			
			
			obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getCpCapAassistRanking())
					.entrySet()) {
				event = new JSONObject();
				
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("cpcapassistranking", list);
			line = obj.toJSONString();
			fw.write(line + ",");							
			
obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getCpDefendRanking())
					.entrySet()) {
				event = new JSONObject();
				
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("cpdefendranking", list);
			line = obj.toJSONString();
			fw.write(line + ",");					
			
			
obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getCpNeutralizeAssistRanking())
					.entrySet()) {
				event = new JSONObject();
				
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("cpneutralizeassistranking", list);
			line = obj.toJSONString();
			fw.write(line + ",");		
			
obj = new JSONObject();
			
			list = new JSONArray();
			for (Map.Entry<String, Integer> entry : MapUtil.sortByValueDesc(getCpNeutralizeRanking())
					.entrySet()) {
				event = new JSONObject();
				
				event.put(entry.getKey(), entry.getValue());
				list.add(event);
			}
			obj.put("cpneutralizeranking", list);
			line = obj.toJSONString();
			fw.write(line + ",");					
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

	public void rank(ArrayList<LogEntry> logEntries, String name, StatScope scope) {
		setScope(scope);
		Iterator<LogEntry> it = logEntries.iterator();
		
		
		LogEntry kill;

		setKillRanking(new HashMap<>());
		setDeathsRanking(new HashMap<>());
		setTkRanking(new HashMap<>());		
		setKdrRanking(new HashMap<>());
		setCpCapRanking(new HashMap<>());

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


}