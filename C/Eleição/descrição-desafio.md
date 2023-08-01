# Decrição do Desafio
Imagine que o TSE contratou sua empresa para desenvolver o sistema das urnas eletrônicas que serão utilizadas nas próximas eleições do país. O sistema deverá realizar as seguintes ações:

- O sistema deverá conter pelo menos três candidatos válidos para prefeito e mais três para vereador (não precisam ser exibidos ao leitor no ato da votação);
- O sistema deverá solicitar ao leitor que vote primeiro para prefeito, informando o número do candidato;
- A partir do número informado pelo leitor, o sistema deverá informar o nome, número e partido do candidato e solicitar que o leitor confirme ou corrija ("C" confirma e "D" corrigir);
- Após confirmar o voto o sistema deverá solicitar que o leitor vote para vereador. Da mesma forma que para prefeito, o sistema irá exibir o número, nome e partido do candidato e as opções: corrigir e confirmar;
- Caso o leitor deseje votar na opção nula deverá informar 000 como número do candidato tanto para prefeito como para vereador. Nesta situação o sistema irá exibir uma tela solicitando que o usuário confirme ou corrija seu voto;
- O sistema deverá encerrar a votação caso o usuário insira um valor negativo para o número do prefeito.

Ao final da votação o sistema deverá exibir:
- Número e o percenteual de votos de todos os candidatos, tanto para prefeito, como para vereador;
- O nome, número e partido do candidato vencedor (prefeito e vereador);
- O percentual de votos nulos.

## Observações da Conclusão
- Adicionei o cadastro dos candidatos para que pudesse realizar testes;
- Situações não foram incuídas/corrijidas como: candidatos do mesmo cargo com mesmo número, mais de uma votação antes do encerramento do sistema;

## Tecnologias Utilizadas
![C](https://img.shields.io/badge/C-000?style=for-the-badge&logo=c)
