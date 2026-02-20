# API Threshold Derivation Framework

Do not copy fixed numbers between projects. Define threshold *types* and document derivation logic from business and system constraints.

## Required Threshold Types
- Latency target (for example p95, p99)
- Availability target and error budget
- Timeout budget by hop (client, edge, service, downstream)
- Throughput and capacity headroom
- Payload size limits
- Concurrency limits (requests, sessions, streams, workers)
- Retry/backoff budget
- Delivery semantics and duplicate handling policy

## Derivation Method
1. Identify business critical path and user/system impact of delay or failure.
2. Map critical path to end-to-end SLO and split budget across components.
3. Use historical peak and growth assumptions to size capacity headroom.
4. Set timeout and retry policies from dependency behavior and idempotency.
5. Validate proposed thresholds with load/failure tests.
6. Assign owner and re-evaluation trigger for every threshold.

## Example Re-evaluation Triggers
- New consumer type or region added
- 95th percentile utilization exceeds planned headroom
- Error-budget burn accelerates beyond policy
- Transport change (for example REST to WebSocket, sync to queue)
- Major data shape or payload growth

## Evidence to Keep
- Source SLO/SLI references
- Capacity model or benchmark links
- Failure injection or load-test results
- Approval record and review date
