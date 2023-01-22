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

    @JsonProperty(value = "problem_name")
    private final String problemName;

    @JsonProperty(value = "algorithm_name")
    private final String algorithmName;

    @JsonProperty(value = "training_accuracy")
    private final Double trainingAccuracy;

    @JsonProperty(value = "training_precision")
    private final Double trainingPrecision;

    @JsonProperty(value = "training_recall")
    private final Double trainingRecall;

    @JsonProperty(value = "training_f1_score")
    private final Double trainingF1Score;

    @JsonProperty(value = "training_loss")
    private final Double trainingLoss;

    @JsonProperty(value = "test_accuracy")
    private final Double testAccuracy;

    @JsonProperty(value = "test_precision")
    private final Double testPrecision;

    @JsonProperty(value = "test_recall")
    private final Double testRecall;

    @JsonProperty(value = "test_f1_score")
    private final Double testF1Score;

    @JsonProperty(value = "test_loss")
    private final Double testLoss;

    @JsonProperty(value = "max_latency_ms")
    private final Double maxLatencyMs;

    @JsonProperty(value = "min_latency_ms")
    private final Double minLatencyMs;

    @JsonProperty(value = "avg_latency_ms")
    private final Double avgLatencyMs;

    @JsonProperty(value = "percentile_latency_ms")
    private final Double percentileLatencyMs;

    @JsonProperty(value = "time")
    private final Double time;
}
