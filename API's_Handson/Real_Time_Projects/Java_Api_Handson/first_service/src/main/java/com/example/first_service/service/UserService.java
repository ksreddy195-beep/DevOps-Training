package com.example.first_service.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.first_service.entity.User;
import com.example.first_service.repository.UserRepository;

@Service
public class UserService {

    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    // CREATE
    public User createUser(User user) {
        return repository.save(user);
    }

    // READ ALL
    public List<User> getAllUsers() {
        return repository.findAll();
    }

    // READ BY ID
    public User getUserById(Long id) {
        return repository.findById(id)
                .orElseThrow(() -> new RuntimeException("User not found with id " + id));
    }

    // UPDATE
    public User updateUser(Long id, User updatedUser) {
        User user = getUserById(id);
        user.setName(updatedUser.getName());
        user.setEmail(updatedUser.getEmail());
        return repository.save(user);
    }

    // DELETE
    public void deleteUser(Long id) {
        repository.deleteById(id);
    }
}
