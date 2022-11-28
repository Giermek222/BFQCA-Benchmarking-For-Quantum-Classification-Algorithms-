package com.example.bfqca_backend.models.dao;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "algorithm")
public class AlgorithmDTO {
    @Id
    @Column(name = "id", nullable = false)
    private Long id;

    @Column(name = "algorithmName", nullable = false)
    private String algorithmName;

    @Column(name = "description", nullable = false)
    private String description;

    @Column(name = "problemName", nullable = false)
    private String problemName;

    public AlgorithmDTO(Long id, String algorithmName, String description, String problemName) {
        this.id = id;
        this.algorithmName = algorithmName;
        this.description = description;
        this.problemName = problemName;
    }

    public AlgorithmDTO() {
        algorithmName = "";
        description = "";
        problemName = "";
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getAlgorithmName() {
        return algorithmName;
    }

    public String getDescription() {
        return description;
    }

    public void setAlgorithmName(String algorithmName) {
        this.algorithmName = algorithmName;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getProblemName() {
        return problemName;
    }

    public void setProblemName(String problemName) {
        this.problemName = problemName;
    }
}
