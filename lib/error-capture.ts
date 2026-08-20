let lastCapturedError: unknown = null
export function consumeLastCapturedError(): unknown { const value = lastCapturedError; lastCapturedError = null; return value }
export function captureError(error: unknown): void { lastCapturedError = error }
