package com.example.bfqca_backend.models.rest;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.NonNull;

import java.io.Serial;
import java.io.Serializable;

@Getter
@Builder(setterPrefix = "with")
public class DatasetRest implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    @NonNull
    @JsonProperty(value = "datasetName")
    private final String username;

    @NonNull
    @JsonProperty(value = "datasetCode")
    private final String password;
}
