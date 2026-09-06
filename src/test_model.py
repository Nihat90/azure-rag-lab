from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

RESOURCE_NAME = "studentxnspl-5289-resource/studentxnspl-5289"

DEPLOYMENT_NAME = "rag-chat


# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default",
)


# --------------------------------------------------
# CLIENT
# --------------------------------------------------

client = OpenAI(
    base_url=f"https://{RESOURCE_NAME}.services.ai.azure.com/openai/v1/",
    api_key=token_provider,
)


# --------------------------------------------------
# TEST
# --------------------------------------------------

response = client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain what RAG is in exactly three sentences."
        }
    ],
)


print(response.choices[0].message.content)
