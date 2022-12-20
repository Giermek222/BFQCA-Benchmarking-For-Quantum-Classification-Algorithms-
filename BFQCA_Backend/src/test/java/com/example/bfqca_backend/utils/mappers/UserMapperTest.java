package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.dao.UserDTO;
import com.example.bfqca_backend.models.rest.AlgorithmRest;
import com.example.bfqca_backend.models.rest.UserRest;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class UserMapperTest {

    static UserRest userRest;
    static UserDTO userDTO;
    static User user;

    static final Long ID = 1L;
    static final String USERNAME = "username";
    static final String PASSWORD = "password";

    @BeforeAll
    static void initializeData() {

        userRest = UserRest.builder()
                .withId(ID)
                .withUsername(USERNAME)
                .withPassword(PASSWORD)
                .build();
        user = User.builder()
                .withId(ID)
                .withUsername(USERNAME)
                .withPassword(PASSWORD)
                .build();
        userDTO = UserDTO.builder()
                .withId(ID)
                .withUserName(USERNAME)
                .withPassword(PASSWORD)
                .build();
    }

    @Test
    void should_MapFromRestToBusiness() {
        User test = UserMapper.mapRestToBusiness(userRest);

        Assertions.assertEquals(USERNAME, test.getUsername());
        Assertions.assertEquals(PASSWORD, test.getPassword());
        Assertions.assertEquals(ID, test.getId());
    }

    @Test
    void should_MapFromDtoToBusiness() {
        User test = UserMapper.mapDtoToBusiness(userDTO);

        Assertions.assertEquals(USERNAME, test.getUsername());
        Assertions.assertEquals(PASSWORD, test.getPassword());
        Assertions.assertEquals(ID, test.getId());
    }

    @Test
    void should_MapFromBusinessToRest() {
        UserRest test = UserMapper.mapBusinesstoRest(user);

        Assertions.assertEquals(USERNAME, test.getUsername());
        Assertions.assertEquals(PASSWORD, test.getPassword());
        Assertions.assertEquals(ID, test.getId());
    }

    @Test
    void should_MapFromBusinessToDTo() {
        UserDTO test = UserMapper.mapBusinessToDto(user);

        Assertions.assertEquals(USERNAME, test.getUserName());
        Assertions.assertEquals(PASSWORD, test.getPassword());
        Assertions.assertEquals(ID, test.getId());
    }
}