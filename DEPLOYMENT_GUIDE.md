# 🚀 Complete DevOps Pipeline - Final Setup Guide

## ✅ What's Already Done

The entire DevOps pipeline infrastructure is now complete and committed to the repository:

### Infrastructure & CI/CD

- ✅ Terraform configuration for Azure infrastructure
- ✅ GitHub Actions workflows for CI/CD
- ✅ Docker containerization for backend and frontend
- ✅ Ansible configuration management
- ✅ Security hardening configurations

### What's Working

- ✅ Automated linting (Python: ruff, JavaScript: ESLint)
- ✅ Automated testing (backend: pytest, frontend: Jest)
- ✅ Docker image building and pushing to GHCR
- ✅ Terraform Cloud integration
- ✅ Azure Container Registry setup

## 🔧 Required GitHub Secrets

You need to add these secrets to your GitHub repository at:
**https://github.com/Pelino-Courses/devops-pipeline-kigaduha/settings/secrets/actions**

### Azure Credentials

```
AZURE_CLIENT_ID: <your-azure-client-id>
AZURE_CLIENT_SECRET: <your-azure-client-secret>
AZURE_TENANT_ID: <your-azure-tenant-id>
AZURE_SUBSCRIPTION_ID: <your-azure-subscription-id>
```

### Azure Credentials JSON (for Azure Login action)

```json
{
  "clientId": "<your-azure-client-id>",
  "clientSecret": "<your-azure-client-secret>",
  "subscriptionId": "<your-azure-subscription-id>",
  "tenantId": "<your-azure-tenant-id>"
}
```

Save this as `AZURE_CREDENTIALS`

### Application Secrets

```
DB_PASSWORD: <create-a-strong-password>
APP_SECRET_KEY: <generate-random-32-char-string>
```

To generate a secure secret key:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Terraform Cloud (already configured)

```
TF_API_TOKEN: <your-token>
TF_CLOUD_ORGANIZATION: <your-org>
```

### Optional (if using Codecov)

```
CODECOV_TOKEN: <your-token>
```

## 📋 Testing Ansible Locally (Optional)

If you want to test Ansible deployment manually:

1. **Install dependencies:**

   ```bash
   cd ansible
   pip install -r requirements.txt
   ansible-galaxy collection install azure.azcollection community.docker
   pip install azure-cli-core azure-mgmt-compute azure-mgmt-network
   ```

2. **Set environment variables:**

   ```bash
   export ARM_CLIENT_ID="<your-azure-client-id>"
   export ARM_CLIENT_SECRET="<your-azure-client-secret>"
   export ARM_TENANT_ID="<your-azure-tenant-id>"
   export ARM_SUBSCRIPTION_ID="<your-azure-subscription-id>"

   # Get these from Terraform outputs after deployment
   export ACR_LOGIN_SERVER="<your-acr>.azurecr.io"
   export IMAGE_TAG="main"
   export DB_PASSWORD="your-strong-password"
   export SECRET_KEY="your-secret-key"
   ```

3. **Test and deploy:**

   ```bash
   # Test connectivity
   ansible all -m ping -i inventory/azure_rm.yml

   # Dry run
   ansible-playbook playbooks/setup-server.yml -i inventory/azure_rm.yml --check

   # Real deployment
   ansible-playbook playbooks/setup-server.yml -i inventory/azure_rm.yml -vv
   ```

## 🔄 Automated Deployment Flow

Once GitHub secrets are configured, every push to `main` triggers:

1. **Build & Test Phase**

   - Backend linting with ruff
   - Frontend linting with ESLint
   - Backend tests with pytest
   - Frontend tests with Jest
   - Security scanning with Trivy

2. **Docker Build Phase**

   - Build backend Docker image
   - Build frontend Docker image
   - Push images to GitHub Container Registry (GHCR)

3. **Infrastructure Phase (if changed)**

   - Terraform provisions/updates Azure infrastructure
   - Creates: VM, Container Registry, Networking, Security Groups

4. **Deployment Phase**
   - Ansible connects to Azure VM
   - Installs Docker and security tools
   - Configures firewall rules
   - Deploys application with Docker Compose
   - Starts: PostgreSQL, Flask backend, React frontend

## 🌐 Accessing Your Application

After successful deployment:

- **Frontend:** `http://<VM_PUBLIC_IP>`
- **Backend API:** `http://<VM_PUBLIC_IP>:5000`
- **Health Check:** `http://<VM_PUBLIC_IP>:5000/health`

The VM public IP is displayed in the GitHub Actions log after deployment.

## 📁 Project Structure

```
devops-pipeline-kigaduha/
├── .github/workflows/
│   ├── ci-cd.yml           # Main CI/CD pipeline
│   └── ci-pipeline.yml     # Additional CI checks
├── ansible/
│   ├── playbooks/
│   │   └── setup-server.yml
│   ├── roles/
│   │   ├── docker/
│   │   ├── security/
│   │   └── app-deploy/
│   ├── inventory/
│   │   └── azure_rm.yml
│   ├── ansible.cfg
│   └── README.md
├── backend/
│   ├── src/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   └── Dockerfile
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── backend.tf
└── docker-compose.yml
```

## 🎯 Next Steps

1. **Add GitHub Secrets** (see above)
2. **Trigger Deployment:**
   ```bash
   git commit --allow-empty -m "Trigger deployment"
   git push origin main
   ```
3. **Monitor Workflow:**

   - Go to: https://github.com/Pelino-Courses/devops-pipeline-kigaduha/actions
   - Watch the CI/CD Pipeline workflow
   - Check for any errors

4. **Verify Deployment:**
   - Get VM public IP from workflow logs
   - Open browser: `http://<VM_IP>`
   - Test the application

## 🐛 Troubleshooting

### Workflow fails at Terraform

- Check Azure credentials are correct
- Verify service principal has Contributor role
- Check Terraform Cloud token is valid

### Workflow fails at Ansible

- Verify VM is accessible (check NSG rules)
- Check SSH key was generated properly
- Verify DB_PASSWORD and APP_SECRET_KEY secrets exist

### Application not accessible

- SSH into VM: `ssh azureuser@<VM_IP>`
- Check containers: `docker ps`
- View logs: `docker compose -f /opt/devops-app/docker-compose.yml logs`
- Check firewall: `sudo ufw status`

### Containers fail to start

- Check ACR credentials
- Verify image tags exist in registry
- Check environment variables in .env file

## 📚 Documentation

- **Ansible:** See `ansible/README.md` for detailed Ansible documentation
- **Terraform:** See `terraform/` for infrastructure details
- **Backend:** See `backend/` for Flask API documentation
- **Frontend:** See `frontend/` for React app documentation

## 🎉 Success Criteria

Your pipeline is working correctly when:

- ✅ All workflow jobs pass (green checkmarks)
- ✅ Docker images are pushed to GHCR
- ✅ Terraform creates infrastructure in Azure
- ✅ Ansible successfully deploys the application
- ✅ Frontend is accessible via browser
- ✅ Backend API responds to health checks
- ✅ Database is running and accessible

---

**Created:** November 20, 2025
**Team:** DevOps Pipeline Project
**Status:** ✅ Complete and Ready for Deployment
