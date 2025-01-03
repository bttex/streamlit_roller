# Rolador de Dados de D&D com Streamlit

Este é um aplicativo web simples para rolar dados de RPG (Role-Playing Game), como os usados em Dungeons & Dragons (D&D). Ele foi construído usando a biblioteca Streamlit em Python.

## Funcionalidades

*   **Seleção do tipo de dado:** Escolha entre dados de 4, 6, 8, 10, 12, 20 e 100 lados (d4, d6, d8, d10, d12, d20 e d100).
*   **Quantidade de dados:** Role múltiplos dados ao mesmo tempo (até 10).
*   **Modificador:** Adicione ou subtraia um modificador ao resultado da rolagem.
*   **Interface amigável:** Interface web interativa criada com Streamlit.
*   **PWA (Progressive Web App):** Suporte para instalação como um aplicativo web progressivo (requer configuração adicional - veja abaixo).

## Como usar

1.  **Pré-requisitos:**
    *   Python 3.7 ou superior.
    *   As seguintes bibliotecas Python:
        *   `streamlit`
        *   `random`
        *   `matplotlib` (Embora não esteja sendo usada para animação neste momento, pode ser útil para futuras implementações)
        *   `numpy` (Similar ao matplotlib)

2.  **Instalação das dependências:**

    ```bash
    pip install streamlit matplotlib numpy
    ```

3.  **Execução do aplicativo:**

    ```bash
    streamlit run your_script_name.py  # Substitua your_script_name.py pelo nome do seu arquivo Python
    ```

4.  **Acesso ao aplicativo:**

    Abra o navegador e acesse o endereço fornecido pelo Streamlit no terminal (geralmente `http://localhost:8501`).

## Como usar o aplicativo

1.  Selecione o tipo de dado que você deseja rolar no menu suspenso "Selecione o tipo de dado".
2.  Insira a quantidade de dados que você deseja rolar no campo "Quantos dados deseja rolar?".
3.  Se desejar, insira um modificador no campo "Modificador (+/-)".
4.  Clique no botão "Rolar Dados".
5.  Os resultados da rolagem individual e o resultado final com o modificador serão exibidos na tela.

## Suporte a PWA (Opcional)

Para habilitar a funcionalidade de PWA, você precisa criar os arquivos `manifest.json` e `service-worker.js` na mesma pasta do seu script Python.

**Exemplo de `manifest.json`:**

```json
{
  "name": "Rolador de Dados de D&D",
  "short_name": "Rolador de Dados",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    {
      "src": "icon.png",  // Substitua pelo caminho do seu ícone
      "sizes": "192x192",
      "type": "image/png"
    }
  ]
}