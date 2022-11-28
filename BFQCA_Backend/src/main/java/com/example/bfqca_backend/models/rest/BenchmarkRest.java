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
    private final Number accuracyLearning;

    @JsonProperty(value = "accuracyTest")
    private final Number accuracyTest;

    @JsonProperty(value = "lossLearning")
    private final Number lossTest;

    @JsonProperty(value = "maxLatency")
    private final Number maxLatency;

    @JsonProperty(value = "minLatency")
    private final Number minLatency;

    @JsonProperty(value = "avgLatency")
    private final Number avgLatency;

    @JsonProperty(value = "latencyPercentile")
    private final Number latencyPercentile;

    @JsonProperty(value = "time")
    private final Number time;

}
