package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.rest.AlgorithmRest;

public class AlgorithmMapper {

    public static Algorithm mapRestToBusiness(AlgorithmRest algorithmRest) {
        return  Algorithm.builder()
                .withAlgorithmName(algorithmRest.getAlgorithmName())
                .withUserName(algorithmRest.getUserName())
                .withDescription(algorithmRest.getDescription())
                .withProblemName(algorithmRest.getProblemName())
                .build();
    }
    
    public static AlgorithmRest mapBusinessToRest(Algorithm algorithm) {
        return AlgorithmRest.builder()
                .withAlgorithmName(algorithm.getAlgorithmName())
                .withUserName(algorithm.getUserName())
                .withDescription(algorithm.getDescription())
                .withProblemName(algorithm.getProblemName())
                .build();
    }

    public static AlgorithmDTO mapBusinessToDto(Algorithm algorithm) {
        return AlgorithmDTO.builder()
                .withAlgorithmName(algorithm.getAlgorithmName())
                .withProblemName(algorithm.getProblemName())
                .withUserName(algorithm.getUserName())
                .withDescription(algorithm.getDescription())
                .build();
    }

    public static Algorithm mapDtoToBusiness(AlgorithmDTO algorithmDTO) {
        return  Algorithm.builder()
                .withAlgorithmName(algorithmDTO.getAlgorithmName())
                .withDescription(algorithmDTO.getDescription())
                .withUserName(algorithmDTO.getUserName())
                .withProblemName(algorithmDTO.getProblemName())
                .build();
    }
}
