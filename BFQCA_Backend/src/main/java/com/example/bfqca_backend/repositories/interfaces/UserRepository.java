package com.example.bfqca_backend.repositories.interfaces;

import com.example.bfqca_backend.models.dao.UserDTO;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserRepository extends IRepository<UserDTO> {

    public void addUser(UserDTO userDTO);
    public void deleteUser(long idToDelete);
    public UserDTO getUser(long idToDelete);
    public List<UserDTO> getUsers();
}
