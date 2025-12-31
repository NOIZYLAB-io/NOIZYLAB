# {PROJECT_NAME}

## Project Type
Python Application / API

## Tech Stack
- **Python**: 3.12+
- **Framework**: FastAPI / Flask / Django
- **Package Manager**: uv (preferred) / pip
- **Type Checking**: mypy (strict)
- **Linting**: ruff
- **Testing**: pytest + pytest-cov
- **Database**: PostgreSQL / SQLite (SQLAlchemy)

## Project Structure
```
src/
├── {package_name}/
│   ├── __init__.py
│   ├── main.py           # Entry point
│   ├── config.py         # Settings (pydantic-settings)
│   ├── api/              # API routes
│   │   ├── __init__.py
│   │   ├── routes/       # Route modules
│   │   └── deps.py       # Dependencies
│   ├── core/             # Core business logic
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Service layer
│   └── utils/            # Utilities
├── tests/
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── pyproject.toml
└── README.md
```

## Key Commands
```bash
# Using uv (recommended)
uv sync                   # Install dependencies
uv run python -m {pkg}    # Run application
uv run pytest             # Run tests
uv run ruff check .       # Lint
uv run mypy src/          # Type check

# Using pip
pip install -e ".[dev]"
python -m {pkg}
pytest
```

## Development Setup
```bash
# Create virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv sync --dev

# Set up pre-commit
pre-commit install
```

## Coding Conventions

### Style
- Follow PEP 8 (enforced by ruff)
- Max line length: 100 characters
- Use type hints everywhere
- Docstrings: Google style

### Imports
```python
# Standard library
from __future__ import annotations
import os
from typing import TYPE_CHECKING

# Third-party
from fastapi import FastAPI

# Local
from .config import settings

if TYPE_CHECKING:
    from .models import User
```

### Type Hints
```python
def process_data(
    items: list[dict[str, Any]],
    *,
    limit: int | None = None,
) -> list[ProcessedItem]:
    ...
```

### Error Handling
```python
from .exceptions import NotFoundError, ValidationError

try:
    result = await service.get(id)
except NotFoundError:
    raise HTTPException(status_code=404, detail="Not found")
```

## FastAPI Patterns

### Router Structure
```python
from fastapi import APIRouter, Depends
from .deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}")
async def get_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
) -> UserResponse:
    ...
```

### Dependencies
```python
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    ...
```

## Database

### SQLAlchemy Models
```python
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
```

### Migrations (Alembic)
```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

## Testing

### Fixtures
```python
@pytest.fixture
async def db_session():
    async with async_session() as session:
        yield session

@pytest.fixture
def client(db_session):
    with TestClient(app) as client:
        yield client
```

### Test Pattern
```python
async def test_create_user(client: TestClient):
    response = client.post("/users/", json={"email": "test@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
```

## Environment Variables
```
DATABASE_URL=postgresql://user:pass@localhost:5432/db
SECRET_KEY=your-secret-key
DEBUG=false
```

## Performance
- Use async everywhere possible
- Connection pooling for database
- Cache with Redis when needed
- Profile with py-spy

## Security
- Never commit secrets
- Use pydantic for input validation
- Parameterized queries (SQLAlchemy handles this)
- Rate limiting on API endpoints
