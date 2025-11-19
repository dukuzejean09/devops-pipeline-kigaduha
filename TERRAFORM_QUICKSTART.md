# Quick Start: Azure Terraform Deployment

## 🚀 Quick Commands

```bash
# 1. Generate SSH Key
ssh-keygen -t rsa -b 4096 -f ~/.ssh/devops-pipeline -N ""

# 2. Navigate to terraform directory
cd terraform

# 3. Create your terraform.tfvars file
cp terraform.tfvars.example terraform.tfvars

# Edit terraform.tfvars with your credentials (use the values provided below)

# 4. Initialize Terraform
terraform init

# 5. Plan infrastructure
terraform plan

# 6. Apply infrastructure
terraform apply

# 7. Get outputs
terraform output
terraform output vm_public_ip
```

## 📋 Your Azure Credentials

Use these values in your `terraform.tfvars`:

```hcl
subscription_id = "f6ade690-722f-42c6-8f3d-800249ece624"
client_id       = "e03ae4b2-0591-4a72-a14d-9cb2414be218"
client_secret   = "Dru8Q~uwHgLQ*********************cgm"  # Use your actual secret
tenant_id       = "fbb4c579-089a-42ec-bd9e-40b04d9c2cbd"

# Add your SSH public key (from: cat ~/.ssh/devops-pipeline.pub)
ssh_public_key = "paste_your_public_key_here"
```

## 🔐 GitHub Secrets to Add

Go to: **Repository Settings → Secrets → Actions → New secret**

| Secret Name | Value |
|------------|-------|
| `AZURE_SUBSCRIPTION_ID` | `f6ade690-722f-42c6-8f3d-800249ece624` |
| `AZURE_CLIENT_ID` | `e03ae4b2-0591-4a72-a14d-9cb2414be218` |
| `AZURE_CLIENT_SECRET` | `Dru8Q~uwHgLQ*********************cgm` |
| `AZURE_TENANT_ID` | `fbb4c579-089a-42ec-bd9e-40b04d9c2cbd` |
| `SSH_PUBLIC_KEY` | Content of `~/.ssh/devops-pipeline.pub` |
| `SSH_PRIVATE_KEY` | Content of `~/.ssh/devops-pipeline` |

## 📦 What Gets Created

- **Resource Group**: `devopspipeline-dev-rg`
- **VM**: Ubuntu 22.04 LTS (Standard_B2s)
- **Public IP**: Static IP for VM access
- **VNet & Subnet**: 10.0.0.0/16 network
- **NSG**: Firewall rules (SSH, HTTP, HTTPS, port 5000)
- **ACR**: Container registry for Docker images
- **Storage Account**: For application data
- **SSH Key**: For secure VM access

## 💰 Estimated Cost

~$44/month for dev environment

## 🔗 Quick Links

- **Full Setup Guide**: [terraform/AZURE_SETUP.md](terraform/AZURE_SETUP.md)
- **Azure Portal**: https://portal.azure.com
- **Terraform Docs**: https://registry.terraform.io/providers/hashicorp/azurerm/latest

## ⚠️ Important Security Notes

1. **Never commit** `terraform.tfvars` to Git
2. **Add to .gitignore**:
   ```
   terraform/terraform.tfvars
   terraform/.terraform/
   terraform/*.tfstate*
   ```
3. **Rotate credentials** periodically
4. **Review costs** in Azure Portal regularly

## 🧹 Clean Up

When done testing:
```bash
terraform destroy
```

Type `yes` when prompted to confirm deletion.
