package com.example.bfqca_backend.services.interfaces;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.filters.RestFilter;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.List;

@Service
public interface AlgorithmService {

    public void ExecuteAlgorithm(Algorithm algorithm, List<String> params, String code) throws IOException;
    public List<Algorithm> GetAlgorithms(int page, int limit, RestFilter filter);

}
