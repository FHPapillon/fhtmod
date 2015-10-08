package com.fht.base;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;
import java.util.Map.Entry;
import java.util.SortedSet;
import java.util.TreeSet;

import com.hp.gagawa.java.elements.A;
import com.hp.gagawa.java.elements.Body;
import com.hp.gagawa.java.elements.Div;
import com.hp.gagawa.java.elements.H1;
import com.hp.gagawa.java.elements.H2;
import com.hp.gagawa.java.elements.H3;
import com.hp.gagawa.java.elements.H4;
import com.hp.gagawa.java.elements.Head;
import com.hp.gagawa.java.elements.Html;
import com.hp.gagawa.java.elements.Img;
import com.hp.gagawa.java.elements.Table;
import com.hp.gagawa.java.elements.Td;
import com.hp.gagawa.java.elements.Text;
import com.hp.gagawa.java.elements.Title;
import com.hp.gagawa.java.elements.Tr;

public class BaseChecker {

	public List<String> usedKits = new ArrayList<String>();
	private Collection<String> initLines;
	private Collection<String> gamePlayObjects;
	private String basePath;

	public HashMap<String, String> vehicle_names;
	private HashMap<String, Float> kitLimit;
	public HashMap<String, String> spawnerCondition;
	private HashMap<String, GenericType> vehicleTypes;

	private HashMap<String, GenericType> weaponTypes;

	private HashMap<String, GenericType> kitTypes;

	private HashMap<String, FH2Object> vehicles;

	private HashMap<String, String> flagNames;

	public HashMap<String, ControlPoint> controlPointsObjects;

	private HashMap<String, ObjectSpawner> objectSpawners;

	public HashMap<String, String> controlPoints;

	public HashMap<String, String> objectControlPoints;
	
	public FhtFileReader fileReader;

	public void check(String[] args) {
		String path, layer, mapname, displayMapname, team1, team2, tickets1, tickets2;

		Collection<String> errors = new ArrayList<>();
		Collection<String> kits_team1 = new ArrayList<>();
		Collection<String> kits_team2 = new ArrayList<>();
		fileReader = new FhtFileReader();

		objectSpawners = new HashMap<String, ObjectSpawner>();
		objectControlPoints = new HashMap<String, String>();

		// Check for the existence of the files
		// ClientArchives.con
		// ServerArchives.con
		// tmp.con
		// init.con
		// GamePlayObjects.con
		mapname = args[0];
		layer = args[1];
		path = FhtConstants.fh2_path + mapname;
		setBasePath(path);

		readObjects();
		readFiles();
		populateCPs();
		populateObjectsSpawners();

		displayMapname = getMapName(path, mapname);
		team1 = getTeam1();
		team2 = getTeam2();
		kits_team1 = getKits("1");
		kits_team2 = getKits("2");
		tickets1 = getTicketTeam1();
		tickets2 = getTicketTeam2();
		checkClientArchives(path, errors);
		checkServerArchives(path, errors);
		// checkInit(path, errors);
		// checkGamePlayObjects(path, errors);
		switch (layer) {
		case "64":
			layer = FhtConstants.gamePlayObjects_64;
			break;
		case "32":
			layer = FhtConstants.gamePlayObjects_32;
			break;
		case "16":
			layer = FhtConstants.gamePlayObjects_16;
			break;
		default:
			layer = FhtConstants.gamePlayObjects_64;
			break;
		}

		createHTMLReport(path, layer, displayMapname, team1, team2, kits_team1,
				kits_team2, tickets1, tickets2);

		checkTmp(path, errors);

		Iterator<String> it = errors.iterator();
		while (it.hasNext()) {
			//System.out.println(it.next());
		}

	}

	public void checkClientArchives(String basePath, Collection<String> errors) {

		checkFile(basePath, errors, FhtConstants.clientArchives,
				FhtConstants.clientArchiveLines);

	}

	private Collection<String> checkFile(String basePath,
			Collection<String> errors, String archive,
			Collection<String> archiveTargetValues) {
		// System.out.println(basePath + archive);
		Collection<String> col;
		String line, line2;
		col = getGamePlayObjects();
		if (col != null) {
			Iterator<String> it = archiveTargetValues.iterator();
			boolean found;
			while (it.hasNext()) {
				line = it.next();
				found = false;
				Iterator<String> it_as_is = col.iterator();
				// System.out.println("1: " + line);

				while (it_as_is.hasNext()) {
					line2 = it_as_is.next();
					if (line2.trim().equals(line.trim()))
						found = true;
					// System.out.println("2: " +line2);
				}
				if (found == false) {
					errors.add(archive + " missing line: " + line);
				}
			}
		} else
			errors.add("Missing the following file: " + archive);
		return col;

	}

	public void checkInit(String basePath, Collection<String> errors) {

		String line, kit;
		
		kit = new String();

		// Find out which kits shall be used in the map

		Iterator<String> it = getInitLines().iterator();
		while (it.hasNext()) {
			line = it.next();
			// Those are the lines to look at
			if (line.startsWith("gameLogic.setKit")) {
				int start = line.indexOf("\"") + 1;
				while (!line.substring(start, start + 1).equals("\"")) {
					kit = kit + line.substring(start, start + 1);
					start++;
				}
				System.out.println(kit);
				// found = checkKit(kit, errors);

				usedKits.add(kit);
				kit = "";

			}

			if (line.startsWith(FhtConstants.numberOfTickets64)) {

				System.out.println(line
						.substring(FhtConstants.numberOfTickets64.length()));

			}
		}

	}

	public void checkServerArchives(String basePath, Collection<String> errors) {

		checkFile(basePath, errors, FhtConstants.serverArchives,
				FhtConstants.serverArchiveLines);
	}

	public void checkTmp(String basePath, Collection<String> errors) {
		String line, lineTmp, kitCompare;
		boolean found = false;

		// Check the file tmp.con
		Collection<String> tmpLines = checkFile(basePath, errors,
				FhtConstants.tmp, FhtConstants.tmpLines);

		// Check for each used kit if it is loaded in tmp.con
		Iterator<String> itKits = usedKits.iterator();
		Iterator<String> itTmp;
		// Check used kits
		while (itKits.hasNext()) {
			found = false;
			itTmp = tmpLines.iterator();
			line = itKits.next();
			while (itTmp.hasNext()) {
				lineTmp = itTmp.next().toLowerCase();
				kitCompare = line.toLowerCase();

				if (lineTmp.contains(kitCompare))
					found = true;
			}
			if (found == false)
				errors.add("tmp.con missing line run ../../objects/kits... for kit "
						+ line);
		}
	}

	private void createHTMLReport(String basePath, String gpo, String mapname,
			String team1, String team2, Collection<String> kits_team1,
			Collection<String> kits_team2, String tickets1, String tickets2) {
		int counter = 0;
		ControlPoint cp;
		// String vehicle, cpName;

		HashMap<String, ObjectSpawner> sortedSpawners = new HashMap<String, ObjectSpawner>();

		Html html = new Html();
		Head head = new Head();

		html.appendChild(head);

		Title title = new Title();
		title.appendChild(new Text(mapname));
		head.appendChild(title);

		Body body = new Body();

		Table table = new Table();
		Tr tr = new Tr();
		Td td = new Td();

		H1 h1 = new H1();
		h1.appendChild(new Text(mapname));
		body.appendChild(h1);
		H2 h2 = new H2();
		h2.appendChild(new Text("Teams"));
		body.appendChild(h2);

		// Teams
		table = new Table();

		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Team:"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(team1));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(" vs "));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(team2));

		// Tickets
		tr = new Tr();
		table.appendChild(tr);

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text("Tickets:"));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(Integer.parseUnsignedInt(tickets1) * 2));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(" vs "));

		td = new Td();
		tr.appendChild(td);
		td.appendChild(new Text(Integer.parseUnsignedInt(tickets2) * 2));

		// Kits
		Iterator<String> it_kits1 = kits_team1.iterator();
		Iterator<String> it_kits2 = kits_team2.iterator();
		while (it_kits1.hasNext() && it_kits2.hasNext()) {

			tr = new Tr();
			table.appendChild(tr);

			td = new Td();
			tr.appendChild(td);
			td.appendChild(new Text("Slot " + counter + ": "));

			td = new Td();
			tr.appendChild(td);
			td.appendChild(new Text(getKit(it_kits1.next())));

			td = new Td();
			tr.appendChild(td);
			td.appendChild(new Text(" vs "));

			td = new Td();
			tr.appendChild(td);
			td.appendChild(new Text(getKit(it_kits2.next())));
			counter++;
		}

		body.appendChild(table);

		// Flags
		h2 = new H2();
		h2.appendChild(new Text("Flags"));
		body.appendChild(h2);
		table = new Table();
		ArrayList<String> columns = new ArrayList<>();
		Iterator<ControlPoint> cpit = controlPointsObjects.values().iterator();

		H4 h4;
		body.appendChild(table);
		while (cpit.hasNext()) {
			table = new Table();
			cp = cpit.next();
			sortedSpawners.clear();
			h2 = new H2();
			h2.appendChild(new Text(getLocalizedFlagName(cp.getName()) + " ("
					+ cp.getId() + ")"));
			body.appendChild(h2);

			if (cp.getTeam() != null) {
				columns.add("Team: ");
				columns.add(cp.getTeam());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}

			if (cp.getRadius() != null) {
				columns.add("Radius: ");
				columns.add(cp.getRadius());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}

			if (cp.getAreaValueTeam1() != null) {
				columns.add("AreaValue1: ");
				columns.add(cp.getAreaValueTeam1());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}

			if (cp.getAreaValueTeam2() != null) {
				columns.add("AreaValue2: ");
				columns.add(cp.getAreaValueTeam2());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}
			if (cp.getShowOnMinimap() != null) {
				columns.add("Show on Minimap: ");
				columns.add(cp.getShowOnMinimap());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}

			if (cp.getTimeToCapture() != null) {
				columns.add("Time to Capture: ");
				columns.add(cp.getTimeToCapture());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}
			if (cp.getTimeToLoose() != null) {
				columns.add("Time to Loose: ");
				columns.add(cp.getTimeToLoose());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}
			if (cp.getIsUncappable() != null) {
				columns.add("Uncappable: ");
				columns.add(cp.getIsUncappable());
				table.appendChild(createRow(columns));
				columns.removeAll(columns);
			}
			body.appendChild(table);
			h4 = new H4();
			h4.appendChild(new Text("Tanks and Planes"));
			body.appendChild(h4);
			processObjectSpawners(body, Fh2SpawnerType.TANKS_AND_PLANES, cp,
					true, true);
			h4 = new H4();
			h4.appendChild(new Text("Transport, Artillery, AA, AT"));
			body.appendChild(h4);
			processObjectSpawners(body,
					Fh2SpawnerType.TRANSPORT_AT_AA_ARTILLERY, cp, true, true);
			h4 = new H4();
			h4.appendChild(new Text("Pickup Kits"));
			body.appendChild(h4);
			processObjectSpawners(body, Fh2SpawnerType.PICKUP_KITS, cp, false,
					false);

		}
		// body.appendChild(table);
		// Object Spawner

		table = new Table();

		// body.appendChild(table);
		html.appendChild(body);

		try {
			File output = new File("" + mapname + ".html");
			PrintWriter out = new PrintWriter(new FileOutputStream(output));
			out.println(html.write());
			//System.out.println(html.write());
			out.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();

		}
		//System.out.println(html.write());

	}

	private Tr createRow(ArrayList<String> cols) {
		Tr tr = new Tr();
		Td td;
		int i = 0;
		while (i < cols.size()) {
			td = new Td();
			tr.appendChild(td);
			td.appendChild(new Text(cols.get(i)));
			i++;
		}
		return tr;
	}

	private HashMap<String, GenericType> fillTypeMap(String source) {
		Collection<String> types = fileReader.getFile(source);
		String template, type;
		StringTokenizer tok;

		HashMap<String, GenericType> map = new HashMap<String, GenericType>();
		Iterator<String> it = types.iterator();
		while (it.hasNext()) {
			tok = new StringTokenizer(it.next(), ":");
			while (tok.hasMoreTokens()) {
				template = tok.nextToken();
				type = tok.nextToken();
				if (WeaponTypes.contains(type.trim()))
					map.put(template, WeaponTypes.valueOf(type));
				if (KitTypes.contains(type.trim()))
					map.put(template, KitTypes.valueOf(type));
				if (VehicleTypes.contains(type.trim()))
					map.put(template, VehicleTypes.valueOf(type));
			}
		}
		return map;
	}



	private String findValueInCollection(String value, Collection<String> col) {
		boolean found = false;
		String line, ret;
		ret = null;
		if (getInitLines() != null) {
			Iterator<String> it = getInitLines().iterator();
			while (it.hasNext() && !found) {
				line = it.next();
				if (line.indexOf(value) != -1) {
					found = true;
					ret = line;
				}
			}
		}
		return ret;
	}
	
	public String getBasePath() {
		return basePath;
	}

	public HashMap<String, String> getFlagNames() {
		return flagNames;
	}

	public Collection<String> getGamePlayObjects() {
		return gamePlayObjects;
	}

	public Collection<String> getInitLines() {
		return initLines;
	}

	private String getKit(String kit){
		
		if (kitLimit.containsKey(kit)) {
			return kit + " limited to " + kitLimit.get(kit).toString();
		}
		else
			return kit;
	}

	private String getKitFromLimitKitMapdata(String line){
		String kit = new String();
		int start, end;
		start = line.indexOf("'")+1;
		end = line.lastIndexOf("'");					
		kit = line.substring(start,  end );
		return kit;
	}

	private String getKitNameFromLine(String line) {
		String kit = "";
		int start = line.indexOf("\"") + 1;
		while (!line.substring(start, start + 1).equals("\"")) {
			kit = kit + line.substring(start, start + 1);
			start++;
		}
		return kit;
	}

	private Collection<String> getKits(String team) {
		ArrayList<String> kits = new ArrayList<>();

		kits.add(getKitNameFromLine(findValueInCollection(FhtConstants.kit
				+ " " + team + " 0", getInitLines())));
		kits.add(getKitNameFromLine(findValueInCollection(FhtConstants.kit
				+ " " + team + " 1", getInitLines())));
		kits.add(getKitNameFromLine(findValueInCollection(FhtConstants.kit
				+ " " + team + " 2", getInitLines())));
		kits.add(getKitNameFromLine(findValueInCollection(FhtConstants.kit
				+ " " + team + " 3", getInitLines())));
		kits.add(getKitNameFromLine(findValueInCollection(FhtConstants.kit
				+ " " + team + " 4", getInitLines())));
		kits.add(getKitNameFromLine(findValueInCollection(FhtConstants.kit
				+ " " + team + " 5", getInitLines())));
		kits.add(getKitNameFromLine(findValueInCollection(FhtConstants.kit
				+ " " + team + " 6", getInitLines())));
		return kits;
	}

	public HashMap<String, GenericType> getKitTypes() {
		return kitTypes;
	}

	private Float getLimitfromLimitKitMapdata(String line){
		int start, end;
		String strLimit;
		start = line.lastIndexOf("=") + 1;
		end = line.lastIndexOf(")");					
		strLimit = line.substring(start,  end );		
		return new Float(strLimit.trim());
	}

	private Div getLinkToTemplateImage(ObjectSpawner spawner, String team) {
		String fh2imagename;
		Div div = new Div();
		div.setId("mydiv").setCSSClass("myclass");

		A link = new A();

		div.appendChild(link);
		switch (team) {
		case "1":
			fh2imagename = spawner.getFh2ImageName1();
			break;
		case "2":
			fh2imagename = spawner.getFh2ImageName2();
			break;

		default:
			fh2imagename = spawner.getFh2ImageName1();
			break;
		}
		if (fh2imagename == null)
			return null;
		link.setHref(
				FhtConstants.fh2VehicleImageLinkPrefix + fh2imagename + "/"
						+ FhtConstants.bigjpg).setTarget("_blank");

		Img image = new Img("some alt", FhtConstants.fh2VehicleImageLinkPrefix
				+ fh2imagename + "/" + FhtConstants.smallgif);
		image.setCSSClass("frame").setId("myimageid");
		link.appendChild(image);

		return div;
	}

	private String getLocalizedFlagName(String flag) {
		if (getFlagNames().containsKey(flag.trim()))
			return getFlagNames().get(flag.trim());
		else
			return flag.trim();
	}

	private String getMapName(String basePath, String mapname) {
		Collection<String> col;
		String line, name;
		boolean found = false;
		name = mapname;
		col = fileReader.getFh2File(basePath + "//info//" + mapname + ".desc");
		if (col != null) {
			Iterator<String> it = col.iterator();
			while (it.hasNext() && !found) {
				line = it.next();
				if (line.indexOf(FhtConstants.name_tag_in_desc) != -1) {
					found = true;
					name = line.substring(
							FhtConstants.name_tag_in_desc.length() + 1,
							line.indexOf(FhtConstants.name_tag_close_in_desc));
				}
			}
		}
		return name;
	}

	private String getNumberOfTicketsFromLine(String line) {
		return line.substring(line.lastIndexOf(" ") + 1, line.length());
	}

	private String getTeam1() {
		String line = findValueInCollection(FhtConstants.team_1, getInitLines());
		return line.substring(line.length() - 4, line.length());
	}

	private String getTeam2() {
		String line = findValueInCollection(FhtConstants.team_2, getInitLines());
		return line.substring(line.length() - 4, line.length());
	}

	private String getTeamTemplateName(ObjectSpawner spawner, String team) {
		switch (team) {
		case "1":

			if (getVehicles().get(spawner.getTemplate1()) != null)
				return getVehicles().get(spawner.getTemplate1())
						.getDisplayName();
			else
				return spawner.getTemplate1();
		case "2":
			if (getVehicles().get(spawner.getTemplate2()) != null)
				return getVehicles().get(spawner.getTemplate2())
						.getDisplayName();
			else
				return spawner.getTemplate2();
		default:
			return "no team given for " + spawner.getName();
		}
	}

	private String getTemplateName(ObjectSpawner spawner, String team) {
		String ret = new String();
		//System.out.println(team);
		switch (team) {
		case "1":
			return getTeamTemplateName(spawner, team);
		case "2":
			return getTeamTemplateName(spawner, team);
		default:
			if (spawner.getTemplate1() != null) {
				ret = getTeamTemplateName(spawner, "1");
			}
			if (spawner.getTemplate2() != null) {
				if (spawner.getTemplate1() != null) {
					ret = ret + "/";
				}
				ret = ret + getTeamTemplateName(spawner, "2");
			}
			// if (spawner.getTemplate1() != null)
			// if (spawner.getTemplate1().startsWith("kubelwagen"))
			// return ret + getLinkToTemplateImage(spawner.getTemplate1());
			// else
			// return ret;
			// else
			return ret;

		}

	}

	private String getTicketTeam1() {
		return getNumberOfTicketsFromLine(findValueInCollection(
				FhtConstants.numberOfTickets64 + " 1", getInitLines()));
	}

	private String getTicketTeam2() {
		return getNumberOfTicketsFromLine(findValueInCollection(
				FhtConstants.numberOfTickets64 + " 2", getInitLines()));
	}

	public HashMap<String, FH2Object> getVehicles() {
		return vehicles;
	}

	public HashMap<String, GenericType> getVehicleTypes() {
		return vehicleTypes;
	}

	public HashMap<String, GenericType> getWeaponTypes() {
		return weaponTypes;
	}

	private void populateCPs() {
		Iterator<String> it_gpo = getGamePlayObjects().iterator();
		controlPointsObjects = new HashMap<String, ControlPoint>();
		String line;
		String cpName = "";
		String cpID = "";
		ControlPoint cp = new ControlPoint();
		// Get all the ControlPoints
		while (it_gpo.hasNext()) {
			line = it_gpo.next();
			if (line.startsWith(FhtConstants.createControlPoint)) {
				if (cp.getId() != null) {
					controlPointsObjects.put(cpID, cp);
					cp = new ControlPoint();
				}

				// This is a control point. Find out its ID and name and store
				// it in a hashmap
				cp = new ControlPoint();
				cpName = line.substring(line.trim().lastIndexOf(" ") + 1);
				cp.setName(cpName);
			}
			if (line.startsWith(FhtConstants.controlPointID)) {
				cpID = line.substring(line.trim().lastIndexOf(" ") + 1);
				cp.setId(cpID);
			}
			if (line.startsWith(FhtConstants.cpRadius)) {
				cp.setRadius(line.substring(line.trim().lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpIsUnstrategicControlPoint)) {
				cp.setIsUnstrategicCP(line.substring(line.trim().lastIndexOf(
						" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpShowOnMinimap)) {
				cp.setShowOnMinimap(line
						.substring(line.trim().lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpAreaValueTeam1)) {
				cp.setAreaValueTeam1(line.substring(line.trim()
						.lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpAreaValueTeam2)) {
				cp.setAreaValueTeam2(line.substring(line.trim()
						.lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpTeam)) {
				cp.setTeam(line.substring(line.trim().lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpTimeToGetControl)) {
				cp.setTimeToCapture(line
						.substring(line.trim().lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpTimeToLoseControl)) {
				cp.setTimeToLoose(line
						.substring(line.trim().lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.cpUnableToChangeTeam)) {
				cp.setIsUncappable(line
						.substring(line.trim().lastIndexOf(" ") + 1));
			}
			if (line.startsWith("if v_arg1 == host") && cp.getId() != null) {
				controlPointsObjects.put(cpID, cp);
				cp = new ControlPoint();
			}
		}
		Iterator<ControlPoint> cpit = controlPointsObjects.values().iterator();
		while (cpit.hasNext()) {
			cp = cpit.next();
			//System.out.println(cp.toString());
			/*
			 * System.out.println("ID:              " + cp.getId());
			 * System.out.println("Name:            " + cp.getName());
			 * System.out.println("Team:            " + cp.getTeam());
			 * System.out.println("Radius:          " + cp.getRadius());
			 * System.out.println("AreaValue1:      " + cp.getAreaValueTeam1());
			 * System.out.println("AreaValue2:      " + cp.getAreaValueTeam2());
			 * System.out.println("Show on Minimap: " + cp.getShowOnMinimap());
			 * System.out.println("Is Unstrategic:  " +
			 * cp.getIsUnstrategicCP()); System.out.println("Time to Capture: "
			 * + cp.getTimeToCapture()); System.out.println("Time to Loose:   "
			 * + cp.getTimeToLoose()); System.out.println("Uncappable:      " +
			 * cp.getIsUncappable());
			 */
		}
	}

	private void populateObjectsSpawners() {
		ObjectSpawner spawner = new ObjectSpawner();
		String line, oName;
		oName = "";

		Iterator<String> it_gpo = getGamePlayObjects().iterator();
		// Get all the Object Spawners
		while (it_gpo.hasNext()) {

			line = it_gpo.next();
			if (line.startsWith(FhtConstants.objectSpawner)) {

				if (spawner.getName() != null) {
					objectSpawners.put(spawner.getName(), spawner);
					// System.out.println("Added " +spawner.getName() + " " +
					// spawner.getTemplate1() + " "+ spawner.getTemplate2() +
					// " " + spawner.isTankorPlane());
					spawner = new ObjectSpawner();
					spawner.setType(Fh2SpawnerType.TRANSPORT_AT_AA_ARTILLERY);

				}
				spawner.setName(line
						.substring(line.trim().lastIndexOf(" ") + 1));

			}
			if (line.startsWith(FhtConstants.objectTemplate1)) {
				spawner.setTemplate1(line.substring(
						line.trim().lastIndexOf(" ") + 1).toLowerCase());

				if (getVehicleTypes().containsKey(spawner.getTemplate1())) {
					spawner.setVehicleType(VehicleTypes
							.valueOf(getVehicleTypes().get(
									spawner.getTemplate1()).toString()));
					switch (spawner.getVehicleType()) {
					case VEHICLE_TYPE_AIR:
					case VEHICLE_TYPE_ARMOREDCAR:
					case VEHICLE_TYPE_HEAVYARMOR:
					case VEHICLE_TYPE_MEDIUMARMOR:
						spawner.setType(Fh2SpawnerType.TANKS_AND_PLANES);
						break;

					default:
						spawner.setType(Fh2SpawnerType.TRANSPORT_AT_AA_ARTILLERY);
						break;
					}
				}
				if (getWeaponTypes().containsKey(spawner.getTemplate1()))
					spawner.setWeaponType(WeaponTypes.valueOf(getWeaponTypes()
							.get(spawner.getTemplate1()).toString()));
				if (getKitTypes().containsKey(spawner.getTemplate1()))
					spawner.setKitType(KitTypes.valueOf(getKitTypes().get(
							spawner.getTemplate1()).toString()));
				spawner.setHUDName1(getTemplateName(spawner, "1"));
				if (getVehicles().containsKey(spawner.getTemplate1()))
					spawner.setFh2ImageName1(getVehicles().get(
							spawner.getTemplate1()).getFh2ImageName());

			}
			if (line.startsWith(FhtConstants.objectTemplate2)) {
				spawner.setTemplate2(line.substring(
						line.trim().lastIndexOf(" ") + 1).toLowerCase());

				if (getVehicleTypes().containsKey(spawner.getTemplate2())) {
					spawner.setVehicleType(VehicleTypes
							.valueOf(getVehicleTypes().get(
									spawner.getTemplate2()).toString()));
					switch (spawner.getVehicleType()) {
					case VEHICLE_TYPE_AIR:
					case VEHICLE_TYPE_ARMOREDCAR:
					case VEHICLE_TYPE_HEAVYARMOR:
					case VEHICLE_TYPE_MEDIUMARMOR:
						spawner.setType(Fh2SpawnerType.TANKS_AND_PLANES);
						break;

					default:
						spawner.setType(Fh2SpawnerType.TRANSPORT_AT_AA_ARTILLERY);
						break;
					}
				}
				if (getWeaponTypes().containsKey(spawner.getTemplate2()))
					spawner.setWeaponType(WeaponTypes.valueOf(getWeaponTypes()
							.get(spawner.getTemplate2()).toString()));
				if (getKitTypes().containsKey(spawner.getTemplate2()))
					spawner.setKitType(KitTypes.valueOf(getKitTypes().get(
							spawner.getTemplate2()).toString()));
				spawner.setHUDName2(getTemplateName(spawner, "2"));
				if (getVehicles().containsKey(spawner.getTemplate2()))
					spawner.setFh2ImageName2(getVehicles().get(
							spawner.getTemplate2()).getFh2ImageName());
			}
			if (spawner.getKitType() != null)
				spawner.setType(Fh2SpawnerType.PICKUP_KITS);

			if (line.startsWith(FhtConstants.objectMinSpawnDelay)) {
				spawner.setMinSpawnDelay(line.substring(line.trim()
						.lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.objectMaxSpawnDelay)) {
				spawner.setMaxSpawnDelay(line.substring(line.trim()
						.lastIndexOf(" ") + 1));
			}
			if (line.startsWith(FhtConstants.objectTimeToLive)) {
				spawner.setTimeToLive(line.substring(line.trim().lastIndexOf(
						" ") + 1));
			}
			if (line.startsWith(FhtConstants.objectTeamlocked)) {
				spawner.setTeamlocked(line.substring(line.trim().lastIndexOf(
						" ") + 1));
			}
			if (line.startsWith(FhtConstants.objectMaxNrOfObjectSpawned)) {
				spawner.setMaxNrSpawned(line.substring(line.trim().lastIndexOf(
						" ") + 1));
			}
			if (line.startsWith("if v_arg1 == host")
					&& spawner.getName() != null) {

				objectSpawners.put(spawner.getName(), spawner);
				spawner = new ObjectSpawner();
				spawner.setType(Fh2SpawnerType.TRANSPORT_AT_AA_ARTILLERY);
			}

			if (line.trim().startsWith(FhtConstants.objectCreate)) {
				// This is a Object. Find the ControlPoins
				oName = line.trim().substring(line.trim().lastIndexOf(" ") + 1);

			}
			if (line.trim().startsWith(FhtConstants.objectControlPointID)) {
				// cpID = line.trim().substring(line.trim().lastIndexOf(" ") +
				// 1);

				objectSpawners.get(oName)
						.setCpID(
								line.trim().substring(
										line.trim().lastIndexOf(" ") + 1));
			}

		}

	}

	private void processObjectSpawners(Body body, Fh2SpawnerType type,
			ControlPoint cp, boolean createLinks, boolean repeatTemplates) {
		String team, additionalInfo;
		ObjectSpawner spawner;
		Integer count;
		HashMap<String, ObjectSpawner> sortedSpawners = new HashMap<String, ObjectSpawner>();
		HashMap<String, Integer> countSpawnersOfSameTemplate = new HashMap<String, Integer>();
		SortedSet<String> keys;
		// Iterator<ObjectSpawner> it = spawner_list.iterator();
		Iterator<Entry<String, ObjectSpawner>> it = objectSpawners.entrySet()
				.iterator();
		Entry<String, ObjectSpawner> objectEntry;
		Table table = new Table();
		Tr tr;
		Td td;
		team = "";

		sortedSpawners.clear();
		countSpawnersOfSameTemplate.clear();
		while (it.hasNext()) {
			objectEntry = it.next();
			spawner = objectEntry.getValue();

			if (spawner.getCpID().equals(cp.getId())
					&& spawner.getType().equals(type)) {
				if (countSpawnersOfSameTemplate.containsKey(spawner
						.getTemplate1() + spawner.getTemplate2())) {
					count = countSpawnersOfSameTemplate.get(spawner
							.getTemplate1() + spawner.getTemplate2());
					count = new Integer(count.intValue() + 1);
					countSpawnersOfSameTemplate.put(spawner.getTemplate1()
							+ spawner.getTemplate2(), count);
				} else
					countSpawnersOfSameTemplate.put(spawner.getTemplate1()
							+ spawner.getTemplate2(), new Integer(1));
				sortedSpawners.put(
						spawner.getTemplate1() + spawner.getTemplate2(),
						spawner);
			}
		}
		keys = new TreeSet<String>(sortedSpawners.keySet());
		for (String key : keys) {
			ObjectSpawner sortedSpawner = sortedSpawners.get(key);
			tr = new Tr();
			table.appendChild(tr);
			td = new Td();

			if (cp.getIsUncappable() != null)
				if (cp.getIsUncappable().equals("1") && cp.getTeam() != null)
					team = cp.getTeam();
				else
					team = "";
			else
				team = "";
			td.appendChild(new Text(countSpawnersOfSameTemplate
					.get(sortedSpawner.getTemplate1()
							+ sortedSpawner.getTemplate2()).intValue()
					+ "x " + getTemplateName(sortedSpawner, team)));
			tr.appendChild(td);
			td = new Td();
			Div link;
			if (createLinks) {
				link = getLinkToTemplateImage(sortedSpawner, "1");
				if (link != null) {
					td.appendChild(link);
					tr.appendChild(td);
				}
				link = getLinkToTemplateImage(sortedSpawner, "2");
				if (link != null) {
					td = new Td();
					td.appendChild(link);
					tr.appendChild(td);
				}
			}
			td = new Td();

			additionalInfo = new String("ttl: " + sortedSpawner.getTimeToLive()
					+ ", " + sortedSpawner.getMinSpawnDelay() + "/"
					+ sortedSpawner.getMaxSpawnDelay());
			if (repeatTemplates) {
				switch (team) {
				case "":
					additionalInfo = additionalInfo + " ("
							+ sortedSpawner.getTemplate1() + "/"
							+ sortedSpawner.getTemplate2() + ")";
					break;
				case "1":
					additionalInfo = additionalInfo + " ("
							+ sortedSpawner.getTemplate1() + ")";
					break;
				case "2":
					additionalInfo = additionalInfo + " ("
							+ sortedSpawner.getTemplate2() + ")";
					break;
				default:
					break;
				}
			}

			td.appendChild(new Text(additionalInfo));
			tr.appendChild(td);

		}
		body.appendChild(table);
	}
	
	private void readFiles() {
		// Check the file Init.con
		setInitLines(fileReader.getFh2File(getBasePath() + FhtConstants.init));
		setGamePlayObjects(fileReader.getFh2File(getBasePath()
				+ FhtConstants.gamePlayObjects_64));
		setMapdata(fileReader.getFh2File(getBasePath()
				+ FhtConstants.mapdata));
	}
	
	private void readObjects() {

		setVehicleTypes(fillTypeMap("VehicleTypes.txt"));
		setWeaponTypes(fillTypeMap("WeaponTypes.txt"));
		setKitTypes(fillTypeMap("KitTypes.txt"));
		setFlagNames();
		readVehicleMasterdata();

		Iterator<Entry<String, FH2Object>> ite = getVehicles().entrySet()
				.iterator();
		Entry<String, FH2Object> objectEntry;

		vehicle_names = new HashMap<>();
		while (ite.hasNext()) {
			objectEntry = ite.next();

			vehicle_names.put(objectEntry.getValue().getTemplate(), objectEntry
					.getValue().getDisplayName());
		}
	}
	
	private void readVehicleMasterdata() {
		Collection<String> types = fileReader.getFile("vehicles_with_imagenames.txt");
		String template, hudName, fh2ImageName;
		StringTokenizer tok;
		FH2Object o;
		template = new String();
		hudName = new String();
		fh2ImageName = new String();
		HashMap<String, FH2Object> map = new HashMap<String, FH2Object>();
		Iterator<String> it = types.iterator();
		while (it.hasNext()) {
			o = new FH2Object();
			tok = new StringTokenizer(it.next(), ",");
			while (tok.hasMoreTokens()) {
				template = tok.nextToken();
				hudName = tok.nextToken();
				fh2ImageName = tok.nextToken();
			}
			o.setDisplayName(hudName);
			o.setTemplate(template);
			o.setFh2ImageName(fh2ImageName);
			map.put(template, o);
		}
		setVehicles(map);
	}
	

	public void setBasePath(String basePath) {
		this.basePath = basePath;
	}

	private void setFlagNames() {
		Collection<String> localizations = fileReader.getFile(("fht_maps.txt"));
		Iterator<String> it = localizations.iterator();
		StringTokenizer tok;
		String string;
		ArrayList<String> tokens = new ArrayList<String>();
		setFlagNames(new HashMap<String, String>());
		int count = 0;
		while (it.hasNext()) {
			string = it.next();
			System.out.println("Line: " + string);
			tok = new StringTokenizer(string, ";");
			tokens.clear();
			count = 0;
			while (tok.hasMoreTokens()) {
				tokens.add(tok.nextToken().trim());
				count++;
			}
			if (count == 2) {
				getFlagNames().put(tokens.get(0), tokens.get(1));

			}
		}
	}

	public void setFlagNames(HashMap<String, String> flagNames) {
		this.flagNames = flagNames;
	}

	public void setGamePlayObjects(Collection<String> gamePlayObjects) {
		this.gamePlayObjects = gamePlayObjects;
	}

	public void setInitLines(Collection<String> initLines) {
		this.initLines = initLines;
	}

	public void setKitTypes(HashMap<String, GenericType> kitTypes) {
		this.kitTypes = kitTypes;
	}

	private void setMapdata(Collection<String> mapdata_lines){
		kitLimit = new HashMap<String, Float>();
		Iterator<String> it = mapdata_lines.iterator();
		
		String line = new String();
		while (it.hasNext()){
			line = it.next().trim();
			if (line.contains("plugin(limitKit")){
				kitLimit.put(getKitFromLimitKitMapdata(line), getLimitfromLimitKitMapdata(line));
			}
//			if (line.contains("plugin(spawnerCondition")) {
//				spawnerCondition.put(getSpawnerFromSpawnerCondition(line), getTeamFlagFromSpawnerCondition(line));
//			}
			
		}
	}
	
	private String getSpawnerFromSpawnerCondition(String line){
		String ret = new String();
		return ret;
	}

	private String getTeamFlagFromSpawnerCondition(String line){
		String ret = new String();
		return ret;
	}
	public void setVehicles(HashMap<String, FH2Object> vehicles) {
		this.vehicles = vehicles;
	}

	public void setVehicleTypes(HashMap<String, GenericType> vehicleTypes) {
		this.vehicleTypes = vehicleTypes;
	}

	public void setWeaponTypes(HashMap<String, GenericType> weaponTypes) {
		this.weaponTypes = weaponTypes;
	}
}
