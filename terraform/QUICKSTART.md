# 🚀 Terraform Cloud - Quick Reference

## Your Configuration

**Terraform Cloud**:
- URL: https://app.terraform.io
- Email: dukuzejean09@gmail.com
- Username: dukx
- Organization: dukx-devops
- Workspace: devops-pipeline-azure

**Azure Infrastructure**:
- Region: East US
- Environment: dev
- Project: devopspipeline
- VM Size: Standard_B2s

**SSH Access**:
- Private Key: `~/.ssh/devops-pipeline`
- Public Key: `~/.ssh/devops-pipeline.pub`

## 📝 Step-by-Step Commands

### 1. Login to Terraform Cloud
```bash
cd /workspaces/devops-pipeline-kigaduha/terraform
terraform login
```
- When browser opens, sign in with: dukuzejean09@gmail.com
- Copy the token and paste it in terminal

### 2. Initialize Terraform
```bash
terraform init
```
Expected output: "Terraform Cloud has been successfully initialized!"

### 3. Format and Validate
```bash
terraform fmt
terraform validate
```

### 4. Plan Infrastructure
```bash
terraform plan
```
This shows what will be created without making changes.

### 5. Apply Infrastructure
```bash
terraform apply
```
Type `yes` when prompted to confirm.

### 6. View Outputs
```bash
terraform output                    # All outputs
terraform output vm_public_ip       # VM IP address
terraform output acr_login_server   # Container registry URL
terraform output ssh_command        # SSH connection command
```

### 7. Connect to VM
```bash
# After apply completes, get the IP
VM_IP=$(terraform output -raw vm_public_ip)

# SSH into the VM
ssh -i ~/.ssh/devops-pipeline azureuser@$VM_IP
```

## 🌐 Terraform Cloud Web UI

Access workspace: https://app.terraform.io/app/dukx-devops/workspaces/devops-pipeline-azure

Features:
- 📊 View runs and history
- 📁 Inspect state files
- 💰 Cost estimates
- 🔔 Notifications
- 👥 Team collaboration

## ⚙️ Required Variables in Terraform Cloud

Before running `terraform plan`, add these in workspace settings:

### Environment Variables (Workspace → Variables → Environment variables):
```
ARM_SUBSCRIPTION_ID = f6ade690-722f-42c6-8f3d-800249ece624 [Sensitive]
ARM_CLIENT_ID = e03ae4b2-0591-4a72-a14d-9cb2414be218 [Sensitive]
ARM_CLIENT_SECRET = Dru8Q~uwHgLQ*********************cgm [Sensitive]
ARM_TENANT_ID = fbb4c579-089a-42ec-bd9e-40b04d9c2cbd [Sensitive]
```

## 📦 Resources Created

When you run `terraform apply`, these Azure resources will be created:

| Resource | Name | Purpose |
|----------|------|---------|
| Resource Group | `devopspipeline-dev-rg` | Container for all resources |
| Virtual Network | `devopspipeline-dev-vnet` | Network (10.0.0.0/16) |
| Subnet | `vm-subnet` | VM subnet (10.0.1.0/24) |
| Network Security Group | `devopspipeline-dev-nsg` | Firewall rules |
| Public IP | `devopspipeline-dev-pip` | Static public IP |
| Network Interface | `devopspipeline-dev-nic` | VM network adapter |
| Virtual Machine | `devopspipeline-dev-vm` | Ubuntu 22.04 LTS |
| Container Registry | `devopspipelinedevacr` | Docker images |
| Storage Account | `devopspipelinedevsa*` | Application storage |

## 💰 Estimated Monthly Cost

- VM (Standard_B2s): ~$30
- Public IP: ~$3
- Storage: ~$1
- Container Registry: ~$5
- Network: ~$5
**Total: ~$44/month**

## 🔧 Common Commands

```bash
# Check Terraform version
terraform version

# Show current state
terraform show

# List resources in state
terraform state list

# Get resource details
terraform state show azurerm_linux_virtual_machine.main

# Refresh state
terraform refresh

# Destroy all resources
terraform destroy

# Apply specific target
terraform apply -target=azurerm_linux_virtual_machine.main

# View workspace
terraform workspace show
```

## 🐛 Troubleshooting

### Error: "No valid credential sources"
**Fix**: Add ARM_* environment variables in Terraform Cloud workspace

### Error: "Organization not found"
**Fix**: Create organization "dukx-devops" at https://app.terraform.io

### Error: "Workspace not found"
**Fix**: Create workspace "devops-pipeline-azure" in your organization

### Error: "Resource name already exists"
**Fix**: Resource names must be globally unique. Edit `project_name` variable

## 📚 Documentation Links

- Terraform Cloud: https://app.terraform.io
- Azure Provider: https://registry.terraform.io/providers/hashicorp/azurerm/latest
- Terraform Docs: https://developer.hashicorp.com/terraform
- Setup Guide: [TERRAFORM_CLOUD_SETUP.md](TERRAFORM_CLOUD_SETUP.md)

## ⚠️ Important Notes

1. **State is stored in Terraform Cloud** - not locally
2. **Variables are encrypted** in Terraform Cloud
3. **Never commit** terraform.tfvars to Git
4. **Review costs** in Azure Portal regularly
5. **Use terraform destroy** when done testing

## 🎯 Quick Start (Full Flow)

```bash
# 1. Navigate to terraform directory
cd /workspaces/devops-pipeline-kigaduha/terraform

# 2. Login to Terraform Cloud
terraform login

# 3. Initialize
terraform init

# 4. Plan (review changes)
terraform plan

# 5. Apply (create resources)
terraform apply

# 6. Get VM IP
terraform output vm_public_ip

# 7. SSH to VM
ssh -i ~/.ssh/devops-pipeline azureuser@<VM_IP>

# 8. When done, destroy
terraform destroy
```

---

**Created for**: dukuzejean09@gmail.com  
**Organization**: dukx-devops  
**Workspace**: devops-pipeline-azure  
**Region**: East US  
**Environment**: dev
