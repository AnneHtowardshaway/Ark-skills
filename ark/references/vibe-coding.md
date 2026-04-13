# Vibe Coding Standard

Use this as the default code style and delivery discipline.

## Formatting

- Indentation: 2 spaces
- Max line width: 80
- One blank line between functions
- Two blank lines between classes
- Keep each function or class under 60 lines when practical

Split large logic into smaller units instead of letting files become
dense and opaque.

## Naming

- Variable / function: `camelCase`
- Class / component: `PascalCase`
- Constant: `UPPER_SNAKE_CASE`

## Error Handling

- Use `try...catch` for synchronous code when failure paths exist.
- Async code must use `await` + `try...catch` or explicit `.catch()`.
- Never silently swallow errors without intent and logging.

## Comments

- Do not comment obvious implementation mechanics.
- Comment intent, tradeoff, and business reason.
- Mark complex algorithms or hacks with `@note`.

Good comment:

```ts
// Keep optimistic rows local until server ack to avoid cross-tab
// consistency drift during bulk edits.
```

Bad comment:

```ts
// Loop through the array and push items.
```

## Delivery Mindset

- Prefer readable code over clever code.
- Prefer stable code over fast-but-fragile code.
- Prefer explicit boundaries over hidden magic.
- Prefer changes that are easy to review and rollback.
