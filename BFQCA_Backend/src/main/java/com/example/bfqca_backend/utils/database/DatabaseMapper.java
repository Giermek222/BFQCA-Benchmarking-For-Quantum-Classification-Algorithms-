package com.example.bfqca_backend.utils.database;

import com.example.bfqca_backend.models.dao.UserDTO;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class DatabaseMapper {
    public static List<UserDTO> getUsers(ResultSet resultSet) throws SQLException {
        List<UserDTO> usersFromDb = new ArrayList<>();

        while (resultSet.next()) {
            usersFromDb.add(
                    UserDTO.builder()
                            .withId(resultSet.getLong("id"))
                            .withUserName(resultSet.getString("userName"))
                            .withPassword(resultSet.getString("password"))
                            .withToken(resultSet.getString("token"))
                            .build()
            );
        }
        return usersFromDb;
    }
}
