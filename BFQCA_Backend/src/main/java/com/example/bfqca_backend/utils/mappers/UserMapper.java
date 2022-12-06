package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.dao.UserDTO;
import com.example.bfqca_backend.models.rest.UserRest;

public class UserMapper {

    public static User mapRestToBusiness(UserRest userRest) {
        return User.builder()
                .withUsername(userRest.getUsername())
                .withPassword(userRest.getPassword())
                .build();
    }

    public static UserRest mapBusinesstoRest(User user) {
        return UserRest.builder()
                .withUsername(user.getUsername())
                .withPassword(user.getPassword())
                .build();
    }

    public static User mapDtoToBusiness(UserDTO userDTO) {
        return User.builder()
                .withUsername(userDTO.getUserName())
                .withPassword(userDTO.getPassword())
                .build();
    }

    public static UserDTO mapBusinessToDto(User user){
        UserDTO userDTO = new UserDTO();
        userDTO.setId(0L);
        userDTO.setUserName(user.getUsername());
        userDTO.setPassword(user.getPassword());
        userDTO.setToken("TOKEN");
        return userDTO;
    }
}
