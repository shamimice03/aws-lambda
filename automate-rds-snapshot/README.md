## Take RDS snapshot based on schedule:

### Need to configure:
- AWS EventBridge
- AWS Lambda
- CloudWatch
- IAM Role and Policy

### Steps:
1. Configure AWS `EventBridge` to take snapshot and delete pervious snapshot based on schedule. ( Suppose `2AM` everyday)

2. Configure `Lambda` function
- Create a `Lambda Execution Role` with appropriate policies
- `New snapshot:` If today is `06/12/2023` then the snapshot name will be `snap-DBname-06-12-2023` 
- `Deleted snapshot:`  The snapshot that was taken previous day `snap-DBname-05-12-2023` will be deleted 

3. Check `CloudWatch` logs if anything unexpected happened
