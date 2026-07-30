package com.bank.loans.dto;

/**
 * Response record for the /api/status endpoint.
 * Provides service metadata for Kubernetes liveness and readiness probes.
 */
public record StatusResponse(
        String serviceName,
        String version,
        String environment,
        long uptimeSeconds
) {}
