from typing import Any, Generic, TypeVar, Protocol

from sqlalchemy import UUID

T = TypeVar("T")


class AbstractSQLRepository(Generic[T], Protocol):
    
    async def get_all(self) -> list[T]:
        ...
    
    async def get(self, id: UUID) -> T | None:
        ...
    
    async def create(self, item: T) -> None:
        ...
        
    async def update(self, changes: dict[str, Any], id: UUID) -> None:
        ...
        
    async def delete(self, id: UUID) -> None:
        ...