package com.example.bfqca_backend.models.business;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;

import java.util.List;

@Getter
@Builder(setterPrefix = "with")
public class Algorithm {
    private final String algorithmName;
    private final String description;
    private final String problemName;
}
