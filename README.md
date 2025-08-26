
# Projeto: Substituição do Oracle OCC por API In-house

## 📘 Descrição
Este projeto tem como objetivo substituir o Oracle OCC por uma solução desenvolvida internamente, focando inicialmente na Home do APP. A nova arquitetura visa reaproveitar funcionalidades existentes no B2C Web e integrá-las ao APP de forma desacoplada e eficiente.

## 🏗️ Arquitetura Proposta
- APP Mobile consome dados da Home via BFF ou diretamente da nova API.
- API Gateway para roteamento e segurança.
- Nova API RESTful `/api/home` com versionamento e documentação.
- Redis/CDN para cache de conteúdo estático.
- Adaptadores para integração com serviços legados (DB2, lógica PHP do B2C).

## 📂 Estrutura de Diretórios Sugerida
```
project-root/
│
├── diagrams/
│   └── arquitetura_occ.py        # Código para gerar o diagrama de arquitetura
│
├── docs/
│   └── reuniao_tecnica_b2c_app.md  # Template de reunião técnica
│
├── README.md
└── requirements.txt
```

## 📦 Dependências
Para gerar o diagrama de arquitetura, instale a biblioteca `diagrams`:
```bash
pip install diagrams
```

## ▶️ Como Executar o Diagrama
1. Navegue até o diretório `diagrams/`:
```bash
cd diagrams
```
2. Execute o script:
```bash
python arquitetura_occ.py
```
3. O diagrama será gerado e exibido automaticamente.

## 📌 Referências
- Template de reunião técnica para avaliação do B2C
- Diagrama gerado com a biblioteca `diagrams`
- Funcionalidades da Home do APP mapeadas para substituição do OCC

