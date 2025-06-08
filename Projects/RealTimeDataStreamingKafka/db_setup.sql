CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMPTZ,
    message TEXT
);

