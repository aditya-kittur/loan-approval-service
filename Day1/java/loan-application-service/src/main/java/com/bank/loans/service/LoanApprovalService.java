package com.bank.loans.service;

import com.bank.loans.domain.LoanApplication;
import com.bank.loans.dto.LoanApplicationRequest;
import com.bank.loans.dto.LoanDecisionResponse;
import com.bank.loans.repository.LoanApplicationRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.Comparator;
import java.util.List;

@Service
public class LoanApprovalService {

    private static final Logger log = LoggerFactory.getLogger(LoanApprovalService.class);

    @Autowired
    private LoanApplicationRepository loanApplicationRepository;

    public LoanDecisionResponse processApplication(LoanApplicationRequest request) {
        log.info("Processing loan application for applicant: {}", request.getApplicantId());

        LoanApplication application = new LoanApplication();

        String status;
        BigDecimal rate;
        String message;

        if (request.getCreditScore() == null || request.getCreditScore() < 300) {
            status = "REJECTED";
            rate = null;
            message = "Credit score too low or not provided";
        } else if (request.getCreditScore() >= 750) {
            status = "APPROVED";
            rate = new BigDecimal("7.5");
            message = "Excellent credit profile";
        } else if (request.getCreditScore() >= 600) {
            status = "APPROVED";
            rate = new BigDecimal("12.0");
            message = "Standard credit profile";
        } else {
            status = "REJECTED";
            rate = null;
            message = "Credit score below minimum threshold";
        }

        return new LoanDecisionResponse(null, status, rate, message);
    }

    /**
     * Retrieves loan applications for an applicant sorted by creation date in descending order.
     *
     * @param applicantId applicant identifier
     * @return matching loan applications sorted newest first, or an empty list when applicantId is blank
     */
    public List<LoanApplication> getLoanApplicationsByApplicant(String applicantId) {
        if (applicantId == null || applicantId.isBlank()) {
            return List.of();
        }

        return loanApplicationRepository.findAll().stream()
                .filter(application -> applicantId.equals(application.getApplicantId()))
                .sorted(Comparator.comparing(
                        LoanApplication::getCreatedAt,
                        Comparator.nullsLast(Comparator.reverseOrder())
                ))
                .toList();
    }
}