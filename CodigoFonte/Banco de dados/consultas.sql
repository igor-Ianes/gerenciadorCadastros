select * from PROFISSIONAL;    -- exibe a tabela de profissionais
select * from ESPECIALIDADE;   -- exibe a tabela de especialidades  
select * from DISPONIBILIDADE; -- exibe a tabela de disponibilidade

-- encontra medicos de uma especialidade especifica
SELECT p.NOME, p.CPF, p.CONTATO, e.NOME
AS ESPECIALIDADE 
FROM PROFISSIONAL p 
JOIN ESPECIALIDADE e ON p.ESPECIALIDADE_ID = e.ID 
WHERE e.NOME = 'Cardiologia';

-- encontra medicos disponiveis em determinada data
SELECT p.NOME, p.CPF, p.CONTATO, d.DIA_SEMANA, d.HORARIO_INICIO, d.HORARIO_FIM 
FROM PROFISSIONAL p 
JOIN DISPONIBILIDADE d ON p.ID = d.PROFISSIONAL_ID 
WHERE '10:00:00' BETWEEN d.HORARIO_INICIO AND d.HORARIO_FIM;
