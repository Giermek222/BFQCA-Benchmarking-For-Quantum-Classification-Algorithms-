package com.example.bfqca_backend.repositories;

import com.example.bfqca_backend.models.dao.AlgorithmDTO;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AlgorithmRepository extends PagingAndSortingRepository<AlgorithmDTO, Long> {
}
