package com.example.bfqca_backend.utils.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnector {

    static final String URL = "jdbc:h2:mem:testdb";
    static final String USERNAME = "sa";
    static final String PASSWORD = "";

    public static Connection connectToDatabase() throws SQLException {
        return DriverManager.getConnection(URL, USERNAME, PASSWORD);
    }
}
