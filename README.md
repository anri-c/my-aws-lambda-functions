

## lambda with codepipeline

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
