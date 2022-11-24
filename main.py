#Importar
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

# exemplo de uso
borges = Pessoa(1, "Mateus Borges")
print(borges)

#chamar o obj do banco de dados
db = Database()

#instancia o objeto 
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy = False)

for pessoa in pessoas:
  print(pessoa)

#criar um objeto com qualquer ator ou diretor
novo = Pessoa(0, "Denzel Washington")
novo = pessoaDAO.save(novo)

#carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy = False)

for pessoa in pessoas:
  print(pessoa)