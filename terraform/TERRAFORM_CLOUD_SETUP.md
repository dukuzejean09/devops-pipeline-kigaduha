# Terraform Cloud Setup Guide

## Step 1: Create Terraform Cloud Account

1. Go to https://app.terraform.io/signup/account
2. Sign up with your email: **dukuzejean09@gmail.com**
3. Choose username: **dukx**
4. Verify your email

## Step 2: Create Organization

1. After login, create a new organization
2. Organization name: **dukx-devops**
3. Email: **dukuzejean09@gmail.com**

## Step 3: Create Workspace

1. Click "New Workspace"
2. Choose "CLI-driven workflow"
3. Workspace name: **devops-pipeline-azure**
4. Click "Create workspace"

## Step 4: Get API Token

1. Click your profile icon (top right)
2. Go to "User Settings"
3. Click "Tokens" in the left menu
4. Click "Create an API token"
5. Description: "Terraform CLI"
6. Copy the token (you'll need it next)

## Step 5: Login from CLI

```bash
cd /workspaces/devops-pipeline-kigaduha/terraform

# Login to Terraform Cloud
terraform login

# When prompted:
# - Enter "yes" to proceed
# - Paste your API token when asked
# - Press Enter
```

## Step 6: Set Workspace Variables

In Terraform Cloud workspace (**devops-pipeline-azure**), add these variables:

### Environment Variables (Sensitive):
Go to: Workspace → Variables → Environment Variables

| Variable | Value | Sensitive | Description |
|----------|-------|-----------|-------------|
| `ARM_SUBSCRIPTION_ID` | `f6ade690-722f-42c6-8f3d-800249ece624` | ✅ Yes | Azure Subscription ID |
| `ARM_CLIENT_ID` | `e03ae4b2-0591-4a72-a14d-9cb2414be218` | ✅ Yes | Service Principal App ID |
| `ARM_CLIENT_SECRET` | `Dru8Q~uwHgLQ*********************cgm` | ✅ Yes | Service Principal Password |
| `ARM_TENANT_ID` | `fbb4c579-089a-42ec-bd9e-40b04d9c2cbd` | ✅ Yes | Azure Tenant ID |

### Terraform Variables:
Go to: Workspace → Variables → Terraform Variables

| Variable | Value | HCL | Sensitive |
|----------|-------|-----|-----------|
| `subscription_id` | `f6ade690-722f-42c6-8f3d-800249ece624` | No | ✅ Yes |
| `client_id` | `e03ae4b2-0591-4a72-a14d-9cb2414be218` | No | ✅ Yes |
| `client_secret` | `Dru8Q~uwHgLQ*********************cgm` | No | ✅ Yes |
| `tenant_id` | `fbb4c579-089a-42ec-bd9e-40b04d9c2cbd` | No | ✅ Yes |
| `project_name` | `devopspipeline` | No | No |
| `environment` | `dev` | No | No |
| `location` | `East US` | No | No |
| `vm_size` | `Standard_B2s` | No | No |
| `admin_username` | `azureuser` | No | No |
| `ssh_public_key` | `ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ...` | No | No |

**Note**: For `ssh_public_key`, use the full content from:
```bash
cat ~/.ssh/devops-pipeline.pub
```

## Step 7: Initialize Terraform

```bash
cd /workspaces/devops-pipeline-kigaduha/terraform

# Initialize with Terraform Cloud
terraform init

# You should see: "Terraform Cloud has been successfully initialized!"
```

## Step 8: Run Terraform Plan

```bash
# Create and review execution plan
terraform plan

# This will run in Terraform Cloud
# You can watch progress at: https://app.terraform.io/app/dukx-devops/workspaces/devops-pipeline-azure
```

## Step 9: Apply Infrastructure

```bash
# Apply the changes
terraform apply

# Type 'yes' when prompted
# Or use: terraform apply -auto-approve
```

## Step 10: View Outputs

```bash
# After successful apply, view outputs
terraform output

# Get specific output
terraform output vm_public_ip
terraform output acr_login_server

# Save to file
terraform output -json > ../terraform-outputs.json
```

## Terraform Cloud Web UI

Access your workspace at:
```
https://app.terraform.io/app/dukx-devops/workspaces/devops-pipeline-azure
```

Here you can:
- View run history
- See state file
- Monitor resource changes
- Review cost estimates
- Set up notifications

## Quick Commands

```bash
# View workspace
terraform workspace show

# View state
terraform show

# Refresh state
terraform refresh

# Destroy resources
terraform destroy
```

## Troubleshooting

### Issue: "No valid credential sources found"

**Solution**: Add environment variables in Terraform Cloud workspace settings:
- `ARM_SUBSCRIPTION_ID`
- `ARM_CLIENT_ID`
- `ARM_CLIENT_SECRET`
- `ARM_TENANT_ID`

### Issue: "Error locking state"

**Solution**: Terraform Cloud handles state locking automatically. If you see this error, wait a few minutes and try again.

### Issue: "Organization not found"

**Solution**: Make sure you created the organization "dukx-devops" in Terraform Cloud.

## Benefits of Terraform Cloud

✅ Remote state management (automatic)
✅ State locking (automatic)
✅ Collaboration with team members
✅ Run history and audit logs
✅ Cost estimation before apply
✅ Policy as code (Sentinel)
✅ Private module registry
✅ VCS integration (GitHub)

## Configuration Summary

- **Organization**: dukx-devops
- **Workspace**: devops-pipeline-azure
- **Email**: dukuzejean09@gmail.com
- **Username**: dukx
- **Region**: East US
- **Environment**: dev

## Next Steps

1. ✅ Login to Terraform Cloud
2. ✅ Create organization and workspace
3. ✅ Add variables
4. ✅ Run `terraform init`
5. ✅ Run `terraform plan`
6. ✅ Run `terraform apply`
7. ✅ Access your Azure VM

---

**Support**: https://support.hashicorp.com/
**Docs**: https://developer.hashicorp.com/terraform/cloud-docs
