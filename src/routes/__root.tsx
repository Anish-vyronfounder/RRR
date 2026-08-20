import { Outlet, createRootRoute } from '@tanstack/react-router'
import '../../styles.css'

export const Route = createRootRoute({
  component: () => (
    <div className="rrr-app">
      <header className="rrr-header"><strong>RRR</strong><nav><a href="/">Home</a><a href="/vision-analysis">Identify</a><a href="/repair">Repair</a><a href="/reuse">Reuse</a><a href="/build">Build</a></nav></header>
      <main><Outlet /></main>
    </div>
  ),
})
