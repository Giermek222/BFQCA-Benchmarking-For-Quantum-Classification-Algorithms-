package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.repositories.interfaces.AlgorithmRepository;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.utils.file_utils.FileSaver;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class AlgorithmServiceImpl implements AlgorithmService {

    static final String rootDirectory =Paths.get(".").toAbsolutePath().getParent().getParent().toAbsolutePath().normalize().toString();
    private static final String pathToPythonScript = rootDirectory + "\\BFQCA_Cowskit\\main.py";
    private static final String pathWithAlgorithms = rootDirectory + "\\BFQCA_Cowskit\\custom_algorithms\\";
    private static final String pathToExecutionFolder = rootDirectory + "\\BFQCA_Cowskit";

    private static final String pathToTestFolder = rootDirectory + "\\BFQCA_Backend\\src\\main\\resources\\hello.py";
    @Autowired
    AlgorithmRepository algorithmRepository;


    @Override
    public void ExecuteAlgorithm(Algorithm algorithm, String Code) throws IOException {
        if (Code != null) {
            algorithmRepository.addAlgorithm(AlgorithmMapper.mapBusinessToDto(algorithm));
            FileSaver.savefile(Code, algorithm.getAlgorithmName(), pathWithAlgorithms);
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
        Process p = new ProcessBuilder(
            "python",
                pathToPythonScript,
                "-a", algorithm.getAlgorithmName(),
                "-d", algorithm.getProblemName()
        ).directory(new File(pathToExecutionFolder)).start();
    }

}
