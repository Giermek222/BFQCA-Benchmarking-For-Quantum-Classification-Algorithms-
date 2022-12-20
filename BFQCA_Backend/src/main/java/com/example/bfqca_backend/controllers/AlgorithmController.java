package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.models.rest.AlgorithmRest;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import com.example.bfqca_backend.utils.mappers.AlgorithmMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@RestController
@RequestMapping("/algorithms")
public class AlgorithmController {

    @Autowired
    AlgorithmService algorithmService;
    SecurityService securityService;

    @PostMapping("/execute")
    public ResponseEntity<Object> addAlgorithm(@RequestHeader HttpHeaders headers, @RequestBody @Valid AlgorithmRest algorithmRest) throws IOException {
        if (Objects.isNull(algorithmRest.getAlgorithmName()) || Objects.isNull(algorithmRest.getDescription()) || Objects.isNull(algorithmRest.getProblemName())  ) {
            return ResponseEntity.badRequest().build();
        }
        algorithmService.ExecuteAlgorithm(AlgorithmMapper.mapRestToBusiness(algorithmRest), algorithmRest.getParams(), algorithmRest.getCode());
        return  ResponseEntity.ok().build();
    }

    @PostMapping("/get")
    public ResponseEntity<Object> getAlgorithm(@RequestHeader HttpHeaders headers,
                                               @RequestParam(value = "page") int page,
                                               @RequestParam(value = "limit") int limit,
                                               @RequestBody(required = false) RestFilter filters) {
        if (Objects.isNull(filters))
            filters = new RestFilter();
        var algorithms = algorithmService.GetAlgorithms(page, limit, filters);
        List<AlgorithmRest> restList = new ArrayList<>();
        for(Algorithm algorithm : algorithms) {
            restList.add(AlgorithmMapper.mapBusinessToRest(algorithm));
        }
        return  ResponseEntity.ok(restList);
    }


}
