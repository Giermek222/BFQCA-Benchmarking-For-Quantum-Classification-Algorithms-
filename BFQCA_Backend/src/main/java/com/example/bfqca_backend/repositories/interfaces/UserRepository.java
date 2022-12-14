package com.example.bfqca_backend.repositories.interfaces;

import com.example.bfqca_backend.models.dao.UserDTO;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserRepository{

    public void addUser(UserDTO userDTO);
    public void deleteUser(long idToDelete);
    public List<UserDTO> getUser(long id);
    public List<UserDTO> getUsers();
    public String logUser(String username, String password);
}
