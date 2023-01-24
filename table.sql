CREATE TABLE IF NOT EXISTS USER_TOKEN (
  ID varchar(64) primary key
);

CREATE  TABLE IF NOT EXISTS DATA_MAPS (
  ID integer primary key,
  Name varchar(20),
  Hint text
);
