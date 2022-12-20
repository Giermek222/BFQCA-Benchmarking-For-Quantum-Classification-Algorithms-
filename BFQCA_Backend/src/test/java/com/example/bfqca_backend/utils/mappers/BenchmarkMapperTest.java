package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.dao.BenchmarkDTO;
import com.example.bfqca_backend.models.rest.AlgorithmRest;
import com.example.bfqca_backend.models.rest.BenchmarkRest;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BenchmarkMapperTest {

    final static String PROBLEM_NAME = "problem name";
    final static String ALGORITHM_NAME = "algorithm name";
    final static Double ACCURACY_LEARNING = 1D;
    final static Double ACCURACY_TEST = 1D;
    final static Double LOSS_LEARNING = 1D;
    final static Double LOSS_TEST = 1D;
    final static Double MAX_LATENCY = 1D;
    final static Double MIN_LATENCY = 1D;
    final static Double AVG_LATENCY = 1D;
    final static Double LATENCY_PERCENTILE = 1D;
    final static Double TIME = 1D;

    static BenchmarkRest benchmarkRest;
    static Benchmark benchmark;
    static BenchmarkDTO benchmarkDTO;

    @BeforeAll
    static void initializeData() {
        benchmarkRest = BenchmarkRest.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();
        benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();
        benchmarkDTO = BenchmarkDTO.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();
    }

    @Test
    void should_MapFromRestToBusiness() {
        Benchmark test = BenchmarkMapper.mapRestToBusiness(benchmarkRest);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
        Assertions.assertEquals(ACCURACY_LEARNING, test.getAccuracyLearning());
        Assertions.assertEquals(ACCURACY_TEST, test.getAccuracyTest());
        Assertions.assertEquals(LOSS_LEARNING, test.getLossLearning());
        Assertions.assertEquals(LOSS_TEST, test.getLossTest());
        Assertions.assertEquals(MAX_LATENCY, test.getMaxLatency());
        Assertions.assertEquals(MIN_LATENCY, test.getMinLatency());
        Assertions.assertEquals(AVG_LATENCY, test.getAvgLatency());
        Assertions.assertEquals(LATENCY_PERCENTILE, test.getLatencyPercentile());
        Assertions.assertEquals(TIME, test.getTime());
    }

    @Test
    void should_MapFromDtoToBusiness() {
        Benchmark test = BenchmarkMapper.mapDtoToBusiness(benchmarkDTO);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
        Assertions.assertEquals(ACCURACY_LEARNING, test.getAccuracyLearning());
        Assertions.assertEquals(ACCURACY_TEST, test.getAccuracyTest());
        Assertions.assertEquals(LOSS_LEARNING, test.getLossLearning());
        Assertions.assertEquals(LOSS_TEST, test.getLossTest());
        Assertions.assertEquals(MAX_LATENCY, test.getMaxLatency());
        Assertions.assertEquals(MIN_LATENCY, test.getMinLatency());
        Assertions.assertEquals(AVG_LATENCY, test.getAvgLatency());
        Assertions.assertEquals(LATENCY_PERCENTILE, test.getLatencyPercentile());
        Assertions.assertEquals(TIME, test.getTime());
    }

    @Test
    void should_MapFromBusinessToRest() {
        BenchmarkRest test = BenchmarkMapper.mapBusinessToRest(benchmark);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
        Assertions.assertEquals(ACCURACY_LEARNING, test.getAccuracyLearning());
        Assertions.assertEquals(ACCURACY_TEST, test.getAccuracyTest());
        Assertions.assertEquals(LOSS_LEARNING, test.getLossLearning());
        Assertions.assertEquals(LOSS_TEST, test.getLossTest());
        Assertions.assertEquals(MAX_LATENCY, test.getMaxLatency());
        Assertions.assertEquals(MIN_LATENCY, test.getMinLatency());
        Assertions.assertEquals(AVG_LATENCY, test.getAvgLatency());
        Assertions.assertEquals(LATENCY_PERCENTILE, test.getLatencyPercentile());
        Assertions.assertEquals(TIME, test.getTime());
    }

    @Test
    void should_MapFromBusinessToDTo() {
        BenchmarkDTO test = BenchmarkMapper.mapBusinessToDto(benchmark);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
        Assertions.assertEquals(ACCURACY_LEARNING, test.getAccuracyLearning());
        Assertions.assertEquals(ACCURACY_TEST, test.getAccuracyTest());
        Assertions.assertEquals(LOSS_LEARNING, test.getLossLearning());
        Assertions.assertEquals(LOSS_TEST, test.getLossTest());
        Assertions.assertEquals(MAX_LATENCY, test.getMaxLatency());
        Assertions.assertEquals(MIN_LATENCY, test.getMinLatency());
        Assertions.assertEquals(AVG_LATENCY, test.getAvgLatency());
        Assertions.assertEquals(LATENCY_PERCENTILE, test.getLatencyPercentile());
        Assertions.assertEquals(TIME, test.getTime());
    }
}