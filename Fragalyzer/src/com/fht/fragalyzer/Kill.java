package com.fht.fragalyzer;

import java.time.LocalDateTime;

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
	private KitType victimKitType;
	private VehicleType attackerVehicleType;
	private VehicleType victimVehicleType;
	private String attackerVehicleName;
	private String victimVehicleName;
	private String mapname;
	private int roundNumber;
	private LocalDateTime datetime;
	private KitType attackerKitType;
	

	public String getMapname() {
		return mapname;
	}
	public void setMapname(String mapname) {
		this.mapname = mapname;
	}
	public int getRoundNumber() {
		return roundNumber;
	}
	public void setRoundNumber(int roundNumber) {
		this.roundNumber = roundNumber;
	}
	public LocalDateTime getDatetime() {
		return datetime;
	}
	public void setDatetime(LocalDateTime datetime) {
		this.datetime = datetime;	
	}
	
	public String getAttackerVehicleName() {
		return attackerVehicleName;
	}
	public void setAttackerVehicleName(String attackerVehicleName) {
		this.attackerVehicleName = attackerVehicleName;
	}
	public String getVictimVehicleName() {
		return victimVehicleName;
	}
	public void setVictimVehicleName(String victimVehicleName) {
		this.victimVehicleName = victimVehicleName;
	}


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
		String killtext = new String();
		
		if (isTeamkill())
			killtext =  " teamkilled " ;
		else
			killtext = " killed ";				
		
		killtext = getPlayer() + killtext + getVictim();
		
		switch (getKillType()) {
		
		case SUICIDE:
			ret =  getPlayer() + " suicided";
			break;
		case INF_INF:
			ret = killtext + " with " + getWeaponName(getWeapon()) + " (" + " " + FragalyzerConstants.kitNames.get(getAttackerKitType()) + " vs " +  FragalyzerConstants.kitNames.get(getVictimKitType()) +  ")";
			break;
		case INF_VEHICLE:
			ret = killtext + " with " + getWeaponName(getWeapon()) + " ("  + " " + FragalyzerConstants.kitNames.get(getAttackerKitType()) + " vs " +  getVehicleName(getVictimVehicle()) +  ")";
			
			break;		
		case VEHICLE_INF:
			ret = killtext + " with " + getVehicleName(getVehicle())+ " ("  + " " + FragalyzerConstants.vehicleNames.get(getVehicle()) + " vs " +  FragalyzerConstants.kitNames.get(getVictimKitType()) +  ")";
			
			break;	
		case VEHICLE_VEHICLE:
			ret = killtext + " with " + getVehicleName(getVehicle())+ " (" + " " + FragalyzerConstants.vehicleNames.get(getVehicle()) + " vs " +  FragalyzerConstants.vehicleNames.get(getVictimVehicle()) +  ")";
			
			break;								
		default:
			break;
		}
		
		return ret;
	}
	
	private String getWeaponName(String name){
		if (FragalyzerConstants.weaponNames.containsKey(name))
			return FragalyzerConstants.weaponNames.get(name);
		else
			return name;
	}
			
	
	
	private String getVehicleName(String name){
		if (FragalyzerConstants.vehicleNames.containsKey(name))
			return FragalyzerConstants.vehicleNames.get(name);
		else
			return name;
	}
	
	public boolean isTeamkill() {
		return teamkill;
	}
	public void setTeamkill(boolean teamkill) {
		this.teamkill = teamkill;
	}
}