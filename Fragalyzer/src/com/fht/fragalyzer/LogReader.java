package com.fht.fragalyzer;

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

import org.json.simple.JSONObject;

import com.fht.fragalyzer.types.DataPoint;

public class LogReader {

	public ArrayList<LogEntry> ret;

	public ArrayList<LogEntry> readBattleLogs(String basePath) {
		System.out.println(basePath);
		Path p = Paths.get(basePath);
		ret = new ArrayList<>();
		LogMapper mapper = new LogMapper();
		LogEntry logEntry;
		HashMap<String, String> missingKits = new HashMap<>();
		HashMap<String, DataPoint> heatmapHM = new HashMap<>();
		String heatmapCoord;
		Kill kill;

		// Walk over all faLog files
		int count = 0;
		FileVisitor<Path> fv = new SimpleFileVisitor<Path>() {
			@Override
			public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
				Scanner scanner;
				int dot = file.toString().lastIndexOf(".");
				LogEntry entry;
				if (file.toString().substring(dot - 5, dot).equals(FragalyzerConstants.logfilename)) {
					System.out.println(file);

					try {
						scanner = new Scanner(file);
					} catch (FileNotFoundException e) {
						return null;
					}
					// now read the file line by line...

					while (scanner.hasNextLine()) {
						// Read each file from the from the log..
						String line = scanner.nextLine();
						// ..and create a proper entry from it
						entry = mapper.createLogEntryFromLogLine(missingKits, line);
						// If an entry was created, add it to the List
						if (entry != null)
							ret.add(entry);

					}
					scanner.close();

				}

				return FileVisitResult.CONTINUE;
			}

		};

		try {
			Files.walkFileTree(p, fv);
		} catch (IOException e) {
			e.printStackTrace();
		}

		// Create from the now created Entries a human-readable list of events
		FileWriter fw = null;
		DataPoint dpo;
		try {
			fw = new FileWriter(basePath + "//result.txt");
			Iterator<LogEntry> it = ret.iterator();
			while (it.hasNext()) {
				logEntry = it.next();
				// Right now we are only interested in Kills
				if (logEntry instanceof Kill) {
					kill = (Kill) logEntry;
					// If a Position is given, then..
					heatmapHM =  getDataPoints(heatmapHM, kill);

				}
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

		Iterator  itkit = missingKits.entrySet().iterator();
		while (itkit.hasNext())
			System.out.println(((Map.Entry)itkit.next()).getKey());

		// Getting a Set of Key-value pairs
		Set entrySet = heatmapHM.entrySet();

		// Obtaining an iterator for the entry set
		Iterator it = entrySet.iterator();
		JSONObject obj;
		String x, y;
		fw = null;
		try {
			fw = new FileWriter(basePath + "//heatmap_with_number.json");
			fw.write("[");

			fw.append(System.getProperty("line.separator")); // e.g.
			while (it.hasNext()) {
				obj = new JSONObject();
				Map.Entry me = (Map.Entry) it.next();
				dpo = (DataPoint) me.getValue();

				obj.put("x", dpo.getX());
				obj.put("y", dpo.getY());
				obj.put("value", dpo.getNumber());

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

		/*
		 * Iterator<LogEntry> dp_it = ret.iterator();
		 * 
		 * fw = null; try { fw = new FileWriter(basePath + "//heatmap.json");
		 * while (dp_it.hasNext()) { obj = new JSONObject(); logEntry =
		 * dp_it.next(); if (logEntry.getPlayerPosition() != null) {
		 * obj.put("x",
		 * logEntry.getPlayerPosition().getXNormalizedDatpointRep());
		 * obj.put("y",
		 * logEntry.getPlayerPosition().getZNormalizedDatapointRep());
		 * obj.put("value", logEntry.toString());
		 * 
		 * fw.write(obj.toJSONString());
		 * fw.append(System.getProperty("line.separator")); // e.g. // "\n"
		 * 
		 * } } } catch (IOException e) { System.err.println(
		 * "Konnte Datei nicht erstellen"); } finally { if (fw != null) try {
		 * fw.close(); } catch (IOException e) { e.printStackTrace(); } }
		 */
		return ret;

	}

	private HashMap<String, DataPoint> getDataPoints(HashMap<String, DataPoint> heatmap, Kill kill) {
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
}
