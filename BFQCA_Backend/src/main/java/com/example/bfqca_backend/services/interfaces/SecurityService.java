package com.example.bfqca_backend.services.interfaces;

import org.springframework.stereotype.Service;

@Service
public interface SecurityService {

    public boolean authenticateUser(String token);
}
