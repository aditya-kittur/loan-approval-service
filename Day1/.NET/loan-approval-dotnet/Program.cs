using LoanApproval.Models;
using LoanApproval.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();
builder.Services.AddSingleton<LoanApprovalService>();

var app = builder.Build();

app.MapOpenApi();

app.MapPost("/api/loans/evaluate", (LoanRequest request, LoanApprovalService service) =>
{
    var decision = service.Evaluate(request);
    return Results.Ok(decision);
})
.WithName("EvaluateLoan");

app.Run();