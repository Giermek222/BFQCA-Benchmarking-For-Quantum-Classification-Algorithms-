package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.rest.UserRest;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import com.example.bfqca_backend.services.interfaces.UserService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/user")
public class UserController {

    UserService userService;
    SecurityService securityService;

    @GetMapping
    ResponseEntity<UserRest> getUsers(@RequestHeader HttpHeaders headers) {
        return null;
    }
}
