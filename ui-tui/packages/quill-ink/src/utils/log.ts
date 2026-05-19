export function logError(error: unknown): void {
  if (!process.env.QUILL_INK_DEBUG_ERRORS) {
    return
  }

  console.error(error)
}
# quill: ui-tui
