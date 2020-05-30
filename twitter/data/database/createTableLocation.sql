DROP TABLE IF EXISTS Location
CREATE TABLE IF NOT EXISTS Location (
                                 woeid int(15) NOT NULL,
                                 name varchar(250)  NULL,
                                 country varchar(250)  NULL,
                                 parentid int(15) NOT NULL,
                                 PRIMARY KEY (woeid))