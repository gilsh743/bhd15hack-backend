CREATE TABLE translated_text (
    id int NOT NULL AUTO_INCREMENT,
    orig varchar(255),
    translated varchar(255),
    PRIMARY KEY (id)
);

INSERT INTO translated_text (orig, translated) VALUES ("hi", "يث")