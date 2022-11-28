package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.filters.AlgorithmFilter;
import com.example.bfqca_backend.models.rest.AlgorithmRest;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/algorithms")
public class AlgorithmController {

    AlgorithmService algorithmService;
    SecurityService securityService;

    @PostMapping("/execute")
    public ResponseEntity<Object> addAlgorithm(@RequestHeader HttpHeaders headers, @RequestBody @Valid AlgorithmRest algorithmRest) throws IOException {

        algorithmService.ExecuteAlgorithm(AlgorithmMapper.mapRestToBusiness(algorithmRest), algorithmRest.getParams());
        return  ResponseEntity.ok().build();
    }

    @PostMapping("/get")
    public ResponseEntity<Object> getAlgorithm(@RequestHeader HttpHeaders headers,
                                               @RequestParam(value = "page") int page,
                                               @RequestParam(value = "limit") int limit,
                                               @RequestBody(required = false) AlgorithmFilter filters) {
        var algorithms = algorithmService.GetAlgorithms(page, limit, filters);
        List<AlgorithmRest> restList = new ArrayList<>();
        for(Algorithm algorithm : algorithms) {
            restList.add(AlgorithmMapper.mapBusinessToRest(algorithm));
        }
        return  ResponseEntity.ok(restList);
    }


}
