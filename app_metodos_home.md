### Funcionalidades da Home (segundo levantamento atual)
[voltar](reuniao_tecnica_b2c_app.md)

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
