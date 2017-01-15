package com.fht.base;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;

public class ObjectCrawler {
	FileWriter fw;
	ArrayList<String> temp_list;
	ArrayList<String> kits;
	ArrayList<String> vehiclesNonTeamlock;
	ArrayList<String> vehiclesWithTeamlock;
	ArrayList<String> allVehicles;	
	String suffix;

	public ObjectCrawler() {
		kits = new ArrayList<>();
		temp_list = new ArrayList<>();
		vehiclesNonTeamlock = new ArrayList<>();
		vehiclesWithTeamlock = new ArrayList<>();
		allVehicles = new ArrayList<>();
	}
	
	public void getGPODump(String basePath) {
		
	}

	public HashMap<String, String> getObjects(String basePath) {
		// Kits
		suffix = "inc";
		dumpAvailableObjects(basePath + "Kits//");
		try {
			fw = new FileWriter("h://newkits.txt");
			Iterator<String> it = kits.iterator();
			while (it.hasNext()) {

				fw.write(it.next());
				fw.append(System.getProperty("line.separator")); // e.g. "\n"

			}
		} catch (IOException e) {
			System.err.println("Konnte Datei nicht erstellen");
		} finally {
			if (fw != null)
				try {
					fw.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
		}
		


		// Vehicles

		suffix = "con";
		dumpAvailableObjects(basePath + "Vehicles//");

		try {
			fw = new FileWriter("h://newvehicles.txt");
			Iterator<String> it = temp_list.iterator();
			while (it.hasNext()) {

				fw.write(it.next());
				fw.append(System.getProperty("line.separator")); // e.g. "\n"

			}
		} catch (IOException e) {
			System.err.println("Konnte Datei nicht erstellen");
		} finally {
			if (fw != null)
				try {
					fw.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
		}

		return null;
	}
	
	private void walkOverGPOs(String basePath) {
		Path p = Paths.get(basePath);
		
		FileVisitor<Path> fv = new SimpleFileVisitor<Path>() {
			@Override
			public FileVisitResult visitFile(Path file,
					BasicFileAttributes attrs) throws IOException {
				
				
				if (file.getFileName().toString().equals(FhtConstants.gpo_name)) {
					System.out.println(file);
					//System.out.println();
					String fileName = file.getFileName().toString();
					switch (suffix) {
					case "con":
						String realName = getObjectNameFromTweak(
								file.getParent(), file.getFileName());
						System.out.println(realName);
						boolean teamlock = getTeamlockInfo(file.getParent(), file.getFileName());
						if (realName != null)
							temp_list.add(fileName.substring(0, fileName.lastIndexOf(".")) + ", "
									+ realName + ", " + teamlock);
						break;
					case "inc":
						temp_list.add(file.getParent().getFileName() + ", "
								+ file.getFileName().toString());

					default:
						break;
					}

				}

				return FileVisitResult.CONTINUE;
			}

		};

		try {
			Files.walkFileTree(p, fv);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}	

	private void dumpAvailableObjects(String basePath) {
		Path p = Paths.get(basePath);
		
		FileVisitor<Path> fv = new SimpleFileVisitor<Path>() {
			@Override
			public FileVisitResult visitFile(Path file,
					BasicFileAttributes attrs) throws IOException {
				
				int dot = file.toString().lastIndexOf(".");
				if (file.toString().substring(dot + 1).equals(suffix)) {
					System.out.println(file);
					//System.out.println();
					String fileName = file.getFileName().toString();
					switch (suffix) {
					case "con":
						String realName = getObjectNameFromTweak(
								file.getParent(), file.getFileName());
						System.out.println(realName);
						boolean teamlock = getTeamlockInfo(file.getParent(), file.getFileName());
						if (realName != null)
							temp_list.add(fileName.substring(0, fileName.lastIndexOf(".")) + ", "
									+ realName + ", " + teamlock);
						break;
					case "inc":
						temp_list.add(file.getParent().getFileName() + ", "
								+ file.getFileName().toString());

					default:
						break;
					}

				}

				return FileVisitResult.CONTINUE;
			}

		};

		try {
			Files.walkFileTree(p, fv);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	private String getObjectNameFromTweak(Path parent, Path path) {
		String name = parent.toString()
				+ "\\"
				+ path.toString()
						.substring(0, path.toString().lastIndexOf("."));
		File file = new File(name + ".tweak");
		String realName = null;
		Scanner scanner;
		boolean found = false;
		try {
			scanner = new Scanner(file);
		} catch (FileNotFoundException e) {
			return realName;
		}
		// now read the file line by line...

		while (scanner.hasNextLine() && !found) {
			String line = scanner.nextLine();

			if (line.contains("ObjectTemplate.vehicleHud.hudName")) {

				realName = line.substring(line.indexOf("\"")+1,
						line.lastIndexOf("\""));
				found = true;
			}
		}
		scanner.close();
		return realName;
	}
	

	private String getObjectNameFromLocalization(Path parent, Path path) {
		String name = parent.toString()
				+ "\\"
				+ path.toString()
						.substring(0, path.toString().lastIndexOf("."));
		File file = new File(name + ".tweak");
		String realName = null;
		Scanner scanner;
		try {
			scanner = new Scanner(file);
		} catch (FileNotFoundException e) {
			return realName;
		}
		// now read the file line by line...

		while (scanner.hasNextLine()) {
			String line = scanner.nextLine();

			if (line.contains("ObjectTemplate.vehicleHud.hudName")) {

				realName = line.substring(line.indexOf("\"")+1,
						line.lastIndexOf("\""));

			}
		}
		scanner.close();
		return realName;
	}
	
	private boolean getTeamlockInfo(Path parent, Path path) {
		String name = parent.toString()
				+ "\\"
				+ path.toString()
						.substring(0, path.toString().lastIndexOf("."));
		File file = new File(name + ".tweak");
		String realName = null;
		Scanner scanner;
		try {
			scanner = new Scanner(file);
		} catch (FileNotFoundException e) {
			return false;
		}
		// now read the file line by line...

		while (scanner.hasNextLine()) {
			String line = scanner.nextLine();

			if (line.contains("ObjectTemplate.dontClearTeamOnExit 1")) {

				return true;

			}
		}
		scanner.close();
		return false;
	}	
}
