package com.bank.loans.controller;

import com.bank.loans.dto.StatusResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.lang.management.ManagementFactory;

/**
 * REST controller providing service metadata for Kubernetes probes.
 */
@RestController
@RequestMapping("/api")
public class StatusController {

    private static final Logger log = LoggerFactory.getLogger(StatusController.class);

    @Value("${spring.profiles.active:development}")
    private String activeProfile;

    /**
     * Returns service metadata including name, version, environment, and uptime.
     *
     * @return HTTP 200 with {@link StatusResponse} payload
     */
    @GetMapping("/status")
    public ResponseEntity<StatusResponse> getStatus() {
        log.info("Returning service status metadata");
        long uptimeSeconds = ManagementFactory.getRuntimeMXBean().getUptime() / 1000L;
        StatusResponse response = new StatusResponse(
                "loan-approval-service",
                "1.0.0-SNAPSHOT",
                activeProfile,
                uptimeSeconds
        );
        return ResponseEntity.ok(response);
    }
}
