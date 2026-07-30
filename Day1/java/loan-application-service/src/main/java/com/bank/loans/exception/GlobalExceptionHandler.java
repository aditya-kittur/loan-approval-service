package com.bank.loans.exception;

import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<List<Map<String, String>>> handleValidationExceptions(MethodArgumentNotValidException ex) {
        List<Map<String, String>> errors = ex.getBindingResult()
                .getFieldErrors()
                .stream()
                .map(this::toError)
                .toList();

        return ResponseEntity.badRequest().body(errors);
    }

    private Map<String, String> toError(FieldError fieldError) {
        Map<String, String> error = new HashMap<>();
        error.put("field", fieldError.getField());
        error.put("error", fieldError.getDefaultMessage());
        return error;
    }
}
