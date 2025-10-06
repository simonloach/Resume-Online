# Setup GitHub Actions OIDC role and CI deploy

This file contains copy-pasteable steps to create an IAM role trusted by GitHub Actions (OIDC), attach a minimal policy, add repository secrets, and trigger the CI workflow that builds and deploys the resume to `s3://simon-resume-bucket`.

Prereqs
- AWS Console access or AWS CLI configured for an IAM user with permission to create roles and policies.
- GitHub repository admin access to add secrets.

1) Create the role with the trust policy
- In the AWS Console: IAM → Roles → Create role → Select "Web identity" → Provider: token.actions.githubusercontent.com
- Alternatively, use the trust policy in `docs/IAM_ROLE_TRUST_POLICY.json` and paste it into the Console's JSON editor when creating the role.

2) Attach inline policy
- Use the inline policy in `docs/IAM_ROLE_INLINE_POLICY.json` for permissions to S3 and CloudFront. Attach it to the role.

3) Copy the role ARN
- After creating the role, copy its ARN (e.g. arn:aws:iam::218734288733:role/GitHubActionsResumeDeployRole)

4) Add GitHub repository secrets
- Settings → Secrets and variables → Actions → New repository secret
  - `AWS_ROLE_TO_ASSUME` = <role-arn>
  - `AWS_REGION` = e.g. `us-east-1`
  - `CLOUDFRONT_DISTRIBUTION_ID` = (optional)

5) Trigger the workflow
- Use the Actions tab → Build and deploy resume → Run workflow, or push a tiny commit to `master`/`main`.

6) Verify
- In Actions logs, verify steps: UV sync → Generate HTML → Generate PDF → Configure AWS credentials → aws s3 sync

Notes
- The trust policy restricts the issuer and repo subject to `simonloach/Resume-Online`. If you want to allow other repos in your org, change the `sub` value accordingly.
- The inline policy limits S3 access to `simon-resume-bucket` only. If you use multiple buckets or a different name, update the policy.
