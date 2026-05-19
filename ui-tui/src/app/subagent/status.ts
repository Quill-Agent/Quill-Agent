/**
 * Quill TUI — subagent status normalization (shared by gateway router + snapshot ledger).
 */
import type { SubagentStatus } from '../../types.js'

export const QUILL_SUBAGENT_STATUSES = new Set<SubagentStatus>([
  'completed',
  'error',
  'failed',
  'interrupted',
  'queued',
  'running',
  'timeout'
])

export function coerceSubagentStatus(status: unknown, fallback: SubagentStatus): SubagentStatus {
  if (typeof status !== 'string') {
    return fallback
  }

  const normalized = status.toLowerCase() as SubagentStatus

  return QUILL_SUBAGENT_STATUSES.has(normalized) ? normalized : fallback
}
