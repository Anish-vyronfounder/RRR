import { Link, createFileRoute } from '@tanstack/react-router'
export const Route = createFileRoute('/')({ component: () => <section className="rrr-card"><p className="eyebrow">KNOW • REPAIR • REUSE</p><h1>RRR</h1><p>Identify, repair, reuse and build with your components.</p><Link className="button" to="/vision-analysis">Start Vision →</Link></section> })
