cd frontend

# Create Vite + React + TypeScript project
npm create vite@latest . -- --template react-ts

# Install dependencies
npm install

# Install additional packages
npm install react-router-dom @tanstack/react-query axios zustand framer-motion lucide-react

# Install Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Install dev dependencies
npm install -D @testing-library/react @testing-library/jest-dom @testing-library/user-event vitest
npm install -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
npm install -D prettier eslint-config-prettier eslint-plugin-react-hooks
npm install -D husky lint-staged

# Initialize Husky
npx husky-init && npm install