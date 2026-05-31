package com.email.email.reply.Controller;

import com.email.email.reply.Entity.Login;
import com.email.email.reply.Entity.Register;
import com.email.email.reply.Service.AuthService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/app")
@AllArgsConstructor
@CrossOrigin(
        origins = "*",
        allowedHeaders = "*",
        methods = {
                RequestMethod.GET,
                RequestMethod.POST,
                RequestMethod.PUT,
                RequestMethod.DELETE,
                RequestMethod.OPTIONS
        }
)
public class LoginRegisterController {

    private final AuthService authService;

    @PostMapping("/register")
    public ResponseEntity<String> register(
            @RequestBody Register register
    ) {

        String response =
                authService.register(register);

        return ResponseEntity.ok(response);
    }

    @PostMapping("/login")
    public ResponseEntity<String> login(
            @RequestBody Login login
    ) {

        String response =
                authService.login(login);

        return ResponseEntity.ok(response);
    }
}