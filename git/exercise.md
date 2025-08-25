# O que é o Git e para que ele serve?

Git é um sistema de controle de versão distribuido que monitora e registra alterações em qualquer arquivo ou grupo de arquivos em um repositório, permitindo a recuperação de iterações específicas conforme necessário. O Git serve para que membros da equipe trabalhem de forma independente e colaborativa em um projeto, mesmo que não estejam no mesmo local de trabalho. Ou seja, cada desenvolvedor pode trabalhar localmente, salvar as alterações que deram certo e sincronizar essas alterações em um repositório Git para que outros colaboradores possam ver a versão mais recente do projeto.

# Qual a diferença entre git init e git clone?

O `git init` cria um repositório ou trasforma um diretório comum em um repositório Git local, ou seja, a partir do git init conseguimos fazer e acessar alterações no projeto. Já o `git clone`, copia um repositório Git existente incluindo todo o histórico de alterações do projeto.

# Como você verifica o estado atual do repositório?

Com o comando `git status`.

# Como adicionar um arquivo específico ao stage?

Para adicionar um arquivo modificado ao stage (área de praparação) use o comando `git add <nome-do-arquivo>`. Isto significa que o arquivo está pronto para o próximo commit.

# Como adicionar todos os arquivos modificados ao stage?

Para adicionar todos os arquivos modificados ao stage use o comando `git add .`.

# Como confirmar (salvar) mudanças no repositório?

Para salvar as mudanças no repositório use o comando `git commit -m "Mensagem explicativa da alteração"`. Esse comando salva os arquivos que estão no stage. A mensagem da alteração deve ser sucinta e na forma imperativa informando o que de fato o commit faz se for aplicado.

# Como visualizar o histórico de commits?

Para visualizar o historico de commits podemos usar os comando `git log`.

# Como criar um novo branch?

Para criar um novo branch use o comando `git branch nome-da-branch`.

