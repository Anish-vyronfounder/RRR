import { Link, createFileRoute } from '@tanstack/react-router'
export const Route = createFileRoute('/identify')({ component: () => <section className="rrr-card"><h1>Identify</h1><p>Use camera or upload a component image.</p><Link className="button" to="/vision-analysis">Open Vision →</Link></section> })
