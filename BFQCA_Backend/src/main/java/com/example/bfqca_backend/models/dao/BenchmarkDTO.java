package com.example.bfqca_backend.models.dao;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder(setterPrefix = "with")
public class BenchmarkDTO {

    private final Long id;
    private final String problemName;
    private final String algorithmName;
    private final Long accuracyLearning;
    private final Long accuracyTest;
    private final Long lossTest;
    private final Long maxLatency;
    private final Long minLatency;
    private final Long avgLatency;
    private final Long latencyPercentile;
    private final Long time;
}
