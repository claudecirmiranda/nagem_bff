# DOCUMENTAÇÃO DOS MÉTODOS DO OCC UTILIZADOS PELO BFF

# Documentação dos Métodos de Favoritos (OCC)

## 1. Criar Lista de Produtos Favoritos

**Função:** `createPurchaseList`  
**Arquivo:** favoriteProductsService.js  
**Rota interna:** `POST /api/nagem/favorite_products/create_list_products`

- **Método OCC:** `POST`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - `body` (object): Dados da lista a ser criada (exemplo: nome, itens).
  - `accessToken` (string): Token de acesso do usuário.
- **Retorno esperado:**
  - Sucesso: Dados da lista criada.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de body:**

**entrada:**

```json
{
  "name": "Favoritos",
  "description": "Minha lista de favoritos",
  "items": [{ "catRefId": "sku123", "quantity": 1 }]
}
```

**Saida:**

```json
{
  "id": "123",
  "name": "Favoritos",
  "description": "Minha lista de favoritos",
  "items": [{ "catRefId": "sku123", "quantity": 1 }],
  "createdDate": "2024-01-01T12:00:00Z"
}
```

---

## 2. Listar Listas de Produtos Favoritos

**Função:** `listPurchaseLists`  
**Arquivo:** favoriteProductsService.js  
**Rota interna:** `GET /api/nagem/favorite_products/list_products_lists`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - `accessToken` (string): Token de acesso do usuário.
- **Retorno esperado:**
  - Sucesso: Objeto com as listas de favoritos do usuário.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de resposta de sucesso:**

```json
{
  "items": [
    {
      "id": "123",
      "name": "Favoritos",
      "description": "Minha lista de favoritos",
      "items": [{ "catRefId": "sku123", "quantity": 1 }],
      "createdDate": "2024-01-01T12:00:00Z"
    }
  ]
}
```

---

## 3. Obter Lista de Produtos Favoritos por ID

**Função:** `getPurchaseList`  
**Arquivo:** favoriteProductsService.js  
**Rota interna:** `GET /api/nagem/favorite_products/get_list_products/:id`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists/{id}`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - `id` (string): ID da lista de favoritos.
  - `accessToken` (string): Token de acesso do usuário.
- **Retorno esperado:**
  - Sucesso: Detalhes da lista de favoritos, incluindo os produtos.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de resposta de sucesso:**

```json
{
  "id": "123",
  "name": "Favoritos",
  "items": [
    {
      "catRefId": "sku123",
      "quantity": 1,
      "addedDate": "2024-01-01T12:00:00Z"
    }
  ]
}
```

---

## 4. Atualizar Itens da Lista de Favoritos

**Função:** `updateItems`  
**Arquivo:** favoriteProductsService.js  
**Rota interna:** `POST /api/nagem/favorite_products/update_items/:id`

- **Método OCC:** `POST`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists/{id}/updateItems`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - `id` (string): ID da lista de favoritos.
  - `body` (object): Dados dos itens a serem atualizados.
  - `accessToken` (string): Token de acesso do usuário.
- **Retorno esperado:**
  - Sucesso: Dados atualizados da lista.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de body:**

**entrada:**

```json
{
  "items": [
    { "catRefId": "sku123", "quantity": 1 },
    { "catRefId": "sku456", "quantity": 2 }
  ]
}
```

**Saida:**

```json
{
  "id": "123",
  "items": [
    { "catRefId": "sku123", "quantity": 1 },
    { "catRefId": "sku456", "quantity": 2 }
  ]
}
```

---

## HOME CONTENT

- **URL interna:** `GET /api/nagem/home/home_content`
- **URL OCC:** (vários, via métodos internos)
- **Métodos usados:**
  - `getCarouselBanners`, `getDynamicBannerBrand`, `getDynamicMiniBanner`, `getDynamicBannerThumb`, `getDynamicPopup`, `getNightOffer`, `getAppHome`, `getHomeTopLink`, `getLightningOffer`, `getNagemCardBanner`, `getBannersMeetNagem`, `getStoresEnabled`, `getSocialLoginOptions`, `productsController.getAllReviews`, `productsController.getCategoryContent`, `productsController.getMenuCategories`, `getPopupHome`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**

  ```json
  {
  "carouselBanners": [
    { "id": "carousel1", "imageUrl": "...", "link": "...", "title": "..." }
  ],
  "bannerBrand": [
    { "id": "brand1", "imageUrl": "...", "brand": "...", "link": "..." }
  ],
  "miniBanner": [
    { "id": "mini1", "imageUrl": "...", "link": "...", "title": "..." }
  ],
  "bannerThumb": [
    { "id": "thumb1", "imageUrl": "...", "link": "...", "title": "..." }
  ],
  "popup": { "id": "popup1", "imageUrl": "...", "link": "..." },
  "nightOffer": { "products": [{ "sku": "...", "name": "...", "price": 99.9 }] },
  "appHome": { "highlights": [...], "categories": [...], "products": [...] },
  "topLinks": [
    { "id": "link1", "title": "...", "url": "..." }
  ],
  "lightningOffer": { "products": [{ "sku": "...", "name": "...", "price": 89.9 }], "banner": {...} },
  "nagemCardBanner": { "id": "cardBanner1", "imageUrl": "...", "link": "...", "title": "..." },
  "bannersMeetNagem": [
    { "id": "meetNagem1", "imageUrl": "...", "link": "...", "title": "..." }
  ],
  "storesEnabled": true,
  "socialLoginOptions": [
    { "google": true, "facebook": true, "apple": false }
  ],
  "reviews": [
    { "productId": "sku123", "rating": 5, "comment": "Ótimo produto!" }
  ],
  "categoryContent": { "id": "cat1", "name": "Categoria X", "products": [...] },
  "menuCategories": [
    { "id": "cat1", "name": "...", "imageUrl": "...", "link": "..." }
  ],
  "popupHome": { "popupId": "...", "imageUrl": "...", "link": "..." }
  }

  ```

---

## HOME REFRESH

- **URL interna:** `GET /api/nagem/home/refresh?avoidJson=true&forceUpdate=true`
- **URL OCC:** (vários, via métodos internos)
- **Métodos usados:** Mesmos do `HOME CONTENT`
- **Entrada:**
  - `accessToken` (header)
  - Query: `avoidJson`, `forceUpdate`
- **Saída:** Igual ao `HOME CONTENT`

---

## GET BANNERS

- **URL interna:** `GET /api/nagem/home/banners`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/Banner_Home`
- **Métodos usados:** `homeService.getBanners`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [
    {
      "url": "v7784079554719369312/collections/image+39+(1).png",
      "repositoryId": "m330001",
      "link": "voltaasaulas",
      "token": "",
      "size": "mediumTag"
    }
  ]
  ```

---

## GET BANNERS CAROUSEL

- **URL interna:** `GET /api/nagem/home/carousel_banners`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/banner_carousel_home`
- **Métodos usados:**
  - `homeService.getCarouselBanners`, depois `homeService.getBannersList`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [
    {
      "url": "v6513603996136993650/collections/Eletrinhos+-+BANNER+PRINCIPAL+DESK+APP.png",
      "repositoryId": "m360302",
      "link": "cupom",
      "title": "slider_image",
      "token": "",
      "size": "mediumTag"
    },
    {
      "url": "v7345631679080958953/collections/Eletrinhos+-+BANNER+PRINCIPAL+DESK+APP-1.png",
      "repositoryId": "m360354",
      "link": "cupom",
      "title": "slider_image",
      "token": "",
      "size": "largeTag"
    }
  ]
  ```

---

## GET BANNER LIGHTNING OFFER

- **URL interna:** `GET /api/nagem/home/lightning_offer`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/oferta_relampago`
- **Métodos usados:**
  - `homeService.getVitrine('oferta_relampago')`, `searchProducts.getProduct`, `homeService.getBannersList`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  { "products": [{ "sku": "...", "name": "...", "price": ... }], "banner": {...} }
  ```

---

## GET BANNER BRAND

- **URL interna:** `GET /api/nagem/home/banner_brand`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/banner_marca`
- **Métodos usados:** `homeService.getBannerBrand`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [
    {
      "url": "v6187601411224870739/collections/download+(2).png",
      "repositoryId": "m80029",
      "link": "search|microsoft",
      "token": ""
    },
    {
      "url": "v4101847939115736028/collections/LG_logo_(2014).svg.png",
      "repositoryId": "m251946",
      "link": "search|lg",
      "token": ""
    }
  ]
  ```

---

## GET APP HOME

- **URL interna:** `GET /api/nagem/home/getAppHome?customerId=27993024&forceUpdate=true`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/home_app`
- **Métodos usados:**
  - `homeService.getAppHome`, `homeService.getAppHomeContent`, `searchProducts.getProductsHome`, `yourviewService.getProductsReviews`, `homeService.getCategoriesTeste`, `homeService.getCartRecommendation`
- **Entrada:**
  - `accessToken` (header)
  - Query: `customerId`, `forceUpdate`
- **Saída:**
  ```json
  [
    {
      "id": "destaque_mobile",
      "name": "Destaque da Home Smartphone",
      "repositoryId": "home_app",
      "searchId": null,
      "link": null,
      "redirect": null,
      "products": [],
      "collection_type": "banner",
      "start": null,
      "end": null,
      "banners": [
        {
          "url": "v2571079679431542651/collections/image+255.png",
          "repositoryId": "m360325",
          "link": "eletrodomesticos30",
          "size": "mediumTag"
        },
        {
          "url": "v60741239225669955/collections/image+254.png",
          "repositoryId": "m360331",
          "link": "link|https://vendaonline.bradescard.com.br/?canal=544&origem=152&tpopto=3&ptovda=16001&campa=002",
          "size": "mediumTag"
        }
      ]
    }
  ]
  ```

---

## GET POPUP HOME

- **URL interna:** `GET /api/nagem/home/get_popup_home`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/popup_home`
- **Métodos usados:** `homeService.getPopupHome`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  {
    "redirect": "SET01",
    "images": [
      {
        "url": "v7451608277392521988/collections/launchDialogHomeTVSamsung.png",
        "size": null
      }
    ]
  }
  ```

---

## GET HOME SPECIAL SHOW CASES

- **URL interna:** `GET /api/nagem/home/getHomeSpecialShowcases`
- **URL OCC:** (vários, via métodos internos)
- **Métodos usados:**
  - `homeService.getAppHome`, `homeService.getAppHomeContent`, `searchProducts.getProductsHome`, `homeService.getCartRecommendation`, `homeService.getCategoriesTeste`, `yourviewService.getProductsReviews`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**

  ```json
  [
    {
      "id": "DescontoEspeciais",
      "name": "DESCONTOS ESPECIAIS",
      "repositoryId": "home_app",
      "searchId": null,
      "link": null,
      "redirect": "showcase|DescontoEspeciais",
      "products": [
        {
          "id": "583294",
          "displayName": "Caixa de Som JBL Charge 5 Wi-Fi 40W Bluetooth à Prova D'água Preta",
          "primaryLargeImageURL": "/ccstore/v1/images/?source=/file/v2616241075149801625/products/583294.583294.jpg&height=940&width=940",
          "listPrice": 1899,
          "salePrice": null,
          "x_lancamento": null,
          "x_prevenda": "0",
          "x_exclusivo": "0",
          "x_exclusivo_app": null,
          "x_freteGratis": null,
          "x_descontoBoleto": 5,
          "x_descontoPix": 5,
          "x_parcelaMximaSemJuros": 10,
          "in_stock": true,
          "x_imageSrcNagemCampaign": null,
          "x_imageSrcManufacturerCampaign": null,
          "rating": 0,
          "total_rating": 0
        }
      ]
    }
  ]
  ```

---

## GET CATEGORIES

- **URL interna:** `GET /api/nagem/home/categories`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/Thumbs`
- **Métodos usados:** `homeService.getCategories`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [
    {
      "url": "v683084329620656408/collections/image+63.png",
      "repositoryId": "m330002",
      "link": "voltaasaulas",
      "title": "Volta as Aulas",
      "token": ""
    },
    {
      "url": "v4074251517160314304/collections/Component+3+(1).png",
      "repositoryId": "m230186",
      "link": "Ofertadasemana",
      "title": "Ofertas da Semana",
      "token": ""
    },
    {
      "url": "v2926784128986122417/collections/Component+4+(1).png",
      "repositoryId": "m230187",
      "link": "GRP185",
      "title": "Smartphones",
      "token": ""
    }
  ]
  ```

---

## GET NIGHT OFFER

- **URL interna:** `GET /api/nagem/home/night_offer`
- **URL OCC:** (vários, via métodos internos)
- **Métodos usados:**
  - `PostLogin`, `settingsService.settingsDev('offerBannerSettings')`, `searchProducts.getSKU`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**

  ```json
  {
    "id": "nightOffer",
    "start": "2025-06-12 17:30:00",
    "end": "2025-06-13 06:00:00",
    "product_id": "609111",
    "token": "ey...",
    "products": [
      {
        "listPrice": 319,
        "salePrice": 239,
        "displayName": "Câmera...",
        "image": "https...",
        "productId": "609111"
      }
    ],
    "linkBanner": "banner_menuAPP_oferta_noturna.png",
    "isDefaultBanner": false,
    "product": {
      "listPrice": 319,
      "salePrice": 239,
      "displayName": "Câmera ...",
      "image": "https...",
      "productId": "609111"
    }
  }
  ```

---

## GET MINI BANNER

- **URL interna:** `GET /api/nagem/home/mini_banner`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/mini_banner`
- **Métodos usados:** `homeService.getMiniBanner`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [
    {
      "image_url": "v2493413822646893165/collections/Banner_Mob_6719.png",
      "size": "mediumTag",
      "on_top": false,
      "redirect": "screen|nagem_card",
      "token": ""
    },
    {
      "image_url": "v785909513092567691/collections/Banner_6719+(1).png",
      "size": "largeTag",
      "title": "Mini Banner",
      "on_top": false,
      "redirect": "screen|nagem_card",
      "token": ""
    }
  ]
  ```

---

## GET DYNAMIC MINIBANNER

- **URL interna:** `GET /api/nagem/home/dynamic_mini_banner`
- **URL OCC:** (usado internamente)
- **Métodos usados:**
  - `homeService.getCollection('home_mini_banner', token)`, `homeService.getBannersList`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [
    {
      "image_url": "v2733292334646701671/collections/image+241.png",
      "repositoryId": "m360312",
      "redirect": "posicao_01",
      "on_top": false,
      "token": "",
      "size": "mediumTag"
    },
    {
      "image_url": "v3220196884676173805/collections/Frame+1000002565.png",
      "repositoryId": "m360356",
      "redirect": "posicao_01",
      "on_top": false,
      "token": "",
      "size": "largeTag"
    },
    {
      "image_url": "v5246385111156892121/collections/image+244.png",
      "repositoryId": "m360313",
      "redirect": "posicao_02",
      "on_top": false,
      "token": "",
      "size": "mediumTag"
    },
    {
      "image_url": "v4226282063616801463/collections/Frame+1000002567.png",
      "repositoryId": "m360357",
      "redirect": "posicao_02",
      "on_top": false,
      "token": "",
      "size": "largeTag"
    }
  ]
  ```

---

## GET CARD NAGEM BANNER

- **URL interna:** `GET /api/nagem/home/card_banner`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/botao_cartao_nagem`
- **Métodos usados:** `homeService.getNagemCardBanner`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  {
    "redirect": "screen|nagem_card"
  }
  ```

---

## GET TO LINK

- **URL interna:** `GET /api/nagem/home/home_top_link`
- **URL OCC:** (usado internamente)
- **Métodos usados:** `homeService.getVitrine('link_topo')`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [{ "id": "link1", "title": "...", "url": "..." }]
  ```

---

## GET VITRINE

- **URL interna:** `GET /api/nagem/home/showcases/:showcaseId`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccadmin/v1/collections`
- **Métodos usados:** `homeService.getVitrine`
- **Entrada:**
  - `accessToken` (header)
  - `showcaseId` (param)
- **Saída:**

  ```json

  ```

---

## GET BANNERS MEET NAGEM

- **URL interna:** `GET /api/nagem/home/banners_meet_nagem`
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections/carrossel_quem_somos`
- **Métodos usados:** `homeService.getBannersMeetNagem`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [
  		{
  			"url": "v8513736117924209834/collections/carrossel_1.jpg",
  			"repositoryId": "m200001",
  			"token": ""
  		},
  		{
  			"url": "v8582979373748387365/collections/carrossel_2.jpg",
  			"repositoryId": "m200002",
  			"token": ""
  		}
  	],
  ```

---

## GET BANNERS LIST - não tem rota no BFF

**Descrição:** Monta uma lista de banners a partir de uma coleção.
- **Usado por:** homeService.getCarouselBanners, homeService.getDynamicMiniBanner, etc.
- **URL interna:** (usado internamente)
- **URL OCC:** `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/collections?categoryIds=<ids>`
- **Métodos usados:** `homeService.getBannersList`
- **Entrada:**
  - `accessToken` (header)
  - `categoryIds` (query)
  ````json
  {
    "categoryIds": "banner_carousel_home"
  }
  ````


- **Saída:**

  ```json
  [
    {
      "url": "v6513603996136993650/collections/Eletrinhos+-+BANNER+PRINCIPAL+DESK+APP.png",
      "repositoryId": "m360302",
      "link": "cupom",
      "title": "slider_image",
      "size": "mediumTag"
    }
  ]
  ```

---

## getDynamicBannerBrand

- **URL interna:** (usado internamente)
- **URL OCC:** (usado internamente)
- **Métodos usados:**
  - `homeService.getCollection('home_banner_marca', token)`, `homeService.getBannersList`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**

  ```json

  ```

---

## getDynamicBannerThumb

- **URL interna:** (usado internamente)
- **URL OCC:** (usado internamente)
- **Métodos usados:**
  - `homeService.getCollection('home_thumbs', token)`, `homeService.getBannersList`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  [{ "id": "dynamicThumb1", "imageUrl": "...", "link": "...", "title": "..." }]
  ```

---

## getDynamicPopup

- **URL interna:** (usado internamente)
- **URL OCC:** (usado internamente)
- **Métodos usados:**
  - `homeService.getCollection('home_popup', token)`, `homeService.getBannersList`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**

  ```json

  ```

---

## getStoresEnabled

- **URL interna:** `GET /api/nagem/home/stores_enabled`
- **URL OCC:** (usado internamente)
- **Métodos usados:** `settingsService.settingsDev('retiraemloja')`
- **Entrada:**
  - Nenhuma ou `accessToken` (header)
- **Saída:**
  ```json
  { "enabled": true }
  ```

---

## getSocialLoginOptions

- **URL interna:** `GET /api/nagem/home/getSocialLoginOptions`
- **URL OCC:** (usado internamente)
- **Métodos usados:** `settingsService.settingsDev('appSocialLogin')`
- **Entrada:**
  - Nenhuma ou `accessToken` (header)
- **Saída:**
  ```json
  {
    "google": true,
    "facebook": true,
    "apple": false
  }
  ```

---

## **LandingPage**:

## GET LANDING PAGE

- **URL interna:**  
  `GET /api/nagem/landing-page/:n/:ntt/:ns`

- **URL OCC:**  
  `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/search?N=<n>&Ntt=<ntt>&Ns=<ns>&Nrpp=100&searchType=simple`

- **Métodos usados:**

  - `landingPageService.getId(n, ntt, ns)`
  - `productsService.getSKU(skuId)` (para detalhar produtos)

- **Entrada:**

  - `n` (param): Filtro de navegação (ex: categoria, pode ser '0' para todos)
  - `ntt` (param): Termo de busca (ex: "acessorios-p-telefonia")
  - `ns` (param): Ordenação
    - `menorPreco` → `sku.activePrice|0`
    - `maiorPreco` → `sku.activePrice|1`
    - `aZ` → `product.displayName|0`
    - `zA` → `product.displayName|1`
    - `maisRelevantes` → `product.displayName|1`

- **Saída:**

  ```json
  [
      {
        "name": "product.brand",
        "id": "brandId",
        "label": "Marca X",
        "count": 10
      }
    ],
    "categories": [
      {
        "name": "product.category",
        "id": "categoryId",
        "label": "Categoria Y",
        "count": 5
      }
    ],
    "searchData": [
      {
        "id": "skuId",
        "displayName": "Nome do Produto",
        "primaryLargeImageURL": "https://cdn...",
        "listPrice": 100,
        "salePrice": 90,
        "x_lancamento": true,
        "x_exclusivo": false,
        "x_exclusivo_app": false,
        "x_prevenda": false,
        "x_freteGratis": true,
        "x_descontoBoleto": 5,
        "x_descontoPix": 10,
        "x_parcelaMximaSemJuros": 10,
        "brand": "Marca X",
        "token": "..."
      }
    ],

  ```

---

## **ListCollections**

## GET COLLECTIONS

- **URL interna:**  
  `GET /api/nagem/collections`

- **URL OCC:**  
  `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccadmin/v1/collections?depth=2&orphaned=false&categoryIds=vitrini_1&showAccessControlInfo=false&showCatalogsCount=false`

- **Métodos usados:**

  - `listCollections.getAll()`

- **Entrada:**

  - Nenhuma ou `accessToken` (header)

- **Saída:**

  ```json
  [
    {
      "repositoryId": "skuId",
      "displayName": "Nome do Produto",
      "primaryFullImageURL": "https://cdn...",
      "listPrice": 100,
      "salePrice": 90
    }
  ]
  ```

---

**siteSettings**:

---

## GET SITE SETTINGS

- **URL interna:**  
  `GET /api/nagem/site`

- **URL OCC:**  
  `GET https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccadmin/v1/sitesettings`

- **Métodos usados:**

  - `listSiteSettings.getAll()`

- **Entrada:**

  - Nenhuma ou `accessToken` (header)

- **Saída:**
  ```json
  [
    {
      "id": "settingId",
      "name": "Nome da Configuração",
      "sub": [],
      "image": "https://cdn...",
      "skus": [],
      "order": 1
    }
  ]
  ```

---

**login**:

---

## POST LOGIN

- **URL interna:**  
  `POST /api/nagem/login`

- **URL OCC:**  
  `POST https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccadmin/v1/login`

- **Métodos usados:**

  - `login.getLogin()`

- **Entrada:**

  - Nenhuma (login técnico, não exige body ou parâmetros do usuário)

- **Saída:**
  ```json
  {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "token_type": "bearer",
    "expires_in": 3600,
    "scope": "read write"
    // ...outros campos retornados pelo OCC
  }
  ```

---

## Métodos do OrderService

---

### 1. Criar Pedido

- **URL interna:**  
  `POST /api/nagem/order/create`
- **URL OCC:**  
  `POST https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders`
- **Método:** `createOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

        ```json
        {
        "isAnonymousCheckout":true,
        "appliedPromotions":[
            "explicitItemFreeDiscount"
        ],
        "shippingMethod":{
            "value":"ground"
        },
        "payments": [
          {
              "customPaymentProperties": {},
        	  "customProperties": {
        		"tipoPagamento": "17",
        	  	"valorPedidoDesconto": "251.28"
        	  },
              "uiIntervention": null,
              "paymentMethod": "invoice",
              "billingAddress": {
                  "lastName": "Apartamento",
                  "country": "BR",
                  "address3": null,
                  "address2": null,
                  "city": "Rio Claro",
                  "prefix": null,
                  "address1": "Rua 10 A",
                  "postalCode": "13506666",
                  "companyName": "Casa",
                  "jobTitle": null,
                  "county": null,
                  "suffix": null,
                  "firstName": "Joao",
                  "phoneNumber": "",
                  "faxNumber": null,
                  "alias": null,
                  "middleName": null,
                  "state": "SP",
                  "email": null
              },
              "currencyCode": "BRL"
          }
        ],
        "shoppingCart":{
            "coupons":[],
            "items":[
                    {
                        "primaryThumbImageURL": "/ccstore/v1/images/?source=/file/v6210193171080212472/products/333883.333883.jpg&height=100&width=100",
                        "rawTotalPrice": 69.9,
                        "displayName": "Game The Sims 3 Ilha Paradisíaca Ed. Limitada PC",
                        "shippingSurchargeValue": 0,
                        "discountAmount": 0,
                        "description": "Game The Sims 3 Ilha Paradisíaca Ed. Limitada PC",
                        "price": 69.9,
                        "primaryImageAltText": "Game The Sims 3 Ilha Paradisíaca Ed. Limitada PC",
                        "id": "ci17000021",
                        "unitPrice": 69.9,
                        "primaryImageTitle": "Game The Sims 3 Ilha Paradisíaca Ed. Limitada PC",
                        "amount": 69.9,
                        "quantity": 1,
                        "productId": "333883",
                        "salePrice": 0,
                        "catRefId": "333883",
                        "siteId": "siteUS",
                        "shopperInput": {},
                        "asset": false,
                        "listPrice": 69.9
                    }
                ],
            "orderTotal":255.1
        },
        "placeAsyncOrder":false,
        "shippingAddress":{
        "lastName": "Apartamento",
        "country": "BR",
        "address3": null,
        "address2": null,
        "city": "Rio Claro",
        "prefix": null,
        "address1": "Rua 10 A",
        "postalCode": "13506666",
        "companyName": "Casa",
        "jobTitle": null,
        "county": null,
        "suffix": null,
        "firstName": "Joao",
        "phoneNumber": "",
        "faxNumber": null,
        "alias": null,
        "middleName": null,
        "state": "SP",
        "email": "jb.spitaletti@gmail.com"

    },
    "billingAddress": {
    "lastName": "Apartamento",
    "country": "BR",
    "address3": null,
    "address2": null,
    "city": "Rio Claro",
    "prefix": null,
    "address1": "Rua 10 A",
    "postalCode": "13506666",
    "companyName": "Casa",
    "jobTitle": null,
    "county": null,
    "suffix": null,
    "firstName": "Joao",
    "phoneNumber": "",
    "faxNumber": null,
    "alias": null,
    "middleName": null,
    "state": "SP",
    "email": null
    }
    }

    ```

          </details>
    ```

- **Saída:**
    <details><summary>Exemplo</summary>

  ```json
  {
    "shippingGroups": [
      {
        "priceInfo": {
          "amount": 172.9,
          "total": 172.9,
          "lkpValExcludingFreeShip": null,
          "shipping": 0,
          "shippingSurchargeValue": 0,
          "tax": 0,
          "subTotal": 172.9,
          "currencyCode": "BRL",
          "totalWithoutTax": 172.9
        },
        "discountInfo": {
          "orderDiscount": 0,
          "discountDescList": [],
          "shippingDiscount": 0
        },
        "locationId": null,
        "shippingMethod": {
          "secondaryCurrencyTaxAmount": 0,
          "shippingTax": 0,
          "cost": 0,
          "taxIncluded": true,
          "externalId": null,
          "taxCode": "",
          "value": "hardgoodShippingGroup",
          "shippingMethodDescription": "hardgoodShippingGroup"
        },
        "shippingGroupId": "sg713173",
        "shippingAddress": {
          "lastName": "Santos",
          "country": "BR",
          "address3": "CASA",
          "address2": "45",
          "city": "Jaboatão dos Guararapes",
          "prefix": null,
          "address1": "Rua São Pedro",
          "postalCode": "54430420",
          "companyName": "CASA",
          "jobTitle": "CASA",
          "county": "Candeias",
          "suffix": null,
          "firstName": "Danilo",
          "phoneNumber": null,
          "faxNumber": null,
          "alias": "Address12",
          "middleName": null,
          "state": "PE",
          "email": "danilo.santos@nagem.com.br"
        },
        "type": "hardgoodShippingGroup",
        "items": [
          {
            "rawTotalPrice": 172.9,
            "returnedQuantity": 0,
            "dynamicProperties": [],
            "shippingSurchargeValue": 0,
            "availabilityDate": null,
            "externalData": [],
            "discountAmount": 0,
            "preOrderQuantity": 0,
            "childItems": [],
            "configuratorId": null,
            "commerceItemId": "ci78002615",
            "price": 172.9,
            "onSale": false,
            "stateDetailsAsUser": "The item has been initialized within the shipping group",
            "commerceId": "ci78002615",
            "unitPrice": 172.9,
            "amount": 172.9,
            "quantity": 1,
            "pointOfNoRevision": false,
            "relationshipType": "SHIPPINGQUANTITYREMAINING",
            "productId": "612952",
            "salePrice": 0,
            "detailedItemPriceInfo": [
              {
                "discounted": false,
                "secondaryCurrencyTaxAmount": 0,
                "amount": 172.9,
                "quantity": 1,
                "configurationDiscountShare": 0,
                "tax": 0,
                "orderDiscountShare": 0,
                "detailedUnitPrice": 172.9,
                "currencyCode": "BRL"
              }
            ],
            "catRefId": "612952",
            "discountInfo": [],
            "siteId": "siteUS",
            "shopperInput": {},
            "asset": false,
            "backOrderQuantity": 0,
            "listPrice": 172.9,
            "status": "INITIAL"
          }
        ]
      }
    ],
    "orderId": "o713138",
    "creationSiteId": "siteUS",
    "lastModifiedDate": "2025-05-14T20:50:23.265Z",
    "dynamicProperties": [
      {
        "value": null,
        "id": "x_itemsInstallments2",
        "label": "Parcelamento do segundo cartão por item"
      },
      {
        "value": null,
        "id": "x_orderInstallments2",
        "label": "Parcelamento do segundo cartão do pedido"
      },
      {
        "value": null,
        "id": "x_bilhetes",
        "label": "Link's para Bilhetes de garantia"
      },
      {
        "value": null,
        "id": "x_orderInstallments",
        "label": "Parcelamento do pedido"
      },
      {
        "value": null,
        "id": "x_itemsInstallments",
        "label": "Parcelamento por item"
      },
      {
        "value": null,
        "id": "x_valorPedido",
        "label": "Valor Pedido"
      },
      {
        "value": null,
        "id": "x_paymentDetails",
        "label": "Informações adicionais sobre os métodos de pagamento"
      },
      {
        "value": null,
        "id": "x_readyForPickUpAt",
        "label": "Pronto para retirar em loja"
      },
      {
        "value": null,
        "id": "x_pedidonagem",
        "label": "Pedido Nagem"
      },
      {
        "value": null,
        "id": "x_prazoEntrega",
        "label": "Prazo Entrega"
      },
      {
        "value": null,
        "id": "x_sode",
        "label": "Informa se o método de entrega é do tipo SODE - (1 ou 0)"
      },
      {
        "value": null,
        "id": "x_codigoRastreio",
        "label": "Código de rastreio do pedido"
      },
      {
        "value": null,
        "id": "x_infoFrete",
        "label": "Informação de Frete"
      },
      {
        "value": null,
        "id": "x_origemPedido",
        "label": "Nome Vendedor"
      },
      {
        "value": "null",
        "id": "x_urlRastreioTransportadora",
        "label": "URL de Rastrreio da Transportadora"
      },
      {
        "value": "null",
        "id": "x_autoTracking",
        "label": "Status de entrega Carro Nagem"
      },
      {
        "value": null,
        "id": "x_PossuiKit",
        "label": "Informa se o pedido possui kit (bundle)"
      },
      {
        "value": null,
        "id": "x_exclusivePriceInfos",
        "label": "Informações sobre o preço exclusivo (quando se aplica)"
      },
      {
        "value": null,
        "id": "x_termosAceite",
        "label": "Link's para termos de aceite de garantia"
      },
      {
        "value": null,
        "id": "x_pedidoEntregueDevolvido",
        "label": "Data de entrega ou devolução"
      },
      {
        "value": null,
        "id": "x_urbanDeliveryHours",
        "label": "Entrega em horas"
      },
      {
        "value": null,
        "id": "x_faturamento",
        "label": "Data de Faturamento"
      },
      {
        "value": null,
        "id": "x_linkPDF",
        "label": "Link para PDF da Nota Fiscal"
      },
      {
        "value": null,
        "id": "x_pickUpPersonDetails",
        "label": "Informações de quem vai retirar em loja"
      },
      {
        "value": null,
        "id": "x_autorizacao",
        "label": "Data de autorização do Pedido"
      },
      {
        "value": null,
        "id": "x_cancelamento",
        "label": "Data e hora cancelamento"
      },
      {
        "value": null,
        "id": "x_status",
        "label": "Status do Pedido"
      },
      {
        "value": null,
        "id": "x_linkNotaFiscal",
        "label": "Link para Nota Fiscal"
      },
      {
        "value": null,
        "id": "x_chegouCliente",
        "label": "Data de chegada no cliente"
      },
      {
        "value": null,
        "id": "x_saiuEntrega",
        "label": "Data de saida para entrega"
      },
      {
        "value": null,
        "id": "x_preparandoEntrega",
        "label": "Data de preparação para entrega"
      }
    ],
    "allowAlternateCurrency": false,
    "payments": [],
    "description": "o713138",
    "priceListGroup": {
      "isTaxIncluded": false,
      "endDate": null,
      "displayName": "Lista de Preços Principal",
      "listPriceList": {
        "repositoryId": "mainPriceListGroup_listPrices"
      },
      "active": true,
      "isPointsBased": false,
      "locale": "pt_BR",
      "shippingSurchargePriceList": {
        "repositoryId": "mainPriceListGroup_shippingSurchargePrices"
      },
      "deleted": false,
      "taxCalculationType": "doNotCalculateTax",
      "repositoryId": "mainPriceListGroup",
      "salePriceList": {
        "repositoryId": "mainPriceListGroup_salePrices"
      },
      "currency": {
        "currencyType": null,
        "symbol": "R$",
        "deleted": false,
        "displayName": "Real Brasileiro",
        "repositoryId": "pt_BR",
        "fractionalDigits": 2,
        "currencyCode": "BRL",
        "numericCode": "986"
      },
      "id": "mainPriceListGroup",
      "includeAllProducts": false,
      "startDate": null
    },
    "creationDate": "2025-05-14T20:42:41.000Z",
    "orderAction": "order",
    "priceInfo": {
      "amount": 172.9,
      "total": 172.9,
      "shipping": 0,
      "shippingSurchargeValue": 0,
      "tax": 0,
      "subTotal": 172.9,
      "currencyCode": "BRL",
      "totalWithoutTax": 172.9
    },
    "sharedWithOrganization": false,
    "discountInfo": {
      "unclaimedCouponMultiPromotions": {},
      "orderCouponsMap": {},
      "orderDiscount": 0,
      "shippingDiscount": 0,
      "orderImplicitDiscountList": [],
      "unclaimedCouponsMap": {},
      "claimedCouponMultiPromotions": {}
    },
    "shoppingCart": {
      "items": [
        {
          "primaryThumbImageURL": "/ccstore/v1/images/?source=/file/v6422799621758069978/products/612952.612952.jpg&height=100&width=100",
          "rawTotalPrice": 172.9,
          "displayName": "Agenda Planner Caderno Inteligente Grey Glam Média + Caderno Inteligente Arco-Íris Pastel Inteligine",
          "dynamicProperties": [],
          "shippingSurchargeValue": 0,
          "discountAmount": 0,
          "externalData": [],
          "description": "Agenda Planner Caderno Inteligente Grey Glam Média + Caderno Inteligente Arco-Íris Pastel Inteligine",
          "isItemValid": true,
          "childItems": [],
          "configuratorId": null,
          "itemDiscountInfos": [],
          "commerceItemId": "ci78002615",
          "price": 172.9,
          "variant": [],
          "primaryImageAltText": "Agenda Planner Caderno Inteligente Grey Glam Média + Caderno Inteligente Arco-Íris Pastel Inteligine",
          "onSale": false,
          "id": "ci78002615",
          "state": "Adicionado ao pedido",
          "stateKey": "INITIAL",
          "unitPrice": 172.9,
          "primaryImageTitle": "Agenda Planner Caderno Inteligente Grey Glam Média + Caderno Inteligente Arco-Íris Pastel Inteligine",
          "childSKUs": [
            {
              "primaryThumbImageURL": null
            }
          ],
          "amount": 172.9,
          "quantity": 1,
          "productId": "612952",
          "pointOfNoRevision": false,
          "salePrice": 0,
          "orderDiscountInfos": [],
          "detailedItemPriceInfo": [
            {
              "discounted": false,
              "secondaryCurrencyTaxAmount": 0,
              "amount": 172.9,
              "quantity": 1,
              "configurationDiscountShare": 0,
              "tax": 0,
              "orderDiscountShare": 0,
              "detailedUnitPrice": 172.9,
              "currencyCode": "BRL"
            }
          ],
          "giftWithPurchaseCommerceItemMarkers": [],
          "originalCommerceItemId": null,
          "taxCode": null,
          "catRefId": "612952",
          "skuProperties": [
            {
              "name": "listingSKUId",
              "id": "listingSKUId",
              "value": null,
              "propertyType": "sku-base"
            },
            {
              "name": "Não Retornável",
              "id": "nonreturnable",
              "value": false,
              "propertyType": "sku-base"
            },
            {
              "name": "Nome",
              "id": "displayName",
              "value": "Agenda Planner Caderno Inteligente Grey Glam Média + Caderno Inteligente Arco-Íris Pastel Inteligine",
              "propertyType": "sku-base"
            },
            {
              "name": "Ativo",
              "id": "active",
              "value": true,
              "propertyType": "sku-base"
            },
            {
              "name": "ID",
              "id": "id",
              "value": "612952",
              "propertyType": "sku-base"
            },
            {
              "name": "Descontável",
              "id": "discountable",
              "value": true,
              "propertyType": "sku-base"
            }
          ],
          "route": "/agenda-planner-caderno-inteligente-grey-glam-m%C3%A9dia-caderno-inteligente-arco-%C3%ADris-pastel-inteligine/product/612952",
          "discountInfo": [],
          "siteId": "siteUS",
          "shopperInput": {},
          "asset": false,
          "listPrice": 172.9
        }
      ],
      "numberOfItems": 1
    },
    "additionalEmails": [],
    "giftWithPurchaseInfo": [],
    "lastModifierId": "53832338",
    "siteId": "siteUS",
    "links": [
      {
        "rel": "self",
        "href": "https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current?exclude=shippingMethod"
      }
    ],
    "markers": [],
    "giftWithPurchaseOrderMarkers": [],
    "productsStock": {
      "612952": 7
    }
  }
  ```

    </details>

---

### 2. Status do Pedido

- **URL interna:**  
  `GET /api/nagem/order/:orderId`
- **URL OCC:**  
  `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/:orderId`
- **Método:** `orderStatus(orderId, accessToken)`
- **Entrada:**
  - `accessToken` (header)
  - `orderId` (param)
- **Saída:**
   <details><summary>Exemplo</summary>
  o objeto de saida é igual o de criar o pedido, mas sem o campo `shippingGroups` e com o campo `id` no lugar de `orderId`.

  ```json
  { "id": "orderId", "creationSiteId": "siteUS", "state": "SUBMITTED", ... }
  ```

   </details>

---

### 3. Aplicar Cupom

- **URL interna:**  
  `PATCH /api/nagem/order/current/coupon`
- **URL OCC:**  
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current`
- **Método:** `patchCoupon(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    { "coupons": ["VALE10"] }
    ```

    </details>

- **Saída:**

  ```json

  ```

---

### 4. Listar Pedidos (OCC)

- **URL interna:**  
  `GET /api/nagem/order/list`
- **URL OCC:**  
  `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders`
- **Método:** `orderList(token, sort, filter, filterDate)`
- **Entrada:**
  - `accessToken` (header)
  - `sort`, `filter`, `filterDate` (query)
- **Saída:**
    <details><summary>Exemplo</summary>

  ```json
  [
    {
      "pedidoId": "o722432",
      "pedidoNr": "722432",
      "pagamento": {
        "vlrPedido": 27.6,
        "vlrFrete": 0
      },
      "status": {
        "state": "SUBMITTED",
        "creationDate": "2025-04-29T23:37:28.000Z",
        "submittedDate": "2025-04-29T23:37:27.000Z",
        "shipOnDate": null,
        "actualShipDate": null,
        "x_cancelamento": null,
        "x_valorPedido": "41.46",
        "x_pedidonagem": "97683923",
        "x_prazoEntrega": null,
        "x_urlRastreioTransportadora": "null",
        "x_autoTracking": "null",
        "x_pedidoEntregueDevolvido": null,
        "x_faturamento": null,
        "x_autorizacao": null,
        "x_status": "Pendente",
        "x_chegouCliente": null,
        "x_saiuEntrega": null,
        "x_preparandoEntrega": null
      },
      "x_orderInstallments": {
        "id": "x_orderInstallments",
        "value": "{\"portion\":1,\"price\":41.46,\"total\":41.46,\"description\":\"\",\"totalInterestOrDiscount\":-1.34}",
        "label": "Parcelamento do pedido"
      },
      "x_itemsInstallments": {
        "id": "x_itemsInstallments",
        "value": "[{\"sku\":\"408824\",\"description\":\"\",\"price\":25.46,\"portion\":1,\"totalInterestOrDiscount\":-1.34}]",
        "label": "Parcelamento por item"
      },
      "x_origemPedido": {
        "id": "x_origemPedido",
        "value": "B2C_APP",
        "label": "Nome Vendedor"
      }
    }
    // ... outros pedidos
  ]
  ```

    </details>

---

### 5. Listar Pedidos (LEGACY)

- **URL interna:**  
  `GET api/nagem/order_legacy/:userId`
- **URL nagem:**  
  `www.nagem.com.br/occ/cloud/listOrdersFromLegacy`
- **URL OCC:**  
  `Serviço magem`
- **Método:** `orderLegacyList(cpf)`
- **Entrada:**
  - `cpf` (param)
- **Saída:**
  ```json
  { "success": true, "data": [ ... ] }
  ```

---

### 6. Status Pedido (LEGACY)

- **URL interna:**  
  `GET /api/nagem/order/legacy/status/:orderId`
- **URL OCC:**  
  `www.nagem.com.br/occ/cloud/detailOrderFromLegacy`
- **URL OCC:**  
  `Serviço magem`
- **Método:** `orderLegacyStatus(orderId)`
- **Entrada:**
  - `orderId` (param)
- **Saída:**
  ```json
  { "success": true, "data": { ... } }
  ```

---

### 7. Adicionar Item ao Pedido Atual

- **URL interna:**  
  `POST /api/nagem/order/current/itens/add`
- **URL OCC:**  
  `POST https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/items/add`
- **Método:** `addItemCurrentOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    {
      "items": [
        {
          "catRefId": "408824",
          "childItems": [],
          "productId": "408824",
          "quantity": 1
        }
      ]
    }
    ```

    </details>

- **Saída:**
   <details><summary>Exemplo de payload</summary>

  ```json
  [
    {
      "primaryThumbImageURL": "/ccstore/v1/images/?source=/file/v3078516058957748031/products/408824.408824.jpg&height=100&width=100",
      "rawTotalPrice": 29.9,
      "displayName": "Papel Chamex A4 75g/m² 210mm x 297mm Office Branco 500 Folhas",
      "dynamicProperties": [],
      "shippingSurchargeValue": 0,
      "discountAmount": 0,
      "externalData": [],
      "childItems": [],
      "itemDiscountInfos": [],
      "commerceItemId": "ci77002827",
      "price": 27.6,
      "variant": [],
      "primaryImageAltText": "Papel Chamex A4 75g/m² 210mm x 297mm Office Branco 500 Folhas",
      "onSale": true,
      "id": "ci77002827",
      "state": "Adicionado ao pedido",
      "stateKey": "INITIAL",
      "unitPrice": 27.6,
      "primaryImageTitle": "Papel Chamex A4 75g/m² 210mm x 297mm Office Branco 500 Folhas",
      "childSKUs": [
        {
          "primaryThumbImageURL": null
        }
      ],
      "amount": 27.6,
      "quantity": 1,
      "productId": "408824",
      "pointOfNoRevision": false,
      "salePrice": 27.6,
      "orderDiscountInfos": [],
      "detailedItemPriceInfo": [
        {
          "discounted": false,
          "secondaryCurrencyTaxAmount": 0,
          "amount": 27.6,
          "quantity": 1,
          "configurationDiscountShare": 0,
          "tax": 0,
          "orderDiscountShare": 0,
          "detailedUnitPrice": 27.6,
          "currencyCode": "BRL"
        }
      ],
      "giftWithPurchaseCommerceItemMarkers": [],
      "catRefId": "408824",
      "skuProperties": [
        {
          "name": "listingSKUId",
          "id": "listingSKUId",
          "value": null,
          "propertyType": "sku-base"
        },
        {
          "name": "Não Retornável",
          "id": "nonreturnable",
          "value": false,
          "propertyType": "sku-base"
        },
        {
          "name": "Nome",
          "id": "displayName",
          "value": "Papel Chamex A4 75g/m² 210mm x 297mm Office Branco 500 Folhas",
          "propertyType": "sku-base"
        },
        {
          "name": "Ativo",
          "id": "active",
          "value": true,
          "propertyType": "sku-base"
        },
        {
          "name": "ID",
          "id": "id",
          "value": "408824",
          "propertyType": "sku-base"
        },
        {
          "name": "Descontável",
          "id": "discountable",
          "value": true,
          "propertyType": "sku-base"
        }
      ],
      "route": "/papel-chamex-a4-75g-m-210mm-x-297mm-office-branco-500-folhas/product/408824",
      "discountInfo": [],
      "siteId": "siteUS",
      "shopperInput": {},
      "asset": false,
      "listPrice": 29.9
    }
  ]
  ```

  </details>

---

### 8. Atualizar Item do Pedido Atual

- **URL interna:**  
  `PATCH /api/nagem/order/current/itens/update/:itemId`
- **URL OCC:**  
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/items/:itemId`
- **Método:** `updateItemCurrentOrder(itemId, data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - `itemId` (param)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    { "quantity": 2 }
    ```

    </details>

- **Saída:**
- mesmo exemplo de saída do item adicionado.

---

### 9. Remover Item do Pedido Atual

- **URL interna:**  
  `DELETE /api/nagem/order/current/itens/delete/:itemId`
- **URL OCC:**  
  `DELETE https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/items/:itemId`
- **Método:** `deleteItemCurrentOrder(itemId, shippingGroupId, accessToken)`
- **Entrada:**
  - `accessToken` (header)
  - `itemId` (param)
- **Saída:**
  - retorna mesma saída do item adicionado, mas sem o item removido.

---

### 10. Obter Pedido Atual

- **URL interna:**  
  `GET /api/nagem/order/current`
- **URL OCC:**  
  `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current`
- **Método:** `getCurrentOrder(token)`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**

  - mesmo payload de criação de pedido
  <details><summary>Exemplo</summary>

  ```json
  {
    "id": "orderId",
    "creationSiteId": "siteUS",
    "state": "SUBMITTED",
    ...
  }
  ```

  </details>

---

<!-- ### 11. Adicionar Grupo de Entrega

- **URL interna:**
  `POST /api/nagem/order/current/shipping_groups/add`
- **URL OCC:**
  `POST /ccstore/v1/orders/current/shippingGroups/add`
- **Método:** `shippingGroupsCurrentOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    { "shippingGroups": [ ... ] }
    ```

    </details>

- **Saída:**
  ```json
  { "success": true, ... }
  ```

--- -->

### 12. Adicionar Endereço ao Grupo de Entrega

- **URL interna:**  
  `PATCH /api/nagem/order/current/shipping_groups/:shippingId`
- **URL OCC:**  
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/shippingGroups/:shippingId`
- **Método:** `addAddressCurrentOrder(data, accessToken, shippingId)`
- **Entrada:**

  - `accessToken` (header)
  - `shippingId` (param)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    {
      "shippingAddress": {
        "addressType": "Address12",
        "country": "BR",
        "lastName": "DEFECT",
        "types": [],
        "address3": "Loja",
        "city": "Recife",
        "address2": "2294",
        "prefix": "",
        "address1": "Estrada dos Remédios",
        "postalCode": "50750360",
        "jobTitle": null,
        "companyName": "Casa",
        "regionName": "",
        "county": "Afogados",
        "suffix": "",
        "state": "PE",
        "firstName": "ZERO",
        "externalAddressId": null,
        "phoneNumber": "",
        "repositoryId": "98018522",
        "faxNumber": "",
        "middleName": "",
        "countryName": "Brasil",
        "email": "email@nagem.com.br",
        "alias": "Address12"
      }
    }
    ```

    </details>

- **Saída:**

  - mesmo payload de criação de pedido, mas com o grupo de entrega atualizado.
  <details><summary>Exemplo</summary>

  ```json
  {
    "id": "orderId",
    "creationSiteId": "siteUS",
    "state": "SUBMITTED",
    ...
  }
  ```

  </details>

---

### 13. Adicionar Método de Entrega

- **URL interna:**  
  `PATCH /api/nagem/order/current/shipping_method`
- **URL OCC:**  
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/shippingGroups`
- **Método:** `addShippingCurrentOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
      <details><summary>Exemplo de payload</summary>

    ```json
    {
      "items": [
        {
          "shippingGroupId": "sg712077",
          "shippingMethod": {
            "value": "000453 - Receba ate"
          }
        }
      ]
    }
    ```

      </details>

- **Saída:**

  - mesmo payload de criação de pedido, mas com o método de entrega atualizado `shippingMethod`.
  <details><summary>Exemplo</summary>

  ```json
  {
    "orderId": "orderId",
    "creationSiteId": "siteUS",
    "state": "SUBMITTED",
    ...
  }
  ```

  </details>

---

### 14. Adicionar Pagamento

- **URL interna:**  
  `POST /api/nagem/order/current/payments/add`
- **URL OCC:**  
  `POST https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/payments/add`
- **Método:** `addPaymentCurrentOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    {
      "items": [
        {
          "type": "invoice",
          "billingAddress": {
            "firstName": "Danilo",
            "lastName": "Teste",
            "country": "BR",
            "postalCode": "50750360",
            "state": "PE",
            "address1": "Estrada dos Remédios",
            "address2": "2294",
            "address3": "Loja",
            "city": "Recife",
            "phoneNumber": "",
            "county": "Afogados",
            "suffix": "",
            "companyName": "Teste Danilo"
          },
          "seqNum": 0,
          "customProperties": {
            "tipoPagamento": 18,
            "valorPedidoDesconto": 41.46
          }
        }
      ]
    }
    ```

    </details>

- **Saída:**

  - mesmo payload de criação de pedido, mas com o pagamento atualizado.
  <details><summary>Exemplo</summary>

  ```json
  {
    "id": "orderId",
    "creationSiteId": "siteUS",
    "state": "SUBMITTED",
    ...
  }
  ```

  </details>

---

### 15. Atualizar Pagamento

- **URL interna:**
  `PATCH /api/nagem/order/current/payments/update`
- **URL OCC:**
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/payments`
- **Método:** `updatePaymentCurrentOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**

    - mesmo payload de add payment de pedido, mas com o campo `payments` atualizado.
    <details><summary>Exemplo de payload</summary>

    ```json
    { "payments": [ ... ] }
    ```

    </details>

- **Saída:**
- mesmo payload de criação de pedido, mas com o pagamento atualizado.
  ```json
  { "success": true, ... }
  ```

---

### 16. Remover Pagamento

- **URL interna:**  
  `DELETE /api/nagem/order/current/payments/:paymentId`
- **URL OCC:**  
  `DELETE https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/payments/:paymentId`
- **Método:** `removePaymentCurrentOrder(data, accessToken, paymentId)`
- **Entrada:**
  - `accessToken` (header)
  - `paymentId` (param)
- **Saída:**

  - mesmo payload de criação de pedido, mas com o pagamento removido.
  <details><summary>Exemplo</summary>

  ```json
  {
    "id": "orderId",
    "creationSiteId": "siteUS",
    "state": "SUBMITTED",
    ...
  }
  ```

  </details>

---

### 17. Fechar Pedido Atual

- **URL interna:**  
  `PATCH /api/nagem/order/current/close`
- **URL OCC:**  
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current`
- **Método:** `closeCurrentOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Payload igual ao de <b>Adicionar Item ao Pedido Atual</b></summary>

    ```json
    {
      "currentOrderId": "o300237",
      "op": "update",
      "x_itemsInstallments": "[{\"sku\":\"463159\",\"description\":\"sem juros\",\"price\":119.9,\"portion\":1,\"totalInterestOrDiscount\":0}]",
      "x_orderInstallments": "{\"portion\":7,\"price\":17.13,\"total\":119.9,\"description\":\"sem juros\",\"totalInterestOrDiscount\":0}",
      "x_itemsInstallments2": null,
      "x_orderInstallments2": null,
      "x_valorPedido": "119.90",
      "x_origemPedido": "B2C_APP",
      "x_paymentDetails": "{\"flags\":[\"Visa\"],\"cardNumbers\":[\"1111\"]}"
    }
    ```

    </details>

- **Saída:**
- mesmo payload de criação de pedido, mas com essas informações atualizadas.

---

### 18. Enviar Pedido Atual

- **URL interna:**  
  `POST /api/nagem/order/current/submit`
- **URL OCC:**  
  `POST https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/submit`
- **Método:** `submitCurrentOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Payload igual ao de <b>Criar Pedido</b></summary>

    ```json
    {
      "payments": [
        {
          "type": "invoice",
          "paymentGroupId": "pg320219"
        }
      ]
    }
    ```

    </details>

- **Saída:**
  <details><summary>Exemplo de resposta</summary>
  - mesmo payload de criação de pedido, mas com todos os campos preenchidos e o estado atualizado para `SUBMITTED`.

  ```json
  { "id": "orderId", "state": "SUBMITTED", ... }
  ```

  </details>

---

### 19. Cancelar Pedido

- **URL interna:**  
  `POST /api/nagem/order/cancel`
- **URL OCC:**  
  `POST https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/cancel`
- **Método:** `cancelOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - método utilizado para cancelar pedidos através do status de pagamento `AUTHORIZE_FAILED`.
  - **Body:**
  <details><summary>Exemplo de payload</summary>

- **Saída:**
  ```json
   { "orderId": "orderId", "state": "CANCELED", ... }
  ```

---

### 20. Repetir Pedido

- **URL interna:**  
  `POST /api/nagem/order/retry`
- **URL OCC:**  
  `POST https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/copyOrder`
- **Método:** `retryOrder(data, accessToken)`
- **Entrada:**

  - `accessToken` (header)
  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    { "orderId": "orderId", "exclude": { ... }, "mergeShippingGroups": true }
    ```

    </details>

- **Saída:**
  ```json
  { "orderId": "orderId", "state": "submitted", ... }
  ```

---

### 21. Repetir Pedido (LEGACY)

- **URL interna:**  
  `PATCH /api/nagem/order/current/items`
- **URL OCC:**  
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/items`
- **Método:** `retryOrderLegacy(data, accessToken)`
- **Entrada:**
  - `accessToken` (header)
  - **Body:**
    <details><summary>Payload igual ao de <b>Adicionar Item ao Pedido Atual</b></summary></details>
- **Saída:**

  ```json
    { "orderId": "orderId", "state": "submitted", ... }

  ```

---

### 22. Confirmar Itens do Carrinho

- **URL interna:**  
  `PATCH /api/nagem/order/current/items/confirm`
- **URL OCC:**  
  `PATCH https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/items`
- **Método:** `checkoutItemsConfirm(data, accessToken)`
- **Entrada:**
  - `accessToken` (header)
  - **Body:**
    <details><summary>Payload igual ao de <b>Adicionar Item ao Pedido Atual</b></summary></details>
- **Saída:**
  - Payload igual ao de <b>Adicionar Item ao Pedido Atual</b>

---

### 23. Preço do Pedido Atual

- **URL interna:**  
  `POST /api/nagem/order/current/price`
- **URL OCC:**  
  `POST https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current/price`
- **Método:** `priceCurrentOrder(data, accessToken)`
- **Entrada:**
  - `accessToken` (header)
  - acredito ser a checkagem de preços do carrinho, mas não foi possível confirmar.
  - **Body:**
- **Saída:**
  ```json
  { "success": true, ... }
  ```

---

### 24. Métodos de Pagamento (Modal)

- Serviço nagem

- **URL interna:**  
  `POST /api/nagem/order/current/payment_methods`
- **URL OCC:**  
  `Serviço nagem`
- **Método:** `paymentMethodsCurrentOrder(data)`
- **Entrada:**

  - **Body:**
    <details><summary>Exemplo de payload</summary>

    ```json
    {
      "items": [
        {
          "sku": "408824",
          "productTypeId": "PT121",
          "brandId": "CHAMEX",
          "quantity": 1,
          "totalPrice": 27.6
        }
      ],
      "totalService": 0,
      "shipping": 0,
      "cardValue": 27.6
    }
    ```

    </details>

- **Saída:**
  ```json
  {
  	"items": [
  		{
  			"sku": "408824",
  			"paymentMethods": [
  				{
  					"code": 20,
  					"type": "R",
  					"description": "NAGEM",
  					"acquirer": "Cielo30",
  					"price": 27.6,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 27.6,
  							"total": 27.6,
  							"description": "sem juros",
  							"totalInterestOrDiscount": 0
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 2,
  					"type": "R",
  					"description": "MASTERCARD",
  					"acquirer": "Cielo30",
  					"price": 27.6,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 27.6,
  							"total": 27.6,
  							"description": "sem juros",
  							"totalInterestOrDiscount": 0
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 1,
  					"type": "R",
  					"description": "VISA",
  					"acquirer": "Cielo30",
  					"price": 27.6,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 27.6,
  							"total": 27.6,
  							"description": "sem juros",
  							"totalInterestOrDiscount": 0
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 5,
  					"type": "R",
  					"description": "AMERICAN EXPRESS",
  					"acquirer": "Cielo30",
  					"price": 27.6,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 27.6,
  							"total": 27.6,
  							"description": "sem juros",
  							"totalInterestOrDiscount": 0
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 7,
  					"type": "B",
  					"description": "Boleto Banco Bradesco",
  					"acquirer": "Bradesco2",
  					"price": 26.22,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 26.22,
  							"total": 26.22,
  							"description": "",
  							"totalInterestOrDiscount": -1.38
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 9,
  					"type": "R",
  					"description": "Elo",
  					"acquirer": "Cielo30",
  					"price": 27.6,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 27.6,
  							"total": 27.6,
  							"description": "sem juros",
  							"totalInterestOrDiscount": 0
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 8,
  					"type": "R",
  					"description": "HIPERCARD",
  					"acquirer": "Cielo30",
  					"price": 27.6,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 27.6,
  							"total": 27.6,
  							"description": "sem juros",
  							"totalInterestOrDiscount": 0
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 13,
  					"type": "R",
  					"description": "JCB",
  					"acquirer": "Cielo30",
  					"price": 27.6,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 27.6,
  							"total": 27.6,
  							"description": "sem juros",
  							"totalInterestOrDiscount": 0
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				},
  				{
  					"code": 18,
  					"type": "X",
  					"description": "PIX",
  					"acquirer": "Pix",
  					"price": 26.22,
  					"installment": "1",
  					"details": [
  						{
  							"portion": 1,
  							"price": 26.22,
  							"total": 26.22,
  							"description": "",
  							"totalInterestOrDiscount": -1.38
  						}
  					],
  					"orderPriority": null,
  					"paymentOneDotTwo": false
  				}
  			]
  		}
  	],
  	"payments": [
  		{
  			"code": 20,
  			"type": "R",
  			"description": "NAGEM",
  			"acquirer": "Cielo30",
  			"price": 27.6,
  			"installment": 1,
  			"maximumFreeInstallment": 1,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": null,
  			"details": [
  				{
  					"portion": 1,
  					"price": 27.6,
  					"total": 27.6,
  					"description": "sem juros",
  					"totalInterestOrDiscount": 0
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 2,
  			"type": "R",
  			"description": "MASTERCARD",
  			"acquirer": "Cielo30",
  			"price": 27.6,
  			"installment": 1,
  			"maximumFreeInstallment": 1,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": null,
  			"details": [
  				{
  					"portion": 1,
  					"price": 27.6,
  					"total": 27.6,
  					"description": "sem juros",
  					"totalInterestOrDiscount": 0
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 1,
  			"type": "R",
  			"description": "VISA",
  			"acquirer": "Cielo30",
  			"price": 27.6,
  			"installment": 1,
  			"maximumFreeInstallment": 1,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": null,
  			"details": [
  				{
  					"portion": 1,
  					"price": 27.6,
  					"total": 27.6,
  					"description": "sem juros",
  					"totalInterestOrDiscount": 0
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 5,
  			"type": "R",
  			"description": "AMERICAN EXPRESS",
  			"acquirer": "Cielo30",
  			"price": 27.6,
  			"installment": 1,
  			"maximumFreeInstallment": 1,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": null,
  			"details": [
  				{
  					"portion": 1,
  					"price": 27.6,
  					"total": 27.6,
  					"description": "sem juros",
  					"totalInterestOrDiscount": 0
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 7,
  			"type": "B",
  			"description": "Boleto Banco Bradesco",
  			"acquirer": "Bradesco2",
  			"price": 26.22,
  			"installment": 1,
  			"maximumFreeInstallment": null,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": 5,
  			"details": [
  				{
  					"portion": 1,
  					"price": 26.22,
  					"total": 26.22,
  					"description": "",
  					"totalInterestOrDiscount": -1.38
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 9,
  			"type": "R",
  			"description": "Elo",
  			"acquirer": "Cielo30",
  			"price": 27.6,
  			"installment": 1,
  			"maximumFreeInstallment": 1,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": null,
  			"details": [
  				{
  					"portion": 1,
  					"price": 27.6,
  					"total": 27.6,
  					"description": "sem juros",
  					"totalInterestOrDiscount": 0
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 8,
  			"type": "R",
  			"description": "HIPERCARD",
  			"acquirer": "Cielo30",
  			"price": 27.6,
  			"installment": 1,
  			"maximumFreeInstallment": 1,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": null,
  			"details": [
  				{
  					"portion": 1,
  					"price": 27.6,
  					"total": 27.6,
  					"description": "sem juros",
  					"totalInterestOrDiscount": 0
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 13,
  			"type": "R",
  			"description": "JCB",
  			"acquirer": "Cielo30",
  			"price": 27.6,
  			"installment": 1,
  			"maximumFreeInstallment": 1,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": null,
  			"details": [
  				{
  					"portion": 1,
  					"price": 27.6,
  					"total": 27.6,
  					"description": "sem juros",
  					"totalInterestOrDiscount": 0
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		},
  		{
  			"code": 18,
  			"type": "X",
  			"description": "PIX",
  			"acquirer": "Pix",
  			"price": 26.22,
  			"installment": 1,
  			"maximumFreeInstallment": null,
  			"maximumInterestInstallment": null,
  			"percentageInterest": null,
  			"percentageDiscount": 5,
  			"details": [
  				{
  					"portion": 1,
  					"price": 26.22,
  					"total": 26.22,
  					"description": "",
  					"totalInterestOrDiscount": -1.38
  				}
  			],
  			"valorMinimoParcela": 15,
  			"orderPriority": null
  		}
  	],
  }
  ```

---

### 25. Métodos de Pagamento (Modal - PROD)

- Serviço nagem
- **URL interna:**  
  `POST /api/nagem/order/payment-methods/searchModal`
- **URL OCC:**  
  `Serviço nagem`
- **Método:** `searchModal(data, accessToken)`
- **Entrada:**
  - `accessToken` (header)
  - **Body:**
    <details><summary>Payload igual ao de <b>Métodos de Pagamento (Modal)</b></summary></details>
- **Saída:**
- mesmo payload de <b>Métodos de Pagamento (Modal)</b>

---

### 26. Remover Pedido Atual

- **URL interna:**  
  `DELETE /api/nagem/order/current`
- **URL OCC:**  
  `DELETE /ccstore/v1/orders/current`
- **Método:** `removeCurrentOrder(accessToken)`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  objeto vazio `{}`

---

### 27. Obter ShippingId (obter ID do Grupo de Entrega)

- **URL interna:**  
  `GET /api/nagem/order/current/shippingId`
- **URL OCC:**  
  `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current?fields=shippingGroups.shippingGroupId`
- **Método:** `getShippingId(token)`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  ```json
  {
    "shippingGroups": [
      {
        "shippingGroupId": "sg713275"
      }
    ],
    "links": [
      {
        "rel": "self",
        "href": "https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/orders/current?fields=shippingGroups.shippingGroupId"
      }
    ]
  }
  ```

---

### 28. Alterar Data de Criação do Pedido

- **URL interna:**  
  `PUT /api/nagem/order/:orderId/creationTime`
- **URL OCC:**  
  `PUT https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccadmin/v1/orders/:orderId`
- **Método:** `changeCreationTimeOrder(orderId, accessToken)`
- **Entrada:**
  - `accessToken` (header)
  - `orderId` (param)
- **Saída:**
- mesmo objeto de criação de pedido com a data de criação atualizada.
<details><summary>Exemplo</summary>

```json
{
  "id": "orderId",
  "creationSiteId": "siteUS",
  "state": "SUBMITTED",
  "creationTime": "2023-10-01T12:00:00Z",
  ...
}
```

  </details>

---

### 29. Obter Número Pedido ECM

- **Serviço nagem**
- **URL interna:**  
  `GET /api/nagem/order/get-numpedecm`
- **URL OCC:**  
  `GET /occ/cloud/ordersubmmit/get-numpedecm`
- **Método:** `getOrderId(token)`
- **Entrada:**
  - `accessToken` (header)
- **Saída:**
  - retorna uma string com o número (um número novo para o pedido) do pedido ECM.

---

# Documentação dos Métodos de Produtos (OCC)

---

## 1. Buscar Produtos (Pesquisa)

**Função:** `search`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/search_products`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/search`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - Query: `terms` (string), `page` (number)
- **Retorno esperado:**
  - Sucesso: Lista de produtos, marcas e categorias encontradas.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de entrada:**

```json
{
  "terms": "notebook",
  "page": 1
}
```

**Exemplo de saída:**

```json
{
 
  "brands": [
    {
      "name": "product.brand",
      "id": "brandId",
      "label": "Marca X",
      "count": 10
    }
  ],
  "categories": [
    {
      "name": "product.category",
      "id": "categoryId",
      "label": "Categoria Y",
      "count": 5
    }
  ],
  "searchData": [
    {
      "id": "sku123",
      "displayName": "Notebook X",
      "primaryLargeImageURL": "https://cdn...",
      "listPrice": 2999.99,
      "salePrice": 2799.99,
      "brand": "Marca X",
      "token": "..."
    }
  ]
}
```

---

## 2. Obter Produto por ID

**Função:** `getProduct`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/product/:productId`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products/{productId}`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.
- **Retorno esperado:**
  - Sucesso: Detalhes do produto.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
{
		"id": "408824",
		"displayName": "Papel Chamex A4 75g/m² 210mm x 297mm Office Branco 500 Folhas",
		"primaryLargeImageURL": "/ccstore/v1/images/?source=/file/v3078516058957748031/products/408824.408824.jpg&height=940&width=940",
		"orderLimit": null,
		"x_limitePorCpf": 0,
		"x_limitePorCarrinho": 0,
		"brand": "CHAMEX",
		"type": "PT121",
		"listPrice": 29.9,
		"salePrice": 27.6,
		"in_stock": true,
		"x_lancamento": null,
		"x_exclusivo": "0",
		"x_exclusivo_app": null,
		"x_prevenda": "0",
		"x_freteGratis": null,
		"x_descontoBoleto": 5,
		"x_descontoPix": 5,
		"x_parcelaMximaSemJuros": 10,
		"productImages": [
			"/ccstore/v1/images/?source=/file/v3078516058957748031/products/408824.408824.jpg&height=940&width=940",
			"/ccstore/v1/images/?source=/file/v6973017325186401926/products/408824.408824_1.jpg&height=940&width=940"
		],
		"quantity": 118250,
		"width": 30,
		"height": 5,
		"weight": 2280,
		"length": 21,
		"token": "...",
		"description": "Papel Chamex A4 75g/m² 210mm x 297mm Office Branco 500 Folhas",
		"longDescription": "<h2><strong><font color=\"red\">A4 75 500 FOLHAS</strong></font></h2>\r\n<div style= 'text-align:justify'>Chamex A4 75g/m² garante ótima performance em todo tipo de atividade, como criar, escrever, imprimir e reproduzir... </div>",
		"productSpecifications": [
			{
				"name": "Marca",
				"id": "brand",
				"value": "CHAMEX"
			}
		],
		"barcode": "7891173023001",
		"link": "https://p9351450c1prd-admin.occa.ocs.oraclecloud.com/ccstore/v1/products/408824?exclude=listPrices%2Cx_statusPromoRelampago%2Cx_groupId%2Cshippable%2Cx_codigoPrecificacao%2CprimaryImageAltText%2CparentCategories%2CdefaultProductListingSku%2Cassetable%2CunitOfMeasure%2CseoUrlSlugDerived%2Cactive%2CthumbImageURLs%2Cx_inicioPromo%2Croute%2CrelatedArticles%2CprimarySourceImageURL%2CsourceImageURLs%2Cx_tipoRegra%2CprimaryThumbImageURL%2CdirectCatalogs%2Cnonreturnable%2CprimaryFullImageURL%2CproductVariantOptions%2CsaleVolumePrices%2Cx_prevendaDe%2CnotForIndividualSale%2CderivedListPriceFrom%2CdefaultParentCategory%2ClistVolumePrice%2CexcludeFromSitemap%2ConlineOnly%2ClistVolumePrices%2CaddOnProducts%2CderivedSalePriceFrom%2Cx_fimPromo%2CprimaryMediumImageURL%2Cx_specialOfferProductId%2Cx_tipoPromo%2Cx_codigoServico%2CcreationDate%2CparentCategoryIdPath%2Cx_qtdMaxParcelasSemJuros%2CparentCategory%2CprimarySmallImageURL%2CavgCustRating%2Cx_fimPromo2%2CsalePrices%2CsmallImageURLs%2CderivedShippingSurchargeFrom%2Cx_preVenda2%2CshippingSurcharges%2CsaleVolumePrice%2CprimaryImageTitle%2Cx_brandId%2Cx_numeroDeDiasDaLimitaoPorCpf%2CrelatedMediaContent%2ClastModifiedDate%2CfullImageURLs%2CderivedDirectCatalogs%2Cx_prevendaAte%2Cx_exclusivo_do_site%2CvariantValuesOrder%2CrepositoryId%2CshippingSurcharge%2CproductImagesMetadata%2Cx_codigoItemServico%2Cconfigurable",
		"x_departamento": "Papéis p/Impressão",
		"kitBundle": [],
		"x_imageSrcNagemCampaign": null,
		"x_imageSrcNagemCapaign": null,
		"x_imageSrcManufacturerCampaign": null,
		"x_imageSrcManufacturerCapaign": null
	},
```

---

## 3. Obter Especificações de Produto

**Função:** `getProductSpecifications`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/product/specifications/:productId`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/productTypes/{typeId}`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.
- **Retorno esperado:**
  - Sucesso: Lista de especificações técnicas do produto.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
[
  {
    "name": "Marca",
    "id": "brand",
    "value": "CHAMEX"
  },
  {
    "name": "Tamanho (mm)",
    "id": "x_PT12102",
    "value": "210 x 297 mm"
  },
  {
    "name": "Formato",
    "id": "x_PT12101",
    "value": "A4"
  },
  {
    "name": "Tecnologia de Impressão",
    "id": "x_PT12106",
    "value": "Jato de Tinta/Laser"
  },
  {
    "name": "Cor",
    "id": "x_PT12105",
    "value": "Branco"
  },
  {
    "name": "Folhas por Pacote",
    "id": "x_PT12104",
    "value": "500"
  },
  {
    "name": "Gramatura (g/m²)",
    "id": "x_PT12103",
    "value": "75g/m²"
  }
]
```

---

## 4. Obter Garantias de Produto

**Função:** `getProductGuarantees`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/product/guarantees/:productId`

- **Método OCC:** *Não faz chamada direta ao OCC*
- **Métodos auxiliares usados:**
  - `productsService.getProduct`
  - `productsService.getProducts`
- **Descrição:**  
  Busca garantias disponíveis para um produto a partir dos dados do produto e consulta dos produtos de garantia.
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.
- **Retorno esperado:**
  - Sucesso: Lista de garantias disponíveis para o produto.
  - Erro: Objeto de erro retornado pelo OCC.

**Exemplo de saída:**

```json
[
  {
    "displayName": "+12 meses após garantia de fábrica",
    "listPrice": 243.76,
    "id": "G0000000481121215001750070"
  },
  {
    "displayName": "+24 meses após garantia de fábrica",
    "listPrice": 422.51,
    "id": "G0000000481122415001750070"
  }
]
```

---

## 5. Notificar Produto

**Função:** `postProductNotification`  
**Arquivo:** productsController.js  
**Rota interna:** `POST /api/nagem/addProductNotification`

- **Método OCC:** `POST`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/productNotify`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - Body:
    ```json
    {
      "email": "cliente@email.com",
      "product_id": "sku123",
      "site_id": "siteUS"
    }
    ```
- **Retorno esperado:**
  - Sucesso: Confirmação de notificação cadastrada.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
{
  "data": {
    "message": "Notificação cadastrada com sucesso"
  }
}
```

---

## 6. Buscar Produtos Relacionados

**Função:** `getRelatedProducts`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/product/related/:productId`

- **Método OCC:** *Não faz chamada direta ao OCC*
- **Métodos auxiliares usados:**
  - `productsService.getProduct`
  - `yourviewService.getProductsReviews`
- **Descrição:**  
  Retorna produtos relacionados a partir dos dados do produto e reviews agregadas.
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.
- **Retorno esperado:**
  - Sucesso: Lista de produtos relacionados.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json

  [
    {
         "id":"079774",
         "displayName":"Marca Texto Lumi Color 200-SL Amarelo 12 Unidades Pilot",
         "primaryLargeImageURL":"/ccstore/v1/images/?source=/file/v3559260943621925788/products/079774.079774.jpg&height=940&width=940",
         "listPrice":39.9,
         "salePrice":null,
         "x_lancamento":null,
         "x_prevenda":"0",
         "x_exclusivo":"0",
         "x_exclusivo_app":null,
         "x_freteGratis":null,
         "x_descontoBoleto":5,
         "x_descontoPix":5,
         "x_parcelaMximaSemJuros":10,
         "in_stock":true,
         "token":"...token...",
         "rating":5,
         "total_rating":1
      }
  ],

```

---

## 7. Buscar Produtos Similares

**Função:** `getSimilarProducts`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/product/similar/:productId`

- **Método OCC:** *Não faz chamada direta ao OCC*
- **Métodos auxiliares usados:**
  - `productsService.getProduct`
  - `yourviewService.getProductsReviews`
- **Descrição:**  
  Retorna produtos similares a partir dos dados do produto e reviews agregadas.
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.
- **Retorno esperado:**
  - Sucesso: Lista de produtos similares.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
[
    {
         "id":"079774",
         "displayName":"Marca Texto Lumi Color 200-SL Amarelo 12 Unidades Pilot",
         "primaryLargeImageURL":"/ccstore/v1/images/?source=/file/v3559260943621925788/products/079774.079774.jpg&height=940&width=940",
         "listPrice":39.9,
         "salePrice":null,
         "x_lancamento":null,
         "x_prevenda":"0",
         "x_exclusivo":"0",
         "x_exclusivo_app":null,
         "x_freteGratis":null,
         "x_descontoBoleto":5,
         "x_descontoPix":5,
         "x_parcelaMximaSemJuros":10,
         "in_stock":true,
         "token":"...token...",
         "rating":5,
         "total_rating":1
      }
  ],

```

---

## 8. Obter Estoque do Produto

**Função:** `getProductStock`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/product/stock/:productId`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/stockStatus?products={productId}&expandStockDetails=true`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.
- **Retorno esperado:**
  - Sucesso: Detalhes de estoque do produto.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
{
    "links": [
      {
        "rel": "self",
        "href": "https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/stockStatus?products=408824&expandStockDetails=true"
      }
    ],
    "autoWrap": true,
    "items": [
      {
        "408824": "IN_STOCK",
        "stockStatus": "IN_STOCK",
        "productSkuInventoryStatus": {
          "408824": 130336
        },
        "locationId": null,
        "productSkuInventoryDetails": [
          {
            "catalogId": "b2c",
            "productId": "408824",
            "preOrderableQuantity": 0,
            "locationId": null,
            "orderableQuantity": 130336,
            "stockStatus": "IN_STOCK",
            "availabilityDate": null,
            "backOrderableQuantity": 0,
            "catRefId": "408824",
            "inStockQuantity": 130336
          }
        ]
      }
    ]
  },
```

---

## 9. Obter Conteúdo de Categoria

**Função:** `getCategoryContent`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/category_content/:categoryId`

- **Método OCC:** *Não faz chamada direta ao OCC*
- **Métodos auxiliares usados:**
  - `productsService.getCollection`
- **Descrição:**  
  Retorna o conteúdo de uma categoria (banners, imagens, redirecionamentos, títulos).
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - `categoryId` (string): ID da categoria.
  - Query: `forceUpdate` (opcional)
- **Retorno esperado:**
  - Sucesso: Conteúdo da categoria (banners, imagens, redirecionamentos, títulos).
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
[
  {
    "type": "banner_principal",
    "images": [
      {
        "url": "v6655413096789184437/collections/Frame+1000003076.png",
        "link": "search|samsung",
        "size": null
      },
      {
        "url": "v3195075875057535621/collections/426483722_796878039145203_4904114791153551422_n.jpg",
        "link": "search|samsung",
        "size": null
      },
      {
        "url": "v6564596227921322234/collections/427666188_796877989145208_8796879101012935171_n.jpg",
        "link": "search|samsung",
        "size": null
      }
    ],
    "redirect": "/search/smartphones/_/N-1567410377+2380810213",
    "title": "Tudo em Smartphones"
  },
  {
    "type": "mini_banner",
    "images": [
      {
        "url": "v1078854707612112402/collections/Frame+1000003104.png",
        "link": "search|galaxy",
        "size": null
      }
    ],
    "redirect": "CAT026",
    "title": null
  }
]
```

---

## 10. Obter Categorias da Loja

**Função:** `getStoreCategories`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/categories`

- **Método OCC:** _Não faz chamada direta ao OCC_
- **Métodos auxiliares usados:**
  - `settingsService.settings('menuSettings')`
  - `productsService.getCategoryFullData('cat10001')`
- **Descrição:**  
  Monta a lista de categorias da loja a partir das configurações do menu e dos dados completos da categoria principal, filtrando e organizando conforme a whitelist definida nas configurações.
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:** Nenhum.
- **Retorno esperado:**
  - Sucesso: Lista de categorias e subcategorias.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
[
  {
    "id": "cat10001",
    "displayName": "Informática",
    "subcategories": [
      {
        "id": "Samsung",
        "type": "brand",
        "href": "https://beta.nagem.com.br/search/smartphones/_/N-1567410377+2380810213",
        "displayName": "Samsung",
        "redirect": "brand|1567410377+2380810213"
      }
    ],
    "bannerImage": "banner1.jpg"
  }
]
```

---

## 11. Obter Subcategorias da Loja

**Função:** `getStoreSubCategories`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/sub_categories/:categoryId`

- **Método OCC:** *Não faz chamada direta ao OCC*
- **Métodos auxiliares usados:**
  - `settingsService.settings('navBarSettings')`
  - `productsService.getSearch('N={categoryId}')`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - `categoryId` (string): ID da categoria.
- **Retorno esperado:**
  - Sucesso: Lista de subcategorias.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
[
  {
    "id": "cat20001",
    "displayName": "Notebooks",
    "searchId": "cat20001"
  }
]
```

---

## 12. Obter Categorias do Menu

**Função:** `getMenuCategories`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/menu_categories`

- **Método OCC:** *Não faz chamada direta ao OCC*
- **Métodos auxiliares usados:**
  - `settingsService.settings('menuSettings')`
  - `productsService.getCategoriesNames`
- **Descrição:**  
  Monta a lista de categorias do menu a partir das configurações e busca os nomes e imagens das categorias quando necessário.
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:** Nenhum.
- **Retorno esperado:**
  - Sucesso: Lista de categorias do menu.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
[
  {
    "id": "CAT026",
    "displayName": "Smartphones",
    "subcategories": [
      {
        "id": "Samsung",
        "type": "brand",
        "href": "https://beta.nagem.com.br/search/smartphones/_/N-1567410377+2380810213",
        "displayName": "Samsung",
        "redirect": "brand|1567410377+2380810213"
      }
    ]
  },
  {
    "id": "SET01",
    "isHighlighted": false,
    "subcategories": [
      {
        "id": "CAT031",
        "displayName": "Áudios Portáteis"
      }
    ]
  }
]
```

---

## 13. Obter Reviews de Todos os Produtos

**Função:** `getAllReviews`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/get_all_reviews`

- **Método OCC:** *Não faz chamada direta ao OCC*
- **Métodos auxiliares usados:**
  - `productsService.getAllProducts`
  - `yourviewService.getProductsReviews`
- **Descrição:**  
  Agrega reviews de todos os produtos consultando os produtos e suas avaliações em serviços auxiliares.
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:** Nenhum.
- **Retorno esperado:**
  - Sucesso: Reviews agregadas dos produtos.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
{
  "reviews": {
    "sku123": { "total_rating": 10, "rating": 4.5 }
  },
  "success": true
}
```

---

## 14. Obter Sugestão de Produtos

**Função:** `autoSuggestion`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/auto_suggestion`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/assembler/pages/Default/services/guidedsearch?Ntt={search}&Ntk=TypeAhead&Nrpp=5`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:**
  - Query: `search` (string)
- **Retorno esperado:**
  - Sucesso: Sugestões de produtos e termos.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
 [
    {
      "id": "589802",
			"sku": "589802",
			"label": "Aspirador de Pó e Água Smart Electrolux A10N1 1250W 220V Cinza e Preto",
			"image": "/ccstore/v1/images/?source=/file/v1776384049784367247/products/589802.589802.jpg&height=940&width=940",
			"price": 359
    }
  ],
 

```

---

## 15. Obter Palavras-chave

**Função:** `getKeywords`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/get_keywords`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccadmin/v1/products?productIds={ids}`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:** Nenhum.
- **Retorno esperado:**
  - Sucesso: Lista de palavras-chave.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
{
  "keywords": ["notebook", "informática", "tecnologia"],
  
}
```

---

## 16. Obter Lojas com Saldo de Produto

**Função:** `getStoresWithProductBalance`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/product/stores_with_product_balance/:productId`

- **Método OCC:** `GET`
- **URL OCC:**  `serviço nagem` `https://www.nagem.com.br/ws/occ/cloud/searchStoresWithProductBalance?codPrd={productId}`
- **Headers necessários:** Nenhum.
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.
- **Retorno esperado:**
  - Sucesso: Lista de lojas com saldo do produto.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
{
  "data": [
    {
      "storeId": "loja01",
      "stock": 5
    }
  ]
}
```
<!-- 
---

<!-- ## 17. Buscar Produtos por Nome

**Função:** `getProductsByName`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/products/display_name`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products?q=displayName co "{text}"`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - Query: `text` (string): termo do nome do produto.
- **Retorno esperado:**
  - Sucesso: Lista de produtos encontrados.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de entrada:**

```json
{
  "text": "notebook"
}
```

**Exemplo de saída:**

```json
{
  "items": [
    {
      "id": "sku123",
      "displayName": "Notebook X",
      "brand": "Marca Y",
      "price": 2999.99
    }
  ]
}
```

--- --> -->

<!-- ## 18. Buscar Produtos por Marca

**Função:** `getProductsByBrand`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/products/brand`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products?q=brand co "{text}"`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - Query: `text` (string): termo da marca.
- **Retorno esperado:**
  - Sucesso: Lista de produtos encontrados.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de entrada:**

```json
{
  "text": "Samsung"
}
```

**Exemplo de saída:**

```json
{
  "items": [
    {
      "id": "sku456",
      "displayName": "Smartphone Samsung Galaxy",
      "brand": "Samsung",
      "price": 1999.99
    }
  ]
}
```

--- -->

<!-- ## 19. Buscar Produto por SKU

**Função:** `getProductBySku`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/products/sku`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products?q=id co "{text}"`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
  - Query: `text` (string): SKU do produto.
- **Retorno esperado:**
  - Sucesso: Produto encontrado.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de entrada:**

```json
{
  "text": "sku123"
}
```

**Exemplo de saída:**

```json
{
  "items": [
    {
      "id": "sku123",
      "displayName": "Notebook X",
      "brand": "Marca Y",
      "price": 2999.99
    }
  ]
}
```

--- -->

## 20. Buscar Todos os Produtos (IDs)

**Função:** `getAllProducts`  
**Arquivo:** productsController.js  

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products?fields=items.id&offset={offset}`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
  - `X-CCAsset-Language: pt-BR`
  - `Content-Type: application/json`
  - `Accept: application/json`
- **Parâmetros de entrada:**
 - `token` (string): token de acesso.
  - `offset` (number): para paginação.
- **Retorno esperado:**
  - Sucesso: Lista de IDs de produtos.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de entrada:**

```json
{
  "offset": 0
}
```

**Exemplo de saída:**

```json
{
  "items": [{ "id": "sku123" }, { "id": "sku456" }]
}
```

---

## 21. Obter Palavras-chave

**Função:** `getKeywords`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/get_keywords`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccadmin/v1/products?productIds={ids}`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:** Nenhum.
- **Retorno esperado:**
  - Sucesso: Lista de palavras-chave.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json
{
  "keywords": ["notebook", "informática", "tecnologia"],
  
}
```

---

## 22. Obter Reviews de Todos os Produtos

**Função:** `getAllReviews`  
**Arquivo:** productsController.js  
**Rota interna:** `GET /api/nagem/get_all_reviews`

- **Método OCC:** `GET`
- **URL OCC:** `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products?fields=items.id&offset={offset}`
- **Headers necessários:**
  - `Authorization: Bearer <accessToken>`
- **Parâmetros de entrada:** Nenhum.
- **Retorno esperado:**
  - Sucesso: Reviews agregadas dos produtos.
  - Erro: Objeto de erro retornado pela OCC.

**Exemplo de saída:**

```json

   {
    "sku123": { "total_rating": 10, "rating": 4.5 }
  },


```

---

## Auxiliares

## 24. getSKU

**Função:** `getSKU`  
**Arquivo:** productsService.js  
**Descrição:** Busca detalhes de um SKU específico no OCC.

- **URL OCC:** `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products/{skuId}`
- **Usado por:** Diversos métodos do controller de produtos, home, vitrines, etc.
- **Parâmetros de entrada:**
  - `skuId` (string): ID do SKU.

**Exemplo de entrada:**

```json
{
  "skuId": "sku123"
}
```

**Exemplo de saída:**

```json
{
  "id": "sku123",
  "displayName": "Notebook X",
  "brand": "Marca Y",
  "price": 2999.99,
  "in_stock": true
}
```

---

## 25. getProductsHome


**Função:** `getProductsHome`  
**Arquivo:** productsService.js  
**Descrição:** Busca produtos para exibir na home, usando critérios de destaque.

- **Método OCC:** *Não faz chamada direta ao OCC no controller*
- **Métodos auxiliares usados:**  
  - `GetAuth` (requisições internas para produtos e estoque)
- **Usado por:** homeService.getAppHome, homeService.getHomeSpecialShowcases, etc.
- **Parâmetros de entrada:**
  - `terms` (string): termo de busca (opcional)
  - `page` (number): página (opcional)
  - `nrpp` (number): número de resultados por página (opcional)
- **Retorno esperado:**
  - Sucesso: Lista de produtos e estoque.
  - Erro: Objeto de erro retornado pelo serviço.

**Exemplo de entrada:**

```json
{
  "terms": "notebook",
  "page": 1,
  "nrpp": 10
}
```

**Exemplo de saída:**

```json
{
  "products": [
    {
      "id": "sku123",
      "displayName": "Notebook X",
      "brand": "Marca Y",
      "price": 2999.99
    }
  ],
  "total": 100
}
```

---

## 26. getCollection

**Função:** `getCollection`  
**Arquivo:** productsService.js  
**Descrição:** Busca uma coleção de produtos ou banners no OCC.

- **URL OCC:** `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/collections/{collectionId}`
- **Usado por:** homeService.getDynamicMiniBanner, homeService.getDynamicBannerBrand, etc.
- **Parâmetros de entrada:**
  - `collectionId` (string): ID da coleção.

**Exemplo de entrada:**

```json
{
  "collectionId": "Banner_Home"
}
```

**Exemplo de saída:**

```json
{
  "repositoryId": "Banner_Home",
  "items": [
    {
      "id": "sku123",
      "displayName": "Notebook X"
    }
  ]
}
```

---
<!-- 
## 27. getBannersList

**Função:** `getBannersList`  
**Arquivo:** productsService.js  
**Descrição:** Monta uma lista de banners a partir de uma coleção.

- **Usado por:** homeService.getCarouselBanners, homeService.getDynamicMiniBanner, etc.
- **Parâmetros de entrada:**
  - `collectionId` (string): ID da coleção.

**Exemplo de entrada:**

```json
{
  "collectionId": "banner_carousel_home"
}
```

**Exemplo de saída:**

```json
[
  {
    "url": "v6513603996136993650/collections/Eletrinhos+-+BANNER+PRINCIPAL+DESK+APP.png",
    "repositoryId": "m360302",
    "link": "cupom",
    "title": "slider_image",
    "size": "mediumTag"
  }
]
```

--- -->

## 28. getProducts

**Função:** `getProducts`  
**Arquivo:** productsService.js  
**Descrição:** Busca múltiplos produtos pelo array de IDs.

- **URL OCC:** `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products?productIds={ids}`
- **Usado por:** Métodos de vitrines, recomendações, etc.
- **Parâmetros de entrada:**
  - `ids` (array de strings): IDs dos produtos.

**Exemplo de entrada:**

```json
{
  "ids": ["sku123", "sku456"]
}
```

**Exemplo de saída:**

```json
{
  "items": [
    { "id": "sku123", "displayName": "Notebook X" },
    { "id": "sku456", "displayName": "Smartphone Y" }
  ]
}
```

---



<!-- ## 31. getCategoryProducts

**Função:** `getCategoryProducts`  
**Arquivo:** productsService.js  
**Descrição:** Busca produtos de uma categoria específica.

- **URL OCC:** `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/search?N={categoryId}`
- **Usado por:** getCategoryContent, vitrines, etc.
- **Parâmetros de entrada:**
  - `categoryId` (string): ID da categoria.

**Exemplo de entrada:**

```json
{
  "categoryId": "cat10001"
}
```

**Exemplo de saída:**

```json
{
  "items": [{ "id": "sku123", "displayName": "Notebook X" }]
}
```

--- -->

## 32. getProductsWithStock

**Função:** `getProductsWithStock`  
**Arquivo:** productsService.js  
**Descrição:** Busca o estoque de múltiplos produtos em lote.

- **URL OCC:** `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/stockStatus?products={productIds}`
- **Usado por:** homeService, vitrines, recomendações, etc.
- **Parâmetros de entrada:**
  - `productIds` (string): IDs dos produtos separados por vírgula.

**Exemplo de entrada:**

```json
{
  "productIds": "sku123,sku456"
}
```

**Exemplo de saída:**

```json
{
  "items": [
    { "productId": "sku123", "stockStatus": "IN_STOCK" },
    { "productId": "sku456", "stockStatus": "OUT_OF_STOCK" }
  ]
}
```
---

## 34. getAutoSuggestion

**Função:** `getAutoSuggestion`  
**Arquivo:** productsService.js  
**Descrição:** Busca sugestões de produtos para autocomplete/typeahead.

- **URL OCC:** `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/assembler/pages/Default/services/guidedsearch?Ntt={search}&Ntk=TypeAhead&Nrpp=5`
- **Usado por:** autoSuggestion (controller), busca rápida, etc.
- **Parâmetros de entrada:**
  - `search` (string): termo de busca.

**Exemplo de entrada:**

```json
{
  "search": "note"
}
```

**Exemplo de saída:**

```json
{
  "resultsList": {
    "records": [
      {
        "attributes": {
          "product.displayName": ["Notebook X"],
          "product.repositoryId": ["sku123"],
          "product.largeImageURLs": ["/ccstore/v1/images/?source=/file/v123/products/sku123.jpg"],
          "sku.minActivePrice": ["2999.99"]
        }
      },
      {
        "attributes": {
          "product.displayName": ["Notebook Y"],
          "product.repositoryId": ["sku456"],
          "product.largeImageURLs": ["/ccstore/v1/images/?source=/file/v456/products/sku456.jpg"],
          "sku.minActivePrice": ["1999.99"]
        }
      }
    ]
  }
}
```

---


## YOURVIEW

## getProductReviews

**Função:** `getProductReviews`  
**Arquivo:** yourviewService.js 
**Descrição:** Busca reviews de um produto específico.
- **URL OCC:** `GET https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/products/{productId}/reviews`
- **Usado por:** getAllReviews, getProduct, etc.
- **Parâmetros de entrada:**
  - `productId` (string): ID do produto.

**Exemplo de entrada:**

```json
{
  "productId": "sku123"
}
```

**Exemplo de saída:**

```json
{
  "reviews": [{ "rating": 5, "comment": "Ótimo produto!" }]
}
```

---

## Observações Gerais
