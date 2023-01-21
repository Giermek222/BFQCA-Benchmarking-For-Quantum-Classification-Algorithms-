package com.example.bfqca_backend.services.interfaces;

import java.util.List;

public interface DatasetService {

    public void saveDataset(String datasetName, String databaseCode);
    public List<String> getDatasets();
}
