package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.models.rest.AlgorithmRest;
import com.example.bfqca_backend.models.rest.BenchmarkRest;
import com.example.bfqca_backend.services.interfaces.BenchmarkService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
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
    SecurityService securityService;


    @PostMapping("/execute")
    public ResponseEntity<Object> addBenchmarks(@RequestHeader HttpHeaders headers, @RequestBody @Valid BenchmarkRest benchmarkRest) throws IOException {
        if (Objects.isNull(benchmarkRest.getAlgorithmName()) ||
                Objects.isNull(benchmarkRest.getProblemName()) ||
                Objects.isNull(benchmarkRest.getAccuracyLearning()) ||
                Objects.isNull(benchmarkRest.getAccuracyTest()) ||
                Objects.isNull(benchmarkRest.getAvgLatency()) ||
                Objects.isNull(benchmarkRest.getMaxLatency()) ||
                Objects.isNull(benchmarkRest.getMinLatency()) ||
                Objects.isNull(benchmarkRest.getLatencyPercentile()) ||
                Objects.isNull(benchmarkRest.getLossLearning()) ||
                Objects.isNull(benchmarkRest.getLossTest()) ||
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
