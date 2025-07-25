TABELA DE ROTAS EXTRAÍDAS
| Nome                       | Rota                                                       | Método |
|--|----|-------|
|getHome                    | /home                                                      | GET   |
|getHomeBanners             | /api/nagem/home/banners                                    | GET   |
|getStoresEnabled           | /api/nagem/home/stores_enabled                             | GET   |
|getAppHome                 | /api/nagem/home/getAppHome                                 | GET   |
|getHomeSpecialShowcases    | /api/nagem/home/getHomeSpecialShowcases                    | GET   |
|getMiniBanner              | /api/nagem/home/mini_banner                                | GET   |
|getCardBanner              | /api/nagem/home/card_banner                                | GET   |
|getBannersBrand            | /api/nagem/home/banner_brand                               | GET   |
|getLightningOffer          | /api/nagem/home/lightning_offer                            | GET   |
|getHomeBannerCorpo         | /api/nagem/home/banner_corpo                               | GET   |
|getHomeCategories          | /api/nagem/home/categories                                 | GET   |
|getHomeItems*              | /home/items                                                | GET   |
|getAllHomeContent          | /api/nagem/home/home_content                               | GET   |
|getHomePromoShowcase*      | /home/promo-showcase                                       | GET   |
|getHomeShowCases           | /api/nagem/home/showcases/:showcaseId                      | GET   |
|getHomeFilipetas           | /home                                                      | GET   |
|getHomeMeetNagemBanners    | /api/nagem/home/banners_meet_nagem                         | GET   |
|createToken                | /api/nagem/user/login                                      | POST  |
|changePassword             | /api/nagem/user/change_password                            | PUT   |
|socialLogin                | /api/nagem/user/social_login                               | POST  |
|addItemOCC                 | /api/nagem/order/current/itens/add                         | POST  |
|checkoutItemsConfirm       | /api/nagem/order/current/checkout_items_confirm            | PATCH |
|updateItemOCC              | /api/nagem/order/current/itens/update/:itemId              | PATCH |
|useCoupon                  | /api/nagem/order/current/coupon                            | PATCH |
|deleteItemOCC              | /api/nagem/order/current/itens/delete/:itemId              | DELETE|
|retryOrderOCC              | /api/nagem/order/retry                                     | POST  |
|retryOrderLegacy           | /api/nagem/order/retry_legacy                              | POST  |
|verifyToken                | /api/nagem/user/token/verify                               | POST  |
|refreshToken               | /api/nagem/user/token/refresh                              | POST  |
|getUserById                | /api/nagem/user                                            | GET   |
|contactUs                  | /api/nagem/user/contact_us                                 | POST  |
|softDeleteUser             | /api/nagem/user                                            | DELETE|
|searchUser                 | /api/nagem/user/search/:email                              | GET   |
|createUser                 | /api/nagem/user/register                                   | POST  |
|verifyCpfUser              | /api/nagem/user/verify/cpf                                 | POST  |
|updateUser                 | /api/nagem/user                                            | PUT   |
|pushRegister               | /api/nagem/user/push/register                              | POST  |
|updateUserPassword         | /user/change-password                                      | PATCH |
|resetPasswordWithoutLogin  | /api/nagem/user/login/reset_password                       | POST  |
|resetPasswordWithLogin     | /api/nagem/user/reset_password                             | POST  |
|forgotPasswordBFF          | /user/forgot-password                                      | POST  |
|getDefaultAddresses        | /api/nagem/user/address/default                            | GET   |
|getAddresses               | /api/nagem/user/address                                    | GET   |
|createAddress              | /api/nagem/user/address                                    | POST  |
|updateAddress              | /api/nagem/user/address/:addressId                         | PUT   |
|getProduct                 | /api/nagem/product/:sku                                    | GET   |
|getProductSpecifications   | /api/nagem/product/specifications/:sku                     | GET   |
|getProductGuarantees       | /api/nagem/product/guarantees/:sku                         | GET   |
|getReviews                 | /api/nagem/yourview/:productId                             | GET   |
|getRelatedProducts         | /api/nagem/product/related/:sku                            | GET   |
|getSimilarProducts         | /api/nagem/product/similar/:sku                            | GET   |
|deleteAddress              | /api/nagem/user/address/:addressId                         | DELETE|
|getOrder                   | /api/nagem/order/:orderId                                  | GET   |
|getCurrentOrder            | /api/nagem/order/current                                   | GET   |
|removeCurrentOrder         | /api/nagem/order/current                                   | DELETE|
|getOrders                  | /api/nagem/orders                                          | GET   |
|getPaymentMethods          | /api/nagem/order/current/payment_methods                   | POST  |
|deletePaymentMethods       | /api/nagem/order/current/payments/:paymentId               | DELETE|
|getSearchProducts          | /api/nagem/search_products                                 | GET   |
|getFilteredSearch          | /api/nagem/filtered_search                                 | GET   |
|autoSuggestion             | /api/nagem/auto_suggestion                                 | GET   |
|getCategories              | /api/nagem/categories                                      | GET   |
|getMenuCategories          | /api/nagem/menu_categories                                 | GET   |
|getCategoriesBanners       | /api/nagem/categories/banners                              | GET   |
|getCategoryContent         | /api/nagem/category_content/:categoryId                    | GET   |
|getSubCategories           | /api/nagem/sub_categories/:categoryId                      | GET   |
|getPromoProducts           | /api/nagem/campaigns_products/:offerId                     | GET   |
|getCampaigns               | /api/nagem/campaigns                                       | GET   |
|getCategoryProducts        | /api/nagem/landing-page/:n/:ntt/:ns                        | GET   |
|getCategoryProducts        | /api/nagem/landing-page/:categoryId/:sort                  | GET   |
|fetchCart                  | /api/nagem/cart/step/1                                     | POST  |
|getWithdrawalStores        | /cart/step/2                                               | POST  |
|getStores                  | /stores                                                    | GET   |
|getMainStoreByCep          | /localization                                              | GET   |
|createOrder                | /api/nagem/order/create                                    | POST  |
|updatePaymentOrder         | /api/nagem/order/current/payments/update                   | PATCH |
|listCreditCards            | /api/nagem/user/credit_card                                | GET   |
|updateCreditCard           | /api/nagem/user/credit_card/:creditCardId                  | PUT   |
|deleteCreditCard           | /api/nagem/user/credit_card/:creditCardId                  | DELETE|
|getAppVersion              | /app-version                                               | GET   |
|getAndroidVersion          | /api/nagem/android_version                                 | GET   |
|getBannerProducts          | /products/pages/:bannerId                                  | GET   |
|setShipping                | /api/nagem/shipping                                        | POST  |
|getShipping                | /api/nagem/shipping_methods                                | GET   |
|getShippingId              | /api/nagem/order/current/shipping_id                       | GET   |
|selectAddress              | /api/nagem/order/current/shipping_address/:shippingGroupId | PATCH |
|selectShipping             | /api/nagem/order/current/shipping_method                   | PATCH |
|addPayment                 | /api/nagem/order/current/payments/add                      | POST  |
|orderPrepare               | /api/nagem/order/current/close                             | PATCH |
|getZipCode                 | /api/nagem/user/address/cep/:zipcode                       | GET   |
|getAutocomplete            | /products/linxAutocomplete                                 | GET   |
|setDeviceId                | /user/device                                               | POST  |
|getDeliveryOptions         | /delivery_options/store/:id                                | GET   |
|setFavoriteAddress         | /user/address/:addressId/favorite                          | POST  |
|getHashtag                 | /hashtags/:hashtag                                         | GET   |
|getLandingPage             | /api/nagem/landing-page/:id                                | GET   |
|getCurrentCart             | /api/nagem/order/current                                   | GET   |
|updateCurrentCart          | /cart/:id                                                  | PATCH |
|orderPrice                 | /api/nagem/order/current/price                             | POST  |
|orderSubmit                | /api/nagem/order/current/submit                            | POST  |
|getStockStatus             | /api/nagem/product/stock/:productId                        | GET   |
|getShippingStores          | /api/nagem/shipping_stores                                 | GET   |
|createNewCart              | /cart                                                      | POST  |
|getRemoteSettings          | /settings                                                  | GET   |
|getReviewStatus            | /user/review/:device_id                                    | GET   |
|postReviewStatus           | /user/review                                               | POST  |
|submitRecoveryCode         | /user/submitCode                                           | POST  |
|pendingDeletion            | /user/pendingDeletion                                      | POST  |
|getNightOffer              | /api/nagem/home/night_offer                                | GET   |
|getFavoritesProducts       | /api/nagem/favorite_products/get_list_products/:listId     | GET   |
|listFavoritesProductsLists | /api/nagem/favorite_products/list_products_lists           | GET   |
|updateFavoritesProducts    | /api/nagem/favorite_products/update_items/:listId          | POST  |
|createFavoritesProducts    | /api/nagem/favorite_products/create_list_products          | POST  |
|addProductNotification     | /api/nagem/addProductNotification                          | POST  |
|listStoresWithProduct      | /api/nagem/product/stores_with_product_balance/:sku        | GET   |
|buyTogether                | /api/nagem/buy_together                                    | POST  |
|relatedToInterest          | /api/nagem/related_to_your_interest                        | POST  |
|alsoBought                 | /api/nagem/who_saw_who_bought                              | POST  |
|viewedProducts             | /api/nagem/viewed_products                                 | POST  |
|getHomeTopLink             | /api/nagem/home/home_top_link                              | GET   |
|getLegacyOrderDetails      | /api/nagem/order_legacy_detail/:id                         | GET   |
|getLegacyOrders            | /api/nagem/order_legacy/:user                              | GET   |


📊 Estatísticas:

- DELETE: 6 rotas
- GET: 66 rotas
- PATCH: 8 rotas
- POST: 36 rotas
- PUT: 4 rotas

Total de rotas: 120
