# Rotas Extraídas

**cart.js**
|ID|Rota|Método|Controller|Função|
|--|----|-------|----------|--------|
|1| /api/nagem/cart/step/1 | post | cartController | cartStep1 |

**collections.js**
|ID|Rota|Método|Controller|Função|
|--|----|-------|----------|--------|
|1| **/api/nagem/collections** | get | listCollections | getCollections |

**favoritesProducts.js**
|ID|Rota|Método|Controller|Função|OCC|APP|
|--|----|-------|----------|--------|--------|--------|
|1| **/api/nagem/favorite_products/create_list_products** | post | favoriteProductController | createPurchaseList |1|
|2| **/api/nagem/favorite_products/list_products_lists** | get | favoriteProductController | listPurchaseLists |2|
|3| **/api/nagem/favorite_products/get_list_products/:id** | get | favoriteProductController | getPurchaseList |3|
|4| **/api/nagem/favorite_products/update_items/:id** | post | favoriteProductController | updateItems |4|

**home.js**
|ID|Rota|Método|Controller|Função|OCC|APP|
|--|----|-------|----------|--------|--------|--------|
|1| /api/nagem/home | get | homeController | get |
|2| **/api/nagem/home/refresh** | get | homeController | refreshHome |5|
|3| **/api/nagem/home/home_content** | get | homeController | getHomeContent |6|Y|
|4| **/api/nagem/home/banners** | get | homeController | getBanners |7|Y|
|5| **/api/nagem/home/carousel_banners** | get | homeController | getCarouselBanners |8|
|6| **/api/nagem/home/lightning_offer** | get | homeController | getLightningOffer |9|Y|
|7| /api/nagem/home/banner_corpo | get | homeController | getBannerCorpo |Y|
|8| **/api/nagem/home/banner_brand** | get | homeController | getBannerBrand |10|Y|
|9| **/api/nagem/home/getAppHome** | get | homeController | getAppHome |11|Y|
|10| **/api/nagem/home/get_popup_home** | get | homeController | getPopupHome |12|
|11| **/api/nagem/home/getHomeSpecialShowcases** | get | homeController | getHomeSpecialShowcases |13|Y|
|12| **/api/nagem/home/categories** | get | homeController | getCategories |14|Y|
|13| **/api/nagem/home/night_offer** | get | homeController | getNightOffer |15|
|14| **/api/nagem/home/mini_banner** | get | homeController | getMiniBanner |16|Y|
|15| **/api/nagem/home/dynamic_mini_banner** | get | homeController | getDynamicMiniBanner |17|
|16| **/api/nagem/home/card_banner** | get | homeController | getNagemCardBanner |18|Y|
|17| **/api/nagem/home/home_top_link** | get | homeController | getHomeTopLink |19|
|18| **/api/nagem/home/showcases/:showcaseId** | get | homeController | getVitrine |20|Y|
|19| **/api/nagem/home/banners_meet_nagem** | get | homeController | getBannersMeetNagem |21|
|20| **/api/nagem/home/stores_enabled** | get | homeController | getStoresEnabled |-|Y|

**index.js**
|ID|Rota|Método|Controller|Função|
|--|----|-------|----------|--------|
|1| / | get | res | render |
|2| /test-ping | get | res | end |
|3| /healthcheck | get | res | end |

**landingPage.js**
|ID|Rota|Método|Controller|Função|OCC|APP|
|--|----|-------|----------|--------|--------|--------|
|1| **/api/nagem/landing-page/:n/:ntt/:ns** | get | landingPageController | getId |22|

**login.js**
|ID|Rota|Método|Controller|Função|OCC|APP|
|--|----|-------|----------|--------|--------|--------|
|1| **/api/nagem/login** | post | login | getLogin |23|

**order.js**
|ID|Rota|Método|Controller|Função|OCC|APP|
|--|----|-------|----------|--------|--------|--------|
|1| **/api/nagem/order/create** | post | orderController | createOrder |24|
|2| **/api/nagem/order/current** | get | orderController | getCurrentOrder |25|
|3| /api/nagem/order/current/shipping_groups/relatetoitems | post | orderController | relatedToItensCurrentOrder |
|4| /api/nagem/order/current/shipping_groups/remove/:shippingId | delete | orderController | removeShippingGroupCurrentOrder |
|5| **/api/nagem/order/current/itens/add** | post | orderController | addItemCurrentOrder |
|6| **/api/nagem/order/current/itens/update/:itemId** | patch | orderController | updateItemCurrentOrder |26|
|7| **/api/nagem/order/current/itens/delete/:itemId** | delete | orderController | deleteItemCurrentOrder |27|
|8| /api/nagem/order/current/shipping_groups | post | orderController | shippingAddCurrentOrder |
|9| **/api/nagem/order/current/price** | post | orderController | priceCurrentOrder |28|
|10| **/api/nagem/order/current/coupon** | patch | orderController | patchCoupon |29|
|11| /api/nagem/order/current/shipping_address/:shippingId | patch | orderController | addAddressCurrentOrder |
|12| **/api/nagem/order/current/shipping_method** | patch | orderController | addShippingCurrentOrder |30|
|13| **/api/nagem/order/current/payments/add** | post | orderController | addPaymentCurrentOrder |31|
|14| **/api/nagem/order/current/payments/update** | patch | orderController | updatePaymentCurrentOrder |32|
|15| /api/nagem/order/get_order_id | get | orderController | getOrderId |
|16| **/api/nagem/order/current/payment_methods** | post | orderController | paymentMethodsCurrentOrder |33|
|17| /api/nagem/order/searchModal | post | orderController | searchModal |
|18| **/api/nagem/order/current/payments/:paymentId** | delete | orderController | removePaymentCurrentOrder |34|
|19| **/api/nagem/order/current/close** | patch | orderController | closeCurrentOrder |35|
|20| **/api/nagem/order/current/submit** | post | orderController | submitCurrentOrder |36|
|21| **/api/nagem/order/:orderId** | get | orderController | orderStatus |37|
|22| **/api/nagem/order_legacy/:userId** | get | orderController | orderLegacyList |38|
|23| /api/nagem/order_legacy_detail/:orderId | get | orderController | orderLegacyStatus |
|24| /api/nagem/orders | get | orderController | orderList |
|25| **/api/nagem/order/retry** | post | orderController | retryOrder |39|
|26| /api/nagem/order/retry_legacy | post | orderController | retryOrderLegacy |
|27| **/api/nagem/order/current** | delete | orderController | removeCurrentOrder |40|
|28| /api/nagem/order/current/shipping_id | get | orderController | getShippingId |
|29| /api/nagem/order/current/checkout_items_confirm | patch | orderController | checkoutItemsConfirm |

**payment.js**
|ID|Rota|Método|Controller|Função|
|--|----|-------|----------|--------|
|1| /api/nagem/payment/pix | post | paymentController | pixPayment |

**products.js**
|ID|Rota|Método|Controller|Função|OCC|APP|
|--|----|-------|----------|--------|--------|--------|
|1| **/api/nagem/search_products** | get | productsService | search |
|2| **/api/nagem/auto_suggestion** | get | productsService | autoSuggestion |41|
|3| **/api/nagem/product/:productId** | get | productsService | getProduct |42|
|4| **/api/nagem/product/specifications/:productId** | get | productsService | getProductSpecifications |43|
|5| **/api/nagem/product/guarantees/:productId** | get | productsService | getProductGuarantees |44|
|6| **/api/nagem/product/related/:productId** | get | productsService | getRelatedProducts |45|
|7| **/api/nagem/product/similar/:productId** | get | productsService | getSimilarProducts |46|
|8| **/api/nagem/product/stock/:productId** | get | productsService | getProductStock |47|
|9| **/api/nagem/product/stores_with_product_balance/:productId** | get | productsService | getStoresWithProductBalance |48|
|10| **/api/nagem/categories** | get | productsService | getStoreCategories |49|
|11| **/api/nagem/menu_categories** | get | productsService | getMenuCategories |50|
|12| /api/nagem/campaigns | get | productsService | getStoreCampaigns |
|13| /api/nagem/filtered_search | get | productsService | getFilteredSearch |
|14| **/api/nagem/get_all_reviews** | get | productsService | getAllReviews |51|
|15| /api/nagem/filtered_products | get | productsService | getFilteredProducts |
|16| **/api/nagem/sub_categories/:categoryId** | get | productsService | getStoreSubCategories |52|
|17| **/api/nagem/category_content/:categoryId** | get | productsService | getCategoryContent |53|
|18| **/api/nagem/get_keywords** | get | productsService | getKeywords |54|
|19| /api/nagem/viewed_products | post | productsService | postViewedProducts |
|20| **/api/nagem/addProductNotification** | post | productsService | postProductNotification |55|
|21| /api/nagem/buy_together | post | productsService | postBuyTogether |
|22| /api/nagem/related_to_your_interest | post | productsService | postRelatedToYourInterest |
|23| /api/nagem/who_saw_who_bought | post | productsService | postWhoSawWhoBought |

**shipping.js**
|ID|Rota|Método|Controller|Função|
|--|----|-------|----------|--------|
|1| /api/nagem/shipping | post | shippingController | shipping |
|2| /api/nagem/nagem_shipping | post | shippingController | nagemShipping |
|3| /api/nagem/shipping_methods | get | shippingController | shippingMethods |
|4| /api/nagem/shipping_stores | get | shippingController | shippingStores |

**sitesettings.js**
|ID|Rota|Método|Controller|Função|OCC|APP|
|--|----|-------|----------|--------|--------|--------|
|1| **/api/nagem/site** | get | listSiteSettings | getSiteSettings |56|

**user.js**
|ID|Rota|Método|Controller|Função|
|--|----|-------|----------|--------|
|1| /api/nagem/user/register | post | userController | register |
|2| /api/nagem/user/verify/cpf | post | userController | verifyCpf |
|3| /api/nagem/user/login | post | userController | login |
|4| /api/nagem/user/token/verify | post | userController | verifyToken |
|5| /api/nagem/user/token/refresh | post | userController | refreshToken |
|6| /api/nagem/user/push/register | post | userController | registerPush |
|7| /api/nagem/user | get | userController | getUserData |
|8| /api/nagem/user | put | userController | putUserData |
|9| /api/nagem/user | delete | userController | userSoftDelete |
|10| /api/nagem/user/address | get | userController | getUserAddress |
|11| /api/nagem/user/address/default | get | userController | getUserDefaultAddress |
|12| /api/nagem/user/address | post | userController | postUserAddress |
|13| /api/nagem/user/address/:addressId | put | userController | putUserAddress |
|14| /api/nagem/user/address/:addressId | delete | userController | userDeleteStore |
|15| /api/nagem/user/address/cep/:cep | get | userController | getBuscaCep |
|16| /api/nagem/user/reset_password | post | userController | postSendPasswordReset |
|17| /api/nagem/user/login/reset_password | post | userController | loginPasswordReset |
|18| /api/nagem/user/search/:email | get | userController | verifyEmail |
|19| /api/nagem/user/credit_card | get | userController | getCreditCard |
|20| /api/nagem/user/credit_card | post | userController | postCreditCard |
|21| /api/nagem/user/credit_card/:creditCardId | put | userController | editCreditCard |
|22| /api/nagem/user/credit_card/:creditCardId | delete | userController | removeCreditCard |
|23| /api/nagem/user/change_password | put | userController | changePassword |
|24| /api/nagem/user/contact_us | post | userController | contactUs |
|25| /api/nagem/user/social_login | post | userController | googleLogin |

**yourview.js**
|ID|Rota|Método|Controller|Função|
|--|----|-------|----------|--------|
|1| /api/nagem/yourview/:productId | get | yourviewController | getProductReviews |


✅ Tabela de rotas com controller e função gerada em 'rotas_controlador_funcao.md'

📊 Estatísticas:

   • Arquivos processados: 14
   
   • Total de rotas encontradas: 115

   • Total de rotas OCC: 56
