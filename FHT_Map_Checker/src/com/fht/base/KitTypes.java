package com.fht.base;

public enum KitTypes implements GenericType{
	KIT_TYPE_AT, KIT_TYPE_SMGASSAULT, KIT_TYPE_RIFLEASSAULT, KIT_TYPE_NCO, KIT_TYPE_ENGINEER, KIT_TYPE_PILOT, KIT_TYPE_SAPPER, KIT_TYPE_TANKER, KIT_TYPE_MEDIC, KIT_TYPE_SNIPER, KIT_TYPE_MORTAR, KIT_TYPE_LMG, KIT_TYPE_HMG, KIT_TYPE_SCOUT, KIT_TYPE_MAGIC;
	public static boolean contains(String test) {

	    for (KitTypes c : KitTypes.values()) {
	        if (c.name().equals(test)) {
	            return true;
	        }
	    }

	    return false;
	}
}
