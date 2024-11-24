from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


# Replace these with your Docker MySQL credentials
DATABASE_URL = "mysql+asyncmy://root:secret@localhost:3309/gaiascycle"

# Async database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session maker for dependency injection
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session