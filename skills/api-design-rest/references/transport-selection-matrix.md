# API Transport Selection Matrix

Use this matrix to decide between synchronous, asynchronous, and real-time API styles for both internal and external consumers.

## Step 1: Classify Interaction
- `sync`: caller needs immediate result to continue user or workflow path.
- `async`: caller can accept deferred completion and eventual consistency.
- `streaming`: server continuously pushes updates in one direction.
- `bidirectional_realtime`: both sides exchange near-real-time messages over a stateful channel.

## Step 2: Evaluate Transport Candidates

| Transport | Best fit | Typical audience | Key risks | Mandatory controls |
| --- | --- | --- | --- | --- |
| `rest` | CRUD, deterministic request-response, cache-aware read paths | both | over-fetching/under-fetching, endpoint sprawl | idempotency, status/error contract, rate limits (public) |
| `graphql` | client-specific aggregation, evolving read shapes | internal/both | N+1, expensive queries, schema drift | query complexity/depth limits, resolver batching, authz per field |
| `grpc` | low-latency service-to-service contracts, strongly typed RPC | internal | protocol gateway complexity for external clients | schema compatibility checks, retry semantics, deadline budgets |
| `websocket` | duplex real-time interactions (collab, trading, game-state) | both | connection fan-out, lifecycle leakage, message ordering | heartbeat, reconnect strategy, session limits, backpressure |
| `sse` | server-to-client live feed with simple client stack | external/both | reconnection storms, one-way semantics limitations | event id/replay window, reconnect policy, stream rate controls |
| `queue` | decoupled async workflows and burst buffering | internal/both | duplicate delivery, poison messages, lag growth | idempotent consumer, DLQ policy, visibility timeout, lag alerts |

## Step 3: Rejection Checklist
- Why not the top two alternatives?
- Which failure mode is hardest with the selected transport?
- How are ordering, deduplication, and replay handled?
- How does this decision differ for internal vs external consumers?

## Step 4: Record Decision
Include all in `decision_context`:
- `api_audience`
- `interaction_mode`
- `primary_transport`
- `selection_rationale`
- `alternatives_considered`
