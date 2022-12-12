package com.example.bfqca_backend.services.interfaces;

import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.filters.RestFilter;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface BenchmarkService {

    public void addBenchmark(Benchmark benchmark);

    public List<Benchmark> getBenchmarks(int page, int limit, RestFilter filter);
}
