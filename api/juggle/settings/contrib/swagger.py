from ..environment import env


SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": env.str("JUGGLE_BASE_API_URL", default="https://juggle.kyleobrien.online"),
}
