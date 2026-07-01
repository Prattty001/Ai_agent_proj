from agent import DataValidationAgent

expected_schema = {
"order_id": "int64",
"customer_name": "object",
"amount": "int64",
"status": "object",
"order_date": "object"
}

agent = DataValidationAgent()

report = agent.validate(
"sample_data/orders.csv",
expected_schema
)

print(report)