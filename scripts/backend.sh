cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Create requirements.txt
cat > requirements.txt << EOL
fastapi
uvicorn[standard]
sqlalchemy
alembic
pydantic
pydantic-settings
python-jose[cryptography]
passlib[bcrypt]
python-multipart
aiosqlite
python-dotenv
httpx
pillow
python-slugify
EOL

# Create requirements-dev.txt
cat > requirements-dev.txt << EOL
pytest
pytest-asyncio
pytest-cov
faker
black
ruff
EOL

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Initialize Alembic
alembic init alembic