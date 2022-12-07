package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.dao.UserDTO;
import com.example.bfqca_backend.repositories.interfaces.UserRepository;
import com.example.bfqca_backend.services.interfaces.UserService;
import com.example.bfqca_backend.utils.mappers.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    UserRepository userRepository;

    @Override
    public void createUser(User user) {
        try
        {
            userRepository.addUser(UserMapper.mapBusinessToDto(user));
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<User> getUsers() {
        List<User> users = new ArrayList<>();
        for (UserDTO userDTO: userRepository.getUsers()) {
            users.add(UserMapper.mapDtoToBusiness(userDTO));
        }
        return users;
    }

    @Override
    public User getUser(long id) {
        List<UserDTO> users = userRepository.getUser(id);
        if (users.isEmpty())
            return null;
        return UserMapper.mapDtoToBusiness(users.get(0));

    }

    @Override
    public void deleteUser(long id) {
        userRepository.deleteUser(id);
    }

    @Override
    public void editUser(User user, long id) {
        deleteUser(id);
        createUser(user);
    }

    @Override
    public String logUser(String username, String password) {

        return userRepository.logUser(username, password);

    }
}
