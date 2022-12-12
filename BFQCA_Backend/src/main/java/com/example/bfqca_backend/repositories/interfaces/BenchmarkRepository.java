package com.example.bfqca_backend.repositories.interfaces;

import com.example.bfqca_backend.models.dao.BenchmarkDTO;
import com.example.bfqca_backend.models.filters.RestFilter;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BenchmarkRepository {

    public List<BenchmarkDTO> getBenchmarks(RestFilter filter);
    public void addBenchmark(BenchmarkDTO benchmarkDTO);
}
