package com.example.bfqca_backend.models.business;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.NonNull;

@Getter
@Builder(setterPrefix = "with")
public class User {
    private final Long id;
    private final String username;
    private final String password;
}
