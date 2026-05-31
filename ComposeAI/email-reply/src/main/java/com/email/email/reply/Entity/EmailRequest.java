package com.email.email.reply.Entity;

import lombok.Data;

@Data
public class EmailRequest {
    private String email;
    private String emailContent;
    private String tone;
}