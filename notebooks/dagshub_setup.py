
import mlflow
import dagshub
mlflow.set_tracking_url("https://dagshub.com/himanshu7-t/mlops-mini-project.mlflow")
dagshub.init(repo_owner='himanshu7-t', repo_name='mlops-mini-project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)