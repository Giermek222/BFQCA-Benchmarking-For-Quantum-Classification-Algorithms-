package com.example.bfqca_backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class })
public class BfqcaBackendApplication {

    public static void main(String[] args) {
        SpringApplication.run(BfqcaBackendApplication.class, args);
    }

}
