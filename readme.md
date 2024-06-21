# NVDA Netcat

Este repositório contém scripts para integrar o NVDA (NonVisual Desktop Access) com Netcat para criar uma conexão de shell reverso. O objetivo é demonstrar como scripts de automação podem ser usados para executar comandos remotos.

## Estrutura do Repositório

- `.github/workflows`: Arquivos de configuração do GitHub Actions.
- `addon`: Arquivos do complemento NVDA.
- `site_scons/site_tools/gettexttool`: Ferramentas de construção.
- `.gitattributes`: Arquivo de atributos do Git.
- `.gitignore`: Arquivo de configuração do Git para ignorar arquivos.
- `buildVars.py`: Variáveis de construção.
- `manifest-translated.ini.tpl`: Modelo de arquivo de manifesto traduzido.
- `manifest.ini.tpl`: Modelo de arquivo de manifesto.
- `readme.md`: Este arquivo README.
- `sconstruct`: Script de construção.

## Pré-requisitos

1. **NVDA**: Certifique-se de que o NVDA está instalado na sua máquina.
2. **Python**: Certifique-se de que o Python está instalado e acessível no PATH do sistema.

## Instalação

### Importando e Usando o Script NVDA

1. **Baixe o Repositório**:
   - Clone ou baixe o repositório a partir do [GitHub](https://github.com/MatheusExner/nvda_netcat) e substitua os endereços IP conforme seu ambiente.

2. **Instale o Complemento NVDA**:
   - Abra o NVDA e vá para `Ferramentas > Gerenciador de Complementos`.
   - Clique em `Instalar` e selecione o arquivo `.nvda-addon` dentro da pasta `addon`.

3. **Atribua um Atalho de Teclado**:
   - No NVDA, vá para `Preferências > Gerenciador de Entrada`.
   - Encontre a ação correspondente ao script importado e atribua um atalho de teclado.

4. **Execute o Script**:
   - Pressione o atalho de teclado atribuído para executar o script e iniciar a conexão de shell reverso.

### Configurando e Executando o Script Python

1. **Certifique-se de que o Python está Instalado**:
   - Baixe e instale o Python a partir do [site oficial](https://www.python.org/).

2. **Configure o Netcat**:
   - Certifique-se de que o Netcat está instalado e configurado corretamente no seu sistema.

3. **Execute o Script Python**:
   - Abra o Prompt de Comando ou o PowerShell.
   - Navegue até o diretório do repositório e execute o script Python para iniciar a conexão de shell reverso.

## Conclusão

Este exemplo demonstra como usar scripts NVDA em conjunto com o Netcat para estabelecer uma conexão de shell reverso. 
