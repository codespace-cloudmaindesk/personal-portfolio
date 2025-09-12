# Declare all targets
.PHONY: all init 

all: init


init:
	@echo "Step 1 : Initializing Node.js project in src/backend..."
	@cd src/backend && npm init -y
	@echo "Backend Node.js project initialized successfully with default configuration."