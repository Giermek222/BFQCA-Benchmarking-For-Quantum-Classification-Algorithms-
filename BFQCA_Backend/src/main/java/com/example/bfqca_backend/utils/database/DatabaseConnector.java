package com.example.bfqca_backend.utils.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnector {

    static final String URL = "jdbc:mysql://localhost:3306/Cookly?useSSL=false&serverTimezone=UTC&useLegacyDatetimeCode=false&allowPublicKeyRetrieval=true";
    static final String USERNAME = "adam";
    static final String PASSWORD = "piwo1";

    public static Connection connectToDatabase() throws SQLException {
        return DriverManager.getConnection(URL, USERNAME, PASSWORD);
    }
}
