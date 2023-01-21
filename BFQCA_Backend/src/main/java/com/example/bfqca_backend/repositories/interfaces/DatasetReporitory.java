package com.example.bfqca_backend.repositories.interfaces;

import java.util.List;

public interface DatasetReporitory {

    public List<String> getDatasets();
    public void saveDataset(String datasetName);
}
