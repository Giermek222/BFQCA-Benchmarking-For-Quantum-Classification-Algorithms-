package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.repositories.interfaces.DatasetReporitory;
import com.example.bfqca_backend.services.interfaces.DatasetService;
import com.example.bfqca_backend.utils.file_utils.FileSaver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.nio.file.Paths;
import java.util.List;

@Service
public class DatasetServiceImpl implements DatasetService {

    @Autowired
    DatasetReporitory datasetReporitory;
    static final String rootDirectory = Paths.get(".").toAbsolutePath().getParent().getParent().toAbsolutePath().normalize().toString();

    private static final String pathWithDatasets = rootDirectory + "\\BFQCA_Cowskit\\custom_datasets\\";

    @Override
    public void saveDataset(String datasetName, String datasetCode) {
        FileSaver.savefile(datasetCode, datasetName, pathWithDatasets);
        datasetReporitory.saveDataset(datasetName);
    }

    @Override
    public List<String> getDatasets() {
        return datasetReporitory.getDatasets();
    }
}
