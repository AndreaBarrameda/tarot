def ai(system_prompt, query):
  import requests

  url = "https://project-meco.as.r.appspot.com/api/meco/openai_api"
  headers = {
      "X-API-KEY": "C7gCjOOi0ZN0yyZ4LtrKP6G5fCtIX9AK",
      "Content-Type": "application/json"
  }
  payload = {
      "query": query,
      "model": "gpt-4o-mini",
      "system_prompt": system_prompt
  }

  response = requests.post(url, json=payload, headers=headers)
  return response.json()


# result = ai(
#             system_prompt=system_prompt,
#             query=query
# )['result']
# print(f'\n\n{result}')