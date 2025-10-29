install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running project..."
	python3 main.py

tests:
	@echo "Running tests..."
	pytest -v

build:
	@echo "Building py-fun package..."
	mkdir -p build/lib
	cp -r src build/lib/
	tar -cvf build/py-fun-SNAPSHOT-0.1.0.tar build/lib

clean:
	@echo "Cleaning build..."
	rm -rf build __pycache__








