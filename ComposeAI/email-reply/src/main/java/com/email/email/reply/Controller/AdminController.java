package com.email.email.reply.Controller;

import com.email.email.reply.Entity.Register;
import com.email.email.reply.Repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/admin")
@AllArgsConstructor
@CrossOrigin("*")
public class AdminController {

    private final UserRepository userRepository;

    @GetMapping("/users")
    public List<Register> getAllUsers(){

        return userRepository.findAll();
    }
}