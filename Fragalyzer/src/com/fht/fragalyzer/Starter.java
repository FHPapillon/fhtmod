package com.fht.fragalyzer;
public class Starter {

	public static void main(String[] args) {
		LogReader lr = new LogReader();
		
		
		Ranker ranker = new Ranker();
		ranker.rank(lr.readBattleLogs("E://fht//fh2//Campaign_19//Fragalyzer"));

	}

}