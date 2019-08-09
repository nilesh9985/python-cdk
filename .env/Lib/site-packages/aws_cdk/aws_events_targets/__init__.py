import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_cloudformation
import aws_cdk.aws_codebuild
import aws_cdk.aws_codepipeline
import aws_cdk.aws_ec2
import aws_cdk.aws_ecs
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_sns
import aws_cdk.aws_sns_subscriptions
import aws_cdk.aws_sqs
import aws_cdk.aws_stepfunctions
import aws_cdk.core
import aws_cdk.custom_resources
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-events-targets", "1.2.0", __name__, "aws-events-targets@1.2.0.jsii.tgz")
@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class CodeBuildProject(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.CodeBuildProject"):
    """Start a CodeBuild build when an AWS CloudWatch events rule is triggered."""
    def __init__(self, project: aws_cdk.aws_codebuild.IProject) -> None:
        """
        :param project: -
        """
        jsii.create(CodeBuildProject, self, [project])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: aws_cdk.aws_events.IRule, _id: typing.Optional[str]=None) -> aws_cdk.aws_events.RuleTargetConfig:
        """Allows using build projects as event rule targets.

        :param _rule: -
        :param _id: -
        """
        return jsii.invoke(self, "bind", [_rule, _id])


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class CodePipeline(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.CodePipeline"):
    """Allows the pipeline to be used as a CloudWatch event rule target."""
    def __init__(self, pipeline: aws_cdk.aws_codepipeline.IPipeline) -> None:
        """
        :param pipeline: -
        """
        jsii.create(CodePipeline, self, [pipeline])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: aws_cdk.aws_events.IRule, _id: typing.Optional[str]=None) -> aws_cdk.aws_events.RuleTargetConfig:
        """Returns the rule target specification. NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        :param _rule: -
        :param _id: -
        """
        return jsii.invoke(self, "bind", [_rule, _id])


@jsii.data_type(jsii_type="@aws-cdk/aws-events-targets.ContainerOverride", jsii_struct_bases=[], name_mapping={'container_name': 'containerName', 'command': 'command', 'cpu': 'cpu', 'environment': 'environment', 'memory_limit': 'memoryLimit', 'memory_reservation': 'memoryReservation'})
class ContainerOverride():
    def __init__(self, *, container_name: str, command: typing.Optional[typing.List[str]]=None, cpu: typing.Optional[jsii.Number]=None, environment: typing.Optional[typing.List["TaskEnvironmentVariable"]]=None, memory_limit: typing.Optional[jsii.Number]=None, memory_reservation: typing.Optional[jsii.Number]=None):
        """
        :param container_name: Name of the container inside the task definition.
        :param command: Command to run inside the container. Default: Default command
        :param cpu: The number of cpu units reserved for the container. Default: The default value from the task definition.
        :param environment: Variables to set in the container's environment.
        :param memory_limit: Hard memory limit on the container. Default: The default value from the task definition.
        :param memory_reservation: Soft memory limit on the container. Default: The default value from the task definition.
        """
        self._values = {
            'container_name': container_name,
        }
        if command is not None: self._values["command"] = command
        if cpu is not None: self._values["cpu"] = cpu
        if environment is not None: self._values["environment"] = environment
        if memory_limit is not None: self._values["memory_limit"] = memory_limit
        if memory_reservation is not None: self._values["memory_reservation"] = memory_reservation

    @property
    def container_name(self) -> str:
        """Name of the container inside the task definition."""
        return self._values.get('container_name')

    @property
    def command(self) -> typing.Optional[typing.List[str]]:
        """Command to run inside the container.

        default
        :default: Default command
        """
        return self._values.get('command')

    @property
    def cpu(self) -> typing.Optional[jsii.Number]:
        """The number of cpu units reserved for the container.

        default
        :default: The default value from the task definition.
        """
        return self._values.get('cpu')

    @property
    def environment(self) -> typing.Optional[typing.List["TaskEnvironmentVariable"]]:
        """Variables to set in the container's environment."""
        return self._values.get('environment')

    @property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        """Hard memory limit on the container.

        default
        :default: The default value from the task definition.
        """
        return self._values.get('memory_limit')

    @property
    def memory_reservation(self) -> typing.Optional[jsii.Number]:
        """Soft memory limit on the container.

        default
        :default: The default value from the task definition.
        """
        return self._values.get('memory_reservation')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ContainerOverride(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class EcsTask(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.EcsTask"):
    """Start a task on an ECS cluster."""
    def __init__(self, *, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, subnet_selection: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None, task_count: typing.Optional[jsii.Number]=None) -> None:
        """
        :param props: -
        :param cluster: Cluster where service will be deployed.
        :param task_definition: Task Definition of the task that should be started.
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param security_group: Existing security group to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnet_selection: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets
        :param task_count: How many tasks should be started when this event is triggered. Default: 1
        """
        props = EcsTaskProps(cluster=cluster, task_definition=task_definition, container_overrides=container_overrides, security_group=security_group, subnet_selection=subnet_selection, task_count=task_count)

        jsii.create(EcsTask, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, rule: aws_cdk.aws_events.IRule, id: typing.Optional[str]=None) -> aws_cdk.aws_events.RuleTargetConfig:
        """Allows using tasks as target of CloudWatch events.

        :param rule: -
        :param id: -
        """
        return jsii.invoke(self, "bind", [rule, id])

    @property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        return jsii.get(self, "securityGroup")


@jsii.data_type(jsii_type="@aws-cdk/aws-events-targets.EcsTaskProps", jsii_struct_bases=[], name_mapping={'cluster': 'cluster', 'task_definition': 'taskDefinition', 'container_overrides': 'containerOverrides', 'security_group': 'securityGroup', 'subnet_selection': 'subnetSelection', 'task_count': 'taskCount'})
class EcsTaskProps():
    def __init__(self, *, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, subnet_selection: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None, task_count: typing.Optional[jsii.Number]=None):
        """Properties to define an ECS Event Task.

        :param cluster: Cluster where service will be deployed.
        :param task_definition: Task Definition of the task that should be started.
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param security_group: Existing security group to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnet_selection: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets
        :param task_count: How many tasks should be started when this event is triggered. Default: 1
        """
        self._values = {
            'cluster': cluster,
            'task_definition': task_definition,
        }
        if container_overrides is not None: self._values["container_overrides"] = container_overrides
        if security_group is not None: self._values["security_group"] = security_group
        if subnet_selection is not None: self._values["subnet_selection"] = subnet_selection
        if task_count is not None: self._values["task_count"] = task_count

    @property
    def cluster(self) -> aws_cdk.aws_ecs.ICluster:
        """Cluster where service will be deployed."""
        return self._values.get('cluster')

    @property
    def task_definition(self) -> aws_cdk.aws_ecs.TaskDefinition:
        """Task Definition of the task that should be started."""
        return self._values.get('task_definition')

    @property
    def container_overrides(self) -> typing.Optional[typing.List["ContainerOverride"]]:
        """Container setting overrides.

        Key is the name of the container to override, value is the
        values you want to override.
        """
        return self._values.get('container_overrides')

    @property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        """Existing security group to use for the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        default
        :default: A new security group is created
        """
        return self._values.get('security_group')

    @property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        """In what subnets to place the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        default
        :default: Private subnets
        """
        return self._values.get('subnet_selection')

    @property
    def task_count(self) -> typing.Optional[jsii.Number]:
        """How many tasks should be started when this event is triggered.

        default
        :default: 1
        """
        return self._values.get('task_count')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'EcsTaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class LambdaFunction(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.LambdaFunction"):
    """Use an AWS Lambda function as an event rule target."""
    def __init__(self, handler: aws_cdk.aws_lambda.IFunction, *, event: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None) -> None:
        """
        :param handler: -
        :param props: -
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire CloudWatch event
        """
        props = LambdaFunctionProps(event=event)

        jsii.create(LambdaFunction, self, [handler, props])

    @jsii.member(jsii_name="bind")
    def bind(self, rule: aws_cdk.aws_events.IRule, _id: typing.Optional[str]=None) -> aws_cdk.aws_events.RuleTargetConfig:
        """Returns a RuleTarget that can be used to trigger this Lambda as a result from a CloudWatch event.

        :param rule: -
        :param _id: -
        """
        return jsii.invoke(self, "bind", [rule, _id])


@jsii.data_type(jsii_type="@aws-cdk/aws-events-targets.LambdaFunctionProps", jsii_struct_bases=[], name_mapping={'event': 'event'})
class LambdaFunctionProps():
    def __init__(self, *, event: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None):
        """Customize the SNS Topic Event Target.

        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire CloudWatch event
        """
        self._values = {
        }
        if event is not None: self._values["event"] = event

    @property
    def event(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        """The event to send to the Lambda.

        This will be the payload sent to the Lambda Function.

        default
        :default: the entire CloudWatch event
        """
        return self._values.get('event')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'LambdaFunctionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class SfnStateMachine(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.SfnStateMachine"):
    """Use a StepFunctions state machine as a target for AWS CloudWatch event rules."""
    def __init__(self, machine: aws_cdk.aws_stepfunctions.IStateMachine, *, input: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None) -> None:
        """
        :param machine: -
        :param props: -
        :param input: The input to the state machine execution. Default: the entire CloudWatch event
        """
        props = SfnStateMachineProps(input=input)

        jsii.create(SfnStateMachine, self, [machine, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: aws_cdk.aws_events.IRule, _id: typing.Optional[str]=None) -> aws_cdk.aws_events.RuleTargetConfig:
        """Returns a properties that are used in an Rule to trigger this State Machine.

        :param _rule: -
        :param _id: -

        see
        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/resource-based-policies-cwe.html#sns-permissions
        """
        return jsii.invoke(self, "bind", [_rule, _id])

    @property
    @jsii.member(jsii_name="machine")
    def machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return jsii.get(self, "machine")


@jsii.data_type(jsii_type="@aws-cdk/aws-events-targets.SfnStateMachineProps", jsii_struct_bases=[], name_mapping={'input': 'input'})
class SfnStateMachineProps():
    def __init__(self, *, input: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None):
        """Customize the Step Functions State Machine target.

        :param input: The input to the state machine execution. Default: the entire CloudWatch event
        """
        self._values = {
        }
        if input is not None: self._values["input"] = input

    @property
    def input(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        """The input to the state machine execution.

        default
        :default: the entire CloudWatch event
        """
        return self._values.get('input')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SfnStateMachineProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class SnsTopic(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.SnsTopic"):
    """Use an SNS topic as a target for AWS CloudWatch event rules.

    Example::
           // publish to an SNS topic every time code is committed
           // to a CodeCommit repository
           repository.onCommit(new targets.SnsTopic(topic));
    """
    def __init__(self, topic: aws_cdk.aws_sns.ITopic, *, message: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None) -> None:
        """
        :param topic: -
        :param props: -
        :param message: The message to send to the topic. Default: the entire CloudWatch event
        """
        props = SnsTopicProps(message=message)

        jsii.create(SnsTopic, self, [topic, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: aws_cdk.aws_events.IRule, _id: typing.Optional[str]=None) -> aws_cdk.aws_events.RuleTargetConfig:
        """Returns a RuleTarget that can be used to trigger this SNS topic as a result from a CloudWatch event.

        :param _rule: -
        :param _id: -

        see
        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/resource-based-policies-cwe.html#sns-permissions
        """
        return jsii.invoke(self, "bind", [_rule, _id])

    @property
    @jsii.member(jsii_name="topic")
    def topic(self) -> aws_cdk.aws_sns.ITopic:
        return jsii.get(self, "topic")


@jsii.data_type(jsii_type="@aws-cdk/aws-events-targets.SnsTopicProps", jsii_struct_bases=[], name_mapping={'message': 'message'})
class SnsTopicProps():
    def __init__(self, *, message: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None):
        """Customize the SNS Topic Event Target.

        :param message: The message to send to the topic. Default: the entire CloudWatch event
        """
        self._values = {
        }
        if message is not None: self._values["message"] = message

    @property
    def message(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        """The message to send to the topic.

        default
        :default: the entire CloudWatch event
        """
        return self._values.get('message')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SnsTopicProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class SqsQueue(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.SqsQueue"):
    """Use an SQS Queue as a target for AWS CloudWatch event rules.

    Example::
           // publish to an SQS queue every time code is committed
           // to a CodeCommit repository
           repository.onCommit(new targets.SqsQueue(queue));
    """
    def __init__(self, queue: aws_cdk.aws_sqs.IQueue, *, message: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None, message_group_id: typing.Optional[str]=None) -> None:
        """
        :param queue: -
        :param props: -
        :param message: The message to send to the queue. Must be a valid JSON text passed to the target queue. Default: the entire CloudWatch event
        :param message_group_id: Message Group ID for messages sent to this queue. Required for FIFO queues, leave empty for regular queues. Default: - no message group ID (regular queue)
        """
        props = SqsQueueProps(message=message, message_group_id=message_group_id)

        jsii.create(SqsQueue, self, [queue, props])

    @jsii.member(jsii_name="bind")
    def bind(self, rule: aws_cdk.aws_events.IRule, _id: typing.Optional[str]=None) -> aws_cdk.aws_events.RuleTargetConfig:
        """Returns a RuleTarget that can be used to trigger this SQS queue as a result from a CloudWatch event.

        :param rule: -
        :param _id: -

        see
        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/resource-based-policies-cwe.html#sqs-permissions
        """
        return jsii.invoke(self, "bind", [rule, _id])

    @property
    @jsii.member(jsii_name="queue")
    def queue(self) -> aws_cdk.aws_sqs.IQueue:
        return jsii.get(self, "queue")


@jsii.data_type(jsii_type="@aws-cdk/aws-events-targets.SqsQueueProps", jsii_struct_bases=[], name_mapping={'message': 'message', 'message_group_id': 'messageGroupId'})
class SqsQueueProps():
    def __init__(self, *, message: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None, message_group_id: typing.Optional[str]=None):
        """Customize the SQS Queue Event Target.

        :param message: The message to send to the queue. Must be a valid JSON text passed to the target queue. Default: the entire CloudWatch event
        :param message_group_id: Message Group ID for messages sent to this queue. Required for FIFO queues, leave empty for regular queues. Default: - no message group ID (regular queue)
        """
        self._values = {
        }
        if message is not None: self._values["message"] = message
        if message_group_id is not None: self._values["message_group_id"] = message_group_id

    @property
    def message(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        """The message to send to the queue.

        Must be a valid JSON text passed to the target queue.

        default
        :default: the entire CloudWatch event
        """
        return self._values.get('message')

    @property
    def message_group_id(self) -> typing.Optional[str]:
        """Message Group ID for messages sent to this queue.

        Required for FIFO queues, leave empty for regular queues.

        default
        :default: - no message group ID (regular queue)
        """
        return self._values.get('message_group_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SqsQueueProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-events-targets.TaskEnvironmentVariable", jsii_struct_bases=[], name_mapping={'name': 'name', 'value': 'value'})
class TaskEnvironmentVariable():
    def __init__(self, *, name: str, value: str):
        """An environment variable to be set in the container run as a task.

        :param name: Name for the environment variable. Exactly one of ``name`` and ``namePath`` must be specified.
        :param value: Value of the environment variable. Exactly one of ``value`` and ``valuePath`` must be specified.
        """
        self._values = {
            'name': name,
            'value': value,
        }

    @property
    def name(self) -> str:
        """Name for the environment variable.

        Exactly one of ``name`` and ``namePath`` must be specified.
        """
        return self._values.get('name')

    @property
    def value(self) -> str:
        """Value of the environment variable.

        Exactly one of ``value`` and ``valuePath`` must be specified.
        """
        return self._values.get('value')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TaskEnvironmentVariable(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CodeBuildProject", "CodePipeline", "ContainerOverride", "EcsTask", "EcsTaskProps", "LambdaFunction", "LambdaFunctionProps", "SfnStateMachine", "SfnStateMachineProps", "SnsTopic", "SnsTopicProps", "SqsQueue", "SqsQueueProps", "TaskEnvironmentVariable", "__jsii_assembly__"]

publication.publish()
