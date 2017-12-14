

## lambda with codepipeline

### iam role policy example

``` yaml

  LambdaWithCodePipelineRolePolicy:
    Type: "AWS::IAM::Policy"
    Properties:
      PolicyName: "LambdaWithCodePipelineRolePolicy"
      PolicyDocument:
        Statement:
          - Effect: "Allow"
            Action:
              - "logs:CreateLogGroup"
              - "logs:CreateLogStream"
              - "logs:PutLogEvents"
            Resource: "arn:aws:logs:*:*:*"
          - Effect: "Allow"
            Action:
              - "codepipeline:PutJobSuccessResult"
              - "codepipeline:PutJobSuccessResult"
            Resource: "*"
      Roles:
        - Ref: "LambdaWithCodePipelineRole"
```

### codepipeline's event example

``` json
{
  "CodePipeline.job": {
    "id": "< codepipeline job id >",
    "accountId": "< aws account id>",
    "data": {
      "actionConfiguration": {
        "configuration": {
          "FunctionName": "< lambda function name>",
          "UserParameters": {
             < user parameter dict >
          }
        }
      },
      "inputArtifacts": [],
      "outputArtifacts": [],
      "artifactCredentials": {
        "secretAccessKey": "< aws secret access key >",
        "sessionToken": "< session token >",
        "accessKeyId": "< aws access key id >"
      }
    }
  }
}

```
