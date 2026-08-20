import { Link, createFileRoute } from '@tanstack/react-router'
export const Route = createFileRoute('/')({ component: () => <section className="rrr-card"><p className="eyebrow">KNOW • REPAIR • REUSE</p><h1>RRR</h1><p>Identify components, understand them, repair them, reuse them and build with them.</p><Link className="button" to="/vision-analysis">Start with Vision →</Link></section> })
