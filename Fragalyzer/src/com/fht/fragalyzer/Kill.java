package com.fht.fragalyzer;

public class Kill extends LogEntry {
	private KillType killType;
	private String victim;
	private String victimVehicle;
	private Position victimPosition;
	private String victimKit;
	private String victimTeam;
	private boolean teamkill;
	public String getVictim() {
		return victim;
	}
	public void setVictim(String victim) {
		this.victim = victim;
	}
	public String getVictimVehicle() {
		return victimVehicle;
	}
	public void setVictimVehicle(String victimVehicle) {
		this.victimVehicle = victimVehicle;
	}
	public Position getVictimPosition() {
		return victimPosition;
	}
	public void setVictimPosition(Position victimPosition) {
		this.victimPosition = victimPosition;
	}
	public String getVictimKit() {
		return victimKit;
	}
	public void setVictimKit(String victimKit) {
		this.victimKit = victimKit;
	}
	public String getVictimTeam() {
		return victimTeam;
	}
	public void setVictimTeam(String victimTeam) {
		this.victimTeam = victimTeam;
	}
	public KillType getKillType() {
		return killType;
	}
	public void setKillType(KillType killType) {
		this.killType = killType;
	}
	
	public String toString() {
		String ret = new String();
		
		switch (getKillType()) {
		case SUICIDE:
			ret = getPlayer() + " killed himself";
			break;
		case INF_INF:
			ret = getPlayer() + ((isTeamkill()) ? " teamkilled "  : " killed ") + getVictim() + " with " + getWeapon();
			break;
		case INF_VEHICLE:
			ret = getPlayer() +  ((isTeamkill()) ? " teamkilled with"  : " killed with")  + getWeapon() + " " + getVictim() + " in his " + getVictimVehicle()  ;
			break;		
		case VEHICLE_INF:
			ret = getPlayer() +  ((isTeamkill()) ? " teamkilled "  : " killed ")  + getVictim() + " with " + getVehicle() + "/" + getWeapon();
			break;	
		case VEHICLE_VEHICLE:
			ret = getPlayer() +  ((isTeamkill()) ? " teamkilled with"  : " killed with ") + getVehicle() + "/" + getWeapon() + getVictim() + " in his " + getVictimVehicle();
			break;								
		default:
			break;
		}

		return ret;
	}
	public boolean isTeamkill() {
		return teamkill;
	}
	public void setTeamkill(boolean teamkill) {
		this.teamkill = teamkill;
	}
}
