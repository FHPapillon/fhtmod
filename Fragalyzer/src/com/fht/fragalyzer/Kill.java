package com.fht.fragalyzer;

import com.fht.fragalyzer.types.KillType;
import com.fht.fragalyzer.types.KitType;
import com.fht.fragalyzer.types.VehicleType;
import com.fht.fragalyzer.types.WeaponType;

public class Kill extends LogEntry {
	private KillType killType;
	private String victim;
	private String victimVehicle;
	private Position victimPosition;
	private String victimKit;
	private String victimTeam;
	private boolean teamkill;
	private WeaponType attackerWeaponType;
	private WeaponType victimWeaponType;
	private KitType attackerKitType;
	public WeaponType getAttackerWeaponType() {
		return attackerWeaponType;
	}
	public void setAttackerWeaponType(WeaponType attackerWeaponType) {
		this.attackerWeaponType = attackerWeaponType;
	}
	public WeaponType getVictimWeaponType() {
		return victimWeaponType;
	}
	public void setVictimWeaponType(WeaponType victimWeaponType) {
		this.victimWeaponType = victimWeaponType;
	}
	public KitType getAttackerKitType() {
		return attackerKitType;
	}
	public void setAttackerKitType(KitType attackerKitType) {
		this.attackerKitType = attackerKitType;
	}
	public KitType getVictimKitType() {
		return victimKitType;
	}
	public void setVictimKitType(KitType victimKitType) {
		this.victimKitType = victimKitType;
	}
	public VehicleType getAttackerVehicleType() {
		return attackerVehicleType;
	}
	public void setAttackerVehicleType(VehicleType attackerVehicleType) {
		this.attackerVehicleType = attackerVehicleType;
	}
	public VehicleType getVictimVehicleType() {
		return victimVehicleType;
	}
	public void setVictimVehicleType(VehicleType victimVehicleType) {
		this.victimVehicleType = victimVehicleType;
	}
	private KitType victimKitType;
	private VehicleType attackerVehicleType;
	private VehicleType victimVehicleType;
	
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
			ret = getPlayer() + " suicided";
			break;
		case INF_INF:
			ret = getPlayer() + ((isTeamkill()) ? " teamkilled "  : " killed ") + getVictim() + " with " + getWeapon() + ": " + FragalyzerConstants.kitNames.get(getAttackerKitType()) + " vs " + FragalyzerConstants.kitNames.get(getVictimKitType());
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