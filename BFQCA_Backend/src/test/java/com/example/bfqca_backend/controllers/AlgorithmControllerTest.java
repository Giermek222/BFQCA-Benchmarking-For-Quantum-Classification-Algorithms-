package com.example.bfqca_backend.controllers;

import com.example.bfqca_backend.models.business.Algorithm;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.services.interfaces.AlgorithmService;
import com.example.bfqca_backend.services.interfaces.SecurityService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.lenient;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(MockitoExtension.class)
@WebMvcTest(AlgorithmController.class)
class AlgorithmControllerTest {

    @MockBean
    private static AlgorithmService algorithmService;


    final static int PAGE = 0;
    final static int LIMIT = 100;

    @Autowired
    private MockMvc mockMvc;


    @Test
    @DisplayName("Save Algorithm - correct algorithm without params and code provided")
    void addAlgorithmWithCorrectDataButNoParams() throws Exception
    {
        final Algorithm algorithm = Algorithm.builder()
                .withAlgorithmName("Name")
                .withDescription("Desc")
                .withProblemName("problem")
                .build();

        doNothing().when(algorithmService).ExecuteAlgorithm(algorithm, null);

        mockMvc.perform(post("/algorithms/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"description\" : \"Desc\"," +
                                " \"problemName\" : \"problem\"}"))
                .andExpect(status().isOk());
    }



    @Test
    @DisplayName("Save Algorithm - correct algorithm with params and code provided")
    void addAlgorithmWithCorrectDataParamsAndCode() throws Exception
    {
        final Algorithm algorithm = Algorithm.builder()
                .withAlgorithmName("Name")
                .withDescription("Desc")
                .withProblemName("problem")
                .build();


        doNothing().when(algorithmService).ExecuteAlgorithm(algorithm,  "hello.py");

        mockMvc.perform(post("/algorithms/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"description\" : \"Desc\"," +
                                " \"problemName\" : \"problem\"}," +
                                " \"params\" : \"{\"132\",\"134\"}\"}," +
                                " \"code\" : \"print(hello)\""))
                .andExpect(status().isOk());
    }



    @Test
    @DisplayName("Save Algorithm - incorrect algorithm without ")
    void addAlgorithmWithInCorrectDataNoDescription() throws Exception
    {
        final Algorithm algorithm = Algorithm.builder()
                .withAlgorithmName("Name")
                .withProblemName("problem")
                .build();

        doNothing().when(algorithmService).ExecuteAlgorithm(algorithm,  null);

        mockMvc.perform(post("/algorithms/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"problemName\" : \"problem\"}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Save Algorithm - incorrect algorithm without ")
    void addAlgorithmWithInCorrectDataNoProblemName() throws Exception
    {
        final Algorithm algorithm = Algorithm.builder()
                .withAlgorithmName("Name")
                .withDescription("Desc")
                .build();

        doNothing().when(algorithmService).ExecuteAlgorithm(algorithm,  null);

        mockMvc.perform(post("/algorithms/execute")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\" : \"Name\"," +
                                " \"description\" : \"Desc\"}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Get Algorithm - No filter")
    void getAlgorithm() throws Exception
    {
        final RestFilter filter = new RestFilter();


        Mockito.doReturn(new ArrayList<Algorithm>()).when(algorithmService).GetAlgorithms(PAGE,LIMIT,filter);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/algorithms/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Get Algorithm - Partial filter with Algorithm name")
    void getAlgorithmPartialFilterAlg() throws Exception
    {
        final RestFilter filter = new RestFilter();


        Mockito.doReturn(new ArrayList<Algorithm>()).when(algorithmService).GetAlgorithms(PAGE,LIMIT,null);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/algorithms/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\":\"name\"}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Get Algorithm - Partial filter with Problem name")
    void getAlgorithmPartialFilterProblem() throws Exception
    {
        final RestFilter filter = new RestFilter();


        Mockito.doReturn(new ArrayList<Algorithm>()).when(algorithmService).GetAlgorithms(PAGE,LIMIT,filter);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/algorithms/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"problem\":\"name\"}"))
                .andExpect(status().isOk());
    }

    @Test
    @DisplayName("Get Algorithm - full filter")
    void getAlgorithmWithFilter() throws Exception
    {
        final RestFilter filter = new RestFilter();

        Mockito.doReturn(new ArrayList<Algorithm>()).when(algorithmService).GetAlgorithms(PAGE,LIMIT,filter);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("page", Integer.toString(PAGE));
        params.add("limit",Integer.toString(LIMIT));

        mockMvc.perform(post("/algorithms/get")
                        .params(params)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"algorithmName\":\"name\", " +
                                "\"problem\":\"name\"}"))
                .andExpect(status().isOk());
    }
}