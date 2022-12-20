package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.repositories.interfaces.AlgorithmRepository;
import com.example.bfqca_backend.services.interfaces.BenchmarkService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.boot.test.mock.mockito.MockBean;

import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(MockitoExtension.class)
class AlgorithmServiceImplTest {

    static final String ALGORITHM_NAME = "algorithm name";

    static final String PROBLEM_NAME = "problem name";

    static final String DESCRIPTION = "description";

    @Mock
    private static AlgorithmRepository algorithmRepository;


    @Test
    @DisplayName("Execute algorithm without code")
    void executeAlgorithmNoCode() {
        
    }

    @Test
    @DisplayName("Execute algorithm with code")
    void executeAlgorithmWithCode() {
    }

    @Test
    void getAlgorithms() {
    }
}