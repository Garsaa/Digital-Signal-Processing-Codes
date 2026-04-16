# Ambiente local para notebooks no VS Code

Este projeto ficou configurado para usar notebooks direto no VS Code, sem abrir navegador, em Windows e Linux.

## O que precisa

- Python 3.11 ou compativel
- Extensao `Python` no VS Code
- Extensao `Jupyter` no VS Code
- Ambiente virtual `.venv`
- `ipykernel` instalado no ambiente

## O que ficou no projeto

- script para criar o `.venv` e instalar tudo
- script para adicionar dependencias novas de forma simples
- configuracao do workspace para o VS Code usar esse ambiente automaticamente
- suporte a Windows e Fedora/Linux
- base minima para notebooks cientificos: `numpy`, `scipy` e `matplotlib`

## Como fica parecido com o Colab

Se voce abrir um arquivo `.ipynb`, o VS Code mostra as celulas separadas, com botao de executar em cada uma, saida logo abaixo e kernel no topo do arquivo.

Se o seu codigo estiver em `.py` e voce quiser algo parecido com celulas do Colab, separe por blocos com:

```python
# %%
```

Isso permite rodar cada bloco na janela interativa do VS Code.

## Windows

### Setup

1. Clone o repositorio.
2. Abra a pasta no VS Code.
3. No terminal da pasta, rode:

```powershell
.\setup.ps1
```

Se preferir:

```bat
setup.bat
```

### Abrir notebooks

1. Instale as extensoes `Python` e `Jupyter` se o VS Code pedir.
2. Abra um `.ipynb`.
3. Selecione o interpretador ou kernel `.venv\Scripts\python.exe`.
4. Rode as celulas normalmente.

### Adicionar dependencias

Para instalar uma dependencia nova e ja salvar no `requirements-notebook.txt`, rode:

```powershell
.\add-dependency.ps1 pandas
.\add-dependency.ps1 seaborn scikit-learn
.\add-dependency.ps1 "librosa==0.11.0"
```

Se preferir usar `.bat`:

```bat
add-dependency.bat pandas
```

Esse comando faz duas coisas:

- instala o pacote dentro do `.venv`
- adiciona o pacote no `requirements-notebook.txt`

## Fedora / Linux

### Setup

1. Clone o repositorio.
2. Garanta que o Python 3 esteja instalado.
3. Abra a pasta no VS Code.
4. No terminal da pasta, rode:

```bash
bash setup.sh
```

### Abrir notebooks

1. Instale as extensoes `Python` e `Jupyter` se o VS Code pedir.
2. Abra um `.ipynb`.
3. Selecione o interpretador ou kernel `.venv/bin/python`.
4. Rode as celulas normalmente.

### Adicionar dependencias

Para instalar uma dependencia nova e ja salvar no `requirements-notebook.txt`, rode:

```bash
bash add-dependency.sh pandas
bash add-dependency.sh seaborn scikit-learn
bash add-dependency.sh "librosa==0.11.0"
```

Esse comando faz duas coisas:

- instala o pacote dentro do `.venv`
- adiciona o pacote no `requirements-notebook.txt`

## Arquivos importantes

- `requirements-notebook.txt`: lista das dependencias do projeto
- `scripts/manage_env.py`: backend cross-platform do setup
- `setup.ps1`, `setup.bat`, `setup.sh`: criam o `.venv` e instalam tudo
- `add-dependency.ps1`, `add-dependency.bat`, `add-dependency.sh`: instalam pacote novo e atualizam o `requirements-notebook.txt`
- `.vscode/settings.json`: faz o VS Code apontar para o Python do projeto
- `src/utils/plotting.py`: utilitario reutilizavel de plotagem

## Observacao importante sobre o .venv

O `.venv` fica no `.gitignore`.
Esse e o jeito mais limpo e confiavel de usar o projeto em outra maquina:

1. versionar `requirements-notebook.txt`
2. clonar o repo
3. rodar o setup do sistema atual

Isso evita poluir o git com milhares de arquivos, reduz o tamanho do repositorio e evita problemas de caminho ou compatibilidade entre maquinas.

## Resumo rapido

Voce nao precisa de JupyterLab no navegador para ter experiencia de notebook no VS Code.
O essencial e: `VS Code + extensoes Python/Jupyter + .venv + ipykernel`.

## Observacao sobre imports nos notebooks

Os notebooks localizam a pasta `src` em tempo de execucao e, a partir dela, importam utilitarios da pasta `utils`:

```python
from utils.plotting import plot_series
```

Isso evita depender de um pacote instalado no ambiente, mas continua deixando o import funcionar dentro dos notebooks do projeto.
