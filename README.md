

## lambda-with-codepipeline.py

### iam role policy example

CloudFormation template

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
              - "codepipeline:PutJobFailureResult"
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

## codepipeline-approval-notify-slack.py

### part of cloudformation template for codepipeline approval stage

``` yaml
 - Name: "Approval"
   Actions:
     - Name: "Approval"
       ActionTypeId:
         Category: "Approval"
         Owner: "AWS"
         Version: "1"
         Provider: "Manual"
       Configuration:
         NotificationArn:
           Ref: "CodepipelineTopic"
         ExternalEntityLink: !Sub "https://${App}.example.com/"
         CustomData: "Please review the latest change and approve or reject."
       RunOrder: "1"
```
