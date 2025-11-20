#!/bin/bash

# Script to get your deployed application's IP address
# Run this after deployment completes

echo "=================================================="
echo "GETTING YOUR APPLICATION IP ADDRESS"
echo "=================================================="
echo ""

# Check if Azure CLI is available
if command -v az &> /dev/null; then
    echo "✅ Azure CLI found. Fetching IP address..."
    echo ""
    
    # Login check
    if az account show &> /dev/null; then
        echo "✅ Already logged in to Azure"
        echo ""
        
        # Get VM IP
        VM_IP=$(az vm list-ip-addresses \
            --resource-group devopspipeline-dev-rg \
            --name devopspipeline-dev-vm \
            --query "[0].virtualMachine.network.publicIpAddresses[0].ipAddress" \
            --output tsv 2>/dev/null)
        
        if [ -n "$VM_IP" ]; then
            echo "=================================================="
            echo "🎉 YOUR APPLICATION IS DEPLOYED!"
            echo "=================================================="
            echo ""
            echo "Frontend URL:    http://$VM_IP"
            echo "Backend API:     http://$VM_IP:5000"
            echo "Health Check:    http://$VM_IP:5000/health"
            echo ""
            echo "=================================================="
            echo ""
            
            # Test connectivity
            echo "Testing connectivity..."
            if curl -s -o /dev/null -w "%{http_code}" "http://$VM_IP:5000/health" | grep -q "200"; then
                echo "✅ Backend is responding!"
            else
                echo "⚠️  Backend might still be starting up. Wait 1-2 minutes."
            fi
            
            exit 0
        else
            echo "❌ Could not find VM. Has it been deployed yet?"
            echo ""
        fi
    else
        echo "⚠️  Not logged in to Azure. Logging in..."
        az login
        exec "$0"  # Re-run script after login
    fi
else
    echo "⚠️  Azure CLI not installed."
    echo ""
fi

# Alternative methods
echo "OTHER WAYS TO GET YOUR IP ADDRESS:"
echo "=================================================="
echo ""
echo "METHOD 1: GitHub Actions"
echo "  1. Go to: https://github.com/Pelino-Courses/devops-pipeline-kigaduha/actions"
echo "  2. Click latest 'CI/CD Pipeline' run"
echo "  3. Click 'deploy' job"
echo "  4. Look for 'Display deployment URL' step"
echo ""
echo "METHOD 2: Terraform Cloud"
echo "  1. Go to: https://app.terraform.io"
echo "  2. Open workspace: devops-pipeline-infrastructure"
echo "  3. Click 'Outputs' tab"
echo "  4. Find: vm_public_ip"
echo ""
echo "METHOD 3: Azure Portal"
echo "  1. Go to: https://portal.azure.com"
echo "  2. Search: devopspipeline-dev-vm"
echo "  3. Look for 'Public IP address'"
echo ""
echo "=================================================="
