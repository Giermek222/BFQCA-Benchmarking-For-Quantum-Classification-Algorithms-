package com.example.bfqca_backend.models.rest;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;

import java.io.Serial;
import java.io.Serializable;
import java.util.List;

@Getter
@Builder(setterPrefix = "with")
public class AlgorithmRest implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    @JsonProperty(value = "algorithmName")
    private final String algorithmName;

    @JsonProperty(value = "description")
    private final String description;

    @JsonProperty(value = "problemName")
    private final String problemName;

    @JsonProperty(value = "params")
    private final List<String> params;
}
