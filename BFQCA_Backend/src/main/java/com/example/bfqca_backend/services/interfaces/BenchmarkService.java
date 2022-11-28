package com.example.bfqca_backend.services.interfaces;

import com.example.bfqca_backend.models.business.Benchmark;
import org.springframework.stereotype.Service;

@Service
public interface BenchmarkService {

    public void addBenchmark(Benchmark benchmark);
}
