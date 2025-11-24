curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-01-01T00:00:00-08:00",
        "value_dt": "2025-01-01T00:00:00-08:00",
        "comment": "start of Q1 2025 in LA"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-03-31T23:59:59.999999-07:00",
        "value_dt": "2025-03-31T23:59:59.999999-07:00",
        "comment": "end of Q1 2025 in LA"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-01-01T00:00:00-05:00",
        "value_dt": "2025-01-01T00:00:00-05:00",
        "comment": "start of Q1 2025 in NY"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-03-31T23:59:59.999999-04:00",
        "value_dt": "2025-03-31T23:59:59.999999-04:00",
        "comment": "end of Q1 2025 in NY"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-01-01T00:00:00+00:00",
        "value_dt": "2025-01-01T00:00:00+00:00",
        "comment": "start of Q1 2025 in London"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-03-31T23:59:59.999999+01:00",
        "value_dt": "2025-03-31T23:59:59.999999+01:00",
        "comment": "end of Q1 2025 in London"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-01-01T00:00:00+01:00",
        "value_dt": "2025-01-01T00:00:00+01:00",
        "comment": "start of Q1 2025 in Rome"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-03-31T23:59:59.999999+02:00",
        "value_dt": "2025-03-31T23:59:59.999999+02:00",
        "comment": "end of Q1 2025 in Rome"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-01-01T00:00:00+09:00",
        "value_dt": "2025-01-01T00:00:00+09:00",
        "comment": "start of Q1 2025 in Tokyo"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-03-31T23:59:59.999999+09:00",
        "value_dt": "2025-03-31T23:59:59.999999+09:00",
        "comment": "end of Q1 2025 in Tokyo"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-01-01T00:00:00+11:00",
        "value_dt": "2025-01-01T00:00:00+11:00",
        "comment": "start of Q1 2025 in Sydney"
    }'
curl -X POST http://localhost:8002/api/timezone-tests/ \
    -H "Content-Type: application/json" \
    -d '{
        "value_str": "2025-03-31T23:59:59.999999+11:00",
        "value_dt": "2025-03-31T23:59:59.999999+11:00",
        "comment": "end of Q1 2025 in Sydney"
    }'
