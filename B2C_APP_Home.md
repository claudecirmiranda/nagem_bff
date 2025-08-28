
# ✅ Próximos Passos - Integração APP com API B2C

Este documento organiza as tarefas por equipe para implementar a rota `/app/home` no B2C, conforme contrato JSON definido pelo APP.

---

## 🔧 Equipe B2C (Backend/API)

| Tarefa | Descrição | Responsável | Status |
|--------|-----------|-------------|--------|
| Criar rota `GET /app/home` | Implementar endpoint que retorna o JSON conforme contrato | [Nome] | ⬜ |
| Mapear origem dos dados | Identificar onde estão os dados de banners, categorias, ofertas etc. | [Nome] | ⬜ |
| Refatorar lógica para desacoplamento | Separar regras de negócio da camada de apresentação PHP | [Nome] | ⬜ |
| Implementar camada de formatação | Garantir que o JSON siga exatamente o contrato esperado | [Nome] | ⬜ |
| Validar sessão unificada | Integrar com sistema de autenticação compartilhado | [Nome] | ⬜ |
| Testar endpoint com dados reais | Validar tempo de resposta, consistência e segurança | [Nome] | ⬜ |

---

## 📱 Equipe APP (Mobile/BFF)

| Tarefa | Descrição | Responsável | Status |
|--------|-----------|-------------|--------|
| Validar contrato JSON | Confirmar que o formato atende às necessidades do front | [Nome] | ✅ |
| Preparar consumo da nova rota | Refatorar chamadas para usar `GET /app/home` | [Nome] | ⬜ |
| Implementar parser do JSON | Traduzir os dados recebidos para componentes visuais | [Nome] | ⬜ |
| Testar integração com sessão unificada | Garantir persistência e sincronização | [Nome] | ⬜ |
| Validar comportamento offline/cache | Definir fallback para dados da Home | [Nome] | ⬜ |

---

## 🧩 Tarefas Compartilhadas

| Tarefa | Descrição | Responsável | Status |
|--------|-----------|-------------|--------|
| Definir estratégia de rollout | Ex: canary release, feature flag, ambiente de staging | [Ambos] | ⬜ |
| Monitorar consumo e erros | Usar logs, métricas e alertas para garantir estabilidade | [Ambos] | ⬜ |
| Documentar contrato e fluxo | Criar documentação técnica para manutenção futura | [Ambos] | ⬜ |


---

## Contrato JSON esperado pelo APP

```json
{
  "bannersCarousel": {
    "tipo": "bannersCarousel",
    "banners": [
      {
        "img": "v485318361505659420/general/SEMANA+GAMER+-+BANNER+APP.png",
        "redirecionamento": "colecao/posicao_01",
        "dispositivo": "smartphone"
      },
      {
        "img": "v4626474517768653833/general/SEMANA+GAMER+-+BANNER+TABLETS.png",
        "redirecionamento": "colecao/posicao_01",
        "dispositivo": "tablet"
      },
      {
        "img": "v7612387884384207331/general/CADEIRAS+GAMER+-+BANNER+APP.png",
        "redirecionamento": "colecao/posicao_02"
      }
    ]
  },
  "bannersMarca": {
    "tipo": "bannersMarca",
    "banners": [
      {
        "img": "v4101847939115736028/collections/LG_logo_(2014).svg.png",
        "redirecionamento": "busca/lg"
      },
      {
        "img": "v3041224718792718283/collections/samsung.png",
        "redirecionamento": "busca/samsung"
      }
    ]
  },
  "miniBanners": {
    "tipo": "miniBanners",
    "banners": [
      {
        "img": "v7238376117246563035/collections/CUPOM+APP+-+MINI+BANNER+APP.png",
        "redirecionamento": "busca/samsung",
        "dispositivo": "smartphone"
      },
      {
        "img": "v7238376117246563035/collections/CUPOM+APP+-+MINI+BANNER+APP2.png",
        "redirecionamento": "busca/samsung",
        "dispositivo": "tablet"
      }
    ]
  },
  "bannersCategoria": {
    "tipo": "bannersCategoria",
    "banners": [
      {
        "img": "v180623436198978007/collections/Tumbrl.png",
        "redirecionamento": "colecao/Tumbrl_01",
        "titulo": "Ofertas da Semana"
      },
      {
        "img": "v1284562344028099285/collections/Frame+1000003101.png",
        "redirecionamento": "busca/notebook",
        "titulo": "Notebook"
      },
      {
        "img": "v4965422493062392395/collections/Frame+1000003102.png",
        "redirecionamento": "busca/Smartwatch",
        "titulo": "Smartwatch"
      },
      {
        "img": "v1282648534463691064/collections/Frame+1000003103.png",
        "redirecionamento": "busca/Cadeira_gamer",
        "titulo": "Cadeira gamer"
      }
    ]
  },
  "ofertaNoturna": {
    "tipo": "ofertaNoturna",
    "inicio": "2025-08-26 17:30:00",
    "fim": "2025-08-27 17:00:00",
    "produtos": [
      {
        "precoVenda": 217.57,
        "precoPromocao": 217.57,
        "titulo": "Caixa de Som JBL JR POP 3W Bluetooth Roxo",
        "img": "v1336302444225000462/products/506907.506907_4.jpg&height=940&width=940",
        "produtoId": "506907"
      }
    ]
  },
  "vitrine1": {
    "tipo": "vitrine",
    "titulo": "SMART TVS",
    "redirecionamento": "colecao/SET01",
    "produtos": [
      {
        "id": "610160",
        "titulo": "Smart TV AOC 32\" S5045 HD Roku Processador Quad Core Visual sem Bordas Dolby Audio Google Assistant AirPlay2",
        "img": "v4753662910697220249/products/610160.610160.jpg&height=940&width=940",
        "precoVenda": 1359,
        "precoPromocao": 999,
        "lancamento": false,
        "prevenda": false,
        "exclusivo": false,
        "exclusivoApp": false,
        "freteGratis": "Frete Grátis Nordeste",
        "parcelaMaximaSemJuros": 10,
        "estoque": 25,
        "seloCampanhaNagem": null,
        "seloCampanhaFabricante": null,
        "nota": 0,
        "numeroAvaliacoes": 0
      }
    ]
  },
  "banner1": {
    "tipo": "banners",
    "banners": [
      {
        "img": "v4098840503878106628/collections/Banner_Mob_5445%2B(1).png",
        "dispositivo": "smartphone",
        "redirecionamento": "busca/smart tv"
      },
      {
        "url": "v7893500540618664452/collections/image+28.png",
        "dispositivo": "tablet",
        "redirecionamento": "busca/smart tv"
      }
    ]
  },
  "linkTopo": {
    "tipo": "linkTopo",
    "links": [
      {
        "titulo": "teste",
        "redirecionamento": "busca/texto"
      },
      {
        "titulo": "teste2",
        "redirecionamento": "busca/texto 2"
      }
    ]
  },
  "ofertaRelampago": {
    "tipo": "ofertaRelampago",
    "titulo": "Oferta relâmpago",
    "subtitulo": "Aproveite as ofertas",
    "inicio": "2025-08-26 17:30:00",
    "fim": "2025-08-27 17:00:00",
    "cor": "#C1C1C1",
    "icone": "v4753662910697220249/products/610160.610160.jpg&height=940&width=940",
    "produtos": [
      {
        "id": "610160",
        "titulo": "Smart TV AOC 32\" S5045 HD Roku Processador Quad Core Visual sem Bordas Dolby Audio Google Assistant AirPlay2",
        "img": "v4753662910697220249/products/610160.610160.jpg&height=940&width=940",
        "precoVenda": 1359,
        "precoPromocao": 999,
        "lancamento": false,
        "prevenda": false,
        "exclusivo": false,
        "exclusivoApp": false,
        "freteGratis": "Frete Grátis Nordeste",
        "parcelaMaximaSemJuros": 10,
        "estoque": 25,
        "seloCampanhaNagem": null,
        "seloCampanhaFabricante": null,
        "nota": 0,
        "numeroAvaliacoes": 0
      }
    ]
  },
  "popupHome": {
    "tipo": "popupHome",
    "banners": [
      {
        "img": "v4965422493062392395/collections/Frame+1000003102.png",
        "redirecionamento": "busca/smart tv",
        "dispositivo": "smartphone"
      },
      {
        "img": "v4965422493062392395/collections/Frame+1000003102.png",
        "redirecionamento": "busca/smart tv",
        "dispositivo": "tablet"
      }
    ]
  },
  "sequencia": [
    "ofertaNoturna",
    "linkTopo",
    "cartaoNagem",
    "bannersCarousel",
    "miniBanners",
    "bannerUsuarioDeslogado",
    "bannersCategoria",
    "bannersMarca",
    "ofertaRelampago",
    "banner1",
    "vitrine1",
    "popupHome"
  ]
}

```
