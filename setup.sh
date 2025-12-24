#!/bin/bash

# PROJECT_NAME="portfolio-e2e"

# echo "🚀 Initializing $PROJECT_NAME (End-to-End Architecture)..."

# mkdir -p $PROJECT_NAME
# cd $PROJECT_NAME || exit 1

# ========================
# ROOT FILES
# ========================
touch README.md .gitignore docker-compose.yml

# ========================
# BACKEND (ASP.NET Core)
# ========================

mkdir -p Backend/{API,Application,Domain,Infrastructure,Tests}

# --- API Layer ---
mkdir -p Backend/API/{Controllers,Middleware,Filters}
touch Backend/API/Controllers/{AuthController.cs,ProjectsController.cs,SkillsController.cs,ContactController.cs,AdminController.cs}
touch Backend/API/Middleware/{JwtMiddleware.cs,RateLimitingMiddleware.cs}
touch Backend/API/Filters/GlobalExceptionFilter.cs
touch Backend/API/{Program.cs,appsettings.json}

# --- Application Layer ---
mkdir -p Backend/Application/{Interfaces,Services,DTOs,Validators}

touch Backend/Application/Interfaces/{IAuthService.cs,IProjectService.cs,ISkillService.cs,IAdminService.cs}
touch Backend/Application/Services/{AuthService.cs,ProjectService.cs,SkillService.cs,AdminService.cs}

mkdir -p Backend/Application/DTOs/Auth
touch Backend/Application/DTOs/Auth/{LoginRequestDto.cs,RegisterRequestDto.cs,AuthResponseDto.cs}
touch Backend/Application/DTOs/{ProjectDto.cs,SkillDto.cs,ContactMessageDto.cs}

touch Backend/Application/Validators/ProjectValidator.cs

# --- Domain Layer ---
mkdir -p Backend/Domain/{Entities,Enums,Common}
touch Backend/Domain/Entities/{User.cs,Project.cs,Skill.cs,ContactMessage.cs,RefreshToken.cs}
touch Backend/Domain/Enums/UserRole.cs
touch Backend/Domain/Common/BaseEntity.cs

# --- Infrastructure Layer ---
mkdir -p Backend/Infrastructure/{Data,Repositories,Auth,Caching,Configuration}

touch Backend/Infrastructure/Data/PortfolioDbContext.cs
mkdir -p Backend/Infrastructure/Data/Migrations

touch Backend/Infrastructure/Repositories/{UserRepository.cs,ProjectRepository.cs,SkillRepository.cs}
touch Backend/Infrastructure/Auth/{JwtTokenGenerator.cs,OAuthProviderService.cs}
touch Backend/Infrastructure/Caching/CacheService.cs
touch Backend/Infrastructure/Configuration/DependencyInjection.cs

# --- Tests ---
mkdir -p Backend/Tests/{UnitTests,IntegrationTests}

touch Backend/Portfolio.sln

# ========================
# FRONTEND (React + TS)
# ========================

mkdir -p Frontend/{public,src}

touch Frontend/public/index.html

mkdir -p Frontend/src/{app,auth,api,components,pages,hooks,styles,types,utils}

# --- App Core ---
touch Frontend/src/app/{App.tsx,routes.tsx,ProtectedRoute.tsx}

# --- Auth ---
touch Frontend/src/auth/{AuthContext.tsx,useAuth.ts,Login.tsx,OAuthCallback.tsx}

# --- API Clients ---
touch Frontend/src/api/{httpClient.ts,authApi.ts,projectApi.ts,skillApi.ts}

# --- Components ---
mkdir -p Frontend/src/components/{layout,ui}
touch Frontend/src/components/layout/{Navbar.tsx,Footer.tsx}
touch Frontend/src/components/ui/{Button.tsx,Modal.tsx}
touch Frontend/src/components/ProjectCard.tsx

# --- Pages ---
mkdir -p Frontend/src/pages/{public,admin}
touch Frontend/src/pages/public/{Home.tsx,Projects.tsx,About.tsx,Contact.tsx}
touch Frontend/src/pages/admin/{Dashboard.tsx,ProjectsAdmin.tsx,SkillsAdmin.tsx,MessagesAdmin.tsx}

# --- Hooks ---
touch Frontend/src/hooks/{useFetch.ts,usePagination.ts}

# --- Styles ---
touch Frontend/src/styles/{global.css,admin.css}

# --- Types ---
touch Frontend/src/types/{User.ts,Project.ts,Skill.ts}

# --- Utils ---
touch Frontend/src/utils/{tokenStorage.ts,constants.ts}

# --- Entry ---
touch Frontend/src/{main.tsx}

# --- Config ---
touch Frontend/{package.json,tsconfig.json,vite.config.ts}

echo "✅ End-to-End project structure created successfully!"
echo "📦 Next steps:"
echo "   1. Initialize Git"
echo "   2. Create ASP.NET & React apps inside this structure"
echo "   3. Start implementing features incrementally"
