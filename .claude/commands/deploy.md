# Deploy Mode

You are now in **DEPLOYMENT MODE**. Prepare and execute deployments safely.

## Deployment Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Database migrations ready
- [ ] Environment variables configured
- [ ] Dependencies locked
- [ ] Changelog updated
- [ ] Rollback plan documented

### Deployment
- [ ] Notify team
- [ ] Deploy to staging first
- [ ] Verify staging
- [ ] Deploy to production
- [ ] Run smoke tests
- [ ] Monitor metrics

### Post-Deployment
- [ ] Verify functionality
- [ ] Check error rates
- [ ] Monitor performance
- [ ] Update documentation
- [ ] Notify stakeholders

## Deployment Targets

### Vercel/Netlify
```bash
# Preview deployment
vercel

# Production
vercel --prod
```

### Docker
```bash
# Build and push
docker build -t app:latest .
docker push registry/app:latest
```

### Kubernetes
```bash
kubectl apply -f k8s/
kubectl rollout status deployment/app
```

## Rollback Procedure

1. Identify the issue
2. Communicate to team
3. Execute rollback
4. Verify restoration
5. Investigate root cause

## Monitoring

- Check application logs
- Monitor error rates
- Watch response times
- Verify integrations
- Check database health

Deploy with confidence but always be ready to rollback.
