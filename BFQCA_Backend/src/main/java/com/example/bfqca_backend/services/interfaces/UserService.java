package com.example.bfqca_backend.services.interfaces;

import com.example.bfqca_backend.models.business.User;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface UserService {

    public void createUser(User user);
    public List<User> getUsers();
    public User getUser(long id);
    public void deleteUser(long id);
    public boolean editUser(User user, long id);
}
