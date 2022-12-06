package com.example.bfqca_backend.services.impl;

import com.example.bfqca_backend.services.interfaces.SecurityService;
import org.springframework.stereotype.Service;

@Service
public class SecurityServiceImpl implements SecurityService {
    @Override
    public boolean authenticateUser(String token) {
        return false;
    }
}
