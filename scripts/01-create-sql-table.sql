drop table if exists test_timezone;
create table test_timezone (
    id serial primary key,
    value_str varchar(100) not null,
    value_dt timestamptz not null,
    comment varchar(100) not null
);
