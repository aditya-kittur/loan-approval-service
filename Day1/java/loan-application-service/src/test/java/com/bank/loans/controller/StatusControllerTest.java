package com.bank.loans.controller;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Unit tests for {@link StatusController} using MockMvc standalone setup.
 */
@ExtendWith(MockitoExtension.class)
class StatusControllerTest {

    /**
     * Verifies GET /api/status returns HTTP 200 and correct serviceName.
     */
    @Test
    void getStatus_returnsServiceMetadata_withHttp200() throws Exception {
        MockMvc mockMvc = MockMvcBuilders
                .standaloneSetup(new StatusController())
                .build();

        mockMvc.perform(get("/api/status"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.serviceName").value("loan-approval-service"));
    }
}
