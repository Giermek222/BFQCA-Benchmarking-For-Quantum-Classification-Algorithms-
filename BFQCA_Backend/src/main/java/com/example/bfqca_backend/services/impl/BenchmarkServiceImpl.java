package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Benchmark;
import com.example.bfqca_backend.models.dao.BenchmarkDTO;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.repositories.interfaces.BenchmarkRepository;
import com.example.bfqca_backend.services.interfaces.BenchmarkService;
import com.example.bfqca_backend.utils.mappers.BenchmarkMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class BenchmarkServiceImpl implements BenchmarkService {

    @Autowired
    BenchmarkRepository benchmarkRepository;
    @Override
    public void addBenchmark(Benchmark benchmark) {
        benchmarkRepository.addBenchmark(BenchmarkMapper.mapBusinessToDto(benchmark));
    }

    @Override
    public List<Benchmark> getBenchmarks(int page, int limit, RestFilter filter) {
        List<BenchmarkDTO> benchmarks = benchmarkRepository.getBenchmarks(filter);
        boolean filteredByName = filter.getAlgorithmname() != null;
        boolean filteredByProblem = filter.getProblem() != null;
        List<Benchmark> returned = new ArrayList<>(){};
        for(BenchmarkDTO dto : benchmarks) {
            if (filteredByName){
                if (!dto.getAlgorithmName().equals(filter.getAlgorithmname()))
                    continue;
            }
            if (filteredByProblem) {
                if (!dto.getProblemName().equals(filter.getProblem()))
                    continue;
            }
            returned.add(BenchmarkMapper.mapDtoToBusiness(dto));
        }
        return returned.stream()
                .skip((long) page * limit)
                .limit(limit)
                .collect(Collectors.toList());
    }

}
