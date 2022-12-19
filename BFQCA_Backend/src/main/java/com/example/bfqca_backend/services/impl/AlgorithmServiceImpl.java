package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.repositories.interfaces.AlgorithmRepository;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Service
public class AlgorithmServiceImpl implements AlgorithmService {

    private static final String TESTPATH = "python D:\\Wladek\repos\\BFQCA\\BFQCA_Backend\src\\main\resources\\hello.py ";
    @Autowired
    AlgorithmRepository algorithmRepository;


    @Override
    public void ExecuteAlgorithm(Algorithm algorithm, List<String> params, String Code) throws IOException {


        if (!Code.equals(null)) {
            algorithmRepository.addAlgorithm(AlgorithmMapper.mapBusinessToDto(algorithm));
            createNewPythonScript(Code);
        }
        runAlgorithm(algorithm, params);
    }

    @Override
    public List<Algorithm> GetAlgorithms(int page, int limit, RestFilter filter) {
        var algorithms = algorithmRepository.getAlgorithms(filter);
        List<Algorithm> returned = new ArrayList<>(){};
        for(AlgorithmDTO dto : algorithms) {
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

    private void createNewPythonScript(String Code) {
       //It should create new file with algorithmin folder with new algorithms. But we have no idea where is that folder right now
    }
}
