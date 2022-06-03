CREATE TABLE role (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE user_role(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT UNIQUE
);
CREATE TABLE user_info(
    id  INTEGER NOT NULL PRIMARY KEY,
    username TEXT UNIQUE
    email TEXT UNIQUE 
    password_hash INTEGER,
    token_secret INTEGER
);
CREATE TABLE user_log(
    id  INTEGER NOT NULL PRIMARY KEY 
    id_user_info TEXT  UNIQUE,
    client_ip INTEGER,
    timestamp TIMESTAMP,
    len INTEGER, rating INTEGER, count INTEGER
);
CREATE TABLE user_history(
    id  INTEGER NOT NULL PRIMARY KEY,
    id_user_info INTEGER,
    username TEXT, 
    email TEXT,
    password_hash TEXT,
    token_secret TEXT,
    timestamp  TIMESTAMP
);