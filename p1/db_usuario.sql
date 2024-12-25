DROP DATABASE IF EXISTS usuarios_db;
CREATE DATABASE usuarios_db;
USE usuarios_db;

USE usuarios_db;
DROP TABLE IF EXISTS usuarios ;
CREATE TABLE  usuarios (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	dados JSON
);

USE usuarios_db;
INSERT INTO usuarios (dados) VALUES 
({
  "nome": "Ana",
  "idade": 30,
  "endereco": {
    "rua": "Rua A",
    "numero": 123,
    "cidade": "São Paulo"
  },
  "email": "ana@email.com"
});

USE usuarios_db;
INSERT INTO usuarios (dados) VALUES (
'{
  "nome": "Carlos",
  "idade": 25,
  "endereco": {
    "rua": "Rua B",
    "numero": 456,
    "cidade": "Rio de Janeiro"
  },
  "telefone": "(11) 98765-4321"
}');

USE usuarios_db;
INSERT INTO usuarios (dados) VALUES
('{
  "nome": "Fernanda",
  "idade": 35,
  "endereco": {
    "rua": "Rua C",
    "numero": 789,
    "cidade": "Belo Horizonte"
  },
  "email": "fernanda@email.com",
  "telefone": "(31) 91234-5678"
}');

SELECT JSON_UNQUOTE(JSON_EXTRACT(dados, '$.nome')) AS usuarios;