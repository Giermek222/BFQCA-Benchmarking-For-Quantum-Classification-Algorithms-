package com.example.bfqca_backend.utils.database;

import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.dao.BenchmarkDTO;
import com.example.bfqca_backend.models.dao.UserDTO;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class DatabaseMapper {
    public static List<UserDTO> getUsers(ResultSet resultSet) throws SQLException {
        List<UserDTO> usersFromDb = new ArrayList<>();

        while (resultSet.next()) {
            usersFromDb.add(
                    UserDTO.builder()
                            .withId(resultSet.getLong("id"))
                            .withUserName(resultSet.getString("userName"))
                            .withPassword(resultSet.getString("password"))
                            .withToken(resultSet.getString("token"))
                            .build()
            );
        }
        return usersFromDb;
    }

    public static List<AlgorithmDTO> getAlgorithms(ResultSet resultSet) throws SQLException {
        List<AlgorithmDTO> algorithmDTOList = new ArrayList<>();

        while (resultSet.next()) {
            algorithmDTOList.add(
                    AlgorithmDTO.builder()
                            .withId(resultSet.getLong("id"))
                            .withAlgorithmName(resultSet.getString("algorithmName"))
                            .withProblemName(resultSet.getString("problemName"))
                            .withDescription(resultSet.getString("algorithmDescription"))
                            .withUserName(resultSet.getString("author"))
                            .build()
            );
        }
        return algorithmDTOList;
    }

    public static List<BenchmarkDTO> getBenchmarks(ResultSet resultSet) throws SQLException {
        List<BenchmarkDTO> benchmarkDTOS = new ArrayList<>();

        while (resultSet.next()) {
            benchmarkDTOS.add(
                    BenchmarkDTO.builder()
                            .withId(resultSet.getLong("id"))
                            .withAlgorithmName(resultSet.getString("algorithmName"))
                            .withProblemName(resultSet.getString("problemName"))
                            .withAccuracyLearning(resultSet.getDouble("accuracyLearning"))
                            .withAccuracyTest(resultSet.getDouble("accuracyTest"))
                            .withLossTest(resultSet.getDouble("lossTest"))
                            .withMaxLatency(resultSet.getDouble("maxLatency"))
                            .withMinLatency(resultSet.getDouble("minLatency"))
                            .withAvgLatency(resultSet.getDouble("avgLatency"))
                            .withLatencyPercentile(resultSet.getDouble("latencyPercentile"))
                            .withTime(resultSet.getDouble("time"))
                            .build()
            );
        }
        return benchmarkDTOS;
    }
}
