package com.example.bfqca_backend.utils.file_utils;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class FileSaver {

    public static void savefile(String Code, String algorithmName, String pathToSave) {
        try {
            File myObj = new File( pathToSave + algorithmName + ".py");
            if (myObj.createNewFile()) {
                Files.writeString(myObj.toPath(), Code);
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
