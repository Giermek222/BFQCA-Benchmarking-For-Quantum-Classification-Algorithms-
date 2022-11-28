package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.services.interfaces.UserService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Override
    public void createUser(User user) {

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
    public boolean deleteUser(long id) {
        return false;
    }

    @Override
    public boolean editUser(User user, long id) {
        return false;
    }
}
