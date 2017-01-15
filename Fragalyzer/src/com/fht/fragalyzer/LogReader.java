package com.fht.fragalyzer;

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
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;



public class LogReader {
	
	public ArrayList<LogEntry> ret;
	
	public ArrayList<LogEntry> readBattleLogs(String basePath) {
		System.out.println(basePath);
		Path p = Paths.get(basePath);
		ret = new ArrayList<>();
		LogMapper mapper = new LogMapper();
		
		int count = 0;
		FileVisitor<Path> fv = new SimpleFileVisitor<Path>() {
			@Override
			public FileVisitResult visitFile(Path file,
					BasicFileAttributes attrs) throws IOException {
				Scanner scanner;
				int dot = file.toString().lastIndexOf(".");
				LogEntry entry;
				if (file.toString().substring(dot -5, dot).equals(FragalyzerConstants.logfilename)) {
					System.out.println(file);
					//System.out.println();
					String fileName = file.getFileName().toString();
				
					try {
						scanner = new Scanner(file);
					} catch (FileNotFoundException e) {
						return null;
					}
					// now read the file line by line...

					while (scanner.hasNextLine()) {
						String line = scanner.nextLine();						
						//System.out.println(line);
						entry = mapper.createLogEntryFromLogLine(line);
						if (entry != null)
							ret.add(entry);
						
					}
					scanner.close();
					
				}

				return FileVisitResult.CONTINUE;
			}

		};

		try {
			Files.walkFileTree(p, fv);
		} catch (IOException e) {
			e.printStackTrace();
		}
		FileWriter fw = null;
		try {
			 fw = new FileWriter(basePath + "//result.txt");
			Iterator<LogEntry> it = ret.iterator();
			while (it.hasNext()) {

				fw.write(it.next().toString());
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
		
		return ret;
		
	}
}
