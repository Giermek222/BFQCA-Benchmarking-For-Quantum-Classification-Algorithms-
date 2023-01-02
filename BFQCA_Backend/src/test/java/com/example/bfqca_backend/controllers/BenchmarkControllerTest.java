package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.services.interfaces.BenchmarkService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.lenient;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(MockitoExtension.class)
@WebMvcTest(BenchmarkController.class)
class BenchmarkControllerTest {
    @MockBean
    private static BenchmarkService benchmarkService;

    final static int PAGE = 0;
    final static int LIMIT = 100;
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

    @Autowired
    private MockMvc mockMvc;


    @Test
    @DisplayName("Get Algorithm - No filter")
    void getAlgorithm() throws Exception
    {
        final RestFilter filter = new RestFilter();


        Mockito.doReturn(new ArrayList<Algorithm>()).when(benchmarkService).getBenchmarks(PAGE,LIMIT,filter);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/benchmarks/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Get Algorithm - Partial filter with Algorithm name")
    void getAlgorithmPartialFilterAlg() throws Exception
    {
        final RestFilter filter = new RestFilter();


        Mockito.doReturn(new ArrayList<Algorithm>()).when(benchmarkService).getBenchmarks(PAGE,LIMIT,filter);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/benchmarks/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\":\"name\"}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Get Algorithm - Partial filter with Problem name")
    void getAlgorithmPartialFilterProblem() throws Exception
    {
        final RestFilter filter = new RestFilter();


        Mockito.doReturn(new ArrayList<Algorithm>()).when(benchmarkService).getBenchmarks(PAGE,LIMIT,filter);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/benchmarks/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"problem\":\"name\"}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Get Algorithm - full filter")
    void getAlgorithmWithFilter() throws Exception
    {
        final RestFilter filter = new RestFilter();

        Mockito.doReturn(new ArrayList<Algorithm>()).when(benchmarkService).getBenchmarks(PAGE,LIMIT,filter);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/benchmarks/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\":\"name\", " +
                                "\"problem\":\"name\"}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Save Benchmark - correct benchmark")
    void addBenchmarkWithCorrectData() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
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

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without Algorithm Name")
    void addBenchmarkWithInCorrectInputMissingAlgorithmName() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
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

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without problem name")
    void addBenchmarkWithInCorrectInputMissingProblemName() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
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

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without accuracy learning")
    void addBenchmarkWithInCorrectInputMissingAccuracyLearning() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without accuracy Test")
    void addBenchmarkWithInCorrectInputMissingAccuracyTest() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without max latency")
    void addBenchmarkWithInCorrectInputMissingMaxLatency() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without LossLearning")
    void addBenchmarkWithInCorrectInputMissingLossLearning() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without")
    void addBenchmarkWithInCorrectInputMissingLossTest() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without min latency")
    void addBenchmarkWithInCorrectInputMissingMinLatency() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without average latency")
    void addBenchmarkWithInCorrectInputMissingAvgLatency() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withLatencyPercentile(LATENCY_PERCENTILE)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without latency percentile")
    void addBenchmarkWithInCorrectInputMissingLatencyPercentile() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withProblemName(PROBLEM_NAME)
                .withAccuracyLearning(ACCURACY_LEARNING)
                .withAccuracyTest(ACCURACY_TEST)
                .withLossLearning(LOSS_LEARNING)
                .withLossTest(LOSS_TEST)
                .withMaxLatency(MAX_LATENCY)
                .withMinLatency(MIN_LATENCY)
                .withAvgLatency(AVG_LATENCY)
                .withTime(TIME)
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"time\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Benchmark - incorrect benchmark without time")
    void addBenchmarkWithInCorrectInputMissingTime() throws Exception
    {
        final Benchmark benchmark = Benchmark.builder()
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
                .build();

        doNothing().when(benchmarkService).addBenchmark(benchmark);

        mockMvc.perform(post("/benchmarks/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"Name\"," +
                                " \"accuracyLearning\" : 1," +
                                " \"accuracyTest\" : 1," +
                                " \"lossLearning\" : 1," +
                                " \"maxLatency\" : 1," +
                                " \"minLatency\" : 1," +
                                " \"avgLatency\" : 1," +
                                " \"latencyPercentile\" : 1," +
                                " \"lossTest\" : 1}"))
                .andExpect(status().isBadRequest());
    }

}