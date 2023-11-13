from openai import OpenAI

class MainLogic:
    def __init__(self) -> None:
        self.client = OpenAI(api_key = "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")
        pass
    def setConfig(self, configs):
        self.configs = configs

    def setApiKey(self, key):
        self.client = OpenAI(api_key = key)
    
    def run(self, index, prompt):
        system_content = self.configs[index]["system"]
        user_content = self.configs[index]["user"].replace("#!!!!!#", prompt)
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
        )
        return completion.choices[0].message