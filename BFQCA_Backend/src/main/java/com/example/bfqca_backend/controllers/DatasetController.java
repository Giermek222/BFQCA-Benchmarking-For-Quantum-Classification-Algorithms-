package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.User;
import com.example.bfqca_backend.models.rest.DatasetRest;
import com.example.bfqca_backend.services.interfaces.DatasetService;
import com.example.bfqca_backend.utils.mappers.UserMapper;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;
import java.util.Objects;

@RestController
@RequestMapping("/dataset")
@CrossOrigin(origins = "*")
public class DatasetController {

    DatasetService datasetService;

    @GetMapping
    ResponseEntity<Object> getDatasets(@RequestHeader HttpHeaders headers) {
        List<String> datasets = datasetService.getDatasets();

        if (Objects.isNull(datasets)) {
            return ResponseEntity.badRequest().build();
        }
        else {
            return  ResponseEntity.ok(datasets);
        }
    }

    @PostMapping
    ResponseEntity<Object> addDataset(@RequestHeader HttpHeaders headers, @RequestBody @Valid DatasetRest dataset) {

    }
}
