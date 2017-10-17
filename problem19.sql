SELECT date FROM generate_series('1901-01-01'::timestamp, '2000-12-31'::timestamp, '1 day') AS date WHERE extract(DAY FROM date) = 1 AND extract(DOW FROM date) = 0;
