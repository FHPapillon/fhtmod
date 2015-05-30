package com.fht.base;

public enum WeaponTypes implements GenericType{
	WEAPON_TYPE_RIFLE, WEAPON_TYPE_GRENADE, WEAPON_TYPE_PISTOL, WEAPON_TYPE_SMG, WEAPON_TYPE_LMG, WEAPON_TYPE_ATMINE, WEAPON_TYPE_APMINE, WEAPON_TYPE_MINEFLAG, WEAPON_TYPE_TARGETING, WEAPON_TYPE_MINEDET, WEAPON_TYPE_GOLD, WEAPON_TYPE_SMOKE, WEAPON_TYPE_ATGUN, WEAPON_TYPE_EXPLOSIVE, WEAPON_TYPE_CLOSE, WEAPON_TYPE_NONLETHAL, WEAPON_TYPE_SNIPER, NUM_WEAPON_TYPES;
	public static boolean contains(String test) {

	    for (WeaponTypes c : WeaponTypes.values()) {
	        if (c.name().equals(test)) {
	            return true;
	        }
	    }

	    return false;
	}
}
