package com.fht.fragalyzer.types;

import java.util.ArrayList;
import java.util.HashMap;

import com.fht.fragalyzer.LogEntry;

public class PlayerStats {
public PlayerStats() {
		super();
		kills = new ArrayList<>();
		flagCaptures = new ArrayList<>();
		// TODO Auto-generated constructor stub
	}
private String playerName;
private ArrayList<LogEntry> kills;
private ArrayList<LogEntry> flagCaptures;
private HashMap<WeaponType, Integer> weaponKills;
public String getPlayerName() {
	return playerName;
}
public void setPlayerName(String playerName) {
	this.playerName = playerName;
}
public ArrayList<LogEntry> getKills() {
	return kills;
}
public void setKills(ArrayList<LogEntry> kills) {
	this.kills = kills;
}
public ArrayList<LogEntry> getFlagCaptures() {
	return flagCaptures;
}
public void setFlagCaptures(ArrayList<LogEntry> flagCaptures) {
	this.flagCaptures = flagCaptures;
}
public HashMap<WeaponType, Integer> getWeaponKills() {
	return weaponKills;
}
public void setWeaponKills(HashMap<WeaponType, Integer> weaponKills) {
	this.weaponKills = weaponKills;
}
}
