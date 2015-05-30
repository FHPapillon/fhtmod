package com.fht.base;





public enum VehicleTypes implements GenericType {
	VEHICLE_TYPE_HEAVYARMOR, VEHICLE_TYPE_MEDIUMARMOR, VEHICLE_TYPE_LIGHTARMOR, VEHICLE_TYPE_AIR, VEHICLE_TYPE_ANTIAIR, VEHICLE_TYPE_RADIO, VEHICLE_TYPE_TRANSPORT, VEHICLE_TYPE_APC, VEHICLE_TYPE_ARMOREDCAR, VEHICLE_TYPE_ARTILLERY, VEHICLE_TYPE_ATGUN, VEHICLE_TYPE_MACHINEGUN, VEHICLE_TYPE_NAVAL, VEHICLE_TYPE_PARACHUTE, VEHICLE_TYPE_SOLDIER, VEHICLE_TYPE_UNUSABLE, VEHICLE_TYPE_BICYCLE;
	public static boolean contains(String test) {

	    for (VehicleTypes c : VehicleTypes.values()) {
	        if (c.name().equals(test)) {
	            return true;
	        }
	    }

	    return false;
	}

}
