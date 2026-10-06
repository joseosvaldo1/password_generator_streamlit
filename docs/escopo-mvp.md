# Escopo do MVP

## 1. Objetivo
Desenvolver uma aplicação web simples, utilizando Streamlit, para gerar senhas seguras com base em chaves e referência informadas pelo usuário. A solução deve permitir configurar o tamanho da senha e receber entradas que personalizam a geração, com foco em simplicidade, rapidez e segurança.

## 2. Contexto do Projeto
O projeto atende a uma necessidade comum: criar senhas fortes e personalizadas sem exigir conhecimentos avançados em segurança da informação. A aplicação deve ser intuitiva, acessível e funcional, com foco em um MVP (Produto Mínimo Viável), isto é, uma versão inicial com recursos essenciais para uso prático.

## 3. Escopo do MVP
O MVP incluirá as funcionalidades mínimas necessárias para que o usuário:
- informe o tamanho da senha;
- informe os dados que compõem a semente da geração;
- gere uma senha segura;
- visualize a senha resultante;
- entenda sua força e tempo estimado de quebra.

## 4. Requisitos Funcionais

### RF01 — Configuração do tamanho da senha
O sistema deve permitir que o usuário informe o número de caracteres da senha a ser gerada.

Critérios:
- valor mínimo definido pelo sistema, como 4 caracteres;
- valor máximo definido pelo sistema, como 15 caracteres;
- validação para impedir valores inválidos.

### RF02 — Informar chave 1
O sistema deve permitir ao usuário informar a primeira chave que participará da geração da senha.

### RF03 — Informar chave 2
O sistema deve permitir ao usuário informar a segunda chave que participará da geração da senha.

### RF04 — Informar referência
O sistema deve permitir ao usuário informar uma referência que personalize a geração.

### RF05 — Geração de senha com base nas entradas
O sistema deve gerar uma senha com base nas chaves e na referência fornecidas.

Critérios:
- a senha deve respeitar o tamanho informado;
- a senha deve utilizar a lógica atual do projeto;
- deve evitar geração inconsistente ou inválida.

### RF06 — Visualização do resultado
A senha gerada deve ser exibida na interface em um local claro e legível.

### RF07 — Validação de entrada
O sistema deve impedir que o usuário gere uma senha com campos vazios ou valores fora do intervalo aceito.

### RF08 — Feedback ao usuário
A interface deve informar ao usuário quando a geração for concluída com sucesso e quando houver erro na configuração.

### RF09 — Força da senha
A interface deve apresentar uma indicação sobre a força da senha gerada.

### RF10 — Tempo estimado para quebrar
A interface deve mostrar uma estimativa do tempo para quebrar a senha, de forma legível e orientada à segurança.

## 5. Requisitos Não Funcionais

### RNF01 — Interface simples e intuitiva
A aplicação deve ter uma interface clara, amigável e de fácil uso, mesmo para usuários iniciantes.

### RNF02 — Performance
A geração da senha deve ocorrer em tempo imediato, sem lentidão perceptível para o usuário.

### RNF03 — Segurança
A geração deve ser baseada em mecanismos seguros e em avaliação coerente da força da senha.

### RNF04 — Portabilidade
A aplicação deve funcionar em ambientes comuns de uso, como Windows, Linux e macOS, desde que o Python e o Streamlit estejam instalados.

### RNF05 — Manutenibilidade
O código deve estar organizado em camadas, com estrutura simples e fácil de entender para futuras melhorias.

### RNF06 — Responsividade
A interface deve ser funcional em telas de desktop e em resoluções médias, sem quebrar o layout principal.

## 6. Requisitos de Usabilidade
- O usuário deve conseguir gerar uma senha em poucos segundos.
- Os campos de entrada devem ser fáceis de identificar.
- O fluxo principal deve ser simples: preencher campos → gerar senha → visualizar resultado.

## 7. Fora de Escopo
Os itens abaixo não fazem parte do MVP e podem ser implementados em versões futuras:

- armazenamento de senhas em banco de dados;
- autenticação de usuários;
- login e cadastro;
- histórico persistente de senhas geradas;
- integração com navegadores ou extensões;
- exportação em arquivos;
- suporte a múltiplos idiomas;
- geração de senhas baseadas em frases ou palavras;
- APIs externas ou backend separado.

## 8. Critérios de Aceitação do MVP
O MVP será considerado concluído quando:
1. o usuário puder definir o tamanho da senha;
2. o usuário puder preencher as chaves e a referência;
3. a aplicação gerar uma senha conforme a lógica definida;
4. a senha seja exibida corretamente na interface;
5. a interface mostre a força e o tempo estimado de quebra;
6. a aplicação valide entradas inválidas e informe o erro de forma clara.

## 9. Resumo do Escopo
O MVP do projeto consiste em uma aplicação web simples para geração de senhas seguras com base em entradas informadas pelo usuário. O foco está na funcionalidade principal: permitir a geração de senhas fortes e personalizadas, com feedback claro de segurança.

## 10. Conclusão
Este MVP pretende entregar uma solução funcional, acessível e prática para geração de senhas robustas. A proposta é manter a aplicação simples, focada no uso direto e na experiência do usuário, deixando recursos mais complexos para evoluções futuras.
