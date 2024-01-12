import openai 

class Summarizer:
    @staticmethod
    def summarize(text):
        openai.api_ky = ''
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=150
        
        )
        summary = response.choices[0].text.strip()
        return summary