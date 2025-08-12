# 🧮 Cálculo de Pitágoras

Um projeto simples em **Python** para calcular a hipotenusa ou um dos catetos de um triângulo retângulo utilizando o **Teorema de Pitágoras**.

## 📌 Funcionalidades
- Calcular a **hipotenusa** a partir dos dois catetos.
- Calcular um **cateto** a partir da hipotenusa e do outro cateto.
- Interface via **linha de comando**.
- Tratamento básico de erros de entrada.

## 📚 Tecnologias
- **Python 3**
- **Matemática / Geometria**
- **CLI (Command Line Interface)**

## 🔢 Fórmula utilizada
O programa segue a fórmula do **Teorema de Pitágoras**:

a² + b² = c²

Onde:
- `a` e `b` → catetos
- `c` → hipotenusa

## 🚀 Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/deyvison55d/calculo-pitagoras.git
Acesse a pasta do projeto:
calculo-pitagoras

Execute o script principal:

-No Windows (PowerShell/Prompt):
py teste.py
ou
python teste.py

-No Linux / macOS:
teste.py

### Observações e sugestões (rápidas)
- Certifica que estás na pasta do projeto quando executar os comandos (onde ficam `teste.py`, `menu.py`, `funções.py`).
- Se quiser padronizar o projeto, eu recomendo **colocar um guard `if __name__ == "__main__":`** em `teste.py` ou renomeá-lo para `main.py`. Assim fica mais profissional e evita execução ao importar.
  Exemplo simples pra `teste.py`:
  ```python
  def main():
      res = menu('Calculo de Pitágoras')
      # ... resto do teu código ...

  if __name__ == "__main__":
      main()
