--create weather table
CREATE TABLE IF NOT EXISTS weather (
        id SERIAL PRIMARY KEY NOT NULL,
        date DATE,
        temperature INT,
        weather VARCHAR(255),
        wind INT,
        humidity INT,
        dewpoint INT,
        pressure INT,
        uv_index VARCHAR(255),
        visibility INT,
        moon_phase VARCHAR(255)
);

