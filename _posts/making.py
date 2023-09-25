import numpy as np
import pandas as pd
import os
import urllib
import json
import xgboost as xgb
import pylab
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import datetime

#%% api 사용한 코드

api_token =''
base_url = 'http://'

headers = {
    'Content-Type' : 'application/json',
    'Authorization' : 'Bearer' + api_token,
    'host' : '접속url'
}

def get_recipes(model_id, request_status=''):
    """
    model_id = 모델 아이디
    request_status = 상태
    """

    url = f'{base_url}/..../{model_id}?request_status={request_status}'
    print(url)

    req = urllib.request.Request(url, headers=headers, method='GET')

    result = ''
    with urllib.request.urlopen(req) as response:
        print("response code : ", response.getcode())
        result = response.read().decode('utf-8')
    result = json.loads(result)
    return result

def update_recipe_history(recipe_number, data):
    url = f'{base_url}/recipe/endpoint/{recipe_number}'

    data = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(
        url, data=data, headers=headers, method='PATCH'
    )

    result = ''
    with urllib.request.urlopen(req) as response:
        print("response code : ", response.getcode())
        result = response.read().decode('utf-8')
    result = json.loads(result)
    return result
 


#%% 배포한 파이프라인의 최신버전 가져오기

from azureml.code import Workspace, Datastore, Dataset, Run
from azureml.pipeline.core import PipelineRun, PublishedPipeline, PipelineEndpoint

workspace_name = 'ml studio에서 Current workspace'
subscription_id = 'ml studio에서 subscription id'
resource_group = 'ml studio에서 resource_group'

ws = Workspace.get(name=workspace_name,
                   subscription_id=subscription_id,
                   resource_group=resource_group)

predict_endpoint_name = 'publish할때 지은 위에 부분 이름'

#엔드포인트 가져오기 default version
predict_endpoint = PipelineEndpoint.get(Workspace=ws, name=predict_endpoint_name)
predict_pipeline_id = predict_endpoint.pipeline_version_list[int(predict_endpoint.default_version)].pipeline_id
predict_published_pipeline = PublishedPipeline.get(ws, predict_pipeline_id)

print('pipeline_id is : ', predict_pipeline_id,
      "/ published_pipeline is : ", predict_published_pipeline)

making_arg1 = 'a'
making_arg2 = 50
pipeline_parameters = {"arg1" : making_arg1,
                       "arg2" : making_arg2,
                       }

predicted_pipeline_run = predict_published_pipeline.submit(ws,
                                                           predict_published_pipeline.name,
                                                           pipeline_parameters)


#%% feature making code

def calcSingleFeatures(df_x, df_y, x_cols, y_col, feature_name, checking_100 = 'N'):
    # feature_name = 새로 만들 feature 이름
    tmp_dat_x = df_x.copy().fillna(0)
    tmp_dat_y = df_y.copy()
    tmp_list = list()
    tmp_tds_y = tmp_dat_x.T.join(tmp_tds_y.set_index('Name'))[y_col]
    isna_grade_list = list(tmp_tds_y[tmp_tds_y.isna()].index)
    for ii in range(tmp_dat_x.shape[0]):
        tmp_row = tmp_dat_x.iloc[ii]

        if checking_100 == 'Y':
            tmp_val_div = 100
        else:
            tmp_val_div = tmp_row.sum()
        
        if tmp_row.sum() > 0 :
            tmp_val = np.dot(np.array(tmp_row[tmp_row>0]), np.array(tmp_tds_y[tmp_row>0])) / tmp_val_div
            if np.sum(tmp_row[isna_grade_list]) > 0 :
                tmp_val = np.nan
        else:
            tmp_val = 0
        tmp_list.append(tmp_val)

    tmp_list = pd.Series(tmp_list, name = feature_name)
    return tmp_list

#%% 파일 형태에 따라 불러오기
import joblib 

file_path = ''
file_list = [file for file in os.listdir(file_path) if 'pkl' in file]

model = joblib.load(file_path + file_list[0])


#%% parameter 할당

gbt_params = {}

model = xgb.XGBRegressor(**gbt_params, random_state =2)

#%% plot scatter

def plot_scatter(x_data, y_data, ycol, title_text, save_path = '', figsize_setting=(7,6),
                 s_size_setting = 100, alpha_setting = 0.75, fontsize_setting = 25, xticks_rotation_setting=0,
                 axis_labels=('Real', 'Pred'), yxline_yn=True, group='',
                 group_coloring=False, rsq_yn=False) :
    os.chdir(save_path)

    z = np.polyfit(x_data.tolist(), y_data.tolist(), 1)
    p = np.poly1d(z)
    plt.figure(figsize=figsize_setting)
    plt.grid(True)

    if yxline_yn == True : 
        plt.plot(x_data, x_data, 'k-', alpha=1, zorder=0, color='grey', linewidth=0.85)

    if group_coloring == True:
        df = pd.concat([x_data, y_data, group], axis=1)
        df.columns = ['x_data','y_data','group']
        c_lst = [plt.cm.Paired(aa) for aa in np.linspace(0.0, 1.0, len(set(df['group'])))]
        group_list = df.groupby('group', as_index=False).mean().group.to_list()
        for ii, gg in enumerate(df.groupby('group')):
            plt.scatter(x=gg[1]['x_data'], y=gg[1]['y_data'], color=c_lst[ii], label='{}'.format(group_list[ii]),
                        s = s_size_setting, alpha = alpha_setting, edgecolors='grey')
        
        pylab.plot(x_data, p(x_data), "r--")
        plt.show()
    
    else:
        plt.scatter(x=x_data, y=y_data, s = s_size_setting, alpha = alpha_setting * 0.75, edgecolors='grey')
        pylab.plot(x_data, p(x_data), "r--")

    plt.title(ycol + '_' + (title_text) + "[" + str(len(y_data)) + "]", fontsize = fontsize_setting * 1.01)
    plt.xlabel(axis_labels[0], fontsize=fontsize_setting*0.7)
    plt.ylabel(axis_labels[1], fontsize=fontsize_setting*0.7)
    plt.xticks(fontsize=fontsize_setting*0.75, rotation = xticks_rotation_setting)
    plt.yticks(fontsize=fontsize_setting*0.75)
    plt.axis([-2.5, 75, -2.5, 72.5])

    if rsq_yn == True:
        plt.annotate("r2={:.2f}%".format(r2_score(x_data,y_data)*100),
                     (x_data.max()*0.6, y_data.min()),
                     fontsize = fontsize_setting, color='grey', weight='bold')
        
    saveNM_fig = '{}_{}_script_{}_{}.png'.format(ycol, title_text, str(len(y_data)), datetime.datetime.now().strftime("%H%M%S"))
    plt.savefig(fname = saveNM_fig, dpi = 300, bbox_inches='tight')
    plt.show()


#%% optuna

import optuna

time_setting = 30 * 1

def objective(trial):
    params= {
        'max_depth' : trial.suggest_int('max_depth', 5, 10),
        'learning_rate' : trial.suggest_float('learning_rate', 0.01, 0.2)
    }

    model = xgb.XGBRegressor(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_valid)
    avg = np.sqrt(mean_squared_error(y_valid, y_pred))

    return avg

def callback(study, trial):
    if study.best_value <= 2:
        study.stop()

study = optuna.create_study(direction='minimize', study_name=('y_find' + '_optimization'))
study.optimize(objective, timeout=time_setting, callbacks=[callback])

xgb_params = study.best_params



#%% pipeline making

from azureml.core import Workspace, Dataset, Datastore, Environment

ws = Workspace.from_config()
compute_target = ws.compute_targets[''] #compute cluster name

myenv = Environment.from_conda_specification(name='env001', file_path='./evn.yaml') #environments에 만들어질 이름과 현재 yaml 파일 위치
myenv.register(workspace=ws)

from azureml.core.runconfig import Runconfiguration
aml_run_config = Runconfiguration()
aml_run_config.target = compute_target
aml_run_config.environment = myenv


from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core import Pipeline, StepSequence, PipelineData
from azureml.pipeline.core.graph import PipelineParameter

default_store = ws.get_default_datastore()

#pipeline data (pipeline input, output) #이름 설정과 datastore 위치
df_feats_prepare = PipelineData("df_feats_prepare", datastore=default_store).as_dataset()
base_grid = PipelineData("base_grid", datastore=default_store).as_dataset()
total_prepare = PipelineData("total_prepare", datastore=default_store).as_dataset()
select_df = PipelineData("select_df", datastore=default_store).as_dataset()

predictResult = PipelineData("predictResult", datastore=default_store).as_dataset()

json_file = json.dumps(dict())
arg_recipe_num = PipelineParameter(name='recipe_num', default = 9999)
arg_recomm_num = PipelineParameter(name='recomm_num', default = 50)
arg_input_dat = PipelineParameter(name='input_dat', default = json_file)


#파이프라인 개별
prepare_step = PythonScriptStep(
    name = 'Prepare data',
    source_directory = './prepare/',
    arguments = [
                "--output_df_feats_prepare", df_feats_prepare,
                "--output_base_grid", base_grid,
                "--output_total_prepare", total_prepare,
                "--output_select_df", select_df,

                "--arg_recipe_num", arg_recipe_num,
                "--arg_recomm_num", arg_recomm_num,
                "--arg_input_dat", arg_input_dat,
                 ],
    output =[df_feats_prepare, base_grid, total_prepare, select_df],
    runconfig=aml_run_config,
    compute_target=compute_target,
    allow_reuse=False,
    )


predict_step = PythonScriptStep(
    name = 'Predict Result',
    source_directory = './predict/',
    inputs = [
                df_feats_prepare.parse_parquet_files(),
                base_grid.parse_parquet_files(),
                total_prepare.parse_parquet_files(),
                select_df.parse_parquet_files(),
            ],

    arguments = [
                "--output_predictResult", predictResult,

                "--arg_recipe_num", arg_recipe_num,
                 ],
    output =[predictResult],
    runconfig=aml_run_config,
    compute_target=compute_target,
    allow_reuse=False,
)

# 합치기

from azureml.core import Experiment

step_sequence = StepSequence(steps=[prepare_step, predict_step])
pipeline = Pipeline(Workspace=ws, steps=step_sequence)

pipeline_run = Experiment(ws, 'living_operate').submit(pipeline)
pipeline_run.name
print(pipeline_run.id)



#%% prepare.py

import argparse
from azureml.core import Workspace, Run

parser = argparse.ArgumentParser()
parser.add_argument("--output_df_feats_prepare", required=True)
parser.add_argument("--output_base_grid", required=True)
parser.add_argument("--output_total_prepare", required=True)
parser.add_argument("--output_select_df", required=True)

parser.add_argument("--arg_recipe_num", type=int)
parser.add_argument("--arg_recomm_num", type=int)
parser.add_argument("--arg_input_dat", type=str)
args = parser.parse_args()


recipe_num = args.arg_recipe_num
recomm_num = args.arg_recomm_num
input_dat = args.arg_input_dat



### 중략
select_dict = {}
if select_dict == {}:
    select_df = pd.DataFrame()
else:
    max_length = max(len(values) if isinstance(values, list) else 1 for values in select_dict.values())

    select_df_temp = {
        key : (values + [None]*(max_length - len(values))) if isinstance(values, list) else [values] * max_length
        for key, values in select_dict.items()
    }

    select_df = pd.DataFrame(select_df_temp)

# 다음 step 전달용

if not (args.output_df_feats_prepare is None) : 
    os.makedirs(args.output_df_feats_prepare, exist_ok=True)
    print('%s created' % args.output_df_feats_prepare)
    path = args.output_df_feats_prepare + '/processed.parquet'
    df_feats_prepare = df_feats_prepare.to_parquet(path)





#%% predict step

import argparse
from azureml.core import Workspace, Run

parser = argparse.ArgumentParser()
parser.add_argument("--output_predictResult", required=True)
args = parser.parse_args()

run = Run.get_context()
if run.id.startswith("OfflineRun"):
    workspace = Workspace.from_config()
else:
    workspace = run.experiment.workspace

datastore = workspace.get_default_datastore()

df_feats_prepare = run.input_datasets['df_feats_prepare'].to_pandas_dataframe()
base_grid = run.input_datasets['base_grid'].to_pandas_dataframe()
total_prepare = run.input_datasets['total_prepare'].to_pandas_dataframe()
select_df = run.input_datasets['select_df'].to_pandas_dataframe()


### 중략


if not (args.output_predictResult is None) : 
    os.makedirs(args.output_predictResult, exist_ok=True)
    print('%s created' % args.output_predictResult)
    path = args.output_predictResult + '/predictResult.parquet'
    predictResult = predictResult.to_parquet(path)





# ### env.yaml

# channel:
#   - conda-forge
#   dependencies:
#   - python=3.8
#   - numpy=1.21.6
#   - pip=20.1.1
#   - scikit-learn=0.22.1
#   - scipy=1.5.3
#   - pip:
#         - joblib==0.14.1
#         - pytorch_tabnet==3.1.1
#         - pandas==1.5.3
#         - xgboost==1.3.3
#         - azureml-inference-server-http
#         - azureml-sdk
#         - uuid
#         - request
#         - openpyxl
#   name: model-evn-living