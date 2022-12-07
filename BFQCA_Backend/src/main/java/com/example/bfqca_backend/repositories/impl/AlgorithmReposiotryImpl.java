package com.example.bfqca_backend.repositories.impl;

import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import com.example.bfqca_backend.models.filters.AlgorithmFilter;
import com.example.bfqca_backend.repositories.interfaces.AlgorithmRepository;
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
public class AlgorithmReposiotryImpl implements AlgorithmRepository {
    @Override
    public void addAlgorithm(AlgorithmDTO algorithmDTO) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("insert into algorithm (algorithmName, problemName, algorithmDescription) values (?,?,?) ");
            statement.setString(1, algorithmDTO.getAlgorithmName());
            statement.setString(2, algorithmDTO.getProblemName());
            statement.setString(3, algorithmDTO.getDescription());
            statement.executeUpdate();
            connection.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<AlgorithmDTO> getAlgorithms(AlgorithmFilter filter) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            StringBuilder query = new StringBuilder("select * from algorithm");
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
            List<AlgorithmDTO> foundAlgorithms = DatabaseMapper.getAlgorithms(resultSet);
            connection.close();
            return  foundAlgorithms;

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
