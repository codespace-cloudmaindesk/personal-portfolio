cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Create requirements.in
cat > requirements.in << EOL
fastapi>=0.110.0
uvicorn[standard]>=0.27.0
sqlalchemy>=2.0.25
alembic>=1.13.1
pydantic>=2.6.0
pydantic-settings>=2.2.0
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
python-multipart>=0.0.9
aiosqlite>=0.19.0
python-dotenv>=1.0.1
httpx>=0.26.0
pillow>=10.2.0
python-slugify>=8.0.4
EOL

# Create requirements-dev.in
cat > requirements-dev.in << EOL
pytest>=8.3.0
pytest-asyncio>=0.24.0
pytest-cov>=6.0.0
faker>=32.0.0
black>=24.10.0
ruff>=0.8.0
EOL

# Install dependencies
pip install pip-tools
pip-compile requirements.in
pip-compile requirements-dev.in 

pip-sync requirements.txt requirements-dev.txt

# Initialize Alembic(Database migrations)
alembic init alembic