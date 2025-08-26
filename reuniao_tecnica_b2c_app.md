## 🧩 Reunião Técnica: Avaliação de Reaproveitamento do B2C no APP

**Objetivo:**  
Investigar a viabilidade de reutilizar funcionalidades do B2C Web no APP, evitando integração com Oracle OCC.

**Participantes:**  
- Claudecir Miranda da Silva  
- Rômulo Nóbrega (Arquiteto)
- Darkson Santos (CIO)

**Data/Hora:**  
26/08/2025

**Local/Link:**  
[Reunião no Teams](https://teams.microsoft.com/l/meetup-join/19%3ameeting_NTNjNDBlNjEtYWI1Yi00MTdkLWI0Y2ItNzlhY2UwYjg1NTBk%40thread.v2/0?context=%7b%22Tid%22%3a%2243b6efd3-133a-4e68-b1e8-84c18550db5d%22%2c%22Oid%22%3a%2284ec9a27-babf-4c23-a565-4931369f63e2%22%7d)

---

### 📌 Pauta

1. **Apresentação do Contexto**
   - APP e B2C são aplicações separadas.
   - Identificadas funcionalidades no B2C que podem atender ao APP.
   - Objetivo é substituir o OCC por uma solução interna.

2. **Mapeamento Funcionalidades Relevantes**
   | Funcionalidade         | Usada no B2C | Relevante para o APP | Acoplada à view? | Acesso via classe/serviço? |
   |------------------------|--------------|-----------------------|------------------|-----------------------------|
   | Banners                | ✅           | ✅                    | ❌               | ✅                          |
   | Categorias             | ✅           | ✅                    | ❌               | ✅                          |
   | Ofertas relâmpago      | ✅           | ✅                    | ❌               | ✅                          |
   | Nagem Card             | ✅           | ✅                    | ❓               | ❓                          |
   | Popup configurável     | ✅           | ✅                    | ❓               | ❓                          |

3. **Revisão Técnica Guiada**
   - Mostrar como as funcionalidades estão implementadas.
   - Verificar separação entre lógica e apresentação.
   - Identificar dependências com sessão, cookies, ou estado do navegador.

4. **Avaliação de Viabilidade Técnica**
   | Critério                          | Avaliação | Observações |
   |----------------------------------|-----------|-------------|
   | Facilidade de desacoplamento     | Alta      | Lógica já em serviços |
   | Complexidade de dependências     | Média     | Algumas dependências com sessão |
   | Tempo estimado para expor via API| Curto     | Pode ser feito com adaptadores |
   | Benefício para o APP             | Alto      | Evita dependência do OCC |

5. **Proposta de Prototipagem**
   - Criar uma API interna experimental com 1 ou 2 funcionalidades.
   - Validar tempo de resposta, formato de dados e integração com o APP.

6. **Próximos Passos**
   - [ ] Identificar responsáveis por cada funcionalidade.
   - [ ] Definir escopo do protótipo.
   - [ ] Estimar esforço para desacoplamento.
   - [ ] Planejar testes de integração com o APP.

---

### 📂 Anexos e Referências
- Diagrama de arquitetura proposto
- [Lista de métodos da Home do APP](app_metodos_home.md)
- Código-fonte ou trechos relevantes do B2C
