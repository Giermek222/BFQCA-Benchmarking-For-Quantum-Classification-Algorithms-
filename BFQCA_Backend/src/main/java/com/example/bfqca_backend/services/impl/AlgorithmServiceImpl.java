package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.repositories.AlgorithmRepository;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.List;

@Service
public class AlgorithmServiceImpl implements AlgorithmService {

    private static final String TESTPATH = "./D:\\Wladek\repos\\BFQCA\\BFQCA_Backend\src\\main\resources\\hello.py ";
    @Autowired
    AlgorithmRepository algorithmRepository;


    @Override
    public void ExecuteAlgorithm(Algorithm algorithm, List<String> params) throws IOException {

        algorithmRepository.save(AlgorithmMapper.mapBusinessToDto(algorithm));
        runAlgorithm(algorithm, params);
    }

    private void runAlgorithm(Algorithm algorithm, List<String> params) throws IOException {
        StringBuilder command = new StringBuilder();
        command.append(TESTPATH);
        command.append(algorithm.getProblemName());
        command.append(" ");
        for (String p : params) {
            command.append(" " + p);
        }
        Runtime.getRuntime().exec(command.toString());
    }
}
