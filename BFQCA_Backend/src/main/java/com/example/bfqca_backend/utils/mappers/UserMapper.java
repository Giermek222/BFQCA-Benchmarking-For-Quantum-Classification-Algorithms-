package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.dao.UserDTO;
import com.example.bfqca_backend.models.rest.UserRest;

public class UserMapper {

    public static User mapRestToBusiness(UserRest userRest) {
        return User.builder()
                .withId(userRest.getId())
                .withUsername(userRest.getUsername())
                .withPassword(userRest.getPassword())
                .build();
    }

    public static UserRest mapBusinesstoRest(User user) {
        return UserRest.builder()
                .withId(user.getId())
                .withUsername(user.getUsername())
                .withPassword(user.getPassword())
                .build();
    }

    public static User mapDtoToBusiness(UserDTO userDTO) {
        return User.builder()
                .withId(userDTO.getId())
                .withUsername(userDTO.getUserName())
                .withPassword(userDTO.getPassword())
                .build();
    }

    public static UserDTO mapBusinessToDto(User user){

        return UserDTO.builder()
                .withId(user.getId())
                .withUserName(user.getUsername())
                .withPassword(user.getPassword())
                .withToken("TOKEN")
                .build();
    }
}
