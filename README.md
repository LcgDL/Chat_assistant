# Chat_assistant
Chatbot - ChatGPT in Python 

Dependencies:
  openai
  gradio _> python 3.8+
  
Create env w. Conda:
    conda create --name myenv
    conda create -n myenv python=3.9
    
    conda env list
        packages conda list -n envname
        conda config --show channels
        conda config --show default_channels
        
conda install --name <conda_env_name> -c <channel_name> <package_name>
conda install --name envName -c defaults openai
conda install -c conda-forge gradio
             
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

with pip:
    python3 -m venv nameEnv

    close and open new terminal or: 
        source nameEnv/bin/activate
    
    pip install openai
    pip install gradio


