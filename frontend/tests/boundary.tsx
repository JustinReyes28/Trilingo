// Deliberate browser-QA fault; this is not imported by the production application.
import { createRoot } from 'react-dom/client'
import { ErrorBoundary } from '../src/components'
import '../src/styles.css'
function IntentionalFailure():never { throw new Error('Intentional boundary QA failure') }
createRoot(document.getElementById('fixture-root')!).render(<ErrorBoundary><IntentionalFailure/></ErrorBoundary>)
