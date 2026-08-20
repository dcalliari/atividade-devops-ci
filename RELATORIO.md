# Atividade Prática: Integração Contínua

## 1. Nome do aluno / dupla

Nome completo: Daniel Bahia Pinheiro Calliari

## 2. Repositório

Link: <https://github.com/dcalliari/atividade-devops-ci>

## 3. Ferramentas utilizadas

* Git
* GitHub
* GitHub Actions
* Python
* Pytest

## 4. O que foi desenvolvido?

Foi feita uma aplicação simples em Python com funções de soma, subtração e multiplicação. Também foram criados testes para conferir se cada função retorna o resultado esperado.

## 5. Como funciona a pipeline?

Sempre que é feito um `git push` para a branch `main`, o GitHub Actions executa a pipeline. Ela baixa o projeto, configura o Python, instala o Pytest e roda os testes. Se todos passarem, a execução fica verde. Se algum falhar, fica vermelha.

## 6. Teste realizado

Foram criados três testes:

1. soma de 2 e 3;
2. subtração de 5 e 3;
3. multiplicação de 4 e 3.

## 7. Falha proposital

A função de soma foi alterada temporariamente para fazer uma subtração. Com isso, o teste da soma falhou porque o resultado retornado foi diferente do esperado.

## 8. Resultado

A pipeline identificou a falha. Depois da correção da função de soma, os três testes passaram novamente.

### Evidências

* [Primeira execução com sucesso](https://github.com/dcalliari/atividade-devops-ci/actions/runs/32430952024)
* [Execução com falha proposital](https://github.com/dcalliari/atividade-devops-ci/actions/runs/32430984586)
* [Execução após a correção](https://github.com/dcalliari/atividade-devops-ci/actions/runs/32431019266)

## 9. Conclusão

Entendi que Integração Contínua ajuda a verificar automaticamente as alterações enviadas para o repositório. A cada envio, os testes são executados e os erros podem ser encontrados mais rápido. Isso deixa o desenvolvimento mais seguro e organizado.
