package com.fht.fragalyzer;

import java.time.LocalDateTime;

public class Round extends LogEntry {
private String mapname;
private int roundNumber;
private LocalDateTime datetime;
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
}
