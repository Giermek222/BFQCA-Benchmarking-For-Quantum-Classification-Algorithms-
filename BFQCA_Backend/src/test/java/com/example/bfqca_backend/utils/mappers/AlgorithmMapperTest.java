package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.rest.AlgorithmRest;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class AlgorithmMapperTest {

    static AlgorithmRest algorithmRest;
    static Algorithm algorithm;
    static AlgorithmDTO algorithmDTO;

    private final static String ALGORITHM_NAME = "test_algorithm";
    private final static String PROBLEM_NAME = "test_problem";
    private final static String DESCRIPTION = "test_description";

    @BeforeAll
    static void initializeData() {
        algorithmRest = AlgorithmRest.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withDescription(DESCRIPTION)
                .withProblemName(PROBLEM_NAME)
                .build();

        algorithm = Algorithm.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withDescription(DESCRIPTION)
                .withProblemName(PROBLEM_NAME)
                .build();

        algorithmDTO = AlgorithmDTO.builder()
                .withAlgorithmName(ALGORITHM_NAME)
                .withDescription(DESCRIPTION)
                .withProblemName(PROBLEM_NAME)
                .build();
    }

    @Test
    void should_MapFromRestToBusiness() {
        Algorithm test = AlgorithmMapper.mapRestToBusiness(algorithmRest);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(DESCRIPTION, test.getDescription());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
    }

    @Test
    void should_MapFromDtoToBusiness() {
        Algorithm test = AlgorithmMapper.mapDtoToBusiness(algorithmDTO);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(DESCRIPTION, test.getDescription());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
    }

    @Test
    void should_MapFromBusinessToRest() {
        AlgorithmRest test = AlgorithmMapper.mapBusinessToRest(algorithm);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(DESCRIPTION, test.getDescription());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
    }

    @Test
    void should_MapFromBusinessToDTo() {
        AlgorithmDTO test = AlgorithmMapper.mapBusinessToDto(algorithm);

        Assertions.assertEquals(ALGORITHM_NAME, test.getAlgorithmName());
        Assertions.assertEquals(DESCRIPTION, test.getDescription());
        Assertions.assertEquals(PROBLEM_NAME, test.getProblemName());
    }

}