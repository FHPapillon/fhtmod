package com.fht.fragalyzer;

import java.util.Date;

public abstract class LogEntry {
	private EventType eventType;
    private Position playerPosition;
    private String playerKit;
	private String player;
	private String playerTeam;
	private String vehicle;
	private String weapon;
	private Date timestamp;
	public EventType getEventType() {
		return eventType;
	}
	public void setEventType(EventType eventType) {
		this.eventType = eventType;
	}
	public Position getPlayerPosition() {
		return playerPosition;
	}
	public void setPlayerPosition(Position playerPosition) {
		this.playerPosition = playerPosition;
	}
	public String getPlayerKit() {
		return playerKit;
	}
	public void setPlayerKit(String playerKit) {
		this.playerKit = playerKit;
	}
	public String getPlayer() {
		return player;
	}
	public void setPlayer(String player) {
		this.player = player;
	}
	public String getVehicle() {
		return vehicle;
	}
	public void setVehicle(String vehicle) {
		this.vehicle = vehicle;
	}
	public String getWeapon() {
		return weapon;
	}
	public void setWeapon(String weapon) {
		this.weapon = weapon;
	}
	public Date getTimestamp() {
		return timestamp;
	}
	public void setTimestamp(Date timestamp) {
		this.timestamp = timestamp;
	}
	public String getPlayerTeam() {
		return playerTeam;
	}
	public void setPlayerTeam(String playerTeam) {
		this.playerTeam = playerTeam;
	}
}
