package com.example.bfqca_backend.models.business;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;

import java.io.Serial;

@Getter
@Builder(setterPrefix = "with")
public class Benchmark {
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
