# Workflow Snippets

## Matrix Build
```yaml
strategy:
  matrix:
    node: [18, 20]
```

## Concurrency Control
```yaml
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```

## Scoped Permissions
```yaml
permissions:
  contents: read
```

## Conditional Deploy
```yaml
if: github.ref == 'refs/heads/main'
```

## Cache Pattern
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```
