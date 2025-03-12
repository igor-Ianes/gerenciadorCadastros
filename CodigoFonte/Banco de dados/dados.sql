-- Inserindo dados na tabela ESPECIALIDADE
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Cardiologia', 'Especialidade médica que trata doenças do coração e do sistema circulatório.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Dermatologia', 'Especialidade médica que trata de doenças e condições da pele.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Neurologia', 'Especialidade médica que trata de doenças do sistema nervoso.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Oftamologia', 'Especialidade médica que trata doenças oculares.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Pediatria', 'Especialidade médica voltada ao cuidado de crianças.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Oncologia', 'Especialidade médica que trata diversos tipos de cancer.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('psiquiatria', 'Especialidade médica que trata doenças mentais.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Ginecologia', 'Especialidade médica que trata da saude da mulher.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Otorrino', 'Especialidade médica que trata de doenças do sistema respiratorio.');
INSERT INTO ESPECIALIDADE (NOME, DESCRICAO) VALUES ('Radiologista', 'Especialidade voltada a aplicação de exames de imagem.');


-- Inserindo dados na tabela PROFISSIONAL
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dr. João Silva', '123.456.789-00', 'joao.silva@gmail.com', 1);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dra. Maria Oliveira', '987.654.321-00', 'maria.oliveira@gmail.com', 2);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dr. Carlos Perreira', '161.222.353-44', 'carlos.pereira@hotmail.com', 3);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dr. Alvaro Perreira', '975.344.991-12', 'alvaro.perreira@gmail.com', 4);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dra. Lucia Gomes', '242.714.655-00', 'lucia.gomes@gmail.com', 6);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dr. Lisandro Ferraz', '734.884.113-40', 'lisandro.ferraz@gmail.com', 3);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dr. Manuel Alvez', '410.023.215-34', 'manuel.alves@hotmail.com', 8);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dr. Rai Montenegro', '324.857.212-90', 'rai.montenegro@gmail.com', 9);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dra. Joana Ricardo', '991.244.225-56', 'joana.ricardo@gmail.com', 7);
INSERT INTO PROFISSIONAL (NOME, CPF, CONTATO, ESPECIALIDADE_ID) VALUES ('Dr. Chen Takamura', '136.538.089-20', 'chen.takamura@gmail.com', 3);

-- Inserindo dados na tabela DISPONIBILIDADE
INSERT INTO DISPONIBILIDADE (PROFISSIONAL_ID, DIA_SEMANA, HORARIO_INICIO, HORARIO_FIM) VALUES (1, 'Segunda-feira', '08:00:00', '12:00:00');
INSERT INTO DISPONIBILIDADE (PROFISSIONAL_ID, DIA_SEMANA, HORARIO_INICIO, HORARIO_FIM) VALUES (4, 'Terça-feira', '13:00:00', '17:00:00');
INSERT INTO DISPONIBILIDADE (PROFISSIONAL_ID, DIA_SEMANA, HORARIO_INICIO, HORARIO_FIM) VALUES (6, 'Quarta-feira', '09:00:00', '12:00:00');
INSERT INTO DISPONIBILIDADE (PROFISSIONAL_ID, DIA_SEMANA, HORARIO_INICIO, HORARIO_FIM) VALUES (9, 'Segunda-feira', '15:00:00', '16:00:00');
INSERT INTO DISPONIBILIDADE (PROFISSIONAL_ID, DIA_SEMANA, HORARIO_INICIO, HORARIO_FIM) VALUES (1, 'Quinta-feira', '08:00:00', '12:00:00');
INSERT INTO DISPONIBILIDADE (PROFISSIONAL_ID, DIA_SEMANA, HORARIO_INICIO, HORARIO_FIM) VALUES (2, 'Sexta-feira', '06:00:00', '08:00:00');