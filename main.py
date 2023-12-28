from openai import OpenAI

client = OpenAI(api_key='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')


completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages=[{'role':'user', 'content': 'write me webpage content regarding data science'}]
                                            )

print(completion.choices[0].message)