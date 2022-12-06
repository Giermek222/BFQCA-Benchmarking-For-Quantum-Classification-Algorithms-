package com.example.bfqca_backend.repositories.impl;

import com.example.bfqca_backend.models.dao.UserDTO;
import com.example.bfqca_backend.repositories.interfaces.UserRepository;
import com.example.bfqca_backend.utils.database.DatabaseConnector;
import org.springframework.stereotype.Repository;

import java.sql.*;
import java.util.List;

@Repository
public class UserRepositoryImpl implements UserRepository {

    @Override
    public void addUser(UserDTO userDTO) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();

            PreparedStatement statement = connection.prepareStatement("insert into user (userName, password, token) values (?,?,?) ");
            statement.setString(1, userDTO.getUserName());
            statement.setString(2, userDTO.getPassword());
            statement.setString(3, userDTO.getToken());
            statement.executeUpdate();
            connection.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void deleteUser(long idToDelete) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("delete from user where id = ? ");
            statement.setLong(1, idToDelete);
            statement.executeUpdate();
            connection.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public UserDTO getUser(long idToDelete) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("select * from user where id = ? ");
            statement.setLong(1, idToDelete);
            ResultSet resultSet = statement.executeQuery();

            connection.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<UserDTO> getUsers() {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("select * from user");
            statement.executeQuery();
            connection.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    private
}
