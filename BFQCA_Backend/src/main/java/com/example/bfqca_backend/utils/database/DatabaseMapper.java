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

    public static List<String> getDataset(ResultSet resultSet) throws SQLException {
        List<String> datasetsFromDb = new ArrayList<>();

        while (resultSet.next()) {
            datasetsFromDb.add(
                    resultSet.getString("problemName")
            );
        }
        return datasetsFromDb;
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
                            .withAlgorithmName(resultSet.getString("algorithm_name"))
                            .withProblemName(resultSet.getString("problem_name"))
                            .withTrainingAccuracy(resultSet.getDouble("training_accuracy"))
                            .withTrainingPrecision(resultSet.getDouble("training_precision"))
                            .withTrainingRecall(resultSet.getDouble("training_recall"))
                            .withTrainingF1Score(resultSet.getDouble("training_f1_score"))
                            .withTrainingLoss(resultSet.getDouble("training_loss"))
                            .withTestAccuracy(resultSet.getDouble("test_accuracy"))
                            .withTestPrecision(resultSet.getDouble("test_precision"))
                            .withTestF1Score(resultSet.getDouble("test_recall"))
                            .withTestRecall(resultSet.getDouble("test_f1_score"))
                            .withTestLoss(resultSet.getDouble("test_loss"))
                            .withMaxLatencyMs(resultSet.getDouble("max_latency_ms"))
                            .withMinLatencyMs(resultSet.getDouble("min_latency_ms"))
                            .withAvgLatencyMs(resultSet.getDouble("avg_latency_ms"))
                            .withPercentileLatencyMs(resultSet.getDouble("percentile_latency_ms"))
                            .withTime(resultSet.getDouble("time"))
                            .build()
            );
        }
        return benchmarkDTOS;
    }
}
