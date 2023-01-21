package com.example.bfqca_backend.models.business;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder(setterPrefix = "with")
public class Benchmark {
    private final String problemName;
    private final String algorithmName;
    private final Double trainingAccuracy;
    private final Double trainingPrecision;
    private final Double trainingRecall;
    private final Double trainingF1Score;
    private final Double trainingLoss;
    private final Double testAccuracy;
    private final Double testPrecision;
    private final Double testRecall;
    private final Double testF1Score;
    private final Double testLoss;
    private final Double maxLatencyMs;
    private final Double minLatencyMs;
    private final Double avgLatencyMs;
    private final Double percentileLatencyMs;
    private final Double time;
}
