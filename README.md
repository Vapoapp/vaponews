# VAPO News — Radar Marítimo

Newsletter marítima gerada automaticamente a cada 6 horas.

## Estrutura

```
vapo-news/
├── app.py              # script principal
├── sources.json        # fontes de notícias
├── requirements.txt    # dependências Python
├── output/
│   ├── newsletter.html # newsletter gerada
│   └── radar.json      # dados estruturados
└── .github/workflows/
    └── vapo-news.yml   # automação GitHub Actions
```

## Configuração no GitHub

1. Crie um repositório no GitHub e envie os arquivos
2. Vá em **Settings → Secrets and variables → Actions**
3. Clique em **New repository secret**
4. Nome: `OPENAI_API_KEY` — Valor: sua chave da OpenAI
5. Pronto. O workflow roda automaticamente a cada 6 horas

## Rodar localmente

Crie um arquivo `.env` na raiz com:
```
OPENAI_API_KEY=sua_chave_aqui
```

Depois:
```bash
pip install -r requirements.txt
python app.py
```

A newsletter será gerada em `output/newsletter.html`.

## Ver a newsletter publicada

Ative o **GitHub Pages** no repositório:
- Settings → Pages → Source: `Deploy from a branch`
- Branch: `main` / pasta: `/ (root)`

A newsletter ficará disponível em:
`https://seu-usuario.github.io/vapo-news/output/newsletter.html`
