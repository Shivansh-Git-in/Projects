package com.email.email.reply.Repository;

import com.email.email.reply.Entity.Register;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserRepository extends JpaRepository<Register, Long> {

    Optional<Register> findByEmail(String email);
}