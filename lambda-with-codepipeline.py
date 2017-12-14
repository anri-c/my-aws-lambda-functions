import boto3

codepipeline = boto3.client('codepipeline')


def put_job_success(jobId, message):
    print(message)
    codepipeline.put_job_success_result(jobId=jobId)

def put_job_failure(jobId, message):
    print(message)
    codepipeline.put_job_failure_result(jobId=jobId, failureDetails={"message": message, "type": "JobFailed"})

def lambda_handler(event, context):
    #print(str(event))

    job = event["CodePipeline.job"]
    jobId = job["id"]
    jobData = job["data"]
    user_param = jobData["actionConfiguration"]["configuration"]["UserParameters"]

    #print("JobData:" + str(jobData))
    #print("UserParameter:" + str(user_param))

    try:
        #  write code...
        #
        put_job_success(jobId, "hello world")
    except Exception, e:
        print(str(e))
        put_job_failure(jobId, str(e))
