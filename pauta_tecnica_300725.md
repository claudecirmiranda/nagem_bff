
# 📋 Pauta de Reunião: Substituição do Oracle OCC no APP

**Data sugerida:** 30/07/2025  
**Duração estimada:** 1h
**Objetivo:** Alinhar as diretrizes técnicas e estratégicas para iniciar a construção de uma API interna que substitua o Oracle OCC, com foco inicial na tela **Home do APP**, garantindo reaproveitamento de componentes existentes, evitando retrabalho e promovendo escalabilidade.

---

## 🎯 Objetivos da Reunião

- Compreender o funcionamento atual do fluxo OCC no APP via BFF.
- Consolidar as chamadas necessárias para a Home do APP.
- Avaliar possibilidades de reaproveitamento da solução B2C existente.
- Definir uma proposta inicial de arquitetura.
- Levantar riscos técnicos e definir próximos passos.

---

## 📋 Agenda Proposta

| Horário | Tema                                                                 | Responsável / Time       |
|--------|----------------------------------------------------------------------|--------------------------|
| 5 min  | Abertura e contextualização da proposta                              | PO / Arquiteto           |
| 10 min | Visão atual do fluxo OCC no App via BFF                              | Tech Lead                |
| 15 min | Levantamento das chamadas necessárias para a Home do App             | Backend / Mobile         |
| 15 min | Análise de possíveis reaproveitamentos (site B2C, APIs legadas, etc.)| Tech Lead / Backend      |
| 10 min | Pontos críticos esperados: cache, performance, estruturação de dados | Arquiteto / Eng. de Dados|
| 10 min | Proposta de arquitetura inicial (nova API, cache, BFF, etc.)         | Arquiteto                |
| 5 min  | Próximos passos e responsáveis                                        | Todos                    |

---

## 🧠 Pauta Técnica

### 1. Cenário Atual
- O APP consome a home via BFF, que por sua vez chama o OCC.
- O B2C (site web PHP) já possui lógica para renderizar a home usando integrações legadas.

### 2. Objetivo Técnico
- Criar uma nova API in-house que substitua o OCC, servindo inicialmente para a Home do APP.
- Avaliar se o APP continuará usando BFF ou se consumirá a nova API diretamente.

### 3. Análise de Reaproveitamento
- Lógica do B2C já acessa informações como: catálogo, estoque, pedidos, clientes.
- Possibilidade de reutilizar conectores, regras de negócio e integrações com DB2.
- Avaliar viabilidade de portar essa lógica para um microsserviço moderno.

### 4. Funcionalidades da Home (segundo levantamento atual)

| Método                | Parâmetros   | Descrição                                                                 |
|-----------------------|--------------|---------------------------------------------------------------------------|
| `getBanners`         | `url`, `repositoryId`, `link`, `title`, `size`     | Retorna os banners principais da home.                                   |
| `getBannerBrand`     | `logoUrl`, `repositoryId`, `link`                  | Retorna logos de marcas.                                                 |
| `getMiniBanner`      | `url`, `size`, `showTop`, `redirect`              | Mini banners com posicionamento variável.                                |
| `getDynamicMiniBanner`| `url`, `repositoryId`, `redirect`                | Banner dinâmico com lógica de exibição.                                  |
| `getCategories`      | `url`, `id`, `link`, `title`                      | Categorias exibidas na home.                                             |
| `getHomeTopLink`     | Nenhum                                            | Informações do topo da home.                                             |
| `getLightningOffer`  | Nenhum                                            | Oferta relâmpago ou null.                                                |
| `getNagemCardBanner` | Nenhum                                            | Redirecionamento para tela "Nagem Card".                                 |
| `getBannersMeetNagem`| Nenhum                                            | Banners especiais "Meet Nagem".                                          |
| `getStoresEnabled`   | Nenhum                                            | Indica se lojas estão habilitadas.                                       |
| `getSocialLoginOptions`| Nenhum                                         | Lista de opções de login social.                                         |
| `getPopupHome`       | Nenhum                                            | Conteúdo configurável de popup.                                          |

### 5. Proposta de Arquitetura

- Nova API RESTful `/api/home` com versionamento e documentação clara (ex: OpenAPI)
- API Gateway para roteamento e segurança
- Redis ou CDN para caching de conteúdo estático (ex.: banners, categorias)
- Integração com serviços legados via adaptadores
- Possibilidade de fallback ou cache em caso de falha no legado

### 6. Pontos de Atenção

- Tempo de resposta da API para o APP (performance crítica)
- Flexibilidade para alterar layout da home sem novos deploys
- Segurança e autenticação (se aplicável)
- Governança de versionamento e integração com outros canais (web, APP)
- Planejamento de entrega por etapas (foco inicial: home)

---

## 📍 Decisões Esperadas da Reunião

- Aprovação da estratégia de substituição do OCC
- Validação sobre reaproveitamento do B2C (ou necessidade de refatoração)
- Aprovação da arquitetura inicial e plano incremental de entregas
- Definição de papéis e responsáveis por cada frente
- Estabelecimento de uma rotina de acompanhamento e validação

---
