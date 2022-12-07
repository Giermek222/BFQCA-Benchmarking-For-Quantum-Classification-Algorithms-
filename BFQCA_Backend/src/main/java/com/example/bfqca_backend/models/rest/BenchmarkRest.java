package com.example.bfqca_backend.models.rest;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;

import java.io.Serial;
import java.io.Serializable;

@Getter
@Builder(setterPrefix = "with")
public class BenchmarkRest implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    @JsonProperty(value = "problemName")
    private final String problemName;

    @JsonProperty(value = "algorithmName")
    private final String algorithmName;

    @JsonProperty(value = "accuracyLearning")
    private final Double accuracyLearning;

    @JsonProperty(value = "accuracyTest")
    private final Double accuracyTest;

    @JsonProperty(value = "lossLearning")
    private final Double lossTest;

    @JsonProperty(value = "maxLatency")
    private final Double maxLatency;

    @JsonProperty(value = "minLatency")
    private final Double minLatency;

    @JsonProperty(value = "avgLatency")
    private final Double avgLatency;

    @JsonProperty(value = "latencyPercentile")
    private final Double latencyPercentile;

    @JsonProperty(value = "time")
    private final Double time;
}
