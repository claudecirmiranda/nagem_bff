from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.network import CloudFront
from diagrams.aws.storage import S3
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Nodejs
from diagrams.onprem.client import Users
from diagrams.onprem.monitoring import Grafana

with Diagram("Arquitetura - Sistema de Conteúdo da Home do App (Substituição do OCC)", show=True, direction="TB"):

    user = Users("Usuário de Negócio (CMS)")
    app = Users("App / BFF")

    with Cluster("Administração de Conteúdo"):
        cms_frontend = Nodejs("Painel CMS")
        cms_backend = Nodejs("CMS API / Backend Admin")
        db = PostgreSQL("Banco de Dados")
        storage = S3("Storage de Imagens")
        cdn = CloudFront("CDN (CloudFront / Cloudflare)")
        cache = Redis("Redis Cache")
        publisher = Lambda("Serviço de Publicação")

        user >> cms_frontend >> cms_backend
        cms_backend >> db
        cms_backend >> storage >> cdn
        cms_backend >> publisher >> cache

    with Cluster("Consumo da API Pública"):
        public_api = Nodejs("API Pública /api/home")
        app >> public_api
        public_api >> cache
        public_api >> db
        public_api >> cdn

    observability = Grafana("Observabilidade")
    cms_backend >> observability
    public_api >> observability
