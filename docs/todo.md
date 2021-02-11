# TODO
## Informações do projeto
### 1. Grade de disciplinas:
- Um aluno pode ter somente uma grade;
- Uma grade pode possuir uma ou várias disciplinas;
    - *A regra do negócio dirá o máximo permitido.*
- A grade irá exibir as seguintes informações:
    | Código | Disciplina | Situação | Horário |
    | --- | --- | --- | --- |
    | ABC123 | Matemática | Confirmada | 9h00 |
    | CBA321 | Física | Confirmada | 11h20 |
- Um exemplo de queryset para essa exibição
    - `Subjects.object.filter(student=pk)`
- [ ] Criar o `template_base.html` do projeto;
- [ ] Criar tabela em `grids.html` para renderizar dados;
- [ ] Criar os seguintes campos no modelo subject:
    - [x] **code**;
    - [x] **situation**;
    - [ ] **shedule**.
- [ ] Criar gerador de código para o campo **code** em **subject**