# Terraform Azure Infrastructure Setup Guide

This guide will help you deploy the infrastructure to Azure using Terraform.

## Prerequisites

- Azure CLI installed (`az --version`)
- Terraform >= 1.5.0 installed (`terraform version`)
- SSH key pair for VM access
- Azure subscription

## Step 1: Azure Service Principal (Already Created)

You already have the service principal credentials:

```bash
Subscription ID: f6ade690-722f-42c6-8f3d-800249ece624
App ID (client_id): e03ae4b2-0591-4a72-a14d-9cb2414be218
Password (client_secret): Dru8Q~uwHgLQ*********************cgm  # Use your actual secret
Tenant ID: fbb4c579-089a-42ec-bd9e-40b04d9c2cbd
```

## Step 2: Generate SSH Key Pair

```bash
# Generate SSH key
ssh-keygen -t rsa -b 4096 -f ~/.ssh/devops-pipeline -N ""

# View your public key
cat ~/.ssh/devops-pipeline.pub
```

## Step 3: Create terraform.tfvars

```bash
cd terraform

# Copy the example file
cp terraform.tfvars.example terraform.tfvars
```

Edit `terraform.tfvars` with your actual values:

```hcl
# Azure Service Principal Credentials
subscription_id = "f6ade690-722f-42c6-8f3d-800249ece624"
client_id       = "e03ae4b2-0591-4a72-a14d-9cb2414be218"
client_secret   = "Dru8Q~uwHgLQ*********************cgm"  # Use your actual secret
tenant_id       = "fbb4c579-089a-42ec-bd9e-40b04d9c2cbd"

# Infrastructure Configuration
project_name = "devopspipeline"
environment  = "dev"
location     = "East US"

# VM Configuration
vm_size        = "Standard_B2s"
admin_username = "azureuser"

# SSH Public Key (paste output from: cat ~/.ssh/devops-pipeline.pub)
ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDxxx..."

tags = {
  Owner      = "YourName"
  CostCenter = "Engineering"
}
```

## Step 4: Initialize Terraform

```bash
cd terraform

# Initialize Terraform
terraform init

# This will:
# - Download Azure provider
# - Set up the workspace
```

## Step 5: Validate and Plan

```bash
# Format your code
terraform fmt

# Validate configuration
terraform validate

# Create an execution plan
terraform plan

# Review the plan carefully
```

## Step 6: Apply Infrastructure

```bash
# Apply the configuration
terraform apply

# Type 'yes' when prompted
```

Expected resources to be created:
- 1 Resource Group
- 1 Virtual Network with 1 Subnet
- 1 Network Security Group
- 1 Public IP
- 1 Network Interface
- 1 Linux VM (Ubuntu 22.04)
- 1 Container Registry (ACR)
- 1 Storage Account
- Role assignments

## Step 7: View Outputs

```bash
# View all outputs
terraform output

# View specific output
terraform output vm_public_ip
terraform output acr_login_server

# Save outputs to file
terraform output -json > ../terraform-outputs.json
```

## Step 8: Connect to Your VM

```bash
# Get the SSH command
terraform output ssh_command

# Or manually
ssh azureuser@<VM_PUBLIC_IP> -i ~/.ssh/devops-pipeline
```

## Step 9: Set Up GitHub Secrets

For GitHub Actions to work, add these secrets to your repository:

Go to: **Settings → Secrets and variables → Actions → New repository secret**

Add the following secrets:

| Secret Name | Value | Description |
|------------|-------|-------------|
| `AZURE_SUBSCRIPTION_ID` | `f6ade690-722f-42c6-8f3d-800249ece624` | Azure Subscription ID |
| `AZURE_CLIENT_ID` | `e03ae4b2-0591-4a72-a14d-9cb2414be218` | Service Principal App ID |
| `AZURE_CLIENT_SECRET` | `Dru8Q~uwHgLQ*********************cgm` | Service Principal Password |
| `AZURE_TENANT_ID` | `fbb4c579-089a-42ec-bd9e-40b04d9c2cbd` | Azure Tenant ID |
| `SSH_PRIVATE_KEY` | Content of `~/.ssh/devops-pipeline` | Private SSH key for VM access |
| `SSH_PUBLIC_KEY` | Content of `~/.ssh/devops-pipeline.pub` | Public SSH key for Terraform |

```bash
# Copy private key (for GitHub Actions to SSH into VM)
cat ~/.ssh/devops-pipeline

# Copy public key (for Terraform to configure VM)
cat ~/.ssh/devops-pipeline.pub
```

## Terraform Commands Reference

```bash
# View current state
terraform show

# List resources
terraform state list

# View specific resource
terraform state show azurerm_linux_virtual_machine.main

# Refresh state
terraform refresh

# Destroy specific resource
terraform destroy -target=azurerm_storage_account.main

# Destroy all infrastructure
terraform destroy
```

## Troubleshooting

### Issue: Authentication Failed

```bash
# Login to Azure CLI
az login

# Set subscription
az account set --subscription f6ade690-722f-42c6-8f3d-800249ece624

# Verify
az account show
```

### Issue: Resource Name Conflicts

Container Registry names must be globally unique. If you get a name conflict:

1. Edit `variables.tf`
2. Change `project_name` to something unique
3. Run `terraform plan` again

### Issue: Quota Exceeded

```bash
# Check your quotas
az vm list-usage --location "East US" --output table

# Request quota increase if needed
```

## Cost Estimate

Approximate monthly costs for `dev` environment:

- VM (Standard_B2s): ~$30/month
- Public IP (Static): ~$3/month
- Storage Account: ~$1/month
- Container Registry (Basic): ~$5/month
- Network bandwidth: ~$5/month

**Total: ~$44/month**

## Next Steps

1. ✅ SSH into your VM
2. ✅ Install Docker on VM
3. ✅ Configure ACR credentials
4. ✅ Deploy your application
5. ✅ Set up monitoring

## Clean Up

When you're done testing:

```bash
# Destroy all resources
terraform destroy

# Confirm by typing 'yes'
```

## Important Notes

- **Never commit** `terraform.tfvars` or `terraform.tfstate` to Git
- **Secure your credentials** - service principal password is sensitive
- **Review costs** regularly in Azure Portal
- **Enable Azure Cost Alerts** for budget management

## Support

If you encounter issues:

1. Check Terraform docs: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
2. Check Azure docs: https://docs.microsoft.com/en-us/azure/
3. Review the error message carefully
4. Check Azure Portal for resource status

---

**Last Updated:** November 2025  
**Terraform Version:** >= 1.5.0  
**Azure Provider Version:** ~> 3.0
