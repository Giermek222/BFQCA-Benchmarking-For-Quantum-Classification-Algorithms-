package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.models.rest.BenchmarkRest;
import com.example.bfqca_backend.services.interfaces.BenchmarkService;
import com.example.bfqca_backend.utils.mappers.BenchmarkMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@RestController
@RequestMapping("/benchmarks")
public class BenchmarkController {

    @Autowired
    BenchmarkService benchmarkService;



    @PostMapping("/execute")
    public ResponseEntity<Object> addBenchmarks(@RequestHeader HttpHeaders headers, @RequestBody @Valid BenchmarkRest benchmarkRest) throws IOException {
        if (Objects.isNull(benchmarkRest.getAlgorithmName()) ||
                Objects.isNull(benchmarkRest.getProblemName()) ||
                Objects.isNull(benchmarkRest.getTrainingAccuracy()) ||
                Objects.isNull(benchmarkRest.getTrainingPrecision()) ||
                Objects.isNull(benchmarkRest.getTrainingRecall()) ||
                Objects.isNull(benchmarkRest.getTrainingF1Score()) ||
                Objects.isNull(benchmarkRest.getTrainingLoss()) ||
                Objects.isNull(benchmarkRest.getTestAccuracy()) ||
                Objects.isNull(benchmarkRest.getTestPrecision()) ||
                Objects.isNull(benchmarkRest.getTestRecall()) ||
                Objects.isNull(benchmarkRest.getTestF1Score()) ||
                Objects.isNull(benchmarkRest.getTestLoss()) ||
                Objects.isNull(benchmarkRest.getMinLatencyMs()) ||
                Objects.isNull(benchmarkRest.getMaxLatencyMs()) ||
                Objects.isNull(benchmarkRest.getAvgLatencyMs()) ||
                Objects.isNull(benchmarkRest.getPercentileLatencyMs()) ||
                Objects.isNull(benchmarkRest.getTime())) {
            return ResponseEntity.badRequest().build();
        }
        benchmarkService.addBenchmark(BenchmarkMapper.mapRestToBusiness(benchmarkRest));
        return  ResponseEntity.ok().build();
    }

    @PostMapping("/get")
    public ResponseEntity<Object> getBenchmarks(@RequestHeader HttpHeaders headers,
                                               @RequestParam(value = "page") int page,
                                               @RequestParam(value = "limit") int limit,
                                               @RequestBody(required = false) RestFilter filters) {
        if (Objects.isNull(filters))
            filters = new RestFilter();
        List<Benchmark> benchmarks = benchmarkService.getBenchmarks(page, limit, filters);
        List<BenchmarkRest> restList = new ArrayList<>();
        for(Benchmark benchmar : benchmarks) {
            restList.add(BenchmarkMapper.mapBusinessToRest(benchmar));
        }
        return  ResponseEntity.ok(restList);
    }


}
