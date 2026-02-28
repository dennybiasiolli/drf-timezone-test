-- insert start and end of Q1 2025 in New York, Rome and Tokyo
insert into test_timezone (value_str, value_dt, comment) values
    -- Los Angeles
    ('2025-01-01T00:00:00-08:00', '2025-01-01T00:00:00-08:00', 'start of Q1 2025 in LA'),
    ('2025-03-31T23:59:59.999999-07:00', '2025-03-31T23:59:59.999999-07:00', 'end of Q1 2025 in LA'),
    -- New York
    ('2025-01-01T00:00:00-05:00', '2025-01-01T00:00:00-05:00', 'start of Q1 2025 in NY'),
    ('2025-03-31T23:59:59.999999-04:00', '2025-03-31T23:59:59.999999-04:00', 'end of Q1 2025 in NY'),
    -- London
    ('2025-01-01T00:00:00+00:00', '2025-01-01T00:00:00+00:00', 'start of Q1 2025 in London'),
    ('2025-03-31T23:59:59.999999+01:00', '2025-03-31T23:59:59.999999+01:00', 'end of Q1 2025 in London'),
    -- Rome
    ('2025-01-01T00:00:00+01:00', '2025-01-01T00:00:00+01:00', 'start of Q1 2025 in Rome'),
    ('2025-03-31T23:59:59.999999+02:00', '2025-03-31T23:59:59.999999+02:00', 'end of Q1 2025 in Rome'),
    -- Tokyo
    ('2025-01-01T00:00:00+09:00', '2025-01-01T00:00:00+09:00', 'start of Q1 2025 in Tokyo'),
    ('2025-03-31T23:59:59.999999+09:00', '2025-03-31T23:59:59.999999+09:00', 'end of Q1 2025 in Tokyo'),
    -- Sydney
    ('2025-01-01T00:00:00+11:00', '2025-01-01T00:00:00+11:00', 'start of Q1 2025 in Sydney'),
    ('2025-03-31T23:59:59.999999+11:00', '2025-03-31T23:59:59.999999+11:00', 'end of Q1 2025 in Sydney');

-- or with timezone names instead of offsets
insert into test_timezone (value_str, value_dt, comment) values
    -- Los Angeles
    ('2025-01-01 00:00:00 America/Los_Angeles', '2025-01-01 00:00:00 America/Los_Angeles', 'start of Q1 2025 in LA'),
    ('2025-03-31T23:59:59.999999 America/Los_Angeles', '2025-03-31T23:59:59.999999 America/Los_Angeles', 'end of Q1 2025 in LA'),
    -- New York
    ('2025-01-01 00:00:00 America/New_York', '2025-01-01 00:00:00 America/New_York', 'start of Q1 2025 in NY'),
    ('2025-03-31 23:59:59.999999 America/New_York', '2025-03-31 23:59:59.999999 America/New_York', 'end of Q1 2025 in NY'),
    -- London
    ('2025-01-01 00:00:00 Europe/London', '2025-01-01 00:00:00 Europe/London', 'start of Q1 2025 in London'),
    ('2025-03-31 23:59:59.999999 Europe/London', '2025-03-31 23:59:59.999999 Europe/London', 'end of Q1 2025 in London'),
    -- Rome
    ('2025-01-01 00:00:00 Europe/Rome', '2025-01-01 00:00:00 Europe/Rome', 'start of Q1 2025 in Rome'),
    ('2025-03-31 23:59:59.999999 Europe/Rome', '2025-03-31 23:59:59.999999 Europe/Rome', 'end of Q1 2025 in Rome'),
    -- Tokyo
    ('2025-01-01 00:00:00 Asia/Tokyo', '2025-01-01 00:00:00 Asia/Tokyo', 'start of Q1 2025 in Tokyo'),
    ('2025-03-31 23:59:59.999999 Asia/Tokyo', '2025-03-31 23:59:59.999999 Asia/Tokyo', 'end of Q1 2025 in Tokyo'),
    -- Sydney
    ('2025-01-01 00:00:00 Australia/Sydney', '2025-01-01 00:00:00 Australia/Sydney', 'start of Q1 2025 in Sydney'),
    ('2025-03-31 23:59:59.999999 Australia/Sydney', '2025-03-31 23:59:59.999999 Australia/Sydney', 'end of Q1 2025 in Sydney');
