CREATE DATABASE sistema_votacao;
USE sistema_votacao;

-- TABELA DE PARTIDOS
CREATE TABLE partidos (
    id_part INT AUTO_INCREMENT PRIMARY KEY,
    nome_partido VARCHAR(100) NOT NULL
);


-- TABELA DE CANDIDATOS
CREATE TABLE candidatos (
    num INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_part INT NOT NULL,

    CONSTRAINT fk_candidato_partido
        FOREIGN KEY (id_part)
        REFERENCES partidos(id_part)
);


-- TABELA DE ELEITORES
CREATE TABLE eleitores (
    id_ele INT AUTO_INCREMENT PRIMARY KEY,
    nome_ele VARCHAR(100) NOT NULL,
    titulo_ele VARCHAR(12) NOT NULL UNIQUE,
    cpf_ele VARCHAR(50) NOT NULL,
    mesario_ele BOOLEAN NOT NULL DEFAULT FALSE,
    senha_ele VARCHAR(20) NOT NULL,
    status_ele BOOLEAN NOT NULL DEFAULT FALSE
);


-- TABELA DE VOTO
CREATE TABLE votos (
    id_voto INT AUTO_INCREMENT PRIMARY KEY,

    num_cand INT NOT NULL,

    datahora_voto DATETIME NOT NULL,

    protocolo VARCHAR(50) NOT NULL,

    CONSTRAINT fk_voto_candidato
        FOREIGN KEY (num_cand)
        REFERENCES candidatos(num)
);

-- Inserindo Dados
INSERT INTO partidos (nome_partido) VALUES
('Partido dos Trabalhadores'),
('Partido da República'),
('União Brasil'),
('Democracia Cristã'),
('VOTO NULO');

INSERT INTO candidatos (num, nome, id_part) VALUES
(13, 'Astolfo Martins', 1),
(22, 'Eliane Fonseca', 2),
(44, 'Sérgio Plínio', 3),
(27, 'Jair Da Silva', 4),
(0, 'VOTO NULO', 5);