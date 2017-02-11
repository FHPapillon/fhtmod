package com.fht.fragalyzer;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import org.json.simple.JSONObject;

import com.fht.fragalyzer.types.DataPoint;
import com.fht.fragalyzer.types.StatScope;

public class HeatmapDataProvider {
	
	private String basePath;


	public HeatmapDataProvider(String basePath) {
		super();
		setBasePath(basePath);
		// TODO Auto-generated constructor stub
	}

	public void dumpHeatMapDataPointsAndEventList(ArrayList<LogEntry> logEntries,  String name, StatScope scope) {
		HashMap<String, DataPoint> heatmapHM = new HashMap<>();
		String heatmapCoord;
		// Create from the now created Entries a human-readable list of events
		FileWriter fw = null;
		DataPoint dpo;
		LogEntry logEntry;
		try {
			fw = new FileWriter(getBasePath() + "//" + scope + "_" + name +   "_result.txt");
			Iterator<LogEntry> it = logEntries.iterator();
			while (it.hasNext()) {
				logEntry = it.next();
				// Right now we are only interested in Kills

				// If a Position is given, then..
				heatmapHM = getDataPoints(heatmapHM, logEntry);

				// Write the event to the file
				fw.write(logEntry.toString());
				fw.append(System.getProperty("line.separator")); // e.g. "\n"

			}
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

		// Getting a Set of Key-value pairs
		Set entrySet = heatmapHM.entrySet();

		// Obtaining an iterator for the entry set
		Iterator it = entrySet.iterator();
		JSONObject obj;
		String x, y;
		fw = null;
		try {
			fw = new FileWriter(getBasePath() + "//" + scope + "_" + name +   "_heatmap_with_number.json");
			fw.write("[");

			fw.append(System.getProperty("line.separator")); // e.g.
			while (it.hasNext()) {
				obj = new JSONObject();
				Map.Entry me = (Map.Entry) it.next();
				dpo = (DataPoint) me.getValue();

				obj.put("x", dpo.getX());
				obj.put("y", dpo.getY());
				obj.put("value", dpo.getNumber() > 1 ? dpo.getNumber() * FragalyzerConstants.heatmapDataPointMultiplicationFactor : dpo.getNumber());

				fw.write(obj.toJSONString() + ",");

				fw.append(System.getProperty("line.separator")); // e.g.
																	// "\n"

			}
			fw.write("]");

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

	private HashMap<String, DataPoint> getDataPoints(HashMap<String, DataPoint> heatmap, LogEntry kill) {
		String heatmapCoord;
		DataPoint dpo;

		if (kill.getPlayerPosition() != null) {

			// ..determine the Coordinate where it occured
			heatmapCoord = Double.toString(kill.getPlayerPosition().getXNormalizedDatapointRounded(1)) + "/"
					+ Double.toString(kill.getPlayerPosition().getZNormalizedDatapointRounded(1));

			// Check if a kill has already occured at that coordinate...
			if (heatmap.containsKey(heatmapCoord)) {
				// ..and add this to it if so
				dpo = heatmap.get(heatmapCoord);
				dpo.setNumber(dpo.getNumber() + 1);
				heatmap.put(heatmapCoord, dpo);
			} else {
				// Otherwise create a new DataPoint for this kill
				dpo = new DataPoint();
				dpo.setX(kill.getPlayerPosition().getXNormalizedDatapointRounded(1));
				dpo.setY(kill.getPlayerPosition().getZNormalizedDatapointRounded(1));
				dpo.setNumber(1);
				heatmap.put(heatmapCoord, dpo);
			}
		}

		if (kill.getVictimPosition() != null) {

			// ..determine the Coordinate where it occured
			heatmapCoord = Double.toString(kill.getVictimPosition().getXNormalizedDatapointRounded(1)) + "/"
					+ Double.toString(kill.getVictimPosition().getZNormalizedDatapointRounded(1));

			// Check if a kill has already occured at that coordinate...
			if (heatmap.containsKey(heatmapCoord)) {
				// ..and add this to it if so
				dpo = heatmap.get(heatmapCoord);
				dpo.setNumber(dpo.getNumber() + 1);
				heatmap.put(heatmapCoord, dpo);
			} else {
				// Otherwise create a new DataPoint for this kill
				dpo = new DataPoint();
				dpo.setX(kill.getVictimPosition().getXNormalizedDatapointRounded(1));
				dpo.setY(kill.getVictimPosition().getZNormalizedDatapointRounded(1));
				dpo.setNumber(1);
				heatmap.put(heatmapCoord, dpo);
			}
		}
		return heatmap;
	}
	public String getBasePath() {
		return basePath;
	}

	public void setBasePath(String basePath) {
		this.basePath = basePath;
	}
}

