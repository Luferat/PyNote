DROP DATABASE IF EXISTS pynotepad;
CREATE DATABASE pynotepad CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pynotepad;

CREATE TABLE config (
    id INT PRIMARY KEY AUTO_INCREMENT,
    var VARCHAR(63) UNIQUE NOT NULL,
    val TEXT NOT NULL
);

CREATE TABLE category (
    cat_id INT PRIMARY KEY AUTO_INCREMENT,
    cat_name VARCHAR(63) NOT NULL
);

CREATE TABLE notepad (
    note_id INT PRIMARY KEY AUTO_INCREMENT,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    note_title VARCHAR(127) NOT NULL,
    note_content TEXT NOT NULL,
    note_category INT NOT NULL,
    note_status ENUM('on', 'off') DEFAULT 'on'
);

CREATE TABLE notecat (
    id INT PRIMARY KEY AUTO_INCREMENT,
    note INT NOT NULL,
    cat INT NOT NULL,
    FOREIGN KEY (note) REFERENCES notepad (note_id),
    FOREIGN KEY (cat) REFERENCES category (cat_id)
);

INSERT INTO config (var, val) VALUES
('sitename', 'PyNote'),
('sitelogo', '<i class="fa-solid fa-file-signature fa-fw"></i>');

INSERT INTO category (cat_name) VALUES
('Cadastros e senhas'),
('Receitas'),
('Sites e links'),
('Dicas'),
('Programação');

INSERT INTO notepad (note_title, note_content, note_category, note_status) VALUES
('Título da Nota 1', 'Conteúdo da Nota 1', 1, 'on'),
('Título da Nota 2', 'Conteúdo da Nota 2', 2, 'on'),
('Título da Nota 3', 'Conteúdo da Nota 3', 3, 'on'),
('Título da Nota 4', 'Conteúdo da Nota 4', 4, 'on'),
('Título da Nota 5', 'Conteúdo da Nota 5', 5, 'on');

INSERT INTO notecat (note, cat) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 1),
(3, 5),
(4, 2),
(4, 3),
(5, 4),
(5, 5);
