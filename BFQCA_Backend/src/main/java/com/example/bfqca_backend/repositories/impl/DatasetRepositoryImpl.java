package com.example.bfqca_backend.repositories.impl;

import com.example.bfqca_backend.repositories.interfaces.DatasetReporitory;
import com.example.bfqca_backend.utils.database.DatabaseConnector;
import com.example.bfqca_backend.utils.database.DatabaseMapper;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestBody;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
public class DatasetRepositoryImpl implements DatasetReporitory {

    @Override
    public List<String> getDatasets() {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("select * from dataset");
            ResultSet resultSet = statement.executeQuery();
            List<String> datasets = DatabaseMapper.getDataset(resultSet);
            connection.close();
            return datasets;

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void saveDataset(String datasetName) {
        try {
            Connection connection = DatabaseConnector.connectToDatabase();
            PreparedStatement statement = connection.prepareStatement("insert into dataset (problemName) values (?)");
            statement.setString(1, datasetName);
            statement.executeUpdate();
            connection.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
