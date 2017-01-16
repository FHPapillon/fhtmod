package com.fht.fragalyzer;

import java.util.ArrayList;
import java.util.StringTokenizer;

import com.fht.fragalyzer.types.EventType;
import com.fht.fragalyzer.types.KillType;

public class LogMapper {
	
	public ArrayList<String> missingKits;
	
	public LogEntry createLogEntryFromLogLine(String logLine) {
		String token;
		int tokenCounter = 0;
		boolean relevant = true;
		LogEntry entry = null;
		missingKits = new ArrayList<>();
		StringTokenizer tok = new StringTokenizer(logLine, FragalyzerConstants.logDelimiter);
		while (tok.hasMoreTokens() && relevant) {
			token = tok.nextToken();
			tokenCounter++;

			switch (tokenCounter) {
			case 1:
				if (token.equals(FragalyzerConstants.KILL)) {
					entry = populateLogEntry(logLine, EventType.KILL);
					System.out.println(entry.toString());
					return entry;
				}
				break;

			default:
				break;
			}

		}
		return entry;
	}

	private LogEntry populateLogEntry(String logLine, EventType eventType) {
		String token;
		String logKey;
		String logValue;
		switch (eventType) {
		case KILL:
			Kill kill = new Kill();
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
					kill.setPlayerKit(logValue);
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
					kill.setVictimKit(logValue);
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
	
	private Kill addMetaData(Kill kill){
		switch (kill.getKillType()) {
		case INF_INF:
			if (FragalyzerConstants.kitTypes.containsKey(kill.getPlayerKit()))
				kill.setAttackerKitType(FragalyzerConstants.kitTypes.get(kill.getPlayerKit()));
			else
				missingKits.add(kill.getPlayerKit());
			if (FragalyzerConstants.kitTypes.containsKey(kill.getVictimKit()))
				kill.setVictimKitType(FragalyzerConstants.kitTypes.get(kill.getVictimKit()));
			else
				missingKits.add(kill.getVictimKit());
			break;

		default:
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
	


	private Kill sanitizeKill(Kill kill) {
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
