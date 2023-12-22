from ..config.main import get_app
from .scrapping import scrapping
from ..infraestructure.messaging.kafka import send_message
app = get_app()


async def insert_scrapped_data():
    data = await scrapping()
    [send_message(item) for item in data]
    app.database["populations"].insert_many(data)
    return data
