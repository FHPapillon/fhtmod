package com.fht.base;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;

public class FhtFileReader {
	public static Collection<String> getFile(String path) {
		Collection<String> col = new ArrayList<String>();
		String line = null;
		try {
			BufferedReader in = new BufferedReader(new FileReader(path));
			while ((line = in.readLine()) != null) {
				col.add(line);
			}
			in.close();
			return col;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}

	public static Collection<String> getUnicodeFile(String path) {
		Collection<String> col = new ArrayList<String>();
		String line = null;
		try {
			//InputStream inStream = new FileInputStream(path);

			 
			BufferedReader in = new BufferedReader(
			   new InputStreamReader(
	                      new FileInputStream(path), "UTF8"));
			
			while ((line = in.readLine()) != null) {
				col.add(line);
			}
			in.close();
			return col;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}

}
