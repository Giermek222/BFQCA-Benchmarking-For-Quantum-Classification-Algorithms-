package com.example.bfqca_backend.utils.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnector {

    static final String URL = "jdbc:sqlserver://bfqca-server.database.windows.net:1433;database=BFQCA";
    static final String USERNAME = "adam";
    static final String PASSWORD = "4b0UllpYIivqC2Q1wE34";

    public static Connection connectToDatabase() throws SQLException {
        return DriverManager.getConnection(URL, USERNAME, PASSWORD);
    }
}
