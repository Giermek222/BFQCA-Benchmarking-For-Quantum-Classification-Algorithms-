package com.example.bfqca_backend.repositories.interfaces;

import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.filters.RestFilter;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AlgorithmRepository{
    public void addAlgorithm(AlgorithmDTO algorithmDTO);
    public List<AlgorithmDTO> getAlgorithms(RestFilter filter);
}
