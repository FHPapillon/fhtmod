package com.fht.fragalyzer;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;


public class Ranker {
	public void rank(ArrayList<LogEntry> logEntries) {
		Iterator<LogEntry> it = logEntries.iterator();
		Integer count;
		Kill kill;
		HashMap<String, Integer> hm = new HashMap<>();
		LogEntry logEntry;
		while (it.hasNext()){
			logEntry = it.next();
			if (hm.containsKey(logEntry.getPlayer())){
				if (logEntry instanceof Kill) {
					kill = (Kill)logEntry;
					hm.put(logEntry.getPlayer(),  new Integer(hm.get(logEntry.getPlayer()).intValue() + 1));
				}
			}
		}
		Iterator it2 = hm.entrySet().iterator();
		while (it2.hasNext()){
			System.out.println((it2.next().toString()));
		}
	}
}
