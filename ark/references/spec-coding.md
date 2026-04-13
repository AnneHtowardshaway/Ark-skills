# Spec Coding

Apply this before any meaningful implementation task.

## Core Rule

Read the project first.

Then produce a spec requirement sheet before coding.

The sheet must explicitly separate:

- `confirmed`
- `required`
- `assumptions`

## Hard Gate

Do not code yet if any of these is unclear:

- goal
- scope
- interface
- state
- exceptions
- acceptance

## Ask Only For What Is Missing

After reading the project, ask only for information that cannot be
reliably inferred from:

- existing code
- current behavior
- project structure
- nearby conventions
- docs already present in the repo

Avoid template-style questioning.

## Typical Missing Inputs After Reading A Project

### UI and page work

- exact target page
- expected interaction
- design draft or screenshot
- empty / loading / error state
- compatibility requirement

### API and data flow work

- request and response schema
- error code semantics
- cache / retry / idempotency rule
- backward compatibility requirement

### State changes

- source of truth
- optimistic update allowance
- rollback behavior
- cross-page or cross-module impact

### Security and permission work

- role model
- frontend-only display or backend hard enforcement
- audit or logging requirement

### AI and agent work

- side effects of tool calls
- human-in-the-loop requirement
- schema for structured output
- timeout / retry / interrupt behavior

### Engineering and release work

- affected environments
- CI / build impact
- feature flag requirement
- rollback plan

## Recommended Output

```md
## Spec Requirement Sheet

### 1. Goal
...

### 2. Current Implementation
...

### 3. Impact Scope
...

### 4. Confirmed
...

### 5. Required
...

### 6. Assumptions
...

### 7. Acceptance Criteria
...

### 8. Risk And Rollback
...
```
