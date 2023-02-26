CREATE DATABASE fashion_week;

USE fashion_week;

CREATE TABLE defiles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    ville VARCHAR(255) NOT NULL,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    maison VARCHAR(255) NOT NULL,
    designer_principal VARCHAR(255) NOT NULL
);

INSERT INTO defiles (nom, ville, date_debut, date_fin, maison, designer_principal)
VALUES
("Fashion Week de Paris", "Paris", "2022-01-17", "2022-01-23", "Louis Vuitton", "Colm Dillane"),
("Fashion Week de Milan", "Milan", "2022-02-23", "2022-03-01", "Gucci", "Alessandro Michele"),
("Fashion Week de Londres", "Londres", "2022-02-12", "2022-02-16", "Burberry", "Riccardo Tisci");