from constructs import Construct
import aws_cdk as cdk
import os
from aws_cdk import Stack, StackProps
import aws_cdk.aws_codestarnotifications as notifications
import aws_cdk.aws_sns_subscriptions as subs
import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_sns as sns
import aws_cdk.aws_chatbot as chatbot
import aws_cdk.aws_sns as sns
import aws_cdk.aws_iam as iam
import aws_cdk.aws_events_targets as targets
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    pipelines as pipelines,
    aws_codepipeline_actions as cpactions,
    
)

from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep,
    ManualApprovalStep
)


from cdk_workshop.pipeline_stage import WorkshopPipelineStage


class WorkshopPipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        

        # Creates a CodeCommit repository called 'WorkshopRepo'
        repo = codecommit.Repository(
            self, "WorkshopRepo", repository_name="WorkshopRepo",
            
        )

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "main"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "npx cdk synth",
                ]
                
            ),
        )

    

        
        
       
        
        
        

          # CODE HERE...

        deploy = WorkshopPipelineStage(self, "Pre-Prod")
        deploy_stage = pipeline.add_stage(deploy)
     
        deploy_stage.add_post( 
            
            pipelines.ShellStep(
                "TestViewerEndpoint", 
                env_from_cfn_outputs={
                    "ENDPOINT_URL": deploy.hc_viewer_url
                },
                commands=["curl -Ssf $ENDPOINT_URL"],
            )
    
         
        )

        deploy_stage.add_post(
            pipelines.ShellStep(
                "TestAPIGatewayEndpoint",
                env_from_cfn_outputs={
                    "ENDPOINT_URL": deploy.hc_endpoint
                },
                commands=[
                    "curl -Ssf $ENDPOINT_URL",
                    "curl -Ssf $ENDPOINT_URL/hello",
                    "curl -Ssf $ENDPOINT_URL/test",
                ],
            )
            
        )

        prod = WorkshopPipelineStage(self, "Prod")
        prod_stage = pipeline.add_stage(prod,
            pre = [ManualApprovalStep('PromoteToProduction')])
        
        prod_stage.add_post(
            
            pipelines.ShellStep(
                "ViewerEndpoint",
                env_from_cfn_outputs={
                    "ENDPOINT_URL": prod.hc_viewer_url
                },
                commands=["curl -Ssf $ENDPOINT_URL"],
                
            )
            
        )

        prod_stage.add_post(
            pipelines.ShellStep(
                "APIGatewayEndpoint",
                env_from_cfn_outputs={
                    "ENDPOINT_URL": prod.hc_endpoint
                },
                commands=[
                    "curl -Ssf $ENDPOINT_URL",
                    "curl -Ssf $ENDPOINT_URL/hello",
                    "curl -Ssf $ENDPOINT_URL/test",
                ],
            )
            
        )

        pipeline.build_pipeline()

        topic = sns.Topic(self, "MyTopic")
        topic.add_subscription(subs.EmailSubscription("osegbej@amazon.com"))
        rule = notifications.NotificationRule(self, "NotificationRule",
            source = pipeline.pipeline,
            events = ["codepipeline-pipeline-pipeline-execution-started", "codepipeline-pipeline-pipeline-execution-failed", "codepipeline-pipeline-manual-approval-needed", "codepipeline-pipeline-manual-approval-succeeded"],
            targets=[topic]
            )
   
        

        