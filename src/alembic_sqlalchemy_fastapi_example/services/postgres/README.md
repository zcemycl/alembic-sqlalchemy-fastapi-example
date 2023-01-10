```
SELECT * FROM pg_stat_activity WHERE state = 'active';
SELECT pg_cancel_backend(<pid of the process>)
SELECT pg_terminate_backend(<pid of the process>)
```
