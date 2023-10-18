
# Code QA Strategies:

## Test Automation

#### Unit Tests:
test a single unit of code (module, class, function) in isolation

#### Integration Tests:
test multiple units together, e.g. code + database + APIs + other services (docker)

#### Acceptance Tests:
software works from the users point of view ("PO says OK")

#### Regression Tests:
after changes, the tests should still pass

## Other Strategies
- logging -> inspect logs 
- code reviews (humans)
- independent reviews (humans)
- end-to-end testing (manually or automated)
-  code analysis (mypy, black, pylint, ...)