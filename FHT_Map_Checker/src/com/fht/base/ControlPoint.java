package com.fht.base;

public class ControlPoint {
private String id;
private String name;

private String timeToLoose;

private String timeToCapture;

private String showOnMinimap;
private String areaValue;
private String isUnstrategicCP;
private String team;
private String radius;
private String areaValueTeam1;
private String areaValueTeam2;
private String isUncappable;
public String getIsUncappable() {
	return isUncappable;
}
public void setIsUncappable(String isUncappable) {
	this.isUncappable = isUncappable;
}
public ControlPoint() {
	super();

	
}
public ControlPoint(String id) {
	super();
	this.id = id;
	
}
public ControlPoint(String id, String name, String timeToLoose,
		String timeToCapture, String showOnMinimap, String areaValue,
		String isUnstrategicCP) {
	super();
	this.id = id;
	this.name = name;
	this.timeToLoose = timeToLoose;
	this.timeToCapture = timeToCapture;
	this.showOnMinimap = showOnMinimap;
	this.areaValue = areaValue;
	this.isUnstrategicCP = isUnstrategicCP;

}
public String getAreaValue() {
	return areaValue;
}
public String getAreaValueTeam1() {
	return areaValueTeam1;
}
public String getAreaValueTeam2() {
	return areaValueTeam2;
}
public String getId() {
	return id;
}
public String getIsUnstrategicCP() {
	return isUnstrategicCP;
}
public String getName() {
	return name;
}
public String getRadius() {
	return radius;
}
public String getShowOnMinimap() {
	return showOnMinimap;
}
public String getTeam() {
	return team;
}
public String getTimeToCapture() {
	return timeToCapture;
}
public String getTimeToLoose() {
	return timeToLoose;
}
public void setAreaValue(String areaValue) {
	this.areaValue = areaValue;
}
public void setAreaValueTeam1(String areaValueTeam1) {
	this.areaValueTeam1 = areaValueTeam1;
}
public void setAreaValueTeam2(String areaValueTeam2) {
	this.areaValueTeam2 = areaValueTeam2;
}
public void setId(String id) {
	this.id = id;
}

public void setIsUnstrategicCP(String isUnstrategicCP) {
	this.isUnstrategicCP = isUnstrategicCP;
}

public void setName(String name) {
	this.name = name;
}

public void setRadius(String radius) {
	this.radius = radius;
}

public void setShowOnMinimap(String showOnMinimap) {
	this.showOnMinimap = showOnMinimap;
}

public void setTeam(String team) {
	this.team = team;
}

public void setTimeToCapture(String timeToCapture) {
	this.timeToCapture = timeToCapture;
}

public void setTimeToLoose(String timeToLoose) {
	this.timeToLoose = timeToLoose;
}

public String toString() {
	String ret = new String();
	ret = ret + "Name:             " + getName() + "\nTeam:             " + team;
	if (getRadius()!=null)
		ret = ret + "\nRadius:           " + getRadius();
	if (getAreaValueTeam1()!=null)
		ret = ret + "\nAreaValue1:       " + getAreaValueTeam1();	
	if (getAreaValueTeam2()!=null)
		ret = ret + "\nAreaValue2:       " + getAreaValueTeam2();		
	if (getTimeToCapture()!=null)
		ret = ret + "\nTimeToCapture:    " + getTimeToCapture();	
	if (getTimeToLoose()!=null)
		ret = ret + " TimeToLoose: " + getTimeToLoose();			
	if (getShowOnMinimap()!=null)		
		ret = ret + "\ngetShowOnMinimap: " + getShowOnMinimap();	
	if (getIsUnstrategicCP()!=null)
		ret = ret + "\nIsUnstrategicCP:  " + getIsUnstrategicCP();		
	if (getIsUncappable()!=null)
		ret = ret + "\nIsUncappable:     " + getIsUncappable();		
	return ret + "\n";
}
}
