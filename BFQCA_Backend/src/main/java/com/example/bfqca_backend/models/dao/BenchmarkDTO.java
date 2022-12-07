package com.example.bfqca_backend.models.dao;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder(setterPrefix = "with")
public class BenchmarkDTO {

    private final Long id;
    private final String problemName;
    private final String algorithmName;
    private final Double accuracyLearning;
    private final Double accuracyTest;
    private final Double lossTest;
    private final Double maxLatency;
    private final Double minLatency;
    private final Double avgLatency;
    private final Double latencyPercentile;
    private final Double time;
}
