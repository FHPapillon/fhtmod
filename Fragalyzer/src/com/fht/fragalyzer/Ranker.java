package com.fht.fragalyzer;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import com.fht.fragalyzer.types.KillType;

public class Ranker {
	public void rank(ArrayList<LogEntry> logEntries) {
		Iterator<LogEntry> it = logEntries.iterator();
		Integer count, countTK, countDeath;
		Kill kill;
		HashMap<String, Integer> hm = new HashMap<>();
		HashMap<String, Integer> deaths = new HashMap<>();
		HashMap<String, Integer> tks = new HashMap<>();
		ArrayList<String> datapoints = new ArrayList<>();
		double max_x = 0;
		double max_z = 0;
		double min_x = 0;
		double min_z = 0;		
		
		LogEntry logEntry;
		while (it.hasNext()) {
			logEntry = it.next();

			if (logEntry instanceof Kill) {
				
				kill = (Kill) logEntry;
				if (kill.getPlayerPosition() != null) {
					if (kill.getPlayerPosition().getXNormalized() > max_x)
						max_x = kill.getPlayerPosition().getXNormalized();
					if (kill.getPlayerPosition().getZNormalized() > max_z)
						max_z = kill.getPlayerPosition().getZNormalized();	
					if (kill.getPlayerPosition().getXNormalized() < min_x)
						min_x = kill.getPlayerPosition().getXNormalized();
					if (kill.getPlayerPosition().getZNormalized() < min_z)
						min_z = kill.getPlayerPosition().getZNormalized();							
				}
				if (!kill.getKillType().equals(KillType.SUICIDE) && !kill.isTeamkill()) {
					if (!hm.containsKey(kill.getPlayer()))
						hm.put(kill.getPlayer(), new Integer(0));
					if (!deaths.containsKey(((Kill) kill).getVictim()))
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
}