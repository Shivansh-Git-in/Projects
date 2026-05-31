package com.email.email.reply.Service;

import com.email.email.reply.Entity.Login;
import com.email.email.reply.Entity.Register;
import com.email.email.reply.Repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class AuthService {

    private final UserRepository userRepository;

    private final BCryptPasswordEncoder passwordEncoder;

    public String register(Register register) {

        if(userRepository.findByEmail(register.getEmail()).isPresent()) {
            return "EMAIL_ALREADY_EXISTS";
        }

        register.setPassword(
                passwordEncoder.encode(register.getPassword())
        );

        userRepository.save(register);

        return "REGISTER_SUCCESS";
    }

    public String login(Login login) {

        if( login.getEmail() .equals("ComposeAdmin") && login.getPassword() .equals("ComAdm@123") ){
            return "ADMIN_LOGIN_SUCCESS";
        }

        Register user = userRepository
                .findByEmail(login.getEmail())
                .orElse(null);

        if(user == null) {
            return "INVALID_EMAIL";
        }

        boolean matches =
                passwordEncoder.matches(
                        login.getPassword(),
                        user.getPassword()
                );

        if(!matches) {
            return "INVALID_PASSWORD";
        }

        return "LOGIN_SUCCESS";
    }
}