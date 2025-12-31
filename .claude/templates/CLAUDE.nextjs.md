# {PROJECT_NAME}

## Project Type
Next.js 14+ App Router Application

## Tech Stack
- **Framework**: Next.js 14+ with App Router
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS + shadcn/ui
- **Database**: {DATABASE} (Prisma ORM)
- **Auth**: {AUTH_PROVIDER}
- **State**: React Query / Zustand
- **Validation**: Zod
- **Testing**: Vitest + Playwright

## Project Structure
```
src/
├── app/                    # Next.js App Router
│   ├── (auth)/            # Auth route group
│   ├── (dashboard)/       # Dashboard route group
│   ├── api/               # API routes
│   └── layout.tsx         # Root layout
├── components/
│   ├── ui/                # shadcn/ui components
│   └── features/          # Feature components
├── lib/
│   ├── db.ts              # Database client
│   ├── auth.ts            # Auth utilities
│   └── utils.ts           # Helper functions
├── hooks/                  # Custom React hooks
├── types/                  # TypeScript types
└── styles/                # Global styles
```

## Key Commands
```bash
pnpm dev          # Start dev server
pnpm build        # Production build
pnpm lint         # Lint code
pnpm test         # Run tests
pnpm db:push      # Push DB schema
pnpm db:studio    # Open Prisma Studio
```

## Architecture Decisions

### Server vs Client Components
- **Server (default)**: Data fetching, DB access, secrets
- **Client ('use client')**: Interactivity, hooks, browser APIs

### Data Fetching
- Server Components: Direct DB/API calls
- Client Components: React Query with server actions

### Styling
- Use Tailwind CSS utilities
- Component variants with `class-variance-authority`
- Use `cn()` for conditional classes

## Conventions

### Naming
- Components: PascalCase (`UserProfile.tsx`)
- Hooks: camelCase with `use` prefix (`useAuth.ts`)
- Utils: camelCase (`formatDate.ts`)
- Routes: kebab-case (`/user-settings`)

### Code Style
- Prefer named exports for components
- Co-locate related files
- Extract complex logic to hooks
- Use server actions for mutations

### Error Handling
- Use error.tsx for route error boundaries
- Implement loading.tsx for suspense
- Use not-found.tsx for 404s

## API Routes
```typescript
// Route Handler pattern
export async function GET(request: Request) {
  // Handle GET
}

export async function POST(request: Request) {
  // Handle POST
}
```

## Environment Variables
Required in `.env.local`:
```
DATABASE_URL=
NEXTAUTH_SECRET=
NEXTAUTH_URL=
```

## Performance
- Use React.lazy for code splitting
- Implement proper caching strategies
- Use Image component for images
- Prefer static generation when possible

## Security
- Validate all inputs with Zod
- Use parameterized queries (Prisma handles this)
- Implement proper CORS
- Use CSP headers
