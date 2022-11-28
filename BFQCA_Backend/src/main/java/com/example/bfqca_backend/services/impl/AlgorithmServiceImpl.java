package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.filters.AlgorithmFilter;
import com.example.bfqca_backend.repositories.AlgorithmRepository;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

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

    @Override
    public List<Algorithm> GetAlgorithms(int page, int limit, AlgorithmFilter filter) {
        var algorithms = algorithmRepository.findAll();
        boolean filteredByName = filter.getAlgorithmname() != null;
        boolean filteredByProblem = filter.getProblem() != null;
        List<Algorithm> returned = new ArrayList<>(){};
        for(AlgorithmDTO dto : algorithms) {
            if (filteredByName){
                if (!dto.getAlgorithmName().equals(filter.getAlgorithmname()))
                    continue;
            }
            if (filteredByProblem) {
                if (!dto.getProblemName().equals(filter.getProblem()))
                    continue;
            }
            returned.add(AlgorithmMapper.mapDtoToBusiness(dto));
        }
        return returned;
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
