#!/usr/bin/env bash
# CLI script to create IAM role for GitHub Actions OIDC and attach inline policy
# Edit BUCKET_NAME and ROLE_NAME before running

set -euo pipefail
BUCKET_NAME="simon-resume-bucket"
ROLE_NAME="GitHubActionsResumeDeployRole"
TRUST_POLICY_FILE="docs/IAM_ROLE_TRUST_POLICY.json"
INLINE_POLICY_FILE="docs/IAM_ROLE_INLINE_POLICY.json"

if [ ! -f "$TRUST_POLICY_FILE" ] || [ ! -f "$INLINE_POLICY_FILE" ]; then
  echo "Missing policy files in docs/ — make sure IAM_ROLE_TRUST_POLICY.json and IAM_ROLE_INLINE_POLICY.json exist"
  exit 1
fi

ROLE_ARN=$(aws iam create-role --role-name "$ROLE_NAME" --assume-role-policy-document file://$TRUST_POLICY_FILE --query 'Role.Arn' --output text)

echo "Created role: $ROLE_ARN"

aws iam put-role-policy --role-name "$ROLE_NAME" --policy-name "ResumeDeployInlinePolicy" --policy-document file://$INLINE_POLICY_FILE

echo "Attached inline policy to $ROLE_NAME"

echo "Now add the following repository secrets in GitHub:"
echo "  AWS_ROLE_TO_ASSUME=$ROLE_ARN"
echo "  AWS_REGION=us-east-1"

echo "Done. You can now trigger the workflow from GitHub Actions UI or push to master/main."
