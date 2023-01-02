package com.example.bfqca_backend.models.business;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder(setterPrefix = "with")
public class Algorithm {
    private final String algorithmName;
    private final String description;
    private final String problemName;
    private final String userName;
}
