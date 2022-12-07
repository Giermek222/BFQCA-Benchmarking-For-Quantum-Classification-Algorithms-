package com.example.bfqca_backend.models.dao;


import lombok.Builder;
import lombok.Getter;

@Getter
@Builder(setterPrefix = "with")
public class UserDTO {
    private Long id;
    private String userName;
    private String password;
    private String token;
}
