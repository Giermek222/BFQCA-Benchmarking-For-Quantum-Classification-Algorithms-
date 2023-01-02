package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import com.example.bfqca_backend.services.interfaces.UserService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.lenient;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(MockitoExtension.class)
@WebMvcTest(UserController.class)
class UserControllerTest {
    @MockBean
    private static UserService userService;

    final static int PAGE = 0;
    final static int LIMIT = 100;

    @Autowired
    private MockMvc mockMvc;



    @Test
    @DisplayName("Get Users")
    void getUsers() throws Exception
    {
        Mockito.doReturn(new ArrayList<User>()).when(userService).getUsers();

        mockMvc.perform(get("/user/all")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Get user by id")
    void getUser() throws Exception
    {
        User user = User.builder()
                .withId(1L)
                .withUsername("username")
                .withPassword("password")
                .build();

        Mockito.doReturn(user).when(userService).getUser(1);
        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("id", "1");

        mockMvc.perform(get("/user")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Register new valid user")
    void Registeruser() throws Exception
    {
        User user = User.builder().withId(1L).withUsername("username").withPassword("password").build();
        doNothing().when(userService).createUser(user);

        mockMvc.perform(post("/user/register")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"username\":\"username\"," +
                            " \"password\":\"password\"}"))
                .andExpect(status().isOk());
    }
}