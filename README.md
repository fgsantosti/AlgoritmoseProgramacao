
# Problemas Prova Final 2023-1

## 1. Problema: Sistema de Cadastro de Alunos
Descrição: Peça aos alunos para criarem um sistema de cadastro de alunos. O sistema deve permitir que o usuário adicione, visualize, edite e remova alunos da lista. Cada aluno deve ter informações como nome, idade e nota. O sistema deve fornecer um menu de opções para o usuário interagir com as funcionalidades.
Dica: Os alunos podem usar estruturas de dados como listas ou dicionários para armazenar as informações dos alunos.

## 2. Problema: Agenda de Compromissos
Descrição: Peça aos alunos para criarem uma agenda de compromissos. O sistema deve permitir que o usuário adicione, visualize, edite e remova compromissos da agenda. Cada compromisso deve ter informações como data, hora e descrição. O sistema também deve fornecer funcionalidades para o usuário visualizar os compromissos de um determinado dia ou período.
Dica: Os alunos podem usar estruturas de dados como listas ou dicionários para armazenar os compromissos e implementar a lógica de filtragem por datas.

## 3. Problema: Sistema de Gestão de Estoque e Vendas
Descrição: Peça aos alunos para criarem um sistema de gestão de estoque e vendas para uma loja. O sistema deve permitir que os usuários cadastrem produtos, atualizem informações de estoque, registrem vendas e gerem relatórios de vendas. Os usuários devem poder pesquisar produtos por nome, verificar a disponibilidade de estoque e registrar vendas com base nas quantidades disponíveis. O sistema deve também atualizar automaticamente o estoque após cada venda.
Dica: O aluno pode implementar algoritmos de busca e reserva eficientes. Os alunos podem usar estruturas de dados como árvores binárias de busca para organizar os produtos e implementar algoritmos eficientes para a atualização do estoque e a geração de relatórios.

## 4. Problema: Sistema de Reservas de Voo
Descrição: Peça aos alunos para criarem um sistema de reservas de voos. O sistema deve permitir que os usuários pesquisem voos disponíveis com base em critérios como origem, destino e data. Os usuários devem poder selecionar um voo e fazer uma reserva, informando seus dados pessoais. O sistema deve garantir que não haja conflito de reservas para o mesmo voo.
Dica: O aluno pode implementar algoritmos de busca e reserva eficientes. Os alunos podem usar estruturas de dados avançadas, como grafos, para representar as rotas de voo.

# Considerem esses requisitos e essas especificações ao desenvolverem os sistemas 

## Sistema de Cadastro de Alunos:

1. Funcionalidades básicas:
   - O sistema deve permitir o cadastro de novos alunos, solicitando as seguintes informações: nome, idade, gênero e curso.
   - O sistema deve ser capaz de exibir a lista de alunos cadastrados, mostrando todas as informações de cada aluno.
   - O sistema deve permitir a edição dos dados de um aluno, como idade, gênero ou curso.
   - O sistema deve permitir a remoção de um aluno da lista de cadastro.
   - O sistema deve ser capaz de buscar um aluno pelo nome e exibir suas informações.

2. Validações:
   - O sistema deve realizar validações para garantir que informações obrigatórias, como nome e idade, sejam fornecidas durante o cadastro e edição dos alunos.
   - O sistema deve validar a idade dos alunos, permitindo apenas valores válidos (por exemplo, idade não pode ser negativa).
   - O sistema deve lidar com possíveis erros de busca, informando ao usuário caso o aluno não seja encontrado.

3. Persistência de dados:
   - O sistema deve ser capaz de armazenar os dados dos alunos de forma persistente, para que os registros não sejam perdidos após o encerramento do programa.
   - Os alunos podem optar por usar arquivos para armazenar os dados em disco ou uma abordagem de banco de dados simples (como SQLite).

4. Interface de usuário:
   - O sistema deve fornecer uma interface de usuário amigável, permitindo que o usuário interaja com as funcionalidades por meio de um menu intuitivo.
   - As opções do menu devem ser claras e bem organizadas, facilitando a navegação e utilização do sistema.


## Agenda de Compromissos:

1. Funcionalidades básicas:
   - O sistema deve permitir o cadastro de compromissos, solicitando as seguintes informações: data, hora, descrição e duração.
   - O sistema deve ser capaz de exibir a lista de compromissos cadastrados, mostrando todas as informações de cada compromisso.
   - O sistema deve permitir a edição dos dados de um compromisso, como data, hora, descrição ou duração.
   - O sistema deve permitir a remoção de um compromisso da agenda.
   - O sistema deve ser capaz de filtrar os compromissos com base em uma data específica ou em um intervalo de datas.
   - O sistema deve fornecer uma funcionalidade para verificar os compromissos de um determinado dia e exibi-los em ordem cronológica.

2. Validações:
   - O sistema deve realizar validações para garantir que informações obrigatórias, como data e hora, sejam fornecidas durante o cadastro e edição dos compromissos.
   - O sistema deve validar a consistência dos dados, como verificar se a hora do compromisso não entra em conflito com outros compromissos já cadastrados.

3. Persistência de dados:
   - O sistema deve ser capaz de armazenar os dados dos compromissos de forma persistente, para que os registros não sejam perdidos após o encerramento do programa.
   - Os alunos podem optar por usar arquivos para armazenar os dados em disco ou uma abordagem de banco de dados simples (como SQLite).

4. Interface de usuário:
   - O sistema deve fornecer uma interface de usuário intuitiva, permitindo que o usuário interaja com as funcionalidades por meio de um menu ou comandos claros.
   - O sistema deve apresentar as informações de forma organizada, facilitando a visualização dos compromissos.

## Sistema de Gestão de Estoque e Vendas:

1. Funcionalidades básicas:
   - O sistema deve permitir o cadastro de produtos, solicitando as seguintes informações: nome, código, quantidade em estoque e preço.
   - O sistema deve ser capaz de exibir a lista de produtos cadastrados, mostrando todas as informações de cada produto.
   - O sistema deve permitir a edição dos dados de um produto, como quantidade em estoque ou preço.
   - O sistema deve permitir a remoção de um produto do estoque.
   - O sistema deve ser capaz de registrar vendas, solicitando as seguintes informações: código do produto e quantidade vendida.
   - O sistema deve atualizar automaticamente a quantidade em estoque após cada venda.

2. Validações:
   - O sistema deve realizar validações para garantir que informações obrigatórias, como nome, código e quantidade em estoque, sejam fornecidas durante o cadastro e edição dos produtos.
   - O sistema deve validar a disponibilidade de estoque durante a realização de vendas, verificando se há quantidade suficiente para atender à demanda.

3. Relatórios:
   - O sistema deve ser capaz de gerar relatórios de vendas, mostrando informações como produtos vendidos, quantidades vendidas e valores totais.
   - O sistema deve permitir a filtragem dos relatórios por data, para que o usuário possa visualizar as vendas em um determinado período.

4. Persistência de dados:
   - O sistema deve ser capaz de armazenar os dados dos produtos e das vendas de forma persistente, para que os registros não sejam perdidos após o encerramento do programa.
   - Os alunos podem optar por usar arquivos para armazenar os dados em disco ou uma abordagem de banco de dados simples (como SQLite).

5. Interface de usuário:
   - O sistema deve fornecer uma interface de usuário intuitiva, permitindo que o usuário interaja com as funcionalidades por meio de um menu ou comandos claros.
   - O sistema deve apresentar as informações de forma organizada, facilitando a visualização dos produtos, vendas e relatórios.

## Sistema de Reservas de Voo:

1. Funcionalidades básicas:
   - O sistema deve permitir que os usuários pesquisem voos disponíveis com base em critérios como origem, destino e data.
   - O sistema deve exibir os voos disponíveis, mostrando informações como número do voo, origem, destino, horário de partida e horário de chegada.
   - O sistema deve permitir que os usuários selecionem um voo e façam uma reserva, fornecendo informações pessoais, como nome, número de passaporte ou documento de identificação.
   - O sistema deve garantir que não haja conflito de reservas para o mesmo voo, ou seja, não pode haver duas reservas para o mesmo assento em um determinado voo.

2. Validações:
   - O sistema deve realizar validações para garantir que informações obrigatórias, como origem, destino e data, sejam fornecidas durante a pesquisa de voos e a reserva.
   - O sistema deve verificar a disponibilidade de assentos no voo selecionado antes de permitir a reserva.
   - O sistema deve lidar com possíveis erros de reserva, como informar ao usuário caso o assento já esteja ocupado.

3. Persistência de dados:
   - O sistema deve ser capaz de armazenar os dados dos voos e das reservas de forma persistente, para que os registros não sejam perdidos após o encerramento do programa.
   - Os alunos podem optar por usar arquivos para armazenar os dados em disco ou uma abordagem de banco de dados simples (como SQLite).

4. Interface de usuário:
   - O sistema deve fornecer uma interface de usuário intuitiva, permitindo que o usuário interaja com as funcionalidades por meio de um menu ou comandos claros.
   - O sistema deve apresentar as informações de forma organizada, facilitando a visualização dos voos, disponibilidade de assentos e informações de reserva.


Deixo aqui disponível os códigos dos problemas resolvidos durante a disciplina de Algoritmos e Programação com Python no meu Github. Os códigos são referentes aos livros:

- Fundamentos da Programação de Computadores, livro da Ana Fernanda Gomes 3º edição e;  

- Introdução à Programação com Python 2º edição, livro do Nilo Ney Coutinho Menezes. 
