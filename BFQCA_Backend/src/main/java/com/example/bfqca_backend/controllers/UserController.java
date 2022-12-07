package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.rest.UserRest;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import com.example.bfqca_backend.services.interfaces.UserService;
import com.example.bfqca_backend.utils.mappers.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/user")
@CrossOrigin(origins = "*")
public class UserController {

    @Autowired
    UserService userService;

    SecurityService securityService;

    @GetMapping("/all")
    ResponseEntity<Object> getUsers(@RequestHeader HttpHeaders headers) {
        List<UserRest> userRests = new ArrayList<>();
        List<User> users = userService.getUsers();
        for (User user : users) {
            userRests.add(UserMapper.mapBusinesstoRest(user));
        }
        return  ResponseEntity.ok(userRests);
    }

    @GetMapping
    ResponseEntity<Object> getUser(@RequestHeader HttpHeaders headers, @RequestParam(value = "id") int id) {
        User users = userService.getUser(id);
        return  ResponseEntity.ok(UserMapper.mapBusinesstoRest(users));
    }

    @PostMapping("/register")
    public ResponseEntity<Object> registerNewUser(@RequestHeader HttpHeaders headers, @RequestBody @Valid UserRest userRest) {
        userService.createUser(UserMapper.mapRestToBusiness(userRest));
        return  ResponseEntity.ok().build();
    }

    @PostMapping("/login")
    public ResponseEntity<Object> logUser(@RequestHeader HttpHeaders headers, @RequestParam(value = "username") String username, @RequestParam(value = "password") String password) {
        String result = userService.logUser(username, password);
        if (result.equals("")) {
            return ResponseEntity.status(401).build();
        }
        return ResponseEntity.ok(result);
    }

    @DeleteMapping
    public ResponseEntity<Object> deleteUser(@RequestHeader HttpHeaders headers, @RequestParam(value = "id") int id) {
        userService.deleteUser(id);
        return  ResponseEntity.ok().build();
    }

    @PutMapping
    public ResponseEntity<Object> editUser(@RequestHeader HttpHeaders headers, @RequestParam(value = "id") int id,  @RequestBody @Valid UserRest userRest) {
        userService.editUser(UserMapper.mapRestToBusiness(userRest) ,id);
        return  ResponseEntity.ok().build();
    }
}
