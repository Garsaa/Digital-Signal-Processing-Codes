# Ambiente local para notebooks no VS Code

Este projeto ficou configurado para usar notebooks direto no VS Code, sem abrir navegador.

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
- base minima para notebooks cientificos: `numpy`, `scipy` e `matplotlib`

## Como fica parecido com o Colab

Se voce abrir um arquivo `.ipynb`, o VS Code mostra as celulas separadas, com botao de executar em cada uma, saida logo abaixo e kernel no topo do arquivo.

Se o seu codigo estiver em `.py` e voce quiser algo parecido com celulas do Colab, separe por blocos com:

```python
# %%
```

Isso permite rodar cada bloco na janela interativa do VS Code.

## Como usar em outro computador

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

4. Instale as extensoes `Python` e `Jupyter` se o VS Code pedir.
5. Abra um `.ipynb`.
6. Selecione o interpretador ou kernel `.venv\Scripts\python.exe`.
7. Rode as celulas normalmente.

## Como adicionar dependencias

Para instalar uma dependencia nova e ja salvar no `requirements-notebook.txt`, rode:

```powershell
.\add-dependency.ps1 nome-do-pacote
```

Exemplos:

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

## Arquivos importantes

- `requirements-notebook.txt`: lista das dependencias do projeto
- `setup.ps1`: cria o `.venv` e instala tudo
- `add-dependency.ps1`: instala pacote novo e atualiza o `requirements-notebook.txt`
- `.vscode/settings.json`: faz o VS Code apontar para o Python do projeto

## Observacao importante sobre o .venv

O `.venv` fica no `.gitignore`.
Esse e o jeito mais limpo e confiavel de usar o projeto em outra maquina:

1. versionar `requirements-notebook.txt`
2. clonar o repo
3. rodar `.\setup.ps1`

Isso evita poluir o git com milhares de arquivos, reduz o tamanho do repositorio e evita problemas de caminho ou compatibilidade entre maquinas.

## Resumo rapido

Voce nao precisa de JupyterLab no navegador para ter experiencia de notebook no VS Code.
O essencial e: `VS Code + extensoes Python/Jupyter + .venv + ipykernel`.
