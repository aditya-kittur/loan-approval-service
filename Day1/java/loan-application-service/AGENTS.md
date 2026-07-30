# AGENTS.md — loan-approval-service

## Service Overview
This is a retail banking loan approval microservice for Zenith Bank's personal lending platform.
It evaluates loan applications from individual customers based on credit score, annual income,
and employment status. It returns an approval/rejection decision with an applicable interest rate.
This service is consumed by the mobile banking app and the branch portal.

## Technology Stack
- Java 21 (use records for DTOs, pattern matching where it improves clarity)
- Spring Boot 3.2.x — never use deprecated APIs from Spring 5 or Spring Boot 2.x
- Maven — never suggest Gradle alternatives
- H2 in-memory database for dev/test; PostgreSQL in production

## How to Build
```bash
mvn clean compile          # compile only
mvn clean test             # compile + unit tests
mvn clean verify           # full build
```

## Architecture Compliance
- Controller layer: REST endpoints only. Zero business logic. Delegate entirely to service.
- Service layer: All business logic lives here. Stateless. Never calls another service directly.
- Repository layer: Spring Data JPA interfaces only. No native queries without documented justification.
- Domain layer (com.bank.loans.domain): Plain Java objects. Zero Spring annotations allowed.
- DTO layer (com.bank.loans.dto): Immutable Java records for all requests and responses.

## Coding guidelines
- Logging: SLF4J only. Declaration: private static final Logger log = LoggerFactory.getLogger(X.class);
- NEVER use System.out.println or java.util.logging
- Dependency injection: constructor injection only. NEVER field injection (@Autowired on a field).
- NEVER return null from a method that could return a collection — return Collections.emptyList() or List.of()
- NEVER use Optional.get() — always use orElseThrow() with a meaningful exception message
- All public methods must have Javadoc

## Testing Standards
- JUnit 5 + Mockito only (NOT JUnit 4, NOT PowerMock)
- Test class naming: {ClassUnderTest}Test.java
- Test method naming: methodName_givenCondition_expectedResult()
- Annotate all unit test classes with @ExtendWith(MockitoExtension.class)
- Minimum 80% branch coverage on the service layer

## Domain Glossary
- Applicant: The individual applying for the loan, identified by applicantId (a UUID string)
- Credit Score: Integer from 300 to 900 on the Indian CIBIL scale. Below 600 is high risk.
- Employment Status: One of: SALARIED, SELF_EMPLOYED, UNEMPLOYED, RETIRED
- Bureau: Credit bureau (CIBIL / Experian / CRIF) — external system, not integrated in v1

## What Agents Must Always Do
- Run mvn compile after any code change
- Add SLF4J logging at INFO level to every new service method entry point
- Add Javadoc to every new public method
- When adding a new service method, add a corresponding unit test

## Definition of Ready (DoR)
- The business requirement is clear and mapped to the correct layer (controller/service/repository).
- Input, output, and edge-case behavior are defined, including null/empty handling expectations.
- Any required DTO or domain model changes are identified before implementation.
- A test approach is identified before coding begins for each new or changed public method.

## Definition of Done (DoD)
- Code follows architecture and coding rules in this file and Java standards instructions.
- Every new or changed public method has Javadoc.
- Every new or changed public method has corresponding unit tests, including happy path and edge cases.
- No `System.out.println` is present; SLF4J logging is used where applicable.
- `mvn compile` passes successfully before considering the task complete.