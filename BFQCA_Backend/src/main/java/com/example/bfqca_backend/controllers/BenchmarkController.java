package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.services.interfaces.BenchmarkService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/benchmarks")
public class BenchmarkController {

    BenchmarkService benchmarkService;
    SecurityService securityService;
}
