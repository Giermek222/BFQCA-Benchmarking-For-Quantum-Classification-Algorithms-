package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.dao.BenchmarkDTO;
import com.example.bfqca_backend.models.rest.BenchmarkRest;

public class BenchmarkMapper {

    public static Benchmark mapRestToBusiness(BenchmarkRest benchmarkRest) {
        return Benchmark.builder()
                .withAlgorithmName(benchmarkRest.getAlgorithmName())
                .withProblemName(benchmarkRest.getProblemName())
                .withTrainingAccuracy(benchmarkRest.getTrainingAccuracy())
                .withTrainingPrecision(benchmarkRest.getTrainingPrecision())
                .withTrainingRecall(benchmarkRest.getTrainingRecall())
                .withTrainingF1Score(benchmarkRest.getTrainingF1Score())
                .withTrainingLoss(benchmarkRest.getTrainingLoss())
                .withTestAccuracy(benchmarkRest.getTestAccuracy())
                .withTestPrecision(benchmarkRest.getTestPrecision())
                .withTestF1Score(benchmarkRest.getTestF1Score())
                .withTestRecall(benchmarkRest.getTestRecall())
                .withTestLoss(benchmarkRest.getTestLoss())
                .withMaxLatencyMs(benchmarkRest.getMaxLatencyMs())
                .withMinLatencyMs(benchmarkRest.getMinLatencyMs())
                .withAvgLatencyMs(benchmarkRest.getAvgLatencyMs())
                .withPercentileLatencyMs(benchmarkRest.getPercentileLatencyMs())
                .withTime(benchmarkRest.getTime())
                .build();
    }

    public static Benchmark mapDtoToBusiness(BenchmarkDTO benchmarkDTO) {
        return Benchmark.builder()
                .withAlgorithmName(benchmarkDTO.getAlgorithmName())
                .withProblemName(benchmarkDTO.getProblemName())
                .withTrainingAccuracy(benchmarkDTO.getTrainingAccuracy())
                .withTrainingPrecision(benchmarkDTO.getTrainingPrecision())
                .withTrainingRecall(benchmarkDTO.getTrainingRecall())
                .withTrainingF1Score(benchmarkDTO.getTrainingF1Score())
                .withTrainingLoss(benchmarkDTO.getTrainingLoss())
                .withTestAccuracy(benchmarkDTO.getTestAccuracy())
                .withTestPrecision(benchmarkDTO.getTestPrecision())
                .withTestF1Score(benchmarkDTO.getTestF1Score())
                .withTestRecall(benchmarkDTO.getTestRecall())
                .withTestLoss(benchmarkDTO.getTestLoss())
                .withMaxLatencyMs(benchmarkDTO.getMaxLatencyMs())
                .withMinLatencyMs(benchmarkDTO.getMinLatencyMs())
                .withAvgLatencyMs(benchmarkDTO.getAvgLatencyMs())
                .withPercentileLatencyMs(benchmarkDTO.getPercentileLatencyMs())
                .withTime(benchmarkDTO.getTime())
                .build();
    }

    public static BenchmarkRest mapBusinessToRest(Benchmark benchmark) {
        return BenchmarkRest.builder()
                .withAlgorithmName(benchmark.getAlgorithmName())
                .withProblemName(benchmark.getProblemName())
                .withTrainingAccuracy(benchmark.getTrainingAccuracy())
                .withTrainingPrecision(benchmark.getTrainingPrecision())
                .withTrainingRecall(benchmark.getTrainingRecall())
                .withTrainingF1Score(benchmark.getTrainingF1Score())
                .withTrainingLoss(benchmark.getTrainingLoss())
                .withTestAccuracy(benchmark.getTestAccuracy())
                .withTestPrecision(benchmark.getTestPrecision())
                .withTestF1Score(benchmark.getTestF1Score())
                .withTestRecall(benchmark.getTestRecall())
                .withTestLoss(benchmark.getTestLoss())
                .withMaxLatencyMs(benchmark.getMaxLatencyMs())
                .withMinLatencyMs(benchmark.getMinLatencyMs())
                .withAvgLatencyMs(benchmark.getAvgLatencyMs())
                .withPercentileLatencyMs(benchmark.getPercentileLatencyMs())
                .withTime(benchmark.getTime())
                .build();
    }

    public static BenchmarkDTO mapBusinessToDto(Benchmark benchmark) {
        return BenchmarkDTO.builder()
                .withAlgorithmName(benchmark.getAlgorithmName())
                .withProblemName(benchmark.getProblemName())
                .withTrainingAccuracy(benchmark.getTrainingAccuracy())
                .withTrainingPrecision(benchmark.getTrainingPrecision())
                .withTrainingRecall(benchmark.getTrainingRecall())
                .withTrainingF1Score(benchmark.getTrainingF1Score())
                .withTrainingLoss(benchmark.getTrainingLoss())
                .withTestAccuracy(benchmark.getTestAccuracy())
                .withTestPrecision(benchmark.getTestPrecision())
                .withTestF1Score(benchmark.getTestF1Score())
                .withTestRecall(benchmark.getTestRecall())
                .withTestLoss(benchmark.getTestLoss())
                .withMaxLatencyMs(benchmark.getMaxLatencyMs())
                .withMinLatencyMs(benchmark.getMinLatencyMs())
                .withAvgLatencyMs(benchmark.getAvgLatencyMs())
                .withPercentileLatencyMs(benchmark.getPercentileLatencyMs())
                .withTime(benchmark.getTime())
                .build();
    }
}
