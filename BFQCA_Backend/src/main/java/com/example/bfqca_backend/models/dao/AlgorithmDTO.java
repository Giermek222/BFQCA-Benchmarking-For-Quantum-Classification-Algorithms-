package com.example.bfqca_backend.models.dao;

import lombok.Builder;
import lombok.Getter;


@Getter
@Builder(setterPrefix = "with")
public class AlgorithmDTO {
    private Long id;
    private String algorithmName;
    private String description;
    private String problemName;
}
