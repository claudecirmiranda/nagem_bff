# Documentação Técnica – Sistema de Gerenciamento de Conteúdo da Home do App (Substituição do Oracle OCC)

✅ Visão Geral da Solução
------------------------

### 🎯 Objetivo:

Implementar um sistema que permita:
*   **Cadastro e gestão de conteúdo** da home do app (banners, categorias, ofertas etc.)
    
*   **Publicação controlada via API REST**
    
*   **Uso de CDN para entrega rápida de imagens**
    
*   **Versionamento e rollback de conteúdo**
    
*   **Painel administrativo para gestão de conteúdo**
    

* * *

🧩 Componentes da Solução
-------------------------

| Componente | Função |
| --- | --- |
| Painel Admin (CMS) | Interface para cadastro e gestão de conteúdo |
| Backend API (Content API) | CRUD de banners, categorias, ofertas etc. |
| Banco de Dados (SQL/NoSQL) | Armazena metadados dos conteúdos (ex: URL da imagem, links, etc.) |
| Armazenamento (ex: S3/GCS) | Armazena as imagens e arquivos (upload via CMS ou endpoint REST) |
| CDN (Cloudflare, AWS CloudFront) | Acelera entrega de imagens e ativos estáticos |
| API pública de conteúdo | Endpoint consumido pelo BFF ou app diretamente |
| Redis | Cache de conteúdo dinâmico (para home do app) |
| Versionamento de conteúdo | Guardar histórico para rollback se necessário |
| Sistema de publicação | Botão "publicar" para mover rascunhos para produção |
| Observabilidade | Logs, tracing, dashboard de erros (Datadog, Grafana, etc.) |

* * *
## Arquitetura - Sistema de Conteúdo da Home do App (Substituição do OCC)

<img width="1236" height="1640" alt="arquitetura_-_sistema_de_conteúdo_da_home_do_app_(substituição_do_occ)" src="https://github.com/user-attachments/assets/650c143c-307d-464e-86c5-c71e6c4e61ad" />

* * *

🔧 Exemplo de Implementação Técnica
-----------------------------------

### 1. Painel CMS Customizado

*   Framework: React + Tailwind + Next.js ou AdminJS (Node)
    
*   Permite cadastrar banners, ofertas, categorias com preview
    
*   Upload de imagem → envia para bucket (S3, GCS)
    

### 2. API Backend (Content API)

*   Frameworks sugeridos:
    *   **Node.js (Express/Fastify)** com TypeORM/Mongoose
        
    *   **Python (FastAPI)** com SQLAlchemy ou MongoEngine
        
    *   **Java (Spring Boot)** com JPA
        
*   Endpoints:
    *   `GET /home` → retorna estrutura da home
        
    *   `POST /banners`, `GET /banners`, `PUT /banners/:id`
        
    *   `GET /categories`, etc.
        
    *   `POST /publish` → gera versão estática/cacheada da home
        

### 3. Armazenamento + CDN

*   Upload de imagem → salva no bucket
    
*   Armazena URL pública com CDN (exemplo: `https://cdn.gcb.com.br/images/banner-abc.jpg`)
    
*   CDN recomendado: Cloudflare, AWS CloudFront, GCP Cloud CDN
    

### 4. Estrutura de Dados (exemplo de um banner)

json

CopiarEditar

```json
{
    "id": "banner-123",
    "title": "Super Promoção",
    "imageUrl": "https://cdn.gcb.com.br/images/promo-1.jpg",
    "link": "/produto/456",
    "size": "medium",
    "position": "top",
    "active": true,
    "startDate": "2025-08-01T00:00:00Z",
    "endDate": "2025-08-10T23:59:59Z"
}
```

### 5. Versionamento e Publicação

*   Tabela `versions` que guarda snapshots da home
    
*   Cada "publicação" salva uma nova versão e atualiza o cache (Redis, por ex.)
    
*   Permite `rollback` via API
    

* * *

📦 Extra: Ferramentas & Infra
-----------------------------

| Função | Ferramenta recomendada |
| --- | --- |
| CMS Headless | Strapi, Sanity.io, Directus, Payload CMS |
| CDN | Cloudflare, AWS CloudFront, GCP Cloud CDN |
| Imagens otimizadas | ImageKit, imgproxy, Thumbor (on-prem) |
| Banco de dados | MongoDB (flexível) ou PostgreSQL |
| Cache | Redis, Varnish |
| API Gateway | Apigee, Kong, API Gateway (GCP/AWS) |
| Observabilidade | Grafana + Loki, Elastic, Datadog |

* * *

📈 Benefícios da Arquitetura Proposta
-------------------------------------

*   Conteúdo gerenciado por usuários de negócio (autonomia)
    
*   Cacheável, rápido e escalável
    
*   Desacoplamento entre app e origem de dados (corte do OCC)
    
*   Controle de versão + rollback
    
*   Menos dependência de deploys para alterar a home

---

## Fluxo de publicação e entrega de conteúdo
```mermaid
flowchart TD
    subgraph "Usuário de Negócio"
        CMS[CMS Admin - Painel Web]
    end

    subgraph "Backend"
        CMS -->|Gestor de conteúdo| CMS_API[CMS API / Backend Admin]
        CMS_API -->|Persistir| DB[Banco de Dados]
        CMS_API -->|Upload de mídia| Storage["Armazenamento (S3/GCS)"]
        Storage -->|Entrega de mídias| CDN[CDN - Cloudflare / CloudFront]
        CMS_API -->|Publicação de conteúdo| Publisher[Publicação de Conteúdo]
        Publisher -->|Controle de Versão| Versionamento[Controle de Versão]
        Publisher -->|Cache| Cache[Cache Redis]
    end

    subgraph "API Pública"
        APP[App Mobile / BFF]
        APP -->|GET /home| HomeAPI[API Pública de Conteúdo]
        HomeAPI -->|Leitura do Cache| Cache
        HomeAPI -->|Fallback| DB
        HomeAPI -->|Entrega de Imagens| CDN
    end

    style CMS_API fill:#f9f,stroke:#333,stroke-width:1px
    style HomeAPI fill:#bbf,stroke:#333,stroke-width:1px
    style CDN fill:#ffd,stroke:#333,stroke-width:1px
    style Cache fill:#efe,stroke:#333,stroke-width:1px
    style DB fill:#eee,stroke:#333,stroke-width:1px
```


---

### 🔎 Explicação do Diagrama

- **Usuário de negócio** acessa o **CMS** para cadastrar e editar conteúdos da Home (banners, categorias etc.).
- As imagens são enviadas para um bucket de **armazenamento** (como S3 ou GCS).
- O CMS envia metadados para o banco de dados e chama o serviço de **Publicação**.
- No momento da publicação, o conteúdo ativo é salvo no Redis e pode ser versionado para rollback.
- A **API Pública** da Home é consumida pelo App (ou BFF) e retorna conteúdo diretamente do cache (com fallback no DB).
- As imagens são servidas via **CDN** para performance.

---

