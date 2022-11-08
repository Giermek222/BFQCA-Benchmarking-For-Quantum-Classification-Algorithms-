package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/algorithms")
public class AlgorithmController {

    AlgorithmService algorithmService;
    SecurityService securityService;

}
