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
                query.append(" where algorithmName = ? and problemName = ? ");
            else if (Objects.nonNull(filter.getAlgorithmname()))
                query.append(" where where algorithmName = ?");
            else if (Objects.nonNull(filter.getProblem()))
                query.append(" where problemName = ? ");


            PreparedStatement statement = connection.prepareStatement(query.toString());

            if (Objects.nonNull(filter.getAlgorithmname()) && Objects.nonNull(filter.getProblem())) {
                statement.setString(1, filter.getAlgorithmname());
                statement.setString(2, filter.getProblem());
            }
            else if (Objects.nonNull(filter.getAlgorithmname())) {
                statement.setString(1, filter.getAlgorithmname());

            }
            else if (Objects.nonNull(filter.getProblem()))
            {
                statement.setString(1, filter.getProblem());
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
                            "(algorithmName, problemName, accuracyLearning, accuracyTest, lossTest, lossLearning, maxLatency, minLatency, avgLatency, latencyPercentile, time) " +
                            "values (?,?,?,?,?,?,?,?,?,?,?) ");
            statement.setString(1, benchmarkDTO.getAlgorithmName());
            statement.setString(2, benchmarkDTO.getProblemName());
            statement.setDouble(3, benchmarkDTO.getAccuracyLearning());
            statement.setDouble(4, benchmarkDTO.getAccuracyTest());
            statement.setDouble(5, benchmarkDTO.getLossTest());
            statement.setDouble(6, benchmarkDTO.getLossLearning());
            statement.setDouble(7, benchmarkDTO.getMaxLatency());
            statement.setDouble(8, benchmarkDTO.getMinLatency());
            statement.setDouble(9, benchmarkDTO.getAvgLatency());
            statement.setDouble(10, benchmarkDTO.getLatencyPercentile());
            statement.setDouble(11, benchmarkDTO.getTime());
            statement.executeUpdate();
            connection.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
