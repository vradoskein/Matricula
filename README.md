# Matricula
A intenção do projeto é ajudar os alunos irregualres a montarem a grade de materias da faculdade. Inicialmente deve ser selecionado as disciplinas ja concluidas, e apos isso é exibido uma lista com as disciplinas disponiveis. O programas é aproveitavel para qualquer grade curricular. 
Para adaptar a sua necessidade, deve ser criado um arquivo txt com as materias e seus pré-requisitos no seguinte formato, o nome da materia seguido por ":", seus pre requisitos separados por virgula "," e por ultimo seu horario (os horarios são numerados de 1 a 15. O 1 é 7:00 na segunda, o 2 é 8:50 na segnda, o 3 é 10:40 na segunda, o 4 é 7:00 na terça...)

Exemplo:
Materia:PreReq1,PreReq2:1
Materia2:PreReq1,PreReq4:7

Para o futuro o programa deve ser capaz de montar a grade com o maior numero de materia, com as materias mais importantes, e outrs variações a serem pensadas futuramente.


O projeto esta sendo desenvolvido em python puro, e para a interface é usado o tkinter
