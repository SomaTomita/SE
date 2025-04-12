# Repository Pattern

## What is Repository Pattern?

Repository Pattern is a design pattern that separates the logic that retrieves data from your database from the business logic of your application. It acts as a collection of domain objects in memory.

Key characteristics:

- Mediates between the domain and data mapping layers
- Provides data access abstraction
- Centralizes common data access functionality
- Provides object-oriented interface to data storage

## Basic Implementation

Here's a basic implementation of the Repository Pattern in Python:

```python
from abc import ABC, abstractmethod
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

# Domain Entity
@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

# Repository Interface
class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

# Concrete Repository Implementation (using SQL database)
class SQLUserRepository(UserRepository):
    def __init__(self, db_connection):
        self.db = db_connection

    def find_by_id(self, id: int) -> Optional[User]:
        query = "SELECT * FROM users WHERE id = ?"
        row = self.db.execute(query, (id,)).fetchone()
        return self._map_to_user(row) if row else None

    def find_all(self) -> List[User]:
        query = "SELECT * FROM users"
        rows = self.db.execute(query).fetchall()
        return [self._map_to_user(row) for row in rows]

    def create(self, user: User) -> User:
        query = """
            INSERT INTO users (username, email, created_at, updated_at)
            VALUES (?, ?, ?, ?)
        """
        cursor = self.db.execute(query, (
            user.username,
            user.email,
            user.created_at,
            user.updated_at
        ))
        user.id = cursor.lastrowid
        return user

    def update(self, user: User) -> User:
        query = """
            UPDATE users
            SET username = ?, email = ?, updated_at = ?
            WHERE id = ?
        """
        self.db.execute(query, (
            user.username,
            user.email,
            datetime.now(),
            user.id
        ))
        return user

    def delete(self, id: int) -> None:
        query = "DELETE FROM users WHERE id = ?"
        self.db.execute(query, (id,))

    def _map_to_user(self, row) -> User:
        return User(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            created_at=row['created_at'],
            updated_at=row['updated_at']
        )

# Usage Example
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str, email: str) -> User:
        user = User(
            id=None,
            username=username,
            email=email,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.user_repository.create(user)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.find_by_id(user_id)

    def update_email(self, user_id: int, new_email: str) -> Optional[User]:
        user = self.user_repository.find_by_id(user_id)
        if user:
            user.email = new_email
            user.updated_at = datetime.now()
            return self.user_repository.update(user)
        return None



# db connection
db_connection = create_connection()
user_repository = SQLUserRepository(db_connection)

user_repository = SQLUserRepository(db_connection)
user_service = UserService(user_repository)
# create User
new_user = user_service.create_user(
            username="john_doe",
            email="john@example.com"
)
# get User Info
user = user_service.get_user(new_user.id)
print(f"Retrieved user: {user}")
# change mail
updated_user = user_service.update_email(
    user_id=new_user.id,
    new_email="john.doe@example.com"
)
# get all User
all_users = user_repository.find_all()
for user in all_users:
    print(f"- {user}")
# delete User
user_repository.delete(new_user.id)
print(f"\nDeleted user with ID: {new_user.id}")

```

## Common File Structure

A typical Repository Pattern implementation often includes these files:

```
repository/
├── base.py          # Base repository with common CRUD operations
├── builder.py       # Builds complex queries
├── bulk_builder.py  # Handles bulk operations
├── finder.py        # Contains specialized find operations
├── serializer.py    # Handles data serialization/deserialization
├── updator.py       # Contains specialized update operations
└── creator.py       # Contains specialized create operations
```

## Role of Each Component

### 1. Base Repository (base.py)

```python
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class BaseRepository(Generic[T], ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
```

### 2. Query Builder (builder.py)

```python
from typing import List, Any, Dict

class QueryBuilder:
    def __init__(self):
        self.conditions: List[str] = []
        self.parameters: Dict[str, Any] = {}
        self.order_by: List[str] = []
        self.limit_value: Optional[int] = None
        self.offset_value: Optional[int] = None

    def where(self, condition: str, params: Dict[str, Any]) -> 'QueryBuilder':
        self.conditions.append(condition)
        self.parameters.update(params)
        return self

    def order_by(self, field: str, ascending: bool = True) -> 'QueryBuilder':
        direction = "ASC" if ascending else "DESC"
        self.order_by.append(f"{field} {direction}")
        return self

    def limit(self, limit: int) -> 'QueryBuilder':
        self.limit_value = limit
        return self

    def offset(self, offset: int) -> 'QueryBuilder':
        self.offset_value = offset
        return self

    def build(self) -> str:
        query = "SELECT * FROM table"

        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)

        if self.order_by:
            query += " ORDER BY " + ", ".join(self.order_by)

        if self.limit_value is not None:
            query += f" LIMIT {self.limit_value}"

        if self.offset_value is not None:
            query += f" OFFSET {self.offset_value}"

        return query
```

### 3. Bulk Operations (bulk_builder.py)

```python
from typing import List, TypeVar, Generic

T = TypeVar('T')

class BulkBuilder(Generic[T]):
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size
        self.items: List[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)
        if len(self.items) >= self.batch_size:
            self.flush()

    def flush(self) -> None:
        if self.items:
            self._execute_bulk_insert(self.items)
            self.items.clear()

    def _execute_bulk_insert(self, items: List[T]) -> None:
        # Implementation specific to the database
        pass
```

### 4. Finder (finder.py)

```python
from typing import List, Optional
from datetime import datetime

class UserFinder:
    def __init__(self, repository):
        self.repository = repository

    def find_by_email(self, email: str) -> Optional['User']:
        return self.repository.find_one({"email": email})

    def find_active_users(self) -> List['User']:
        return self.repository.find_many({
            "status": "active",
            "last_login_at": {"$gt": datetime.now() - timedelta(days=30)}
        })

    def find_by_role(self, role: str) -> List['User']:
        return self.repository.find_many({"role": role})
```

### 5. Serializer (serializer.py)

```python
from typing import Dict, Any
from datetime import datetime

class UserSerializer:
    def to_dict(self, user: 'User') -> Dict[str, Any]:
        return {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'created_at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat()
        }

    def from_dict(self, data: Dict[str, Any]) -> 'User':
        return User(
            id=data.get('id'),
            email=data['email'],
            username=data['username'],
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at'])
        )
```

### 6. Updator (updator.py)

```python
from typing import Dict, Any

class UserUpdator:
    def __init__(self, repository):
        self.repository = repository

    def update_last_login(self, user_id: int) -> None:
        self.repository.update_one(
            {"id": user_id},
            {"$set": {"last_login_at": datetime.now()}}
        )

    def update_status(self, user_id: int, status: str) -> None:
        self.repository.update_one(
            {"id": user_id},
            {"$set": {"status": status}}
        )
```

### 7. Creator (creator.py)

```python
from typing import Optional

class UserCreator:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, email: str, username: str, password: str) -> 'User':
        # Validate input
        self._validate_input(email, username, password)

        # Hash password
        hashed_password = self._hash_password(password)

        # Create user
        user = User(
            email=email,
            username=username,
            password=hashed_password,
            status="active",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        return self.repository.create(user)

    def _validate_input(self, email: str, username: str, password: str) -> None:
        if not email or not username or not password:
            raise ValueError("All fields are required")
```

## When to Use Repository Pattern

Use the Repository Pattern when:

1. You want to isolate data access logic
2. You need to unit test your application without using a real database
3. You want to maintain a consistent data access interface
4. You need to work with multiple data sources
5. You want to cache data access results

## Benefits

1. **Separation of Concerns**

   - Separates data access from business logic
   - Makes the code more maintainable
   - Easier to test

2. **Centralized Data Access**

   - Single point of data access
   - Consistent data access patterns
   - Easier to implement caching

3. **Domain-Focused**

   - Works with domain objects
   - Hides data access complexity
   - More object-oriented approach

4. **Testability**
   - Easy to mock for testing
   - Can test business logic in isolation
   - Supports dependency injection

## Best Practices

1. Keep the repository interface simple and focused
2. Use repository per aggregate root/entity
3. Return domain objects, not database entities
4. Hide data access implementation details
5. Consider using the Unit of Work pattern for transactions
6. Use dependency injection
7. Implement proper error handling

## Common Anti-patterns to Avoid

1. Bloated repositories with business logic
2. Exposing ORM/database specific features
3. Breaking repository abstraction
4. Not using interfaces
5. Mixing query and command responsibilities

## Conclusion

The Repository Pattern is a powerful way to abstract data access and maintain a clean separation between your domain logic and data access code. While it may add some complexity to your codebase, the benefits of maintainability, testability, and flexibility often outweigh the costs.
