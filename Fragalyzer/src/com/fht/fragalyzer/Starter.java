package com.fht.fragalyzer;
public class Starter {

	public static void main(String[] args) {
		LogReader lr = new LogReader();
		
		
		Ranker ranker = new Ranker();
		ranker.rank(lr.readBattleLogs("c://data//Fragalyzer"));

	}

}