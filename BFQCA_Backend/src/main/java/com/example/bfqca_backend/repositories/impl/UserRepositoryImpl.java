package com.example.bfqca_backend.repositories.impl;

import com.example.bfqca_backend.models.dao.UserDTO;
import com.example.bfqca_backend.repositories.interfaces.UserRepository;
import com.example.bfqca_backend.utils.database.DatabaseConnector;
import com.example.bfqca_backend.utils.database.DatabaseMapper;
import org.springframework.stereotype.Repository;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
public class UserRepositoryImpl implements UserRepository {

    @Override
    public void addUser(UserDTO userDTO) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("insert into users (userName, password, token) values (?,?,?) ");
            statement.setString(1, userDTO.getUserName());
            statement.setString(2, userDTO.getPassword());
            statement.setString(3, userDTO.getToken());
            System.out.println(statement.toString());
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
            PreparedStatement statement = connection.prepareStatement("delete from users where id = ? ");
            statement.setLong(1, idToDelete);
            statement.executeUpdate();
            connection.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<UserDTO> getUser(long idToDelete) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("select * from users where id = ? ");
            statement.setLong(1, idToDelete);
            ResultSet resultSet = statement.executeQuery();
            List<UserDTO> userDTOS = DatabaseMapper.getUsers(resultSet);
            connection.close();
            return  userDTOS;


        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<UserDTO> getUsers() {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("select * from users");
            ResultSet resultSet = statement.executeQuery();
            List<UserDTO> userDTOS = DatabaseMapper.getUsers(resultSet);
            connection.close();
            return  userDTOS;

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public String logUser(String username, String password) {
        try {
            String loginResult;
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("select * from users where userName = ? and password = ?");
            statement.setString(1, username);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                loginResult = resultSet.getString("token");
            }
            else {
                loginResult = "";
            }

            connection.close();
            return  loginResult;


        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }


}
