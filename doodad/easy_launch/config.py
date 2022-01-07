# Change these things
CODE_DIRS_TO_MOUNT = [
    # '/global/scratch/users/patrickhaoy/s3doodad/railrl-private', 
    # '/global/scratch/users/patrickhaoy/s3doodad/multiworld', 
    # '/global/scratch/users/patrickhaoy/s3doodad/doodad',
    # '/global/scratch/users/patrickhaoy/s3doodad/bullet-manipulation-affordances',
    # '/global/scratch/users/patrickhaoy/s3doodad/bullet-manipulation-affordances/roboverse/envs/assets/bullet-objects',
    # '/global/scratch/users/patrickhaoy/s3doodad/rllab',

    '/home/patrickhaoy/code/railrl-private',
    '/home/patrickhaoy/code/multiworld',
    # '/home/patrickhaoy/code/doodad',
    '/home/patrickhaoy/code/bullet-manipulation-affordances',
    '/home/patrickhaoy/code/bullet-manipulation-affordances/roboverse/envs/assets/bullet-objects',
    '/home/patrickhaoy/code/rllab',
    '/2tb/home/patrickhaoy/data/affordances/data/antialias_reset_free_rotated_semicircle_top_drawer_pnp_v2_small'
]
NON_CODE_DIRS_TO_MOUNT = [
]
DIR_AND_MOUNT_POINT_MAPPINGS = [
#     dict(
#         local_dir='/home/ashvin/mujoco/',
#         mount_point='/root/mujoco',
#     ),
]
LOCAL_LOG_DIR = '/2tb/home/patrickhaoy/data/affordances'
RUN_DOODAD_EXPERIMENT_SCRIPT_PATH = (
    '/home/ashvin/code/doodad/doodad/easy_launch/run_experiment.py'
)
AWS_S3_PATH="s3://s3doodad/doodad/logs"
# You probably don't need to change things below
# Specifically, the docker image is looked up on dockerhub.com.
# DOODAD_DOCKER_IMAGE = "anair17/railrl-hand-tf-v1"
DOODAD_DOCKER_IMAGE = "anair17/railrl-dice-v1" # 'anair17/railrl-hand-v3' # 'anair17/railrl-gpu-v7a' # 'anair17/railrl-gpu-v6-cuda9' # 'anair17/railrl-gpu-v6' # 'vitchyr/railrl-vitchyr-gpu-v2-2'
# DOODAD_DOCKER_IMAGE = "snasiriany/railrl-lha-v4" #
# DOODAD_DOCKER_IMAGE = "anair17/railrl-gpu-v3"
INSTANCE_TYPE = 'c4.large'
SPOT_PRICE = 0.1
SPOT_PRICE_LOOKUP = {'c4.large': 0.1, 'm4.large': 0.1, 'm4.xlarge': 0.2, 'm4.2xlarge': 0.4}
# GPU_DOODAD_DOCKER_IMAGE = "anair17/railrl-hand-v3"
GPU_DOODAD_DOCKER_IMAGE = "anair17/railrl-dice-v1" # "anair17/borel-v2" #
# GPU_DOODAD_DOCKER_IMAGE = "anair17/railrl-hand-tf-v1"
# GPU_DOODAD_DOCKER_IMAGE = 'anair17/railrl-hand-v3' # 'anair17/railrl-hand-v1a' # 'anair17/railrl-gpu-v7a' # 'anair17/railrl-gpu-v6-cuda9' #  # 'vitchyr/railrl-vitchyr-gpu-v3'
# GPU_DOODAD_DOCKER_IMAGE = "snasiriany/railrl-lha-v4" #
GPU_INSTANCE_TYPE = 'g3.4xlarge'
GPU_SPOT_PRICE = 1.0
GPU_AWS_IMAGE_ID = "ami-0680f279"
GPU_SINGULARITY_IMAGE = "/home/ashvin/code/singularity/railrl-hand-v1a-sandbox" # railrl_hand_v1_img.simg" # gpuv6cuda9.img"
SINGULARITY_IMAGE = "/home/ashvin/code/singularity/railrl-hand-v1a-sandbox" # railrl_hand_v1_img.simg" # gpuv6cuda9.img"
SINGULARITY_PRE_CMDS = [
    # 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mjpro150/bin',
    'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/global/home/users/patrickhaoy/.mujoco/mujoco200/bin',
]
SSH_HOSTS=dict(
    localhost=dict(
        username="ashvin",
        hostname="localhost",
    ),
    surgical1=dict(
        username="ashvin",
        hostname="surgical1",
    ),
    newton1=dict(
        username="ashvin",
        hostname="newton1",
    ),
    newton2=dict(
        username="ashvin",
        hostname="newton2",
    ),
    newton3=dict(
        username="ashvin",
        hostname="newton3",
    ),
    newton4=dict(
        username="ashvin",
        hostname="newton4",
    ),
    newton5=dict(
        username="ashvin",
        hostname="newton5",
    ),
    newton6=dict(
        username="ashvin",
        hostname="newton6",
    ),
    newton7=dict(
        username="ashvin",
        hostname="newton7",
    ),
)
SSH_DEFAULT_HOST="fail"
# SSH_LOG_DIR = '/home/ashvin/data/s3doodad'
SSH_LOG_DIR = '/media/4tb/ashvin/data/s3doodad'
SSH_PRIVATE_KEY = '/home/ashvin/.ssh/id_rsa'
REGION_TO_GPU_AWS_IMAGE_ID = {
    'us-west-1': "ami-0b2985bdb79796529",
    'us-east-1': "ami-0680f279",
    'us-west-2': "ami-0e57f21d309963e66",
    'us-east-2': "ami-0c323cf1a03b771e5",
}
# REGION_TO_GPU_AWS_AVAIL_ZONE = {
#     'us-east-1': 'us-east-1d',
# }
# This really shouldn't matter and in theory could be whatever
OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/doodad-output/'
"""
Slurm Settings
# see https://research-it.berkeley.edu/services/high-performance-computing/user-guide/savio-user-guide#Hardware
"""
SLURM_CONFIGS = dict(
    cpu = dict(
        account_name='fc_rail',
        n_gpus=0,
        partition='savio',
        max_num_cores_per_node=20,
        time_in_mins=720,
    ),
    cpu2 = dict(
        account_name='fc_rail',
        n_gpus=0,
        partition='savio2',
        max_num_cores_per_node=20,
        time_in_mins=720,
    ),
    cpu3 = dict(
        account_name='fc_rail',
        n_gpus=0,
        partition='savio3',
        max_num_cores_per_node=20,
        time_in_mins=720,
    ),
    cpu_lowprio = dict(
        account_name='co_rail',
        n_gpus=0,
        partition='savio',
        max_num_cores_per_node=20,
        time_in_mins=720,
        extra_flags="--qos savio_lowprio",
    ),
    cpu_lowprio2 = dict(
        account_name='co_rail',
        n_gpus=0,
        partition='savio2',
        max_num_cores_per_node=20,
        time_in_mins=720,
        extra_flags="--qos savio_lowprio",
    ),
    cpu_lowprio3 = dict(
        account_name='co_rail',
        n_gpus=0,
        partition='savio3',
        max_num_cores_per_node=20,
        time_in_mins=720,
        extra_flags="--qos savio_lowprio",
    ),
    gpu = dict(
        account_name='co_rail',
        n_gpus=1,
        gpu_string=":TITAN",
        partition='savio3_gpu',
        max_num_cores_per_node=8,
        n_cpus_per_task=4,
        # extra_flags="--exclude n0145.savio3",
        extra_flags="--qos rail_gpu3_normal",
        # extra_flags="--qos savio_lowprio",
        time_in_mins=1440, #720,
    ),
    savio3_2080 = dict(
        account_name='co_rail',
        n_gpus=1,
        gpu_string=":GTX2080TI",
        partition='savio3_gpu',
        max_num_cores_per_node=8,
        n_cpus_per_task=4,
        # extra_flags="--exclude n0145.savio3",
        extra_flags="--qos savio_lowprio",
        time_in_mins=1440, #720,
    ),
    savio3_v100 = dict(
        account_name='co_rail',
        n_gpus=1,
        gpu_string=":V100",
        partition='savio3_gpu',
        max_num_cores_per_node=8,
        n_cpus_per_task=4,
        # extra_flags="--exclude n0145.savio3",
        extra_flags="--qos savio_lowprio",
        time_in_mins=1440, #720,
    ),
    gpu_lowprio = dict(
        account_name='co_rail',
        n_gpus=1,
        partition='savio2_gpu',
        max_num_cores_per_node=8,
        n_cpus_per_task=2,
        extra_flags="--qos savio_lowprio",
        time_in_mins=720,
    ),
    savio2_double = dict(
        account_name='co_rail',
        n_gpus=1,
        partition='savio2_gpu',
        max_num_cores_per_node=8,
        n_cpus_per_task=4,
        extra_flags="--qos savio_lowprio",
        time_in_mins=1440,#720,
    ),
    gpu_lowprio2 = dict(
        account_name='co_rail',
        n_gpus=1,
        partition='savio2_1080ti',
        max_num_cores_per_node=8,
        n_cpus_per_task=2,
        extra_flags="--qos savio_lowprio",
        time_in_mins=720,
    )
)
BRC_EXTRA_SINGULARITY_ARGS = '--writable -B /usr/lib64 -B /var/lib/dcv-gl -B /global'
# BRC_EXTRA_SINGULARITY_ARGS = "--nv -B /global -B /usr/lib64 -B /var/lib/dcv-gl -B /global/home/groups/co_rail/anair17/python/jaxenv37:/global/home/groups/co_rail/anair17/python/jaxenv37:ro --writable-tmpfs /global/home/groups/co_rail/anair17/railrl_hand_v2"
TASKFILE_PATH_ON_BRC = '/global/scratch/users/anair17/s3doodad/railrl/taskfile_from_doodad.sh'
SSS_CODE_DIRS_TO_MOUNT = [
    '/global/scratch/users/patrickhaoy/s3doodad/railrl-private',
    '/global/scratch/users/patrickhaoy/s3doodad/multiworld',
    '/global/scratch/users/patrickhaoy/s3doodad/doodad',
    '/global/scratch/users/patrickhaoy/s3doodad/bullet-manipulation-affordances',
    '/global/scratch/users/patrickhaoy/s3doodad/rllab'
]
SSS_NON_CODE_DIRS_TO_MOUNT = [
]
SSS_DIR_AND_MOUNT_POINT_MAPPINGS = [
    dict(
        local_dir='/global/home/users/patrickhaoy/.mujoco',
        mount_point='/root/.mujoco',
    ),
]
SSS_LOG_DIR = '/global/scratch/users/patrickhaoy/s3doodad/outputs'
# SSS_IMAGE = '/global/scratch/users/anair17/s3doodad/singularity/railrl-hand-v1a-sandbox'
# SSS_GPU_IMAGE = '/global/scratch/users/anair17/s3doodad/singularity/railrl-hand-v1a-sandbox'
# SSS_CPU_IMAGE = '/global/scratch/users/anair17/s3doodad/singularity/railrl-hand-v1a-sandbox'
SSS_IMAGE = '/global/home/groups/co_rail/anair17/railrl_hand_v2'
SSS_GPU_IMAGE = SSS_IMAGE
SSS_CPU_IMAGE = SSS_IMAGE
SSS_RUN_DOODAD_EXPERIMENT_SCRIPT_PATH = (
    '/global/scratch/users/patrickhaoy/s3doodad/doodad/doodad/easy_launch/run_experiment.py'
)
SSS_PRE_CMDS = [
    'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/global/home/users/patrickhaoy/.mujoco/mujoco200/bin',
    # 'alias conda="/global/software/sl-7.x86_64/modules/langs/python/3.7/bin/conda"',
    'source /global/software/sl-7.x86_64/modules/langs/python/3.7/etc/profile.d/conda.sh',
    'conda activate /global/scratch/users/patrickhaoy/python/valenv',
    #'conda activate /global/scratch/users/patrickhaoy/anaconda3/envs/torch110a',
    'export PYTHONPATH=$PYTHONPATH:/global/scratch/users/patrickhaoy/s3doodad/railrl-private',
    'export PYTHONPATH=$PYTHONPATH:/global/scratch/users/patrickhaoy/s3doodad/multiworld',
    'export PYTHONPATH=$PYTHONPATH:/global/scratch/users/patrickhaoy/s3doodad/doodad',
    'export PYTHONPATH=$PYTHONPATH:/global/scratch/users/patrickhaoy/s3doodad/bullet-manipulation-affordances',
    'export PYTHONPATH=$PYTHONPATH:/global/scratch/users/patrickhaoy/s3doodad/bullet-manipulation-affordances/roboverse/envs/assets/bullet-objects',
    'export PYTHONPATH=$PYTHONPATH:/global/scratch/users/patrickhaoy/s3doodad/rllab'
]
# SSS_PRE_CMDS = [ # for jax
#     'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/global/home/users/anair17/.mujoco/mujoco200/bin',
#     'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/global/home/users/anair17/.mujoco/mjpro150/bin',
#     'export LD_LIBRARY_PATH=/global/software/sl-7.x86_64/modules/langs/cuda/11.2/lib64:$LD_LIBRARY_PATH',
#     # 'alias conda="/global/software/sl-7.x86_64/modules/langs/python/3.7/bin/conda"',
#     'source /global/software/sl-7.x86_64/modules/langs/python/3.7/etc/profile.d/conda.sh',
#     'conda activate /global/home/groups/co_rail/anair17/python/jaxenv37',
#     'export D4RL_DATASET_DIR=/global/scratch/users/anair17/s3doodad/d4rl_data',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/mj_envs:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/mjrl:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/hand_dapg:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/bullet-objects:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/bullet-manipulation:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/metaworld:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/jaxrl:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/percentile-regression:$PYTHONPATH',
#     'export PYTHONPATH=/global/scratch/users/anair17/s3doodad/d4rl:$PYTHONPATH',
# ]
# SSS_PRE_CMDS = [
#     'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH'
#     ':/global/home/users/anair17/.mujoco/mjpro150/bin'
#     ':/global/home/users/anair17/.mujoco/mujoco200/bin',
#     'export PATH=/global/home/users/vitchyr/railrl/bin:/opt/conda/envs/railrl/bin/:$PATH',
# ]
BAIR_DATASET_LOCATION = "/media/ashvin/bair/softmotion30_44k/numpy/"
SPACEMOUSE_HOSTNAME = "euler1.bair.berkeley.edu"


GCP_BUCKET='patrick-gcp-bucket'
GCP_PROJECT='ashvin-val'
GCP_IMAGE='ashvin-torch4cuda9'
S3_BUCKET='your_bucket'
AZ_SUB_ID='dc2a7d68-6f03-4c8b-9fab-291d5cbedd37'
AZ_CLIENT_ID='ec0d30fe-4b51-439a-a7af-4259cc2ae1b4'
AZ_TENANT_ID='1466f6e4-adf5-439f-a023-d0d9afd3e764'
AZ_SECRET='_NSwydTN3~QmK_RKVT_W9q0aA9boL_K9yi'
AZ_CONTAINER='doodadcontainer'
# AZ_CONN_STR='DefaultEndpointsProtocol=https;AccountName=anair17;A$countKey=p4QF4k/Y1sH+cWtgZq2jmdLynANLRs9mkaPv4laTsIEetAjE6TIZtv69nliacyx7b4S3O0cUJIfyE0at$XHQjQ==;EndpointSuffix=core.windows.net'
AZ_CONN_STR='DefaultEndpointsProtocol=https;AccountName=anair17;AccountKey=p4QF4k/Y1sH+cWtgZq2jmdLynANLRs9mkaPv4laTsIEetAjE6TIZtv69nliacyx7b4S3O0cUJIfyE0at2XHQjQ==;EndpointSuffix=core.windows.net'

GCP_IMAGE_NAME = 'ashvin-torch4cuda9'
GCP_GPU_IMAGE_NAME = 'ashvin-torch4cuda9'
GCP_BUCKET_NAME = 'patrick-gcp-bucket'
GCP_DEFAULT_KWARGS = dict(
    zone='us-west1-b',
    instance_type='n1-standard-4',
    image_project='ashvin-val',
    terminate=True,
    preemptible=True,  # is much more expensive!
    gpu_kwargs=dict(
        gpu_model='nvidia-tesla-k80',
        num_gpu=1,
    )
)
GCP_FILE_TYPES_TO_SAVE = (
    '*.txt', '*.csv', '*.json', '*.gz', '*.tar',
    '*.log', '*.pkl', '*.mp4', '*.png', '*.jpg',
    '*.jpeg', '*.patch', '*.html'
)

# CODE_DIRS_TO_MOUNT = [
# ]
# NON_CODE_DIRS_TO_MOUNT = [
# ]
# LOCAL_LOG_DIR = '/tmp/doodad-output/'
# OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/doodad-output/'


# """
# AWS Settings
# """
# AWS_S3_PATH = 'TODO'

# # The docker image is looked up on dockerhub.com.
# DOODAD_DOCKER_IMAGE = 'TODO'
# INSTANCE_TYPE = 'c4.2xlarge'
# SPOT_PRICE = 0.3

# GPU_DOODAD_DOCKER_IMAGE = 'TODO'
# GPU_INSTANCE_TYPE = 'g3.4xlarge'
# GPU_SPOT_PRICE = 0.5
# REGION_TO_GPU_AWS_IMAGE_ID = {
#     'us-west-1': "ami-874378e7",
#     'us-east-1': "ami-ce73adb1",
# }
# AWS_FILE_TYPES_TO_SAVE = (
#     '*.txt', '*.csv', '*.json', '*.gz', '*.tar',
#     '*.log', '*.pkl', '*.mp4', '*.png', '*.jpg',
#     '*.jpeg', '*.patch', '*.html'
# )

# """
# SSH Settings
# """
# SSH_HOSTS = dict(
#     default=dict(
#         username='TODO',
#         hostname='TODO.domain.edu',
#     ),
# )
# SSH_DEFAULT_HOST = 'vitchyr'
# SSH_PRIVATE_KEY = '~/.ssh/id_rsa'
# SSH_LOG_DIR = '~/shared/res'
# SSH_TMP_DIR = '~/shared/tmp'

# """
# Local Singularity Settings
# """
# SINGULARITY_IMAGE = 'TODO'
# SINGULARITY_PRE_CMDS = [
# ]


# """
# Slurm Script Settings (or HTP).

# The comments assume you're running on BRC.
# """
# SLURM_CONFIGS = dict(
#     cpu=dict(
#         account_name='TODO',
#         partition='TODO',
#         n_gpus=0,
#         max_num_cores_per_node=20,
#     ),
#     gpu=dict(
#         account_name='TODO',
#         partition='TODO',
#         n_gpus=1,
#         max_num_cores_per_node=8,
#         n_cpus_per_task=2,
#     ),
# )
# # This is necessary for the GPU machines on BRC.
# BRC_EXTRA_SINGULARITY_ARGS = '--writable -B /usr/lib64 -B /var/lib/dcv-gl'
# # Point to some directory on slurm where tasks will be copied to
# TASKFILE_DIR_ON_BRC = 'TODO'


# # This is the same as `CODE_DIRS_TO_MOUNT` but the paths should be relative to
# # wherever you're running the slurm jobs (e.g. on BRC).
# SSS_CODE_DIRS_TO_MOUNT = [
# ]
# SSS_NON_CODE_DIRS_TO_MOUNT = [
# ]
# # where do you want doodad to output to when using SSS (or HTP) mode?
# SSS_LOG_DIR = '/global/scratch/vitchyr/doodad-log'


# # point to your singularity image with an absolute path on BRC.
# SSS_GPU_IMAGE = 'TODO'
# SSS_CPU_IMAGE = 'TODO'
# # point to `doodad/easy_launch/run_experimenty.py`
# SSS_RUN_DOODAD_EXPERIMENT_SCRIPT_PATH = 'TODO'
# # add any extra pre-commands to your script
# SSS_PRE_CMDS = [
#     'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH'
# ]


# """
# GCP Settings

# To see what zones support GPU, go to https://cloud.google.com/compute/docs/gpus/
# """
# GCP_IMAGE_NAME = 'TODO'
# GCP_GPU_IMAGE_NAME = 'TODO'
# GCP_BUCKET_NAME = 'TODO'

# GCP_DEFAULT_KWARGS = dict(
#     zone='us-west1-a',
#     instance_type='n1-standard-4',
#     image_project='TODO',
#     terminate=True,
#     preemptible=False,  # is much more expensive!
#     gpu_kwargs=dict(
#         gpu_model='nvidia-tesla-k80',
#         num_gpu=1,
#     )
# )
# GCP_FILE_TYPES_TO_SAVE = (
#     '*.txt', '*.csv', '*.json', '*.gz', '*.tar',
#     '*.log', '*.pkl', '*.mp4', '*.png', '*.jpg',
#     '*.jpeg', '*.patch', '*.html'
# )

# # Overwrite with private configurations
# try:
#     from doodad.easy_launch.config_private import *
# except ImportError as e:
#     from doodad.utils import REPO_DIR
#     import os.path as osp
#     command_to_run = "cp {} {}".format(
#         __file__,
#         __file__[:-3] + '_private.py',
#         )
#     print("You should set up the private config files. Run:\n\n  {}\n".format(
#         command_to_run
#     ))
