package com.fht.fragalyzer;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Locale;
import java.util.StringTokenizer;

import com.fht.fragalyzer.types.EventType;
import com.fht.fragalyzer.types.KillType;

public class LogMapper {

	public LogMapper() {
		super();
		
	}

	public HashMap<String, String> missingKits;
	private int roundCount;
	private String mapname;
	private LocalDateTime datetime;
	private HashMap<String, EventType> rounds;

	public LogEntry createLogEntryFromLogLine(HashMap<String, String> in_missingKits, String logLine) {
		String token;
		int tokenCounter = 0;
		boolean relevant = true;
		LogEntry entry = null;
		String prevLogLine;
		
		
		missingKits = in_missingKits;
		StringTokenizer tok = new StringTokenizer(logLine, FragalyzerConstants.logDelimiter);
		while (tok.hasMoreTokens() && relevant) {
			token = tok.nextToken();
			tokenCounter++;
			prevLogLine = logLine;
			switch (tokenCounter) {
			case 1:
				if (token.equals(FragalyzerConstants.KILL)) {

					entry = getKillDataFromLog(logLine, EventType.KILL);
					
					entry.setMapname(mapname);
					entry.setRoundNumber(roundCount);
					
					// System.out.println(entry.toString());
				}

				if (token.startsWith(FragalyzerConstants.INIT)) 
					entry = getRoundDataFromLog(logLine, EventType.INIT);
					// System.out.println(entry.toString());
				
				break;
			default:
				break;
			}

		}
		return entry;
	}

	private LogEntry getRoundDataFromLog(String logLine, EventType eventType) {
		LogEntry round = new LogEntry();
		round.setEventType(EventType.INIT);
		String token;
		String logKey;
		String logValue;
		StringTokenizer tok = new StringTokenizer(logLine, FragalyzerConstants.logDelimiter);
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern ( "yyyy.MM.dd,HH:mm" , Locale.GERMANY );
		
		while (tok.hasMoreTokens()) {
			token = tok.nextToken();
			StringTokenizer tokenTokenizer = new StringTokenizer(token, FragalyzerConstants.tokenDelimiter);
			// System.out.println(token);

			logKey = tokenTokenizer.nextToken();
			logValue = tokenTokenizer.nextToken();

			switch (logKey) {

			case (FragalyzerConstants.LevelName):
				round.setMapname(logValue);
				
				break;
			case (FragalyzerConstants.StartDate):
				LocalDateTime ldt = null;
				try {
					
					ldt = LocalDateTime.parse(logValue, formatter);
					
				} catch (Exception e) {
					
				}
				round.setDatetime(ldt);
				break;
			default:
				break;
			}
			
		}
		if (round.getMapname().equals(mapname)) {
			if (!(round.getDatetime().equals(datetime)))
				roundCount++;
		}
		else
		{
			mapname = round.getMapname();
			datetime = round.getDatetime();
			roundCount = 1;
		}
		round.setRoundNumber(roundCount);
		return round;
	}

	private LogEntry getKillDataFromLog(String logLine, EventType eventType) {
		String token;
		String logKey;
		String logValue;
		switch (eventType) {
		case KILL:
			LogEntry kill = new LogEntry();
			kill.setEventType(EventType.KILL);
			// System.out.println(logLine);
			StringTokenizer tok = new StringTokenizer(logLine, FragalyzerConstants.logDelimiter);
			// System.out.println("KILL");
			// Filter out first eventtype Token
			token = tok.nextToken();
			while (tok.hasMoreTokens()) {
				token = tok.nextToken();
				StringTokenizer tokenTokenizer = new StringTokenizer(token, FragalyzerConstants.tokenDelimiter);
				// System.out.println(token);

				logKey = tokenTokenizer.nextToken();
				logValue = tokenTokenizer.nextToken();

				switch (logKey) {

				case (FragalyzerConstants.AttackerName):
					kill.setPlayer(logValue);
					break;
				case (FragalyzerConstants.AttackerKit):
					kill.setPlayerKit(logValue.toLowerCase());
					break;
				case (FragalyzerConstants.AttackerTeam):
					kill.setPlayerTeam(logValue);
					break;
				case (FragalyzerConstants.AttackerVehicle):
					kill.setVehicle(logValue);
					break;
				case (FragalyzerConstants.AttackerWeapon):
					kill.setWeapon(logValue);
					break;
				case (FragalyzerConstants.VictimKit):
					kill.setVictimKit(logValue.toLowerCase());
					break;
				case (FragalyzerConstants.VictimName):
					kill.setVictim(logValue);
					break;
				case (FragalyzerConstants.VictimTeam):
					kill.setVictimTeam(logValue);
					break;
				case (FragalyzerConstants.VictimVehicle):
					kill.setVictimVehicle(logValue);
					break;
				case (FragalyzerConstants.AttackerPos):
					kill.setPlayerPosition(getPositionFromLog(logValue));
					break;
				case (FragalyzerConstants.VictimPos):
					kill.setVictimPosition(getPositionFromLog(logValue));
					break;
				default:
					break;
				}
			}
			kill = sanitizeKill(kill);
			kill = addMetaData(kill);
			return sanitizeKill(kill);

		default:
			break;
		}
		return null;
	}

	private LogEntry addMetaData(LogEntry kill) {
		switch (kill.getKillType()) {

		case VEHICLE_INF:
		case INF_VEHICLE:
		case VEHICLE_VEHICLE:
		case INF_INF:
			if (FragalyzerConstants.kitTypes.containsKey(kill.getPlayerKit()))
				kill.setAttackerKitType(FragalyzerConstants.kitTypes.get(kill.getPlayerKit()));
			else
				missingKits.put("k: " + kill.getPlayerKit(), "");
			if (FragalyzerConstants.kitTypes.containsKey(kill.getVictimKit()))
				kill.setVictimKitType(FragalyzerConstants.kitTypes.get(kill.getVictimKit()));
			else
				missingKits.put("v: " + kill.getVictimKit(), "");
			if (FragalyzerConstants.vehicleTypes.containsKey(kill.getVehicle()))
				kill.setAttackerVehicleType(FragalyzerConstants.vehicleTypes.get(kill.getVehicle()));
			else
				missingKits.put("v: " + kill.getVehicle(), "");
			if (FragalyzerConstants.vehicleTypes.containsKey(kill.getVictimVehicle()))
				kill.setVictimVehicleType(FragalyzerConstants.vehicleTypes.get(kill.getVictimVehicle()));
			else
				missingKits.put("v: " + kill.getVictimVehicle(), "");
			if (FragalyzerConstants.weaponTypes.containsKey(kill.getWeapon()))
				kill.setAttackerWeaponType(FragalyzerConstants.weaponTypes.get(kill.getWeapon()));
			else
				missingKits.put("w: " + kill.getWeapon(), "");

			if (FragalyzerConstants.vehicleNames.containsKey(kill.getVehicle()))
				kill.setAttackerVehicleName(FragalyzerConstants.vehicleNames.get(kill.getVehicle()));
			else
				missingKits.put("w: " + kill.getVehicle(), "");

			if (FragalyzerConstants.vehicleNames.containsKey(kill.getVictimVehicle()))
				kill.setVictimVehicleName(FragalyzerConstants.vehicleNames.get(kill.getVictimVehicle()));
			else
				missingKits.put("w: " + kill.getVictimVehicle(), "");
			break;

		default:
			/*
			 * if
			 * (FragalyzerConstants.kitTypes.containsKey(kill.getPlayerKit()))
			 * kill.setAttackerKitType(FragalyzerConstants.kitTypes.get(kill.
			 * getPlayerKit())); else missingKits.put(kill.getPlayerKit(), "");
			 * if
			 * (FragalyzerConstants.kitTypes.containsKey(kill.getVictimKit()))
			 * kill.setVictimKitType(FragalyzerConstants.kitTypes.get(kill.
			 * getVictimKit())); else missingKits.put(kill.getVictimKit(), "");
			 * 
			 * if
			 * (FragalyzerConstants.weaponTypes.containsKey(kill.getWeapon()))
			 * kill.setAttackerWeaponType(FragalyzerConstants.weaponTypes.get(
			 * kill.getWeapon())); else missingKits.put(kill.getWeapon(), "");
			 */
			break;
		}
		return kill;
	}



	private Position getPositionFromLog(String logPosition) {
		Position pos = new Position();
		double value;
		StringTokenizer tok = new StringTokenizer(logPosition, ",");
		String token;
		int count = 0;
		while (tok.hasMoreTokens()) {
			token = tok.nextToken();
			count++;
			switch (count) {
			case 1:
				pos.setX(new Double(token).doubleValue());
				break;
			case 2:
				pos.setY(new Double(token).doubleValue());
				break;
			case 3:
				pos.setZ(new Double(token).doubleValue());
				break;
			default:
				break;
			}
		}
		return pos;

	}

	private LogEntry sanitizeKill(LogEntry kill) {
		// Suicide
		if (kill.getPlayer() == null || kill.getPlayer().equals(kill.getVictim())) {
			kill.setKillType(KillType.SUICIDE);
			if (kill.getPlayer() == null)
				kill.setPlayer(kill.getVictim());
			return kill;
		}

		boolean attackerIsInf = false;
		if (kill.getVehicle() != null) {
			String attackerVehicle = kill.getVehicle().toLowerCase().substring(0, 3);
			attackerIsInf = isInfantry(attackerVehicle);
		}
		boolean victimIsInf = false;
		if (kill.getVictimVehicle() != null) {
			String victimVehicle = kill.getVictimVehicle().toLowerCase().substring(0, 3);
			victimIsInf = isInfantry(victimVehicle);
		}

		if (attackerIsInf && victimIsInf)
			kill.setKillType(KillType.INF_INF);

		if (attackerIsInf && !victimIsInf)
			kill.setKillType(KillType.INF_VEHICLE);

		if (!attackerIsInf && victimIsInf)
			kill.setKillType(KillType.VEHICLE_INF);

		if (!attackerIsInf && !victimIsInf)
			kill.setKillType(KillType.VEHICLE_VEHICLE);

		if (kill.getPlayerTeam().equals(kill.getVictimTeam()))
			kill.setTeamkill(true);
		else
			kill.setTeamkill(false);
		return kill;
	}

	private boolean isInfantry(String log) {
		switch (log) {
		case FragalyzerConstants.ba:
		case FragalyzerConstants.bj:
		case FragalyzerConstants.bw:
		case FragalyzerConstants.ch:
		case FragalyzerConstants.cw:
		case FragalyzerConstants.eu:
		case FragalyzerConstants.ga:
		case FragalyzerConstants.gc:
		case FragalyzerConstants.gm:
		case FragalyzerConstants.gs:
		case FragalyzerConstants.gw:
		case FragalyzerConstants.ia:
		case FragalyzerConstants.jp:
		case FragalyzerConstants.re:
		case FragalyzerConstants.se:
		case FragalyzerConstants.ua:
		case FragalyzerConstants.uc:
		case FragalyzerConstants.up:
		case FragalyzerConstants.us:
		case FragalyzerConstants.waw:
		case FragalyzerConstants.uw:
			return true;

		default:
			return false;

		}
	}

}
