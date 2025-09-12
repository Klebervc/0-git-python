# O que é o Git e para que ele serve?

Git é um sistema de controle de versão distribuido que monitora e registra alterações em qualquer arquivo ou grupo de arquivos em um repositório, permitindo a recuperação de iterações específicas conforme necessário. O Git serve para que membros da equipe trabalhem de forma independente e colaborativa em um projeto, mesmo que não estejam no mesmo local de trabalho. Ou seja, cada desenvolvedor pode trabalhar localmente, salvar as alterações que deram certo e sincronizar essas alterações em um repositório Git para que outros colaboradores possam ver a versão mais recente do projeto

# Qual a diferença entre git init e git clone?

O `git init` inicia um repositório Git ou trasforma um diretório comum em um repositório Git local, ou seja, a partir do git init conseguimos fazer e acessar alterações no projeto. Já o `git clone`, copia um repositório Git existente incluindo todo o histórico de alterações do projeto.

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

# O que é uma branch no git?

Uma branch no git é uma linha de desenvolvimento independente (ramificação) em um repositório que diverge da linha principal de desenvolvimento `main` e que permite trabalhar no projeto sem alterar a `main`. Assim, uma branch permite tabalhar em paralelo em diferentes tarefas, ajudam a avitar conflitos em diferentes partes do projeto e torna possível revisar e testar códigos antes de inseri-los na versão principal.

# Como criar uma branch no git?

Para criar um novo branch use o comando `git branch nome-da-branch`.

# Como entrar em uma branch no git?

Para entrar ou mudar de branch no git usamos o comando `git checkout nome-da-branch`. 
Para criar e já entrar na branch use o comando `git checkout -b nome-da-branch`.

# Para que serve uma branch no git?

Uma branch serve para:

- Desenvolvimento independente: a branch serve como uma linha de desenvolvimento que pode ser alterada sem que altere a `main` do projeto.
- Novas features: permite criar novas funcionalidades ao projeto sem interferir no projeto principal.
- Corrige bugs: faz a correção de erros sem afetar a versão principal do projeto.
- Experimentos: serve para realizarmos experimentos com segurança testando novas ideias.
- Paralelismo: com várias branches podemos acelerar o desenvolvimento do projeto com os outros membros da equipe simultaneamente. 
- Organização: organiza o hitórico do projeto com as ramificações sendo para diferentes tarefas e objetivos.

# O que é um Pull Request?

O Pull Request é uma solicitação para que as suas mudanças feitas em um código em uma branch de um repositório sejam analizadas e, se aprovadas, integradas a `main` do projeto. O processo funciona da seguinte forma:

- Cria-se uma nova branch para realizar mudanças no código ou nova funcionalidade.
- Comita todas as alterações na branch criada.
- Abre um Pull Request para que outros membros da equipe vejam as mudanças feitas.
- Revisores analisam o código vendo se está tudo certo, sugerem melhorias ou aprovam.
- Quando tudo estiver certo o Pull Request é aceito e feito o `merge`. Assim, as mudanças passam a fazer parte da branch principal do projeto. 

# O que é um Merge

Merge é o processo de unir o conteúdo de duas branches em um só. O processo do merge é a última etapa descrita no exercício anterior. Abaixo temos um esquema de merge de uma branch criada `feature` para a `main` do projeto. Após o merge `G` os commits `D` e `E` da branch `feature` fazem parte do histórico de commits da `main`. O histórico da branch mesclada na branch destino é importante pois ajuda a entender o que veio de onde.

```
main:    A---B---C-------G
               \       /
feature:         D---E
```

# O que é um Fast-Forward Merge?

O Fast-Forward acontece quando a branch de destino (pode ser a `main`) não teve novos commits desde quando a nova branch foi criada. O git apenas avança o ponteiro da branch destino (pode ser a `main`) sem criar commit de merge. No exemplo abaixo, após o `merge`, o git avança o ponteiro da `main` até `F`. 

Antes do merge:

```
A---B---C  (main)
         \
          D---E---F  (feature)
```

Após o merge:

```
A---B---C---D---E---F  (main, feature)
```

# O que é um Squash Merge?

O Squash Merge é um merge no git onde todos os commits de uma branch são "espremidos" em um único commit antes de serem adicionados à branch principal (geralmente a `main`). Nesse caso, os commits originais da branch mesclada não entram no histórico da `main`. No diagrama, após o squash merge, `G` é o único commit contendo as mudanças combinadas de `D`, `E` e `F`. Os commits da branch `feature` não entram no histórico da `main`.

Antes do Squash Merge:
```
A---B---C           (main)
     \
      D---E---F     (feature)

```
Após o Squash Merge:
```
A---B---C---G       (main)
             \
              D---E---F     (feature, ainda intacta)

```
# O que é um Pull Request em modo draft?

Um Pull Request em modo `draft` é uma função de plataformas de controle de versão como `Github` que permitem o desenvolvedor abrir uma uma Pull Request antes que o projeto esteja pronto para ser revisado ou mesclado (`merge`). O Pull Request em modo `draft` serve para obter feedback antes de definir o código, discutindo implementações com outros desenvolvedores.

# O que é um Pull Request em modo open?

Um Pull Resquest em modo `open` é a forma padrão do Pull Request, ou seja, indica que o projeto está pronto para ser revisado, comentado e, se tudo estiver certo, mesclado (`merge`). Se o Pull Request é criado sem marcar como `draft` ele é automaticamente `open`. Para um Pull Request passar de modo `draft` para `open` é necessário clicar em "Ready for review" no `Github`.

# O que é o pip do Python?

O `pip` é o gerenciador de pacotes oficial do python usado para instalar, remover, atualizar e gerenciar bibliotecas e pacotes que não fazem parte da biblioteca padrão do python.

Alguns comandos com `pip` são:

| Código | Função |
|--------|--------|
| `pip install nome-do-pacote`        | Instala um pacote     |
| `pip uninstall nome-do-pacote`       | Remove um pacote       |
| `pip list`       | Lista todos os pacotes instalados       |
| `pip show nome-do-pacote` | Mostra detalhes de um pacote  |
| `pip install -r requirements.txt` | Instala os pacotes listados em um arquivo |

# O que é uma requirements.txt?

Uma `requirements.txt` é um arquivo texto usado em projetos Python contendo todas as bibliotecas que serão necessárias para o projeto funcionar. O seu uso é importante pois ele permite recriar o ambiente de desenvolvimento idêntico em qualquer máquina além de automatizar a instalação de pacotes com o `pip`.

Um exemplo de uma `requirements.txt` é como segue:

```
requests==2.31.0
flask>=2.0,<3.0
numpy
```
Esse `requirements.txt` contém exatamente: a versão 2.31.0 do pacote, uma versão entre 2 (inclusive) até antes de 3.0 e a versão atual do python.

Para instalar todos os pacotes listados no arquivo de uma vez temos o comando: `pip install -r requirements.txt`.

# O que é uma .gitignore?

Um `.gitignore` é um arquivo usado em projetos que usam o Git e especifica quais arquivos ou pastas devem ser ignorados pelo Git. Isto significa que esses arquivos não serão rastreados, versionados ou enviados para o repositório.

O `.gitignore` serve para que arquivos desnecessários não sejam incuídos no repositório, como:

- Arquivos temporários (ex: `Thumbs.db`, `.DS_Store`)
- Ambientes Virtuais (ex: `venv/`)
- Arquivos de configuração locais (ex: `.env`)
- Compilação ou dependências (ex: `__pycache__/`, `node_modules/`)
- Arquivos grandes que não precisam ser versionados

O Git inicialmente verifica o arquivo `.gitignore` antes de adicionar arquivos com o `git add`.

# O que é um Jupyter Notebook?

O Jupyter Notebook é uma aplicação web e ambiente interativo de código aberto usada principalmente em Machine Learning, ciência de dados, estatística e desenvolvimento em python que combina:

- Códigos executáveis
- Textos Formatados (Markdown)
- Gráficos e visualizações
- Equações Matemáticas (LaTex)

Podemos executa-lo célula por célula o que permite uma maior liberdade com códigos. Seu uso pode ser variado: 

- Carrega dados com `pandas`.
- Plota gráficos dos dados com `matplotlib` ou `seaborn`.
- Explica os passos em células de texto.
- Treina modelos de machine learning com `scikit-learn`.

O Jupyter Notebook é salvo com a extensão `.ipynb`.

# Como utilizar um Jupyter Notebook no vscode?

- Abra o VScode e vá para a aba de extenções.
- Instale Python e Jupyter.
- Crie um arquivo `.ipynb` clicando em `File > New File`, e salve como `exemplo.ipynb` ou abra um arquivo `.ipynb` se existir.
- Após abrir o notebook, no canto superior direito, verá algo como: "Select Kernel" ou o nome de um ambiente, como por exemplo `Python 3.10.12 ('venv': venv)`, então escolha o kernel que deseja usar.
- Clique em uma célula e pressione `Shift+Enter` para executa-la. A saída aparecerá logo abaixo.
- Se clicar em "Restart Kernel" o Kernel será reiniciado e todas as variáveis seram esquecidas.

# O que é o kernel utilizado no Jupyter Notebook?

O kernel é o responsável por executar o código Python no notebook e manter o estado da sessão o que significa que:

- Ele lembra das variáveis e funções das células.
- Se o kernel for reiniciado tudo é esquecido como se tivesse aberto um notebook novamente.
- Você pode escolher qual ambiente Python ou linguagem usar, dependendo do kernel.

# Qual a forma mais fácil de criar esse kernel e utilizá-lo no vscode?

Pode usar um ambiente virtual com o pacote `ipykernel`.

- Primeiro abra o terminal no VSCode.
- Crie um ambiente virtual com o comando `python -m venv venv` (isso cria uma pasta /venv com ambiente isolado).
- Ative o ambiente isolado usando o comando `.\venv\Scripts\activate`. Aparecerá `venv` no início da linha no terminal. Isso indica que o ambiente está ativado.
- Digita o comando `pip install jupyter ipykernel` para instalar o `jupyter` e o `ipykernel`.
- Crie o kernel com o comando `python -m ipykernel install --user  --name myenv --display-name "Python (myenv)"`. `name-myenv` é o nome interno do kernel e `display-name "Python (myenv)"` é o nome que vai aparecer no VS Code.
- Abra ou crie um arquivo `.ipynb` e selecione o kernel. Agora está usando o seu próprio kernel, isolado, com o Python e os pacotes do ambiente virtual.
- Use normalmente o notebook como ja mencionado acima.
- Se quiser deletar esse kernel digite `jupyter kernelspec uninstall venv` no terminal. 
