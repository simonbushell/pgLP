from pgLP.app import create_app
from pgLP.settings import DevConfig, ProdConfig

app = create_app(DevConfig)

