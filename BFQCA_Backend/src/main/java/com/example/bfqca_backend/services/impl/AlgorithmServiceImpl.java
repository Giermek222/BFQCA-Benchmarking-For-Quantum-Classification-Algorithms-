package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.repositories.interfaces.AlgorithmRepository;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class AlgorithmServiceImpl implements AlgorithmService {

    private static final String TESTPATH = "python D:\\Wladek\\repos\\inzynierka\\BFQCA-Benchmarking-For-Quantum-Classification-Algorithms-\\BFQCA_Backend\\src\\main\\resources\\hello.py ";
    private static final String ALGORITMPATH = "D:\\Wladek\\repos\\inzynierka\\BFQCA-Benchmarking-For-Quantum-Classification-Algorithms-\\BFQCA_Backend\\src\\main\\resources\\python_algorithms\\";
    @Autowired
    AlgorithmRepository algorithmRepository;


    @Override
    public void ExecuteAlgorithm(Algorithm algorithm, String Code) throws IOException {
        if (Code != null) {
            algorithmRepository.addAlgorithm(AlgorithmMapper.mapBusinessToDto(algorithm));
            createNewPythonScript(Code, algorithm.getAlgorithmName());
        }

        runAlgorithm(algorithm);
    }

    @Override
    public List<Algorithm> GetAlgorithms(int page, int limit, RestFilter filter) {
        var algorithms = algorithmRepository.getAlgorithms(filter);
        List<Algorithm> returned = new ArrayList<>(){};
        for(AlgorithmDTO dto : algorithms) {
            returned.add(AlgorithmMapper.mapDtoToBusiness(dto));
        }
        return returned.stream()
                .skip((long) page * limit)
                .limit(limit)
                .collect(Collectors.toList());
    }

    private void runAlgorithm(Algorithm algorithm) throws IOException {
        StringBuilder command = new StringBuilder();
        command.append(TESTPATH);
        Runtime.getRuntime().exec(command.toString());
    }

    private void createNewPythonScript(String Code, String algorithmName) {
        try {
            File myObj = new File( ALGORITMPATH + algorithmName + ".py");
            if (myObj.createNewFile()) {
                Files.writeString(myObj.toPath(), Code);
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
