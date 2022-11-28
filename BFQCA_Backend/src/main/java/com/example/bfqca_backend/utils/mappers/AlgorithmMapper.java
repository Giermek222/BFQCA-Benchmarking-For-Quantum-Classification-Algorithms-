package com.example.bfqca_backend.utils.mappers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.rest.AlgorithmRest;

public class AlgorithmMapper {

    public static Algorithm mapRestToBusiness(AlgorithmRest algorithmRest) {
        return  Algorithm.builder()
                .withAlgorithmName(algorithmRest.getAlgorithmName())
                .withDescription(algorithmRest.getDescription())
                .withProblemName(algorithmRest.getProblemName())
                .build();
    }
    
    public static AlgorithmRest mapBusinessToRest(Algorithm algorithm) {
        return AlgorithmRest.builder()
                .withAlgorithmName(algorithm.getAlgorithmName())
                .withDescription(algorithm.getDescription())
                .withProblemName(algorithm.getProblemName())
                .build();
    }

    public static AlgorithmDTO mapBusinessToDto(Algorithm algorithm) {
        AlgorithmDTO algorithmDTO = new AlgorithmDTO();
        algorithmDTO.setAlgorithmName(algorithm.getAlgorithmName());
        algorithmDTO.setDescription(algorithm.getDescription());
        algorithmDTO.setProblemName(algorithm.getProblemName());
        return algorithmDTO;
    }

    public static Algorithm mapDtoToBusiness(AlgorithmDTO algorithmDTO) {
        return  Algorithm.builder()
                .withAlgorithmName(algorithmDTO.getAlgorithmName())
                .withDescription(algorithmDTO.getDescription())
                .withProblemName(algorithmDTO.getProblemName())
                .build();
    }
}
