package com.example.bfqca_backend.models.dao;



public class UserDTO {
    private Long id;
    private String userName;
    private String password;
    private String token;

    public UserDTO() {
        id = 0L;
        userName = "";
        password = "";
        token = "";
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }


    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
}
