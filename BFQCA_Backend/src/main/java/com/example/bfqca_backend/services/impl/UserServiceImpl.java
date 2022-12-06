package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.dao.UserDTO;
import com.example.bfqca_backend.repositories.interfaces.UserRepository;
import com.example.bfqca_backend.services.interfaces.UserService;
import com.example.bfqca_backend.utils.mappers.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    UserRepository userRepository;

    @Override
    public void createUser(User user) {
        try
        {
            UserDTO userToSave = UserMapper.mapBusinessToDto(user);
            userRepository.addUser(userToSave);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<User> getUsers() {
        return null;
    }

    @Override
    public User getUser(long id) {
        return null;
    }

    @Override
    public void deleteUser(long id) {
        return;
    }

    @Override
    public boolean editUser(User user, long id) {
        return false;
    }
}
