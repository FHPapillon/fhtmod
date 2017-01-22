package com.fht.fragalyzer;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import com.fht.fragalyzer.types.EventType;
import com.fht.fragalyzer.types.KillType;
import com.fht.fragalyzer.types.PlayerStats;
import com.fht.fragalyzer.types.WeaponType;

public class Ranker {
	public void rank(ArrayList<LogEntry> logEntries) {
		Iterator<LogEntry> it = logEntries.iterator();
		Integer count, countTK, countDeath;
		LogEntry kill;
		HashMap<String, Integer> hm = new HashMap<>();
		HashMap<String, Integer> deaths = new HashMap<>();
		HashMap<String, Integer> tks = new HashMap<>();
		ArrayList<String> datapoints = new ArrayList<>();
		
		PlayerStats stats = new PlayerStats();
		HashMap<String, PlayerStats> playerEvents = new HashMap<>();
				LogEntry logEntry;
		while (it.hasNext()) {
			logEntry = it.next();

			if (logEntry.getEventType().equals(EventType.KILL)) {
				
				kill =  logEntry;			
				
				//Add to player's eventlist
				if (!playerEvents.containsKey(kill.getPlayer())) {
					stats = new PlayerStats();
					stats.setPlayerName(kill.getPlayer());
				}
				else {
					stats = playerEvents.get(kill.getPlayer());
				}
				stats.getKills().add(kill);
				playerEvents.put(kill.getPlayer(), stats);
				
				if (!kill.getKillType().equals(KillType.SUICIDE) && !kill.isTeamkill()) {
					if (!hm.containsKey(kill.getPlayer()))
						hm.put(kill.getPlayer(), new Integer(0));
					if (!deaths.containsKey(kill.getVictim()))
						deaths.put(kill.getVictim(), new Integer(0));		
					
					count = hm.get(kill.getPlayer());
					count = new Integer(count.intValue() + 1);
					countDeath = deaths.get(kill.getVictim());
					countDeath = new Integer(countDeath.intValue() + 1);					
					hm.put(kill.getPlayer(), count);
					deaths.put(kill.getVictim(), count);
					datapoints.add(kill.getPlayerPosition().getDataPointRepresentation());
				}
				if (kill.isTeamkill()) {
					if (!tks.containsKey(logEntry.getPlayer()))
						tks.put(logEntry.getPlayer(), new Integer(0));
					countTK = tks.get(logEntry.getPlayer());
					countTK = new Integer(countTK.intValue() + 1);
					tks.put(logEntry.getPlayer(), countTK);
				}

			}

		}

		createPlayerStats(playerEvents);
		
		
		
		Iterator it2 = MapUtil.sortByValueDesc(hm).entrySet().iterator();

		while (it2.hasNext()) {
			
			System.out.println((it2.next().toString()));
		}
		System.out.println("Deaths");
		it2 = MapUtil.sortByValueDesc(deaths).entrySet().iterator();

		while (it2.hasNext()) {
			System.out.println((it2.next().toString()));
		}		
		
		System.out.println("TKs");
		it2 = MapUtil.sortByValueDesc(tks).entrySet().iterator();

		while (it2.hasNext()) {
			System.out.println((it2.next().toString()));
		}
	}
	
	
	
	private HashMap<String, PlayerStats> createPlayerStats(HashMap<String, PlayerStats> playerEvents) {
		//Walk over each player
		HashMap<String, PlayerStats> stats = playerEvents;
		for (Map.Entry<String, PlayerStats> entry : stats.entrySet()) {
		    String player = entry.getKey();
		    PlayerStats playerStats = entry.getValue();
		    
		    //Count number of kill per WeaponType
		    playerStats = countWeaponTypeKills(playerStats);
		}
		
		return stats;
	}
	
	/*
	 * Per player, count the kills with a special WeaponType
	 */
	private PlayerStats countWeaponTypeKills(PlayerStats stats){
		Iterator<LogEntry> it = stats.getKills().iterator();
		HashMap<WeaponType, Integer> weaponKill = new HashMap<>();
		LogEntry logEntry;
		
		while (it.hasNext()){
			logEntry = it.next();
			switch (logEntry.getKillType()) {
			case INF_INF:
			case INF_VEHICLE:
				if (weaponKill.containsKey(logEntry.getAttackerWeaponType()))
					weaponKill.put(logEntry.getAttackerWeaponType(), new Integer(weaponKill.get(logEntry.getAttackerWeaponType()).intValue()+1));
				else
					weaponKill.put(logEntry.getAttackerWeaponType(), new Integer(1));
				break;

			default:
				break;
			}
			
		}
		System.out.println("Player " + stats.getPlayerName());
		for (Map.Entry<WeaponType, Integer> entry : weaponKill.entrySet()) {
			WeaponType weaponType = entry.getKey();
		    Integer numberOfKills = entry.getValue();
		    
		    //Count number of kill per WeaponType
		    System.out.println(FragalyzerConstants.weaponTypeNames.get(weaponType) + ": " + numberOfKills.intValue());
		}		
		
		
		
		return stats;
	}
}