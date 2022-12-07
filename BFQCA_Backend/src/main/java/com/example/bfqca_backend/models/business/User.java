package com.example.bfqca_backend.models.business;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder(setterPrefix = "with")
public class User {
    private final Long id;
    private final String username;
    private final String password;
}
