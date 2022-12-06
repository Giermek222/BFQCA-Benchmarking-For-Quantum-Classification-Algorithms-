package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.rest.UserRest;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import com.example.bfqca_backend.services.interfaces.UserService;
import com.example.bfqca_backend.utils.mappers.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.io.IOException;

@RestController
@RequestMapping("/user")
@CrossOrigin(origins = "*")
public class UserController {

    @Autowired
    UserService userService;

    SecurityService securityService;

    @GetMapping
    ResponseEntity<UserRest> getUsers(@RequestHeader HttpHeaders headers) {
        return null;
    }

    @PostMapping("/register")
    public ResponseEntity<Object> addAlgorithm(@RequestHeader HttpHeaders headers, @RequestBody @Valid UserRest userRest) throws IOException {

        userService.createUser(UserMapper.mapRestToBusiness(userRest));
        return  ResponseEntity.ok().build();
    }
}
