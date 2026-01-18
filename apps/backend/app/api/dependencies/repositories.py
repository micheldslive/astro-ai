from fastapi import Depends
from pymongo.collection import Collection

from app.api.dependencies.mongo import get_agents_collection

from app.entities.agents import AgentsEntity
from app.repositories.base.mongo import MongoRepository


def get_agents_repository(
    collection: Collection = Depends(get_agents_collection),
) -> MongoRepository:
    return MongoRepository(collection=collection, entity_cls=AgentsEntity)
