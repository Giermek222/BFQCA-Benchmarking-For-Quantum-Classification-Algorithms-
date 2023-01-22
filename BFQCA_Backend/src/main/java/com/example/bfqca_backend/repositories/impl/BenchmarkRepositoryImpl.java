package com.example.bfqca_backend.repositories.impl;

import com.example.bfqca_backend.models.dao.BenchmarkDTO;
import com.example.bfqca_backend.models.filters.RestFilter;
import com.example.bfqca_backend.repositories.interfaces.BenchmarkRepository;
import com.example.bfqca_backend.utils.database.DatabaseConnector;
import com.example.bfqca_backend.utils.database.DatabaseMapper;
import org.springframework.stereotype.Repository;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Objects;
@Repository
public class BenchmarkRepositoryImpl  implements BenchmarkRepository {
    @Override
    public List<BenchmarkDTO> getBenchmarks(RestFilter filter) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            StringBuilder query = new StringBuilder("select * from benchmark");
            if (Objects.nonNull(filter.getAlgorithmname()) && Objects.nonNull(filter.getProblem()))
                query.append(" where algorithm_name LIKE ? and problem_name LIKE ? ");
            else if (Objects.nonNull(filter.getAlgorithmname()))
                query.append(" where where algorithm_name LIKE ?");
            else if (Objects.nonNull(filter.getProblem()))
                query.append(" where problem_name LIKE ? ");


            PreparedStatement statement = connection.prepareStatement(query.toString());

            if (Objects.nonNull(filter.getAlgorithmname()) && Objects.nonNull(filter.getProblem())) {
                statement.setString(1, "%" + filter.getAlgorithmname() + "%");
                statement.setString(2, "%" + filter.getProblem() + "%");
            }
            else if (Objects.nonNull(filter.getAlgorithmname())) {
                statement.setString(1, "%" + filter.getAlgorithmname() + "%");

            }
            else if (Objects.nonNull(filter.getProblem()))
            {
                statement.setString(1, "%" + filter.getProblem() + "%");
            }
            ResultSet resultSet = statement.executeQuery();
            List<BenchmarkDTO> foundBenchmarks = DatabaseMapper.getBenchmarks(resultSet);
            connection.close();
            return  foundBenchmarks;

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void addBenchmark(BenchmarkDTO benchmarkDTO) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement(
                    "insert into benchmark " +

                            "(algorithm_name, problem_name, training_accuracy, training_precision, training_recall, training_f1_score, training_loss, test_accuracy, test_precision, test_recall, test_f1_score, test_loss, max_latency_ms, min_latency_ms, avg_latency_ms, percentile_latency_ms, time) " +
                            "values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ");
            statement.setString(1, benchmarkDTO.getAlgorithmName());
            statement.setString(2, benchmarkDTO.getProblemName());
            statement.setDouble(3, benchmarkDTO.getTrainingAccuracy());
            statement.setDouble(4, benchmarkDTO.getTrainingPrecision());
            statement.setDouble(5, benchmarkDTO.getTrainingRecall());
            statement.setDouble(6, benchmarkDTO.getTrainingF1Score());
            statement.setDouble(7, benchmarkDTO.getTrainingLoss());
            statement.setDouble(8, benchmarkDTO.getTestAccuracy());
            statement.setDouble(9, benchmarkDTO.getTestPrecision());
            statement.setDouble(10, benchmarkDTO.getTestRecall());
            statement.setDouble(11, benchmarkDTO.getTestF1Score());
            statement.setDouble(12, benchmarkDTO.getTestLoss());
            statement.setDouble(13, benchmarkDTO.getMaxLatencyMs());
            statement.setDouble(14, benchmarkDTO.getMinLatencyMs());
            statement.setDouble(15, benchmarkDTO.getAvgLatencyMs());
            statement.setDouble(16, benchmarkDTO.getPercentileLatencyMs());
            statement.setDouble(17, benchmarkDTO.getTime());
            statement.executeUpdate();
            connection.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
