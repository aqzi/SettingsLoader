from pydantic import BaseModel, Field


class InferenceSettings(BaseModel):
    model_name: str
    max_output_tokens: int
    timout: int
    max_retries: int

class AppServerSettings(BaseModel):
    host: str
    port: int
    workers: int

class EnvSettings(BaseModel):
    test: str

class SecretsSettings(BaseModel):
    chatbot_api_key: str
    test: str

class ArgsSettings(BaseModel):
    show_config: bool = Field(False, description="Entire config will be printed if true")

class AppSettings(BaseModel):
    data_path: str
    text_classifier: InferenceSettings
    app_server: AppServerSettings