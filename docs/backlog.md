# Backlog Mínimo do Projeto

## Release 1 - Core

### [ ] RF-01 — Definir tamanho da senha
**Descrição:** O usuário deve poder informar o número de caracteres da senha.

**Critério de aceite:**
- [ ] O sistema exibe um campo para inserir o tamanho da senha.
- [ ] O valor aceito deve estar dentro do intervalo mínimo e máximo definido.
- [ ] Se o valor for inválido, o sistema informa o erro e não gera a senha.

### [ ] RF-02 — Informar chave 1
**Descrição:** O usuário deve informar a primeira chave usada na geração da senha.

**Critério de aceite:**
- [ ] Existe um campo para a primeira chave.
- [ ] A chave é considerada no cálculo da senha.
- [ ] Campos vazios geram erro de validação.

### [ ] RF-03 — Informar chave 2
**Descrição:** O usuário deve informar a segunda chave usada na geração da senha.

**Critério de aceite:**
- [ ] Existe um campo para a segunda chave.
- [ ] A chave participa da geração da senha.
- [ ] Campos vazios geram erro de validação.

### [ ] RF-04 — Informar referência
**Descrição:** O usuário deve informar a referência usada para personalizar a senha.

**Critério de aceite:**
- [ ] Existe um campo de referência.
- [ ] A referência entra na lógica da geração.
- [ ] Campos vazios geram erro de validação.

### [ ] RF-05 — Gerar senha com base nas chaves e referência
**Descrição:** O sistema deve gerar uma senha aleatória determinística baseada nos dados informados.

**Critério de aceite:**
- [ ] A senha é gerada após a interação do usuário.
- [ ] A senha respeita os critérios configurados.
- [ ] A geração usa os valores informados nas entradas.

### [ ] FT-01 — Interface básica de geração
**Descrição:** A interface deve permitir que o usuário configure os critérios e veja o resultado.

**Critério de aceite:**
- [ ] O usuário consegue visualizar todos os campos de entrada.
- [ ] A senha gerada aparece na tela.
- [ ] A interface funciona sem erros visuais básicos.

---

## Release 2 - Qualidade

### [ ] RF-06 — Validar regras da senha
**Descrição:** O sistema deve impedir configurações inválidas ou inconsistentes.

**Critério de aceite:**
- [ ] Se o tamanho for inválido, o sistema bloqueia a geração.
- [ ] Se qualquer campo obrigatório estiver vazio, o sistema informa o erro.
- [ ] Mensagens de validação são claras e compreensíveis.

### [ ] RF-07 — Feedback visual de sucesso/erro
**Descrição:** O sistema deve informar ao usuário sobre o resultado da operação.

**Critério de aceite:**
- [ ] Em caso de sucesso, a aplicação confirma a geração da senha.
- [ ] Em caso de erro, mostra uma mensagem explicando o problema.
- [ ] O feedback é visível na interface sem quebrar o layout.

### [ ] FT-02 — Experiência de uso refinada
**Descrição:** Melhorar a usabilidade da aplicação para uma experiência mais clara e amigável.

**Critério de aceite:**
- [ ] Os campos e botões estão organizados visualmente.
- [ ] O fluxo principal é simples e direto.
- [ ] A aplicação se mantém estável em uso comum.

---

## Release 3 - Entrega Final

### [ ] RF-08 — Exibir força da senha
**Descrição:** O usuário deve visualizar uma indicação da força da senha gerada.

**Critério de aceite:**
- [ ] A interface mostra o nível de força da senha.
- [ ] A avaliação é baseada em critérios de entropia e variedade.
- [ ] O feedback ajuda o usuário a entender a segurança da senha.

### [ ] RF-09 — Exibir tempo estimado para quebrar a senha
**Descrição:** O sistema deve mostrar uma estimativa de tempo de quebra da senha.

**Critério de aceite:**
- [ ] A interface mostra uma estimativa em unidades legíveis.
- [ ] A mensagem reflete um cenário realista de ataque offline.
- [ ] O valor é apresentado de forma clara ao usuário.

### [ ] FT-03 — Finalização da entrega
**Descrição:** A aplicação deve estar pronta para uso em ambiente de demonstração ou entrega final.

**Critério de aceite:**
- [ ] A aplicação executa sem erros básicos.
- [ ] Todas as funcionalidades do MVP estão disponíveis.
- [ ] A interface final está consistente e pronta para uso.

---

## Resumo do Backlog

- Release 1: foco em geração básica e interface principal.
- Release 2: foco em validação, qualidade e usabilidade.
- Release 3: foco em força, estimativa de segurança e entrega estável.
