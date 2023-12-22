from src.config.main import get_app
from src.infraestructure.database.mongoose import shutdown_db_client,startup_db_client
from src.infraestructure.messaging.kafka import create_kafka_producer, close_producer
from src.routers.population import router as population_router
from fastapi.middleware.cors import CORSMiddleware

app =get_app()
    


@app.on_event("startup")
def startup():
    startup_db_client()
    create_kafka_producer()
    print("Connected to the MongoDB database!")

    

@app.on_event("shutdown")
def shutdown():
    shutdown_db_client()
    close_producer()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(population_router, tags=["population"], prefix="/population")
