package com.fht.fragalyzer;

public class Position {
	private double x;
	private double y;
	private double z;
	private static final double calculationFactor = 4.096;
	private static final int scale = 2048;
	private static final int mapSizeFactor = 2;

	public double getX() {
		return x;
	}

	public void setX(double x) {
		this.x = x;
	}

	public double getY() {
		return y;
	}

	public void setY(double y) {
		this.y = y;
	}

	public double getZ() {
		return z;
	}

	public void setZ(double z) {
		this.z = z;
	}

	public double getZNormalized() {
		return convertBF2CoordinateToNormal(z);
	}

	public double getXNormalized() {
		return convertBF2CoordinateToNormal(x);
	}
	
	public String getZNormalizedDatapointRep() {
		return Double.toString(round(getZNormalized(), 10));
	}

	public String getXNormalizedDatpointRep() {
		return Double.toString(round(getXNormalized(), 10));
	}
	
	public double getZNormalizedDatapointRounded(int roundtonext) {
		return round(getZNormalized(), roundtonext);
	}

	public double getXNormalizedDatapointRounded(int roundtonext) {
		return round(getXNormalized(), roundtonext);
	}	
	

	private Double convertBF2CoordinateToNormal(double bf2CoordinateValue) {
		double value, scaled_value;
		value = bf2CoordinateValue;

		scaled_value = value + 250;
		
		scaled_value = scaled_value * calculationFactor;
		
		if (scaled_value <0)
			scaled_value = 0;
		if (scaled_value > 2048)
			scaled_value = 2048;
		return new Double(scaled_value);
	}

	private Double convertBF2CoordinateToNormalOne(double bf2CoordinateValue) {
		double value, scaled_value;
		value = bf2CoordinateValue;

		scaled_value = value + 250;
		
		
		scaled_value = value * calculationFactor;
		value = scale + scaled_value;

		return new Double(value / mapSizeFactor);
	}

	public String getDataPointRepresentation() {

		String ret = new String();
		ret = ret + "x : " + Double.toString(round(getXNormalized(), 1)) + ", y : "
				+ Double.toString(round(getZNormalized(), 1));
		return ret;
	}

	double round(double i, int v) {
		return Math.ceil(i / v) * v;
	}

}
