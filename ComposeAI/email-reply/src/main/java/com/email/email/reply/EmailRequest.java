package com.email.email.reply;

import lombok.Data;

@Data
public class EmailRequest {
    private String emailContent;
    private String tone;
}