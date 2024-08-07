import os

from lagent.llms import GPTAPI, INTERNLM2_META, LMDeployClient, LMDeployServer

internlm_server = dict(type=LMDeployServer,
                       path='internlm/internlm2_5-7b',
                       model_name='internlm2',
                       meta_template=INTERNLM2_META,
                       top_p=0.8,
                       top_k=1,
                       temperature=0,
                       max_new_tokens=8192,
                       repetition_penalty=1.02,
                       stop_words=['<|im_end|>'])

internlm_client = dict(type=LMDeployClient,
                       model_name='internlm2-chat-7b',
                       url='http://22.8.27.215:23333',
                       meta_template=INTERNLM2_META,
                       top_p=0.8,
                       top_k=1,
                       temperature=0,
                       max_new_tokens=8192,
                       repetition_penalty=1.02,
                       stop_words=['<|im_end|>'])

gpt4 = dict(type=GPTAPI,
            model_type='gpt-4-turbo',
            key=os.environ.get('OPENAI_API_KEY', 'YOUR OPENAI API KEY'))

puyu = dict(
    type=GPTAPI,
    model_type='internlm2.5-latest-inner',
    openai_api_base='https://puyu.openxlab.org.cn/puyu/api/v1/chat/completions',
    key=os.environ.get('PUYU_API_KEY', 'YOUR PUYU API KEY'),
    meta_template=[
        dict(role='system', api_role='system'),
        dict(role='user', api_role='user'),
        dict(role='assistant', api_role='assistant'),
        dict(role='environment', api_role='environment')
    ],
    top_p=0.8,
    top_k=1,
    temperature=0.8,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=['<|im_end|>'])
