package com.example.bfqca_backend.models.rest;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.NonNull;

import java.io.Serial;
import java.io.Serializable;

@Getter
@Builder(setterPrefix = "with")
public class UserRest implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    @NonNull
    @JsonProperty(value = "username")
    private final String username;

    @NonNull
    @JsonProperty(value = "password")
    private final String password;
}
