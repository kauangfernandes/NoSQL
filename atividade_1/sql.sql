DROP DATABASE IF EXISTS nosql;
CREATE DATABASE nosql;
USE nosql;

USE nosql;
DROP TABLE IF EXISTS pacientes;
CREATE TABLE  pacientes(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	dados JSON
);


INSERT INTO pacientes (dados) 
VALUES (
	JSON_OBJECT(
	'nome', 'Kauan',
	'idade', 25,
	'endereco',
		JSON_OBJECT(
			'rua', 'Rua dos Bobos',
			'numero', '0',
			'bairro', 'Centro',
			'cidade', 'São Paulo',
			'cep', '12345-678'
		)
	)
),(
	JSON_OBJECT(
	'nome', 'Maria',
	'idade', 30,
	'endereco', 
		JSON_OBJECT(
			'rua', 'Avenida Principal',		    
			'numero', '123',
			'bairro', 'Jardim',
			'cidade', 'Rio de Janeiro',
		    'cep', '23456-789'
		),
	'historico', 
		JSON_OBJECT(
			'medico', 'X',
			'doenca', JSON_OBJECT(
				'nome', 'X',
				'nome', 'diabetes'
			)
		)
	    )
),(
	JSON_OBJECT(
	'nome', 'X',
	'idade', 30,
	'endereco', 
		JSON_OBJECT(
			'rua', 'Avenida Principal',		    
			'numero', '123',
			'bairro', 'Jardim',
			'cidade', 'Rio de Janeiro',
		    'cep', '23456-789'
		),
	'historico', 
		JSON_OBJECT(
			'medico', 'Y',
			'doenca', JSON_OBJECT(
				'nome', 'X',
				'nome', 'y'
			)
		)
	    )
);
SELECT * FROM pacientes;

#a) Extraia o nome do segundo paciente.

SELECT JSON_UNQUOTE(JSON_EXTRACT(dados, '$.nome')) AS paciente
FROM pacientes
WHERE id = 2;

#b) Liste todos os pacientes que possuem diabetes ou qualquer outra doença.

SELECT * FROM pacientes
WHERE JSON_CONTAINS(dados, '$.historico.doenca.nome', '"diabetes"');

#c) Se não tiver, incluir o campo doença.


#d) Crie uma consulta que retorne apenas os pacientes que têm mais de uma doença listada em seu histórico médico.

