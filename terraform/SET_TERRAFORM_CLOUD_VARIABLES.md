# Set Azure Credentials in Terraform Cloud

Since we removed the ARM_* variables from terraform.tfvars to fix the warnings, you need to set them as environment variables in Terraform Cloud.

## Steps to Set Environment Variables in Terraform Cloud:

1. **Go to Terraform Cloud**:
   - Visit: https://app.terraform.io/app/dukx/workspaces/devops-pipeline-infrastructure

2. **Navigate to Variables**:
   - Click on your workspace: `devops-pipeline-infrastructure`
   - Click on the **"Variables"** tab

3. **Add Environment Variables** (mark each as "Sensitive"):

   | Variable Name | Value | Category | Sensitive |
   |--------------|-------|----------|-----------|
   | `ARM_SUBSCRIPTION_ID` | `<your-subscription-id>` | env | ✓ |
   | `ARM_CLIENT_ID` | `<your-client-id>` | env | ✓ |
   | `ARM_CLIENT_SECRET` | `<your-client-secret>` | env | ✓ |
   | `ARM_TENANT_ID` | `<your-tenant-id>` | env | ✓ |

4. **Important**:
   - Select **"Environment variable"** (not "Terraform variable")
   - Check the **"Sensitive"** checkbox for each one
   - Click **"Add variable"** for each

## Alternative: Use Terraform Cloud API (Quick Method)

You can also set these via API. Here's a script (requires your Terraform Cloud API token):

```bash
# Set your Terraform Cloud token
export TFC_TOKEN="<your-terraform-cloud-api-token>"
export TFC_ORG="dukx"
export TFC_WORKSPACE="devops-pipeline-infrastructure"

# Get workspace ID
WORKSPACE_ID=$(curl -s \
  --header "Authorization: Bearer $TFC_TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  https://app.terraform.io/api/v2/organizations/$TFC_ORG/workspaces/$TFC_WORKSPACE | jq -r '.data.id')

# Set ARM_SUBSCRIPTION_ID
curl -s \
  --header "Authorization: Bearer $TFC_TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  --request POST \
  --data '{
    "data": {
      "type": "vars",
      "attributes": {
        "key": "ARM_SUBSCRIPTION_ID",
        "value": "<your-subscription-id>",
        "category": "env",
        "sensitive": true
      }
    }
  }' \
  https://app.terraform.io/api/v2/workspaces/$WORKSPACE_ID/vars

# Set ARM_CLIENT_ID
curl -s \
  --header "Authorization: Bearer $TFC_TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  --request POST \
  --data '{
    "data": {
      "type": "vars",
      "attributes": {
        "key": "ARM_CLIENT_ID",
        "value": "<your-client-id>",
        "category": "env",
        "sensitive": true
      }
    }
  }' \
  https://app.terraform.io/api/v2/workspaces/$WORKSPACE_ID/vars

# Set ARM_CLIENT_SECRET
curl -s \
  --header "Authorization: Bearer $TFC_TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  --request POST \
  --data '{
    "data": {
      "type": "vars",
      "attributes": {
        "key": "ARM_CLIENT_SECRET",
        "value": "<your-client-secret>",
        "category": "env",
        "sensitive": true
      }
    }
  }' \
  https://app.terraform.io/api/v2/workspaces/$WORKSPACE_ID/vars

# Set ARM_TENANT_ID
curl -s \
  --header "Authorization: Bearer $TFC_TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  --request POST \
  --data '{
    "data": {
      "type": "vars",
      "attributes": {
        "key": "ARM_TENANT_ID",
        "value": "<your-tenant-id>",
        "category": "env",
        "sensitive": true
      }
    }
  }' \
  https://app.terraform.io/api/v2/workspaces/$WORKSPACE_ID/vars

echo "✓ All Azure credentials set in Terraform Cloud!"
```

## After Setting Variables

Once you've set these environment variables in Terraform Cloud, run:

```bash
cd /workspaces/devops-pipeline-kigaduha/terraform
terraform plan
```

The warnings should be gone!
