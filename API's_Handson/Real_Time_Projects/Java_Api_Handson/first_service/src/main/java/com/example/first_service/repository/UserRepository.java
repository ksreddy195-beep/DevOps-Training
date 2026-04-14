package com.example.first_service.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.first_service.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
}