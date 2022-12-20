package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.dao.BenchmarkDTO;
import com.example.bfqca_backend.models.rest.BenchmarkRest;

public class BenchmarkMapper {

    public static Benchmark mapRestToBusiness(BenchmarkRest benchmarkRest) {
        return Benchmark.builder()
                .withAlgorithmName(benchmarkRest.getAlgorithmName())
                .withProblemName(benchmarkRest.getProblemName())
                .withAccuracyLearning(benchmarkRest.getAccuracyLearning())
                .withAccuracyTest(benchmarkRest.getAccuracyTest())
                .withAvgLatency(benchmarkRest.getAvgLatency())
                .withLatencyPercentile(benchmarkRest.getLatencyPercentile())
                .withLossTest(benchmarkRest.getLossTest())
                .withLossLearning(benchmarkRest.getLossLearning())
                .withMaxLatency(benchmarkRest.getMaxLatency())
                .withMinLatency(benchmarkRest.getMinLatency())
                .withTime(benchmarkRest.getTime())
                .build();
    }

    public static Benchmark mapDtoToBusiness(BenchmarkDTO benchmarkDTO) {
        return Benchmark.builder()
                .withAlgorithmName(benchmarkDTO.getAlgorithmName())
                .withProblemName(benchmarkDTO.getProblemName())
                .withAccuracyLearning(benchmarkDTO.getAccuracyLearning())
                .withAccuracyTest(benchmarkDTO.getAccuracyTest())
                .withAvgLatency(benchmarkDTO.getAvgLatency())
                .withLossLearning(benchmarkDTO.getLossLearning())
                .withLatencyPercentile(benchmarkDTO.getLatencyPercentile())
                .withLossTest(benchmarkDTO.getLossTest())
                .withMaxLatency(benchmarkDTO.getMaxLatency())
                .withMinLatency(benchmarkDTO.getMinLatency())
                .withTime(benchmarkDTO.getTime())
                .build();
    }

    public static BenchmarkRest mapBusinessToRest(Benchmark benchmark) {
        return BenchmarkRest.builder()
                .withAlgorithmName(benchmark.getAlgorithmName())
                .withProblemName(benchmark.getProblemName())
                .withAccuracyLearning(benchmark.getAccuracyLearning())
                .withAccuracyTest(benchmark.getAccuracyTest())
                .withLossLearning(benchmark.getLossLearning())
                .withAvgLatency(benchmark.getAvgLatency())
                .withLatencyPercentile(benchmark.getLatencyPercentile())
                .withLossTest(benchmark.getLossTest())
                .withMaxLatency(benchmark.getMaxLatency())
                .withMinLatency(benchmark.getMinLatency())
                .withTime(benchmark.getTime())
                .build();
    }

    public static BenchmarkDTO mapBusinessToDto(Benchmark benchmark) {
        return BenchmarkDTO.builder()
                .withAlgorithmName(benchmark.getAlgorithmName())
                .withProblemName(benchmark.getProblemName())
                .withAccuracyLearning(benchmark.getAccuracyLearning())
                .withAccuracyTest(benchmark.getAccuracyTest())
                .withAvgLatency(benchmark.getAvgLatency())
                .withLossLearning(benchmark.getLossLearning())
                .withLatencyPercentile(benchmark.getLatencyPercentile())
                .withLossTest(benchmark.getLossTest())
                .withMaxLatency(benchmark.getMaxLatency())
                .withMinLatency(benchmark.getMinLatency())
                .withTime(benchmark.getTime())
                .build();
    }
}
