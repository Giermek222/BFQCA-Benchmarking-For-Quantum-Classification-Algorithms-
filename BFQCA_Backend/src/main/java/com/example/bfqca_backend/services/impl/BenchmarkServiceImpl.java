package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.repositories.interfaces.BenchmarkRepository;
import com.example.bfqca_backend.services.interfaces.BenchmarkService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BenchmarkServiceImpl implements BenchmarkService {

    @Autowired
    BenchmarkRepository benchmarkRepository;
    @Override
    public void addBenchmark(Benchmark benchmark) {
    }

    @Override
    public void getBenchmarks() {
    }
}
