package com.example.bfqca_backend.models.business;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder(setterPrefix = "with")
public class Benchmark {
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
